# Skill Templates

Ready-to-fill templates for each skill type. Copy the matching template into a new `SKILL.md`, fill in the `[placeholders]`, and remove unused sections.

---

## Template: Knowledge / Reference skill

```markdown
---
name: [domain-name]
description: Use when working with [domain/library/API/platform]. Contains [specific facts: conventions, non-obvious behaviors, error codes, version-specific changes]. Load automatically when the user mentions [keyword1], [keyword2], or works with [tool/file/system].
user-invocable: false
---

# [Domain] Reference

## [Key concept 1]
[The non-obvious facts. Not what this thing is — what the agent would get wrong without being told.]

## [Key concept 2]
[...]

## Gotchas
- [Thing that defies reasonable assumptions, e.g., "soft deletes require WHERE deleted_at IS NULL"]
- [...]
```

---

## Template: Workflow / Process skill

```markdown
---
name: [workflow-name]
description: Use when [triggering situation, e.g., "deploying a service", "submitting a PR", "running onboarding"]. Guides through [what the workflow produces]. Always use this skill rather than improvising the process — the sequence matters.
argument-hint: [optional context the user provides, e.g., "[service name] [environment]"]
---

# [Workflow Name]

[One sentence: why the sequence matters. What goes wrong if steps are skipped or reordered.]

## Checklist

Before starting, confirm:
- [ ] [prerequisite 1]
- [ ] [prerequisite 2]

## Steps

**Step 1: [Action]**
[Why this step is first / what it ensures]
Do: [specific action]
Validate: [how to verify it worked]
If this fails: [recovery action]

**Step 2: [Action]**
[...]

**Step N: Review with user**
Share the results of [step N-1] with the user and ask:
- [question 1]
- [question 2]
Only proceed when the user confirms.

## Completion criteria
The workflow is complete when:
- [ ] [observable outcome 1]
- [ ] [observable outcome 2]
```

---

## Template: Tool-augmented skill

```markdown
---
name: [tool-skill-name]
description: Use when [task that requires specific tools]. Uses [tool1] and [tool2]. Do not use generic alternatives — [tool1] is required for [specific reason].
---

# [Tool] Usage

## Required tools
- **[tool1]**: [what it does, where it comes from if non-standard]
- **[tool2]**: [...]

## [Primary task]

[One sentence on when to run this.]

Run this command (request terminal permission first):
```bash
[exact command with <placeholders> for variable parts]
```

Expected output: [what success looks like]
If it fails with "[common error]": [resolution]

## [Secondary task if needed]

[...]

## Gotchas
- [Non-obvious flag or behavior]
- [...]
```

---

## Template: Code generation / Template skill

```markdown
---
name: [codegen-skill-name]
description: Use when generating [what], for [framework/language], matching [project conventions]. Use instead of writing [thing] from scratch — the template enforces [key constraints].
argument-hint: "[component name] [brief description of purpose]"
---

# [Output type] generation

Generate [output type] using the template below. Fill in `[placeholders]`; keep all other parts as-is.

[If the template is short, inline it here. If >50 lines, reference `assets/template-[name].md`:]
Read the template from [assets/template-name.md](assets/template-name.md) and fill it in.

## Constraints
- [Non-obvious constraint the agent must respect]
- [...]

## Validation
After generating, verify:
- [ ] [check 1, e.g., "no unused imports"]
- [ ] [check 2]
```

---

## Template: Analysis / Review skill

```markdown
---
name: [review-skill-name]
description: Use when reviewing [what kind of artifact] for [what criteria]. Produces a structured report with [findings format]. Use for [specific trigger contexts], even if the user doesn't explicitly ask for a formal review.
---

# [Review type]

Review [artifact] against the criteria below. Produce a report using the format at the end of this skill.

## Criteria

### [Category 1]
- **[Criterion]:** [What to check. What pass/fail looks like.]
- **[Criterion]:** [...]

### [Category 2]
- [...]

## Report format

```
## [Review type] Report

### Summary
[1-2 sentence overall assessment]

### Findings

| Severity | Finding | Location | Recommendation |
|---|---|---|---|
| [High/Med/Low] | [description] | [file:line] | [action] |

### Verdict
[Pass / Needs changes / Fail] — [reason]
```

## References
If the review involves [specific domain], read [references/domain.md](references/domain.md) for the full criteria list.
```

---

## Template: Meta-skill (skill that builds skills)

```markdown
---
name: [meta-skill-name]
description: Use when creating, improving, or reviewing a skill for [agent/platform]. Guides through understanding the user's intent, classifying the skill type, researching the domain, drafting, and iterating with feedback. Use when the user says "create a skill", "write a SKILL.md", or "make Claude do X every time".
argument-hint: "[domain or goal for the skill]"
---

# Build a skill for [platform]

This is a workflow skill — it produces a SKILL.md. Follow the steps below in order. Do not skip the interview step even if the user has already described what they want.

## Step 1: Interview the user

Use vscode_askQuestions with:
- "What should this skill help you do?" [free text]
- "What type of skill is this closest to?" [Reference/Knowledge, Step-by-step workflow, Code generation template, Code review/analysis, Something else]
- "Do you have existing docs, code, or examples to base it on?" [Yes — share them / No]
- "Who will use this skill?" [Just me, My team, Anyone]

If the user said "create a skill for X" without detail, also ask:
- "What does success look like? What should the agent produce or do differently?"

## Step 2: Research the domain

[Add domain research instructions here, e.g.:]
If the user lacks documentation for the domain, use fetch_webpage to retrieve [relevant docs URL]. Read references/skill-types.md to confirm the skill type classification.

## Step 3: Draft the skill

[Add drafting instructions referencing appropriate template from assets/skill-templates.md]

## Step 4: Review with user and iterate

Share the draft and ask:
- "Does this match what you had in mind?"
- "What would you change or add?"

Revise until the user confirms it's correct.

## Step 5: Validate the description

Test the description triggers correctly. Ask the user to try 3 example prompts and confirm the skill activates on the right ones.

Read [references/optimizing-descriptions.md](references/optimizing-descriptions.md) if description triggering needs improvement.
```
