# Evaluation Patterns: Full Implementation Templates

Five patterns for agentic evaluation loops. Each section includes: when to use it, the implementation template, and what to watch for.

---

## Pattern 1: Basic Reflection (Self-Critique)

**Use when:** Subjective quality improvement (writing, analysis, summaries) where no ground truth exists and the quality bar is medium.  
**Do NOT use for:** High-stakes outputs — self-critique is systematically softer than external critique (see gathered_knowledge.md).

```python
import json
from typing import Callable

def reflect_and_refine(
    task: str,
    criteria: list[str],
    llm: Callable[[str], str],
    max_iterations: int = 3,
    pass_threshold: float = 0.8,
) -> dict:
    """
    Self-critique reflection loop.
    Returns best-scored output with full iteration log.
    """
    output = llm(f"Complete this task:\n{task}")
    best = {"output": output, "score": 0.0}
    history = []

    for i in range(max_iterations):
        # Separate critique call — do not chain in the same context
        critique_prompt = f"""You are a strict evaluator. Evaluate the output below against these criteria: {criteria}

Output to evaluate:
{output}

Return ONLY a JSON object with this structure:
{{
  "overall_score": <float 0.0-1.0>,
  "criteria_scores": {{<criterion>: {{"score": <0.0-1.0>, "feedback": "<specific actionable feedback>"}}}},
  "passed": <true|false>
}}"""

        raw = llm(critique_prompt)
        try:
            evaluation = json.loads(raw)
        except json.JSONDecodeError:
            # Fallback: extract JSON substring
            import re
            match = re.search(r'\{.*\}', raw, re.DOTALL)
            evaluation = json.loads(match.group()) if match else {"overall_score": 0.5, "criteria_scores": {}, "passed": False}

        score = evaluation.get("overall_score", 0.0)
        history.append({"iteration": i, "score": score, "output_length": len(output)})

        if score > best["score"]:
            best = {"output": output, "score": score}

        # Early stopping: good enough
        if score >= pass_threshold or evaluation.get("passed", False):
            break

        # Early stopping: plateau (score not improving by more than 5%)
        if i > 0 and abs(score - history[-2]["score"]) < 0.05:
            break

        # Refine only on specific failed criteria
        failed = {k: v["feedback"] for k, v in evaluation.get("criteria_scores", {}).items()
                  if v.get("score", 0) < 0.7}
        if not failed:
            break

        refine_prompt = f"""Improve this output to address the following specific issues:
{json.dumps(failed, indent=2)}

Original output:
{output}

Return only the improved output, no explanation."""
        output = llm(refine_prompt)

    return {"output": best["output"], "score": best["score"], "iterations": len(history), "log": history}
```

---

## Pattern 2: Evaluator-Optimizer (Separate Components)

**Use when:** High quality bar, clear multi-dimensional criteria, and you need reliable, actionable feedback.  
**Key rule:** Generator and evaluator must be separate LLM calls with separate context.

