---
title: "Skill templates"
tags:
  - skills
  - templates
  - agent
  - copilot
  - claude
date_created: 2026-04-02
date_changed: 2026-04-02
---

# Skill templates

Ready-to-fill templates for each skill type. Copy the matching template into a new `SKILL.md`, fill
in `[placeholders]`, and remove unused sections.

XML tags are used throughout to separate content types — instructions, context, constraints, and
examples are unambiguous to Claude when wrapped in semantic tags. Read
[references/xml-tags.md](../references/xml-tags.md) for canonical tag names, nesting patterns, and
the HTML-collision warning (avoid HTML tag names like `<div>`, `<p>`, etc.).

---

## Template: Knowledge / Reference skill

````markdown
---
name: [domain-name]
description: >
  Use when working with [domain/library/API/platform]. Contains [specific facts: conventions,
  non-obvious behaviors, error codes, version-specific changes]. Load automatically when the user
  mentions [keyword1], [keyword2], or works with [tool/file/system].
user-invocable: false
---

# [Domain] Reference

<context>

[Background the reader needs to apply the rules below. What is this domain?
Who uses it? What problem does it solve? Keep to 2–4 sentences — not an intro for beginners,
just enough orientation so the rules make sense.]
</context>

## [Key concept 1]

<rules>

- [The non-obvious facts. Not what this thing is — what the agent would get wrong without being told.]
- [State each rule with its reason: "X is required because Y" is stronger than just "do X".]
</rules>

## [Key concept 2]

<rules>

- [...]
</rules>

## Gotchas

<gotchas>

