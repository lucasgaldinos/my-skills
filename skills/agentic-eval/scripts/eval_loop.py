#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
eval_loop.py — Core evaluator-optimizer loop (Patterns 1 + 2 combined)

Run with: uv run eval_loop.py --task "Write a Python sort function" --max-iter 3
Requires:  ANTHROPIC_API_KEY environment variable

Implements a generator-evaluator-refiner loop with:
- Configurable max iterations and convergence detection
- Structured JSON feedback (not prose) passed to the refiner
- Noise mitigation: evaluator runs 3x per iteration and averages scores
- Separate model for judge (mitigates self-preference bias, arXiv:2410.21819)
"""

import argparse
import json
import os
import re
import sys
from typing import Optional

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
    print("Set it with: export ANTHROPIC_API_KEY=sk-ant-...", file=sys.stderr)
    sys.exit(1)

import anthropic

client = anthropic.Anthropic()

GENERATOR_MODEL = "claude-sonnet-4-5"
EVALUATOR_MODEL = "claude-opus-4-5"   # Deliberately different (self-preference bias mitigation)
EVAL_RUNS = 3
DEFAULT_MAX_ITER = 3
DEFAULT_THRESHOLD = 0.80
CONVERGENCE_DELTA = 0.02


def generate(task: str, feedback: Optional[dict] = None, prev_output: Optional[str] = None) -> str:
    if feedback is None:
        prompt = task
    else:
        prompt = f"""{task}

Previous attempt:
{prev_output}

Structured feedback from evaluator:
{json.dumps(feedback, indent=2)}

Improve the output addressing each piece of feedback. Return only the improved output."""

    response = client.messages.create(
        model=GENERATOR_MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def evaluate_once(output: str, task: str, rubric: dict) -> dict:
    rubric_str = "\n".join(
        f"- {k} (weight {v['weight']:.1f}): {v['description']}"
        for k, v in rubric.items()
    )
    prompt = f"""You are a strict, impartial evaluator. Score this output against each criterion independently.

Task: {task}

Output to evaluate:
{output}

Rubric (score each 0.0-1.0):
{rubric_str}

Respond with ONLY valid JSON:
{{
  "scores": {{"criterion_name": 0.0}},
  "feedback": {{"criterion_name": "specific improvement needed"}},
  "total": 0.0
}}

Be strict: 0.8 means 20% unmet. Feedback must be actionable."""

    response = client.messages.create(
        model=EVALUATOR_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = re.sub(r"^```[a-z]*\n?", "", response.content[0].text.strip())
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def evaluate(output: str, task: str, rubric: dict, runs: int = EVAL_RUNS) -> dict:
    results = [r for _ in range(runs) for r in [_safe_eval(output, task, rubric)] if r]
    if not results:
        raise RuntimeError("All evaluation runs failed")

    all_criteria = results[0]["scores"].keys()
    avg_scores = {k: sum(r["scores"].get(k, 0.0) for r in results) / len(results) for k in all_criteria}
    avg_total = sum(r.get("total", 0.0) for r in results) / len(results)
    closest = min(results, key=lambda r: abs(r.get("total", 0.0) - avg_total))

    return {
        "scores": avg_scores,
        "feedback": closest["feedback"],
        "total": avg_total,
        "variance": max(r.get("total", 0.0) for r in results) - min(r.get("total", 0.0) for r in results),
    }


def _safe_eval(output, task, rubric):
    try:
        return evaluate_once(output, task, rubric)
    except (json.JSONDecodeError, KeyError):
        return None


def run_loop(task: str, rubric: dict, max_iter: int = DEFAULT_MAX_ITER, threshold: float = DEFAULT_THRESHOLD) -> dict:
    history = []
    prev_score = 0.0
    plateau_count = 0
    output = None
    feedback = None

    print(f"Starting eval loop: max_iter={max_iter}, threshold={threshold:.2f}\n")

    for i in range(max_iter):
        print(f"Iteration {i + 1}/{max_iter}")
        output = generate(task, feedback=feedback, prev_output=output)
        result = evaluate(output, task, rubric)
        score = result["total"]
        feedback = result["feedback"]

        history.append({"iteration": i + 1, "output": output,
                        "scores": result["scores"], "total": score,
                        "variance": result.get("variance", 0.0), "feedback": feedback})

        print(f"  Score: {score:.3f} (variance: {result.get('variance', 0):.3f})")
        for k, v in result["scores"].items():
            print(f"    {k}: {v:.2f}")

        if score >= threshold:
            print(f"\n Threshold reached ({score:.3f} >= {threshold:.2f}). Stopping.")
            break

        delta = abs(score - prev_score)
        if delta < CONVERGENCE_DELTA:
            plateau_count += 1
            if plateau_count >= 2:
                print(f"\n Convergence detected (delta={delta:.4f}). Stopping.")
                break
        else:
            plateau_count = 0
        prev_score = score
        print()

    best = max(history, key=lambda h: h["total"])
    print(f"\nBest output from iteration {best['iteration']} (score={best['total']:.3f})")
    return {"best_output": best["output"], "best_score": best["total"],
            "best_iteration": best["iteration"], "history": history}


DEFAULT_RUBRIC = {
    "correctness": {"weight": 0.40, "description": "Factually correct, addresses the task fully. 1.0=fully correct, 0.0=wrong."},
    "completeness": {"weight": 0.30, "description": "All required parts present. 1.0=nothing missing, 0.0=major sections absent."},
    "clarity":      {"weight": 0.20, "description": "Clear and understandable. 1.0=no re-reading needed, 0.0=confusing."},
    "conciseness":  {"weight": 0.10, "description": "No unnecessary content. 1.0=no fluff, 0.0=bloated."},
}


def main():
    parser = argparse.ArgumentParser(description="Evaluator-optimizer loop")
    parser.add_argument("--task", required=True)
    parser.add_argument("--max-iter", type=int, default=DEFAULT_MAX_ITER)
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--rubric-file", help="Path to JSON rubric file")
    parser.add_argument("--output-file", help="Save best output to this file")
    args = parser.parse_args()

    rubric = DEFAULT_RUBRIC
    if args.rubric_file:
        with open(args.rubric_file) as f:
            rubric = json.load(f)

    result = run_loop(args.task, rubric, max_iter=args.max_iter, threshold=args.threshold)
    print("\n" + "=" * 60)
    print(result["best_output"])

    if args.output_file:
        with open(args.output_file, "w") as f:
            f.write(result["best_output"])

    sys.exit(0 if result["best_score"] >= args.threshold else 1)


if __name__ == "__main__":
    main()
