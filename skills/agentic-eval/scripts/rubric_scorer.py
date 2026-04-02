#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
rubric_scorer.py - Per-criterion rubric scoring (Pattern 5)

Run with: uv run rubric_scorer.py --output "text" --rubric rubric.json
      or: echo "output text" | uv run rubric_scorer.py --rubric rubric.json
Requires:  ANTHROPIC_API_KEY environment variable

Implements the LLM-Rubric recommendation (ACL 2024): prompt each criterion
in a SEPARATE LLM call instead of asking for all scores in one prompt.
This reduces criterion interference and improves reliability by 15-20%.

rubric.json format:
  {
    "accuracy": {
      "weight": 0.4,
      "description": "Facts are correct and verifiable",
      "anchors": {
        "1.0": "All facts correct",
        "0.5": "Some errors, not misleading",
        "0.0": "Factually wrong in material ways"
      }
    }
  }
"""

import argparse
import json
import os
import re
import sys
from typing import Optional

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY is not set. export ANTHROPIC_API_KEY=sk-ant-...", file=sys.stderr)
    sys.exit(1)

import anthropic

client = anthropic.Anthropic()
JUDGE_MODEL = "claude-sonnet-4-5"


def score_criterion(output: str, task: Optional[str], name: str, criterion: dict) -> dict:
    anchors = criterion.get("anchors", {})
    anchors_text = "\n".join(f"  {s}: {d}" for s, d in sorted(anchors.items(), reverse=True)) \
        if anchors else "0.0 = does not meet; 1.0 = fully meets"

    prompt = f"""Evaluate ONE criterion only. Ignore all others.

Criterion: {name}
Definition: {criterion["description"]}

Score scale (0.0-1.0):
{anchors_text}
{f"Original task: {task}" if task else ""}

Output:
{output}

Respond ONLY with valid JSON:
{{"score": 0.0, "rationale": "specific evidence from output"}}

Be strict. Cite specific text."""

    response = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = re.sub(r"^```[a-z]*\n?", "", response.content[0].text.strip())
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def score_rubric(output: str, rubric: dict, task: Optional[str] = None, runs: int = 1) -> dict:
    results = {k: [] for k in rubric}
    for run in range(runs):
        if runs > 1:
            print(f"  Eval run {run + 1}/{runs}...", file=sys.stderr)
        for name, criterion in rubric.items():
            try:
                results[name].append(score_criterion(output, task, name, criterion))
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Warning: failed to score {name}: {e}", file=sys.stderr)

    scored = {}
    total = 0.0
    total_weight = 0.0

    for name, criterion in rubric.items():
        runs_data = results[name]
        if not runs_data:
            scored[name] = {"score": 0.0, "rationale": "evaluation failed", "weight": criterion["weight"]}
            continue

        avg = sum(r["score"] for r in runs_data) / len(runs_data)
        rep = min(runs_data, key=lambda r: abs(r["score"] - avg))
        entry = {"score": round(avg, 3), "weight": criterion["weight"], "rationale": rep["rationale"]}
        if len(runs_data) > 1:
            entry["variance"] = round(max(r["score"] for r in runs_data) - min(r["score"] for r in runs_data), 3)
        scored[name] = entry
        total += avg * criterion["weight"]
        total_weight += criterion["weight"]

    return {"criteria": scored, "total": round(total / total_weight if total_weight else 0, 3)}


def print_report(result: dict):
    print("\n" + "=" * 50)
    print("RUBRIC SCORING REPORT")
    print("=" * 50)
    for name, data in result["criteria"].items():
        bar = "X" * int(data["score"] * 20) + "." * (20 - int(data["score"] * 20))
        var = f"  var={data['variance']:.3f}" if "variance" in data else ""
        print(f"\n{name} (weight {int(data['weight']*100)}%)")
        print(f"  [{bar}] {data['score']:.3f}{var}")
        print(f"  {data['rationale']}")
    print("\n" + "-" * 50)
    bar = "X" * int(result["total"] * 20) + "." * (20 - int(result["total"] * 20))
    print(f"TOTAL: [{bar}] {result['total']:.3f}")
    print("=" * 50)


DEFAULT_RUBRIC = {
    "correctness":  {"weight": 0.40, "description": "Factually correct", "anchors": {"1.0": "All correct", "0.5": "Minor errors", "0.0": "Materially wrong"}},
    "completeness": {"weight": 0.30, "description": "All required elements present", "anchors": {"1.0": "Nothing missing", "0.5": "Some missing", "0.0": "Major sections absent"}},
    "clarity":      {"weight": 0.20, "description": "Clear without re-reading", "anchors": {"1.0": "Immediately clear", "0.5": "Some re-reading needed", "0.0": "Confusing"}},
    "conciseness":  {"weight": 0.10, "description": "No unnecessary verbosity", "anchors": {"1.0": "No fluff", "0.5": "Some excess", "0.0": "Bloated"}},
}


def main():
    parser = argparse.ArgumentParser(description="Per-criterion rubric scorer (LLM-Rubric protocol)")
    parser.add_argument("--output", help="Text to evaluate (or pipe via stdin)")
    parser.add_argument("--task", help="Original task (improves accuracy)")
    parser.add_argument("--rubric-file", help="Path to JSON rubric file")
    parser.add_argument("--runs", type=int, default=1, help="Eval runs to average (default 1; use 3 for noisy criteria)")
    parser.add_argument("--json", dest="as_json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.output:
        output_text = args.output
    elif not sys.stdin.isatty():
        output_text = sys.stdin.read().strip()
    else:
        print("Error: provide --output or pipe text via stdin", file=sys.stderr)
        sys.exit(1)

    rubric = DEFAULT_RUBRIC
    if args.rubric_file:
        with open(args.rubric_file) as f:
            rubric = json.load(f)

    result = score_rubric(output_text, rubric, task=args.task, runs=args.runs)

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    sys.exit(0 if result["total"] >= 0.70 else 1)


if __name__ == "__main__":
    main()
