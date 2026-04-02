# Rubric Design Guide

How to design evaluation criteria that produce reliable, actionable results. Based on academic findings from LLM-Rubric (ACL 2024) and Autorubric (arXiv 2025).

---

## The Fundamental Problem

Most rubric failures come from **ambiguous criteria** that different evaluators (human or LLM) interpret differently. A rubric with Cohen's kappa < 0.6 across two judge runs is not reliable enough to use for autonomous evaluation — it is essentially random.

**Always check reliability** before deploying a rubric autonomously: run the same rubric on 5 sample outputs twice and measure agreement.

---

## Rules for Criterion Design

### Rule 1: One criterion per question
Never combine two qualities in one criterion. Bad: "Is the output accurate and well-written?" Good: two separate criteria — "Accuracy" and "Clarity".

### Rule 2: Define the criterion operationally
Not: "Clarity" — too vague.  
Yes: "Clarity: A reader with no prior domain knowledge can understand the main point without re-reading."

### Rule 3: Anchor with examples (few-shot calibration)
Per LLM-Rubric research, 2 examples per criterion (one low score, one high score) dramatically improve reliability. Include them in your rubric definition.

### Rule 4: Use coarse scales
Academic evidence: binary (PASS/FAIL) and 3-point (FAIL/PARTIAL/PASS) scales outperform 1–10 scales in inter-rater reliability. Use continuous 0.0–1.0 only for weighted aggregation, not for human-readable output.

### Rule 5: Order criteria by importance, not alphabetically
Evaluators (human and LLM) show recency and primacy effects. Put the most important criterion first AND last for robustness.

### Rule 6: Hard gates before soft scores
If any criterion is a hard requirement (code compiles, output is valid JSON), check it first as a binary gate before running weighted scoring. Do not average a hard failure into a 0.3 score — it should be a total failure.

---

## Criterion Independence Check

Before finalizing a rubric, check each pair of criteria:

> "Could an output score high on criterion A but low on criterion B without contradiction?"

If no: the criteria are correlated and should be merged into one.

**Common overlaps to avoid:**
- Accuracy + Correctness (same thing)
- Clarity + Readability (very high overlap)
- Completeness + Thoroughness (same thing)
- Conciseness + Brevity (same thing)

---

## Rubric Templates by Output Type

### Code Output
```python
CODE_RUBRIC = {
    "correctness": {
        "weight": 0.5,
        "definition": "The code produces the correct output for the given inputs. Hard gate — if tests fail, overall score is 0.",
        "scale": "binary",
        "examples": [
            {"output": "def add(a, b): return a - b", "score": 0.0, "reason": "Wrong operator"},
            {"output": "def add(a, b): return a + b", "score": 1.0, "reason": "Correct"},
        ]
    },
    "readability": {
        "weight": 0.3,
        "definition": "A developer unfamiliar with this codebase can understand the function's purpose from reading it without comments.",
        "scale": "0.0-1.0",
    },
    "error_handling": {
        "weight": 0.2,
        "definition": "The code handles invalid inputs gracefully (raises appropriate exceptions or returns sensible defaults).",
        "scale": "binary",
    }
}
```

### Text / Analysis Output
```python
TEXT_RUBRIC = {
    "accuracy": {
        "weight": 0.4,
        "definition": "All factual claims are verifiable and correct. No hallucinations or unsupported assertions.",
        "scale": "0.0-1.0",
    },
    "completeness": {
        "weight": 0.3,
        "definition": "The output addresses all parts of the original request. Nothing important is missing.",
        "scale": "0.0-1.0",
    },
    "clarity": {
        "weight": 0.3,
        "definition": "The main point is understandable without domain expertise and without re-reading.",
        "scale": "0.0-1.0",
    }
}
```

### Structured Data Output (JSON/YAML)
```python
STRUCTURED_RUBRIC = {
    "schema_validity": {
        "weight": 0.5,
        "definition": "Output parses without errors and matches the required schema. Hard gate.",
        "scale": "binary",
    },
    "completeness": {
        "weight": 0.3,
        "definition": "All required fields are present and non-null where required.",
        "scale": "0.0-1.0",
    },
    "data_accuracy": {
        "weight": 0.2,
        "definition": "Field values accurately represent the described entities.",
        "scale": "0.0-1.0",
    }
}
```

---

## Reliability Validation

After designing a rubric, validate it before use:

```python
def validate_rubric_reliability(rubric_fn, sample_outputs: list[str], threshold: float = 0.6) -> dict:
    """
    Run the rubric twice on the same outputs and measure consistency.
    Returns Cohen's kappa approximation.
    """
    scores_run1 = [rubric_fn(o)["overall_score"] for o in sample_outputs]
    scores_run2 = [rubric_fn(o)["overall_score"] for o in sample_outputs]

    # Simple correlation as reliability proxy
    import statistics
    diffs = [abs(a - b) for a, b in zip(scores_run1, scores_run2)]
    mean_diff = statistics.mean(diffs)
    reliability = 1.0 - mean_diff  # Rough approximation

    return {
        "reliability": round(reliability, 3),
        "reliable": reliability >= threshold,
        "mean_score_diff": round(mean_diff, 3),
        "recommendation": "Ready to use" if reliability >= threshold else "Rubric criteria too ambiguous — add examples or simplify"
    }
```

---

## Common Rubric Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| "Rate this 1–10" | Low inter-rater reliability | Use PASS/FAIL or 3-point scale |
| "Is this good?" | No operational definition | Define exactly what "good" means for this criterion |
| "Accuracy, clarity, and helpfulness" | Three criteria in one prompt | Prompt each separately |
| Missing examples | High variance across runs | Add 1–2 calibration examples per criterion |
| >5 criteria | Criteria overlap; diluted signal | Merge or drop until ≤5 |
| Vague weights | All criteria treated equally | Assign weights that reflect business priority |
