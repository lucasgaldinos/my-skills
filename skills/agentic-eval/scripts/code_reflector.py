#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.25.0",
#   "pytest>=7.0.0",
# ]
# ///
"""
code_reflector.py - Test-driven code refinement (Pattern 3)

Run with: uv run code_reflector.py --task "Write an email validator" \
                                    --test-file test_email.py \
                                    --output-file email_validator.py
Requires:  ANTHROPIC_API_KEY environment variable

Uses test failures as ground-truth evaluation signal - no LLM judge needed.
The loop:
  1. Generate code from task description
  2. Run the test suite (pytest)
  3. If tests fail -> send structured failure report back to LLM as feedback
  4. Refine and repeat until tests pass or max_iter reached

Tests are deterministic; this pattern has the highest signal-to-noise ratio.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Error: ANTHROPIC_API_KEY is not set. export ANTHROPIC_API_KEY=sk-ant-...", file=sys.stderr)
    sys.exit(1)

import anthropic

client = anthropic.Anthropic()
GENERATOR_MODEL = "claude-sonnet-4-5"
DEFAULT_MAX_ITER = 5


def extract_code(text: str) -> str:
    match = re.search(r"```(?:python|py)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    text = re.sub(r"^```[a-z]*\n?", "", text.strip())
    return re.sub(r"\n?```$", "", text).strip()


def generate_code(task: str, test_content: str, previous_code: str = None, failure_report: dict = None) -> str:
    if previous_code is None:
        prompt = f"""Write Python code to complete this task.

Task: {task}

The code will be tested with:
```
{test_content}
```

Return ONLY the implementation code, no test code."""
    else:
        failures_text = "\n".join(f"- {f['test']}: {f['error']}" for f in failure_report.get("failures", []))
        prompt = f"""Fix this Python code to make the failing tests pass.

Task: {task}

Current code:
```python
{previous_code}
```

Failing tests ({failure_report.get('failed', '?')} of {failure_report.get('total', '?')} total):
{failures_text}

Return ONLY the fixed implementation code."""

    response = client.messages.create(
        model=GENERATOR_MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )
    return extract_code(response.content[0].text)


def run_tests(code: str, test_file: Path) -> dict:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        test_content = test_file.read_text()

        # Infer module name from test file imports
        import_match = re.search(r"^(?:from|import)\s+(\w+)", test_content, re.MULTILINE)
        module_name = import_match.group(1) if import_match else test_file.stem.replace("test_", "")

        (tmp / f"{module_name}.py").write_text(code)
        (tmp / test_file.name).write_text(test_content)

        proc = subprocess.run(
            [sys.executable, "-m", "pytest", test_file.name, "-v", "--tb=short", "--no-header", "-q"],
            capture_output=True, text=True, cwd=tmp_dir, timeout=60
        )

        stdout = proc.stdout
        passed = failed = 0
        failures = []
        current_test = None
        err_lines = []

        for line in stdout.split("\n"):
            if "passed" in line and "failed" not in line:
                m = re.search(r"(\d+) passed", line)
                if m:
                    passed = int(m.group(1))
            if "failed" in line:
                m = re.search(r"(\d+) failed", line)
                if m:
                    failed = int(m.group(1))
            if line.startswith("FAILED "):
                if current_test and err_lines:
                    failures.append({"test": current_test, "error": " ".join(err_lines[-3:])})
                current_test = line.replace("FAILED ", "").split(" - ")[0].strip()
                err_lines = []
            elif current_test and line.strip():
                err_lines.append(line.strip())

        if current_test and err_lines:
            failures.append({"test": current_test, "error": " ".join(err_lines[-3:])})

        if failed > 0 and not failures:
            failures.append({"test": "unknown", "error": stdout[-1500:]})

        return {"passed": passed, "failed": failed, "total": passed + failed,
                "failures": failures, "stdout": stdout, "all_pass": proc.returncode == 0}


def run_loop(task: str, test_file: Path, max_iter: int, output_file: Path = None) -> dict:
    history = []
    code = None
    test_content = test_file.read_text()

    print(f"Starting test-driven refinement: max_iter={max_iter}\n")

    for i in range(max_iter):
        print(f"Iteration {i + 1}/{max_iter}")
        failure_report = history[-1]["test_result"] if history else None

        print("  Generating code...", end=" ", flush=True)
        code = generate_code(task, test_content, previous_code=code, failure_report=failure_report)
        print("done")

        print("  Running tests...", end=" ", flush=True)
        test_result = run_tests(code, test_file)
        print(f"done ({test_result['passed']}/{test_result['total']} passing)")

        history.append({"iteration": i + 1, "code": code, "test_result": test_result})

        if test_result["all_pass"]:
            print(f"\n All {test_result['passed']} tests pass! Done.")
            break

        for f in test_result["failures"][:3]:
            print(f"    FAIL: {f['test']}")
        print()

    best = next((h for h in reversed(history) if h["test_result"]["all_pass"]), None)
    if best is None:
        best = max(history, key=lambda h: h["test_result"]["passed"])

    if output_file:
        output_file.write_text(best["code"])
        print(f"Code saved to {output_file}")

    return {"success": best["test_result"]["all_pass"], "best_code": best["code"],
            "best_iteration": best["iteration"],
            "passed": best["test_result"]["passed"], "failed": best["test_result"]["failed"]}


def main():
    parser = argparse.ArgumentParser(description="Test-driven code refinement loop")
    parser.add_argument("--task", required=True)
    parser.add_argument("--test-file", required=True, help="pytest-compatible test file")
    parser.add_argument("--output-file", help="Save final code to this file")
    parser.add_argument("--max-iter", type=int, default=DEFAULT_MAX_ITER)
    parser.add_argument("--print-code", action="store_true")
    args = parser.parse_args()

    test_file = Path(args.test_file)
    if not test_file.exists():
        print(f"Error: test file not found: {test_file}", file=sys.stderr)
        sys.exit(1)

    result = run_loop(args.task, test_file, args.max_iter,
                      Path(args.output_file) if args.output_file else None)

    status = "SUCCESS" if result["success"] else "PARTIAL"
    print(f"\n{status}: {result['passed']} tests passing, {result['failed']} failing")
    print(f"Best result from iteration {result['best_iteration']}")

    if args.print_code:
        print("\n" + result["best_code"])

    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