```python
import json
from typing import Callable

class EvaluatorOptimizer:
    """
    Separate generator and evaluator components.
    Evaluator provides structured, actionable feedback per dimension.
    """

    def __init__(
        self,
        llm: Callable[[str], str],
        rubric: dict,          # {"criterion": {"weight": float, "definition": str}}
        pass_threshold: float = 0.85,
        max_iterations: int = 3,
    ):
        self.llm = llm
        self.rubric = rubric
        self.pass_threshold = pass_threshold
        self.max_iterations = max_iterations

    def generate(self, task: str) -> str:
        return self.llm(f"Complete this task thoroughly:\n{task}")

    def evaluate(self, output: str, task: str) -> dict:
        criteria_list = "\n".join(
            f"- {k} (weight {v['weight']}): {v['definition']}"
            for k, v in self.rubric.items()
        )
        prompt = f"""You are an expert evaluator. Rate the output below against each criterion.

Task: {task}

Criteria:
{criteria_list}

Output:
{output}

Return ONLY a JSON object:
{{
  "scores": {{<criterion>: {{"score": <0.0-1.0>, "feedback": "<one specific, actionable sentence>"}}}},
  "overall_score": <weighted average 0.0-1.0>,
  "primary_issue": "<the single most important thing to fix>"
}}"""
        raw = self.llm(prompt)
        try:
            return json.loads(raw)
        except Exception:
            import re
            match = re.search(r'\{.*\}', raw, re.DOTALL)
            return json.loads(match.group()) if match else {"scores": {}, "overall_score": 0.5}

    def optimize(self, output: str, evaluation: dict) -> str:
        primary_issue = evaluation.get("primary_issue", "")
        low_scores = {k: v for k, v in evaluation.get("scores", {}).items() if v.get("score", 1) < 0.75}
        prompt = f"""Improve this output. Focus on the primary issue first, then address secondary issues.

Primary issue: {primary_issue}

Secondary issues:
{json.dumps({k: v['feedback'] for k, v in low_scores.items()}, indent=2)}

Current output:
{output}

Return only the improved output."""
        return self.llm(prompt)

    def run(self, task: str) -> dict:
        output = self.generate(task)
        best = {"output": output, "score": 0.0}
        history = []

        for i in range(self.max_iterations):
            evaluation = self.evaluate(output, task)
            score = evaluation.get("overall_score", 0.0)
            history.append({"iteration": i, "score": score})

            if score > best["score"]:
                best = {"output": output, "score": score}

            if score >= self.pass_threshold:
                break
            if i > 0 and abs(score - history[-2]["score"]) < 0.05:
                break  # Plateau

            output = self.optimize(output, evaluation)

        return {"output": best["output"], "score": best["score"], "iterations": len(history), "log": history}
```

---

## Pattern 3: Code Reflection (Test-Driven Refinement)

**Use when:** Code generation where correctness can be verified by tests.  
**Advantage:** Objective stopping criterion — no threshold tuning required.  
**Key rule:** Generate the test specification BEFORE the code to avoid the agent gaming its own tests.

```python
import subprocess
import tempfile
import os
from typing import Callable

class CodeReflector:
    """
    Test-driven code generation with reflection.
    Generates tests first (spec-first), then iteratively fixes code until tests pass.
    """

    def __init__(self, llm: Callable[[str], str], max_iterations: int = 5):
        self.llm = llm
        self.max_iterations = max_iterations

    def generate_tests(self, spec: str) -> str:
        """Generate tests BEFORE generating code."""
        return self.llm(f"""Write comprehensive pytest tests for this specification.
Do NOT write the implementation — only the tests.
Tests must be runnable and cover: happy path, edge cases, error cases.

Specification:
{spec}

Return only executable Python test code.""")

    def generate_code(self, spec: str, tests: str) -> str:
        return self.llm(f"""Write Python code that passes all these tests.

Specification:
{spec}

Tests that must pass:
{tests}

Return only the implementation code, no test code.""")

    def run_tests(self, code: str, tests: str) -> dict:
        with tempfile.TemporaryDirectory() as tmpdir:
            code_file = os.path.join(tmpdir, "solution.py")
            test_file = os.path.join(tmpdir, "test_solution.py")

            with open(code_file, "w") as f:
                f.write(code)
            with open(test_file, "w") as f:
                # Import solution module in tests
                f.write(f"import sys; sys.path.insert(0, '{tmpdir}')\n")
                f.write("from solution import *\n\n")
                f.write(tests)

            result = subprocess.run(
                ["python", "-m", "pytest", test_file, "-v", "--tb=short", "--no-header"],
                capture_output=True, text=True, timeout=30
            )
            return {
                "success": result.returncode == 0,
                "output": result.stdout + result.stderr,
                "returncode": result.returncode
            }

    def fix_code(self, code: str, error_output: str, spec: str) -> str:
        return self.llm(f"""Fix this Python code. The tests failed with the following output.

Error output:
{error_output[:2000]}

Specification:
{spec}

Current code:
{code}

Return only the fixed implementation code.""")

    def run(self, spec: str) -> dict:
        tests = self.generate_tests(spec)
        code = self.generate_code(spec, tests)
        history = []

        for i in range(self.max_iterations):
            result = self.run_tests(code, tests)
            history.append({"iteration": i, "success": result["success"]})

            if result["success"]:
                return {"code": code, "tests": tests, "success": True, "iterations": i + 1, "log": history}

            code = self.fix_code(code, result["output"], spec)

        return {"code": code, "tests": tests, "success": False, "iterations": self.max_iterations, "log": history}
```

