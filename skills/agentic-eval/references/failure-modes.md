# Failure Modes: Diagnosis and Fixes

When an evaluation loop is not working, use this guide to identify the root cause and fix it.

---

## Failure 1: Loop Always Hits max_iterations

**Symptom**: The loop never stops early. Every run uses all iterations and may still produce poor output.

**Diagnosis checklist:**
1. Is the refinement prompt producing meaningfully different outputs? Log output similarity between iterations — if >80% identical, the refinement prompt is not working.
2. Is the pass_threshold set too high? Try lowering to 0.75 to see if it stops.
3. Is the evaluator providing actionable feedback? If feedback is "the output could be better", the refine prompt has nothing to work with.
4. Is convergence detection enabled? If not, add it.

**Fixes:**
- Add similarity check: if `edit_distance(prev, current) / len(prev) < 0.2`, stop — it's not changing.
- Make the `optimize()` prompt more directive: "Address specifically: {feedback}. Do not change anything else."
- Check if the criteria are achievable — sometimes the bar is set impossible and no output can pass.

---

## Failure 2: Score Improves But Quality Doesn't

**Symptom**: The loop terminates early with a high score, but the output is still bad by human judgment.

**Root cause**: Evaluation gaming — the generator has learned to optimize for the evaluator's signals rather than the underlying task.

**Diagnosis**: Add a held-out human evaluation or a ground-truth check on a sample of "passing" outputs.

**Fixes:**
- Use a **different model** for generation and evaluation (prevents same-model self-preference).
- Add a hard-coded ground-truth check as a gate before the rubric score matters.
- Blind the evaluator to the original task when possible — only show the output and the criteria.
- Rotate evaluation criteria order to prevent the generator from gaming ordering effects.

---

## Failure 3: LLM Judge Always Prefers One Output

**Symptom**: In comparative evaluation, the judge always picks the first candidate, or always picks the longest output.

**Root cause**: Positional bias or verbosity bias (confirmed by arXiv:2406.07791 and CALM framework, ICLR 2025).

**Diagnosis**: Run the same comparison with positions swapped. If the judge changes its verdict, positional bias is present.

**Fixes:**
- Always run pairwise comparisons in **both orders** and average results (see patterns.md Pattern 4).
- Add explicit anti-verbosity instruction: "Do not prefer longer outputs. Rate conciseness as a criterion."
- Use absolute scoring (rate each output independently on a rubric) instead of pairwise comparison.
- Switch to a different judge model — different models have different bias profiles.

---

## Failure 4: Self-Critique Too Lenient

**Symptom**: When using Basic Reflection (Pattern 1), the agent almost always scores its own output as passing on the first iteration. No meaningful improvement happens.

**Root cause**: Self-preference bias — agents grade their own work on a curve (confirmed by arXiv:2410.21819, NeurIPS 2024).

**Diagnosis**: Compare self-critique scores to scores from an external evaluator call on the same outputs. If self-critique scores are consistently 15%+ higher, the bias is confirmed.

**Fixes:**
- Switch to Pattern 2 (Evaluator-Optimizer) with a **separate LLM call** as evaluator.
- In the self-critique prompt, add: "Be strict and critical. Assume the reader will reject any output that does not fully meet all criteria."
- Use a chain-of-thought preamble that forces the evaluator to find problems before scoring: "First, list everything wrong with this output. Then, score it."

---

## Failure 5: Structured Output Parse Failures

**Symptom**: JSON parse errors crash the loop. `json.loads()` raises `JSONDecodeError`.

**Root cause**: LLMs occasionally generate JSON with markdown formatting (`json ... `), trailing commas, or comment syntax.

**Fix pattern:**
```python
import json, re

def safe_parse_json(raw: str) -> dict:
    """Robust JSON parser with multiple fallback strategies."""
    # Strategy 1: Direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Strategy 2: Extract JSON from markdown code block
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # Strategy 3: Find first complete JSON object
    match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)?\}', raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    # Strategy 4: Return safe default
    return {"overall_score": 0.5, "feedback": "parse_failed", "passed": False}
```

**Prevention**: Use Pydantic with `.model_validate_json()` which is more tolerant. Or use an LLM SDK's structured output mode (Anthropic tool_use, OpenAI response_format) to enforce JSON at the API level.

---

## Failure 6: Criteria Overlap Inflates Scores

**Symptom**: Scores are consistently high (0.85+) but outputs are mediocre. Different criteria produce very similar scores across all outputs.

**Root cause**: Criteria are correlated — "accuracy" and "correctness" measure the same thing, so the rubric double-counts.

**Diagnosis**: Run the rubric on 5 diverse outputs (some good, some bad). If two criteria have correlation > 0.8 across outputs, they overlap.

**Fix**: Merge overlapping criteria into one. Prefer fewer, more orthogonal criteria over many correlated ones. See rubric-design.md for independence check.

---

## Failure 7: Verbosity Creep

**Symptom**: After 2+ iterations, outputs get progressively longer without improving quality. The evaluator keeps passing them because "more complete" is confused with "better".

**Root cause**: Refinement prompts that say "improve and expand" cause the generator to add content rather than fix problems.

**Fix**: Add "Do not add new content. Only fix the specific issues listed." to refine prompts. Add a `max_length` criterion to the rubric if conciseness matters.

---

## Failure 8: Loop Terminates Correctly But Final Output Is Wrong Iteration

**Symptom**: Iteration 2 was better than iteration 3, but the loop returns iteration 3 (the last one).

**Root cause**: Not tracking the best-scored iteration separately from the latest.

**Fix**: Always maintain a `best = {"output": ..., "score": 0.0}` variable and update it only when `score > best["score"]`. Return `best["output"]`, not the current `output` at loop end.

---

## Quick Diagnostic Checklist

When an eval loop isn't working, check in this order:

1. [ ] Is the refinement prompt producing different outputs? (check similarity)
2. [ ] Is the evaluator providing specific, actionable feedback? (not just "it could be better")
3. [ ] Is the same model judging its own outputs? (self-preference bias)
4. [ ] Are criteria independent and well-defined with examples?
5. [ ] Is JSON parsing robust with fallback strategies?
6. [ ] Is the best-iteration tracking in place?
7. [ ] Is convergence detection enabled (plateau stop)?
8. [ ] Is max_iterations set appropriately for the quality bar?