- [Behavior that defies reasonable assumptions, e.g., "soft deletes require WHERE deleted_at IS NULL
  — the ORM will not add this automatically"]
- [Edge case that silently produces wrong output if the rule is not followed]
</gotchas>

<examples>
<example>

Input: [realistic user request or code snippet]
Output: [correct agent behavior or output]
</example>
</examples>
````

---

## Template: Workflow / Process skill

```markdown
---
name: [workflow-name]
description: >
  Use when [triggering situation, e.g., "deploying a service", "submitting a PR",
  "running onboarding"]. Guides through [what the workflow produces]. Always use this skill
  rather than improvising the process — the sequence matters.
argument-hint: "[service name] [environment]"
---

# [Workflow Name]

<context>

[One sentence: why the sequence matters. What goes wrong if steps are skipped or reordered.]
</context>

<prerequisites>

Before starting, confirm:
- [ ] [prerequisite 1]
- [ ] [prerequisite 2]
</prerequisites>

## Step 1: [Action]

<instructions>

[Why this step is first and what it ensures]
Do: [specific action]
</instructions>

<validation>

Expected result: [what success looks like]
How to verify: [command to run or condition to check]
</validation>

<recovery>

If this fails: [corrective action before moving to Step 2]
</recovery>

## Step 2: [Action]

<instructions>

[...]
</instructions>

<validation>

[...]
</validation>

## Step N: Review with user

<checkpoint>

Share the results of Step N-1 with the user and ask:
- [question 1]
- [question 2]
Only proceed when the user confirms.
</checkpoint>

## Completion criteria

<rules>

The workflow is complete when:
- [ ] [observable outcome 1]
- [ ] [observable outcome 2]
</rules>
````

---

## Template: Tool-augmented skill

````markdown
---
name: [tool-skill-name]
description: >
  Use when [task that requires specific tools]. Uses [tool1] and [tool2]. Do not use generic
  alternatives — [tool1] is required for [specific reason].
---

# [Tool] Usage

<context>

[One sentence on what this tool does and why it's the right choice for this task.]

Required tools:
- **[tool1]**: [what it does; where to install it if non-standard]
- **[tool2]**: [...]
</context>

## [Primary task]

<instructions>

[One sentence on when to run this.]
Run the following command (request terminal permission first):
</instructions>

<command>

```bash
[exact command with <placeholder> for variable parts]
```
</command>

<example_run>

Input: [sample file path or argument]
Output: [expected output indicating success]
</example_run>

<error_handling>

If the command fails with "[common error message]":
[resolution steps — be specific, not "check the docs"]
</error_handling>

## [Secondary task if needed]

<instructions>

[...]
</instructions>

<command>

```bash
[exact command]
```
</command>

## Gotchas

<gotchas>

- [Non-obvious flag or behavior — state the reason it matters]
- [...]
</gotchas>
````

---

## Template: Code generation / Template skill

````markdown
---
name: [codegen-skill-name]
description: >
  Use when generating [what], for [framework/language], matching [project conventions]. Use instead
  of writing [thing] from scratch — the template enforces [key constraints].
argument-hint: "[component name] [brief description of purpose]"
---

# [Output type] generation

<instructions>

Generate [output type] using the template below. Fill in every `[placeholder]`; keep all
other parts verbatim. The structure cannot change — it enforces [key constraint].

[If the template is >50 lines, move it to assets/ and reference it here:]
Read the template from [assets/template-name.md](assets/template-name.md) and fill it in.
</instructions>

<template>

[The exact output structure the agent fills in.
Use [FILL: description] for parts the agent writes.
Add inline comments to explain constraints on specific sections:
e.g., # NEVER change this import — it enables X]
</template>

<constraints>

- [Non-obvious constraint — stated with reason, not just the rule]
- [What to never change in the template and why]
</constraints>

<validation>
After generating, verify:
- [ ] [check 1, e.g., "no unused imports"]
- [ ] [check 2, e.g., "barrel export added to index.ts"]
</validation>
````

---

## Template: Analysis / Review skill

````markdown
---
name: [review-skill-name]
description: >
  Use when reviewing [what kind of artifact] for [what criteria]. Produces a structured report
  with [findings format]. Use for [specific trigger contexts], even if the user doesn't explicitly
  ask for a formal review.
---

# [Review type]

<instructions>

Review [artifact] against the criteria below. Produce a report using the format in
`<output_format>` at the end of this skill. Cite specific file paths and line numbers for every
finding.
</instructions>

<criteria>
<category name="[Category 1]">

- **[Criterion]:** [What to check. Pass = [X]. Fail = [Y].]
- **[Criterion]:** [...]
</category>

<category name="[Category 2]">

- **[Criterion]:** [...]
</category>
</criteria>

<output_format>

## [Review type] report

### Summary

[1–2 sentence overall assessment]

### Findings

| Severity | Finding | Location | Recommendation |
| --- | --- | --- | --- |
| High/Med/Low | [description] | [file:line] | [action] |

### Verdict

[Pass / Needs changes / Fail] — [reason]
</output_format>

<rules>

If the review involves [specific domain], read [references/domain.md](references/domain.md) for the full criteria list before proceeding.
</rules>
````

---

## Template: Meta-skill (skill that builds skills)

````markdown
---
name: [meta-skill-name]
description: >
  Use when creating, improving, or reviewing a skill for [agent/platform]. Guides through
  understanding the user's intent, classifying the skill type, researching the domain, drafting, and iterating with feedback. Use when the user says "create a skill", "write a SKILL.md", or "make Claude do X every time".
argument-hint: "[domain or goal for the skill]"
---

# Build a skill for [platform]

<context>

This is a workflow skill — it produces a SKILL.md. Follow the steps below in order.
Do not skip the interview step even if the user has already described what they want.
</context>

## Step 1: Interview the user

<instructions>

Use vscode_askQuestions with:
- "What should this skill help you do?" [free text]
- "What type of skill is this closest to?" — Reference/Knowledge, Workflow, Code generation,
  Analysis/Review, Something else
- "Do you have existing docs, code, or examples to base it on?" — Yes, No
- "Who will use this skill?" — Just me, My team, Anyone

If the user said "create a skill for X" without detail, also ask:
- "What does success look like? What should the agent produce or do differently?"
</instructions>

## Step 2: Research the domain

<instructions>

- If the user lacks documentation for the domain, use fetch_webpage to retrieve the relevant docs URL.
- Read references/skill-types.md to confirm the skill type classification.
- Summarize findings in `references/gathered_knowledge.md`.
</instructions>

## Step 3: Draft the skill

<instructions>

Read assets/skill-templates.md and select the template matching the skill type.
Fill every placeholder. Apply XML tags to separate instructions, context, rules, and examples.
Read references/xml-tags.md for canonical tag names.
</instructions>

## Step 4: Review with user and iterate

<checkpoint>

Share the draft and ask:
- "Does this match what you had in mind?"
- "What would you change or add?"

Revise until the user confirms it's correct.
</checkpoint>

## Step 5: Validate the description

<instructions>

Ask the user to try 3 example prompts that should trigger the skill and 2 that should not.
Read references/optimizing-descriptions.md if description triggering needs improvement.
</instructions>

<rules>

The skill is complete when:
- [ ] User confirms the output matches their intent
- [ ] Skill activates on representative "should trigger" prompts
- [ ] Skill does NOT activate on unrelated prompts
</rules>
````