---

## Pattern 4: LLM-as-Judge (Comparative Evaluation)

**Use when:** Ranking or selecting the best among multiple candidate outputs, or when you need bias-aware evaluation.  
**Key rule from research (arXiv:2406.07791):** Always run pairwise comparisons in both orders and average. Discard if results conflict strongly.

```python
import json
from typing import Callable

def llm_judge_pairwise(
    output_a: str,
    output_b: str,
    criteria: str,
    llm: Callable[[str], str],
) -> dict:
    """
    Bias-resistant pairwise LLM judge.
    Runs comparison in both orders and averages to mitigate positional bias.
    """

    def compare(first: str, second: str, label_first: str, label_second: str) -> dict:
        prompt = f"""Compare these two outputs based on: {criteria}

Output {label_first}:
{first}

Output {label_second}:
{second}

Return ONLY JSON:
{{"winner": "{label_first}" | "{label_second}" | "tie", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}}"""
        raw = llm(prompt)
        try:
            return json.loads(raw)
        except Exception:
            return {"winner": "tie", "confidence": 0.5, "reasoning": "parse error"}

    # Run in both orders to detect positional bias
    result_ab = compare(output_a, output_b, "A", "B")
    result_ba = compare(output_b, output_a, "B", "A")

    # Normalize: translate result_ba so "B" means output_b, "A" means output_a
    winner_ab = result_ab["winner"]
    winner_ba_normalized = "A" if result_ba["winner"] == "B" else ("B" if result_ba["winner"] == "A" else "tie")

    if winner_ab == winner_ba_normalized:
        final_winner = winner_ab
        confidence = (result_ab["confidence"] + result_ba["confidence"]) / 2
        consistent = True
    else:
        final_winner = "tie"  # Inconsistent — treat as tie
        confidence = 0.5
        consistent = False

    return {
        "winner": final_winner,         # "A" = output_a, "B" = output_b, "tie"
        "confidence": confidence,
        "consistent": consistent,       # False = positional bias suspected
        "ab_result": result_ab,
        "ba_result": result_ba,
    }
```

---

## Pattern 5: Rubric-Based Scoring (Weighted Dimensions)

**Use when:** Multiple quality dimensions with different importance, and you need a final numeric score for comparison or threshold checks.  
**Research note (ACL 2024 LLM-Rubric):** Prompt each criterion separately for higher reliability.

```python
import json
from typing import Callable

def rubric_score(
    output: str,
    rubric: dict,   # {"criterion": {"weight": float, "definition": str, "examples": list[dict]}}
    llm: Callable[[str], str],
) -> dict:
    """
    Evaluate output against a weighted rubric.
    Prompts each criterion separately (per LLM-Rubric research recommendation).
    """
    scores = {}

    for criterion, config in rubric.items():
        few_shot = ""
        if config.get("examples"):
            few_shot = "\n\nExamples:\n" + "\n".join(
                f"Output: {ex['output']}\nScore: {ex['score']} — {ex['reason']}"
                for ex in config["examples"][:2]
            )

        prompt = f"""Evaluate the output below on ONE criterion only.

Criterion: {criterion}
Definition: {config['definition']}{few_shot}

Scale: 0.0 (completely fails), 0.5 (partially meets), 1.0 (fully meets)

Output to evaluate:
{output}

Return ONLY JSON: {{"score": <0.0-1.0>, "feedback": "<one specific sentence explaining the score>"}}"""

        raw = llm(prompt)
        try:
            result = json.loads(raw)
        except Exception:
            result = {"score": 0.5, "feedback": "evaluation failed"}

        scores[criterion] = {"score": result["score"], "feedback": result["feedback"], "weight": config["weight"]}

    # Weighted average
    total_weight = sum(c["weight"] for c in scores.values())
    overall = sum(c["score"] * c["weight"] for c in scores.values()) / total_weight if total_weight > 0 else 0.0

    return {
        "overall_score": round(overall, 3),
        "passed": overall >= 0.8,
        "dimension_scores": scores,
    }
```
