---
name: agentic-eval
description: |
  Use this skill when adding self-critique, reflection, or iterative quality improvement to an agent workflow. Triggers on "add evaluation loop", "implement reflect-and-refine", "self-critique my output", "add LLM-as-judge scoring", "build evaluator-optimizer", "improve output quality automatically", "add rubric-based scoring", "code refinement loop", "test-driven generation", or "how do I know my agent output is good enough". Also triggers when asked to design or validate an evaluation rubric for agent outputs.
argument-hint: "[task type: code | text | structured] [evaluation pattern: reflect | evaluator-optimizer | llm-judge | rubric] [quality threshold if known]"
user-invocable: true
---

# Agentic Evaluation Patterns

A **workflow skill** — follow steps in order. Each step has an explicit reason; skipping steps produces garbage evals that score high but don't track quality.

The key insight: **invest 80% of your effort in rubric design, 20% in the loop**. A poor rubric with a perfect loop still produces meaningless results. A good rubric with a simple loop improves output reliability dramatically.

## Step 1: Identify task type and success criteria

Before writing any code, determine:

1. **What type of output is being evaluated?**
   - Code → Pattern 3 (test-driven) is usually best
   - Text/reports → Pattern 1 (reflect-and-refine) or Pattern 4 (LLM-as-judge)
   - Structured data (JSON, schemas) → Pattern 5 (rubric-based with per-criterion prompting)

2. **What does "good enough" mean for this task?**
   - Is there a ground truth (test cases, reference output)? → Use objective eval
   - Is it subjective (style, clarity, persuasiveness)? → Need LLM-as-judge with rubric
   - Is it a mix? → Combine: objective criteria (correctness) + subjective criteria (clarity)

3. **What are the hard constraints?**
   - Token budget per iteration? (5 iters × 3K = 15K per run)
   - Latency requirements? (self-critique is fast; external judge adds a full LLM call)
   - Stakes? (Low → 3 iterations is fine; High → use external evaluator + human spot-check)

**Why this matters**: choosing the wrong pattern produces evals that look correct but aren't measuring what you care about. Pattern selection cannot be undone without rewriting the loop.

## Step 2: Select the evaluation pattern

Use the decision matrix:

| Situation                                                      | Pattern              | Notes                                         |
| -------------------------------------------------------------- | -------------------- | --------------------------------------------- |
| Fast iteration, low stakes                                     | 1 — Reflect-Refine   | Cheap, but agent is soft on its own mistakes  |
| Separate generator and evaluator responsibilities needed       | 2 — Evaluator-Optimizer | Clear separation; scalable                 |
| Generating code with runnable tests                            | 3 — Code Reflection  | Tests are ground truth; no LLM judge needed   |
| Comparing multiple outputs or approaches                       | 4 — LLM-as-Judge     | Must run pairwise in both orders (bias)       |
| Multi-dimensional quality (style + accuracy + format + ...)    | 5 — Rubric-Based     | Prompt each criterion separately (LLM-Rubric) |

**Load [references/patterns.md](references/patterns.md) for the Python implementation of whichever pattern you selected.**

Default recommendation: Pattern 2 (Evaluator-Optimizer) for text/reports; Pattern 3 (Code Reflection) for code. Avoid Pattern 1 for anything quality-critical — self-critique is systematically lenient.

## Step 3: Design the rubric

This is the highest-leverage step. Read [references/rubric-design.md](references/rubric-design.md) for the 8 design rules, templates by output type, and the independence validation method.

Critical rules (non-negotiable):

- **3–5 dimensions max**. More than 5 means dimensions overlap and scores become meaningless.
- **Each dimension must be independently variable** — you must be able to construct an output that scores high on one and low on another. If not, they overlap; merge them.
- **Use quantitative anchors**: "5 = all required sections present; 4 = missing ≤ 1 section" not "5 = excellent."
- **Include at least one negative criterion**: "contains no hallucinated information", "does not exceed word limit."
- **Test the rubric on 3–5 known outputs** (including at least one known-bad) before using it in the loop. If a known-bad output scores > 0.6, the rubric is broken.

**Calibration**: after rubric design, run it 3 times on the same output. If score variance > 10%, the anchors are too vague. Fix before proceeding.

Academic basis: ACL 2024 LLM-Rubric found that prompting each criterion in a separate LLM call increases reliability by 15–20%. Autorubric 2025 established Cohen's kappa < 0.6 = rubric is too ambiguous for autonomous use.

