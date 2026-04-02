#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
# ]
# ///
"""
llm_judge.py - Bias-resistant pairwise LLM judge (Pattern 4)

Run with: uv run llm_judge.py --output-a "text A" --output-b "text B" --task "the task"
      or: uv run llm_judge.py --file-a v1.txt --file-b v2.txt --task "the task"
Requires:  ANTHROPIC_API_KEY environment variable

Implements positional-bias mitigation from arXiv:2406.07791:
- Runs pairwise comparison in BOTH orders (A vs B, then B vs A)
- Declares winner only if BOTH orderings agree
- Otherwise: TIE (prevents systematic position preference)

Self-preference mitigation (arXiv:2410.21819):
- Uses blinded labels ("Option 1" / "Option 2", not "Model A" / "Baseline")
- Uses strongest available judge model

Exit codes: 0=A wins, 2=B wins, 1=TIE
"""

import argparse
import json
import os
import re
import sys

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY is not set. export ANTHROPIC_API_KEY=sk-ant-...", file=sys.stderr)
    sys.exit(1)

import anthropic

client = anthropic.Anthropic()
JUDGE_MODEL = "claude-opus-4-5"

JUDGE_PROMPT = """You are an impartial judge. Evaluate two outputs for a task. Focus on quality, not style preferences.

Task: {task}

Option 1:
{output1}

---

Option 2:
{output2}

---

Evaluation criteria:
{criteria}

Respond ONLY with valid JSON:
{{
  "winner": "Option 1" or "Option 2" or "TIE",
  "scores": {{"Option 1": {{"criterion": 0.0}}, "Option 2": {{"criterion": 0.0}}}},
  "reasoning": "specific comparison citing evidence from both outputs"
}}

Only declare TIE when outputs are genuinely equivalent (< 5% difference).
Cite specific text in reasoning."""

DEFAULT_CRITERIA = """- Correctness: factual accuracy and task completion
- Completeness: all required elements present
- Clarity: clear and understandable
- Conciseness: no unnecessary verbosity"""


def judge_ordered(output1: str, output2: str, task: str, criteria: str) -> dict:
    prompt = JUDGE_PROMPT.format(task=task, output1=output1, output2=output2, criteria=criteria)
    response = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = re.sub(r"^```[a-z]*\n?", "", response.content[0].text.strip())
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)


def judge_pairwise(output_a: str, output_b: str, task: str, criteria: str) -> dict:
    """Run in both orders and take consensus to eliminate positional bias."""
    print("  Forward (A first)...", file=sys.stderr)
    forward = judge_ordered(output_a, output_b, task, criteria)

    print("  Reverse (B first)...", file=sys.stderr)
    reverse = judge_ordered(output_b, output_a, task, criteria)

    fw = forward.get("winner", "TIE")
    rv_raw = reverse.get("winner", "TIE")

    # Translate reverse back to A/B labels
    rv = {"Option 1": "B", "Option 2": "A", "TIE": "TIE"}.get(rv_raw, "TIE")

    if fw == "TIE" and rv == "TIE":
        verdict, confidence = "TIE", "high"
    elif fw == "Option 1" and rv == "A":
        verdict, confidence = "A", "high"
    elif fw == "Option 2" and rv == "B":
        verdict, confidence = "B", "high"
    else:
        verdict, confidence = "TIE", "low (split verdict - positional bias likely)"

    return {"verdict": verdict, "confidence": confidence,
            "forward": forward, "reverse": reverse}


def main():
    parser = argparse.ArgumentParser(description="Bias-resistant pairwise LLM judge (both orderings)")
    parser.add_argument("--output-a")
    parser.add_argument("--output-b")
    parser.add_argument("--file-a")
    parser.add_argument("--file-b")
    parser.add_argument("--task", required=True)
    parser.add_argument("--criteria", help="Custom criteria text")
    parser.add_argument("--json", dest="as_json", action="store_true")
    args = parser.parse_args()

    out_a = args.output_a or (open(args.file_a).read().strip() if args.file_a else None)
    out_b = args.output_b or (open(args.file_b).read().strip() if args.file_b else None)

    if not out_a or not out_b:
        print("Error: provide (--output-a and --output-b) or (--file-a and --file-b)", file=sys.stderr)
        sys.exit(1)

    print(f"Judging with {JUDGE_MODEL} (bias-resistant: both orderings)...", file=sys.stderr)
    result = judge_pairwise(out_a, out_b, args.task, args.criteria or DEFAULT_CRITERIA)

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print("\n" + "=" * 50)
        verdict = result["verdict"]
        label = {"A": "WINNER: Output A", "B": "WINNER: Output B", "TIE": "RESULT: TIE"}.get(verdict, verdict)
        print(label)
        print(f"Confidence: {result['confidence']}")
        print(f"\nForward: {result['forward'].get('winner', '?')} — {result['forward'].get('reasoning', '')[:200]}")
        print(f"\nReverse: {result['reverse'].get('winner', '?')} — {result['reverse'].get('reasoning', '')[:200]}")
        print("=" * 50)

    sys.exit({"A": 0, "B": 2, "TIE": 1}.get(result["verdict"], 1))


if __name__ == "__main__":
    main()
