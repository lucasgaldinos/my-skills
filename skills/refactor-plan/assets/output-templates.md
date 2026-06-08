# Output Templates — Three Modes

<context>

This file contains the three output templates the workflow produces in Step 5,
selected by the user's mode choice in Step 1.1: `analyze`, `plan`, or `apply`.
Fill every `[placeholder]`. Keep the structure verbatim — the headings are the
contract that downstream tools and reviewers rely on.
</context>

---

## Mode: `analyze` — inline report only

<template>

````markdown
# Refactor Analysis: <target>

## Scope

- Target: <file/folder/module>
- Motivation (from user): <Step 1.2 answer verbatim>
- Stated change axes: <Step 1.3 answer verbatim>
- Constraints: <Step 1.4 answer verbatim>

## Findings

### Smell 1: <name>

- Evidence: <file:line(s)>
- Category: Creational | Structural | Behavioral
- SOLID violation (if any): <SRP | OCP | LSP | ISP | DIP> — <why>
- Recommendation: <GoF pattern OR Fowler refactoring>
- Runner-up considered: <alternative> — rejected because <reason>
- Cost: <new files/classes, indirection added, test surface delta>
- Reversibility: <low | medium | high> — <why>

### Smell 2: <name>

<...repeat structure...>

## What is *not* recommended

- <Pattern X> would be premature here because <no observed change axis>.
- <Pattern Y> is tempting but the discriminator <question> points to <chosen> instead.

## Open questions for the user

- <Anything that affects the recommendation but wasn't covered>
````

</template>

<rules>

- Every recommendation MUST cite file:line evidence. No evidence → no recommendation.
- The "What is not recommended" section is mandatory — it documents alternatives
  considered and prevents reviewers from re-litigating the same questions.
</rules>

---

## Mode: `plan` — write to `spec/refactor-<short-name>.md`

<template>

````markdown
---
title: Refactor plan — <short descriptive name>
date_created: <YYYY-MM-DD>
owner: <team or user>
tags: [refactor, design-pattern, technical-debt]
---

# Introduction

<One paragraph: what is being refactored and why.>

## 1. Scope & Motivation

- Target: <file/folder/module>
- Motivation: <from interview>
- Change axes addressed: <list>
- Out of scope: <explicit exclusions>

## 2. Current state

<Findings from Step 2/3, with file:line evidence per smell.>

## 3. Proposed changes

For each change, provide:

- Change ID: REF-001
- Smell addressed: <name + evidence>
- Proposed pattern / refactoring: <name>
- Discriminator vs. runner-up: <why this and not the alternative>
- Mechanical steps (Fowler-level, in shippable order):
  1. <Extract Method on lines X-Y of file Z>
  2. <Move Method from A to B>
  3. <Introduce interface I, implement in classes C1, C2>
  4. ...
- Acceptance check: <how to verify this step is complete>

## 4. Sequencing & risk

- Order of changes: REF-001 → REF-002 → ... — <why this order>
- Reversal points: <after which change is the codebase still shippable>
- Test coverage prerequisites: <tests that must exist before each change>

## 5. Acceptance criteria

- Concrete, testable criteria drawn from interview Step 1.7:
  - [ ] <criterion 1>
  - [ ] <criterion 2>

## 6. Out of scope / explicit non-goals

- <What this plan deliberately does not change>

## 7. References

- <Link to design-patterns-intro.md sections for each pattern used>
- <Link to refactoring.guru pages if mirrored>
````

</template>

<rules>

- File location: prefer `spec/refactor-<short-name>.md` if a `spec/` folder exists in
  the workspace. Fall back to `plans/` or `docs/refactor/` only if `spec/` is absent.
- Each "Proposed change" must list mechanical Fowler-level steps, not just the
  pattern name. The plan must be executable by a reader who knows refactoring but not
  the codebase.
- The sequencing section is mandatory — refactor plans without explicit ordering
  produce merge conflicts and broken intermediate states.
</rules>

---

## Mode: `apply` — produce plan first, then edit files

<instructions>

The `apply` mode is `plan` followed by execution. Order of operations:

1. Produce the full plan exactly as in `plan` mode.
2. Pause for explicit user confirmation. Ask: "Apply REF-001 through REF-N as
   listed? (yes / no / partial)". Do not edit any file before confirmation.
3. For each REF-N in order:
   1. Make the file edits with `replace_string_in_file` or `multi_replace_string_in_file`.
   2. Run available tests/lint (request terminal permission per command).
   3. If any check fails, stop. Report failure with diff and decide rollback or
      continue with the user.
4. After all REF-N applied, produce the summary template below.
</instructions>

<template>

````markdown
# Refactor applied: <short name>

## Summary

- Plan: <link to spec/refactor-<short-name>.md>
- Changes applied: REF-001 ... REF-N
- Files modified: <list>
- LOC delta: +<added> / -<removed>

## Verification

- Tests: <pass | fail with details>
- Lint: <pass | fail with details>
- Build: <pass | fail with details>

## Acceptance criteria

- [ ] <criterion 1> — <met | not met>
- [ ] <criterion 2> — <met | not met>

## Follow-ups

- <Anything deferred from the plan to a later iteration, with reason>
````

</template>

<rules>

- Never apply without explicit user confirmation following the plan.
- Run tests/lint after every REF-N, not just at the end. Halting early on
  failure is cheaper than diagnosing a multi-step regression.
- If a step's tests fail and rollback is chosen, revert only that step's edits, not
  prior steps that passed.
</rules>

---

## Cross-mode constraints

<rules>

- Language-agnostic output. Do not assume any specific programming language unless
  the user's repo confirms it. Future per-language templates will live under
  `assets/templates/<language>/`; until then, describe steps in prose.
- Cite, don't paraphrase. When referencing user motivation, copy their words; do
  not summarize them — summaries lose the constraint signal.
- No pattern jargon without grounding. Every pattern name must be paired with the
  smell it addresses. "Apply Strategy" alone is not actionable; "Apply Strategy to
  replace the `if-elif-elif` block in `router.py:45-90` so new routing algorithms can
  be added without editing the router" is.
</rules>