## Step 4: Implement the loop

Pull the implementation from [references/patterns.md](references/patterns.md) for your chosen pattern. Wire in:

- Your rubric (from Step 3) as the evaluation function
- A `max_iterations` cap — default **3** for most tasks; 5 for quality-critical; never > 7
- A convergence check: if `score_delta < 0.02` for 2 consecutive iterations → stop early
- A feedback formatter: pass structured JSON feedback (not prose) to the refiner

**Bias protections to apply:**

| Bias                | Mitigation                                                             |
| ------------------- | ---------------------------------------------------------------------- |
| Self-preference     | Never use the same model as both generator and judge                   |
| Positional bias     | For pairwise: run both orderings (A vs B AND B vs A); take consensus   |
| Length bias         | Explicitly add "brevity is valued" as a rubric criterion               |
| Evaluation noise    | Run evaluator 3× per iteration; use average score                      |
| Confidence paradox  | Add "claims certainty only when justified" as an explicit criterion    |

Load [references/failure-modes.md](references/failure-modes.md) if the loop behaves unexpectedly after implementation.

## Step 5: Validate and calibrate

Before using the loop in production:

1. **Run on 5 diverse inputs** and check that score changes track actual quality changes
2. **Test on a known-bad output**: if it scores > 0.6/1.0, the rubric is miscalibrated
3. **Check score delta per iteration**: if iteration 2 and 3 have identical scores, the refinement prompt isn't producing different outputs
4. **Spot-check 10% of outputs manually**: if your LLM eval score correlation with human judgment is < 0.7 (Pearson), fix the rubric before scaling

**Convergence thresholds by task:**

| Task type          | Min threshold (pass) | Plateau = stop when delta < |
| ------------------ | -------------------- | ----------------------------- |
| Creative/style     | 0.65                 | 0.03 for 2 consecutive iters  |
| Analysis/reports   | 0.75                 | 0.02 for 2 consecutive iters  |
| Code correctness   | 0.90                 | Tests pass = done             |
| Factual accuracy   | 0.85                 | 0.02 for 2 consecutive iters  |

## Step 6: Integrate with domain knowledge and skill structure

For domain-specific evaluation criteria (e.g., evaluating medical summaries, legal documents, API design quality):

1. Invoke `/research` to fetch current best practices and domain-specific quality criteria from authoritative sources
2. Incorporate domain criteria as named rubric dimensions (not vague overrides of existing ones)
3. If the evaluation logic is complex enough to be reused, invoke `/skills-best-practices` to package it as a standalone evaluation skill — this keeps the parent workflow clean and makes the rubric reusable

If you're building the evaluation as a sub-skill: the rubric goes in the sub-skill's `references/rubric.md`; the loop implementation goes in the sub-skill's `scripts/`; the parent skill only calls the sub-skill by name.

---

## Quick reference: iteration count

- **3 iterations**: default. 60–70% quality improvement for most tasks. Sweet spot.
- **5 iterations**: quality-critical outputs (code for production, formal reports).
- **7+ iterations**: only with train/validation split to detect overfitting. Stop when validation score plateaus.

**Golden rule**: if score plateaus for 2 consecutive iterations (delta < 0.02), stop immediately. You are optimizing noise, not improving the output.

---

## References

| File                                                                   | Load when                                                           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [references/patterns.md](references/patterns.md)                       | Implementing any evaluation pattern (Python code inside)           |
| [references/rubric-design.md](references/rubric-design.md)             | Designing or debugging a rubric in Step 3                          |
| [references/failure-modes.md](references/failure-modes.md)             | Loop behaves unexpectedly (loop, gaming, bias, noise, wrong output) |
| [references/gathered_knowledge.md](references/gathered_knowledge.md)   | Academic citations needed; deep dive on LLM judge bias research    |

Scripts for standalone use (CLI-runnable):

| Script                                                       | What it does                                          |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| [scripts/eval_loop.py](scripts/eval_loop.py)                 | Core evaluator-optimizer loop (Patterns 1+2 combined) |
| [scripts/rubric_scorer.py](scripts/rubric_scorer.py)         | Per-criterion rubric scoring (Pattern 5)              |
| [scripts/llm_judge.py](scripts/llm_judge.py)                 | Bias-resistant pairwise judge (Pattern 4)             |
| [scripts/code_reflector.py](scripts/code_reflector.py)       | Test-driven code refinement (Pattern 3)               |
