---
title: "XML tags in agent skills"
tags:
  - xml
  - prompting
  - claude
  - skills
  - structured-prompting
date_created: 2026-04-02
date_changed: 2026-04-02
---

# XML tags in agent skills

XML tags are the primary mechanism for disambiguating content types inside a SKILL.md. Claude was
trained on XML-structured corpora and parses named tags with higher fidelity than prose formatting.
When a SKILL.md mixes instructions, context, variable inputs, and examples, XML tags eliminate
ambiguity about which part of the text the agent should follow vs. read as data.

> [!NOTE]
> Source: <https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/use-xml-tags>

## HTML collision warning

> [!WARNING]
> Never use standard HTML tag names inside SKILL.md files. GitHub's markdown renderer and many
> preview tools will interpret them as formatting markup, stripping the tags from the text the
> agent sees.

Tags to **avoid** (reserved by HTML):

| Avoid | Reason |
| --- | --- |
| `<div>`, `<p>`, `<span>` | Block/inline display elements |
| `<b>`, `<i>`, `<em>`, `<strong>` | Text formatting |
| `<code>`, `<pre>` | Code formatting |
| `<a>`, `<img>` | Link/media |
| `<table>`, `<tr>`, `<td>` | Table structure |
| `<script>`, `<style>` | Code injection risk |

Use **semantic, domain-specific names** instead — they pass through markdown renderers untouched
and are more meaningful to Claude.

## Universal tags (usable in any skill type)

| Tag | Purpose | When to use |
| --- | --- | --- |
| `<instructions>` | The agent's directive | Wrapping the primary behavioral rule set |
| `<context>` | Background the agent needs | Domain knowledge, project constraints |
| `<input>` | Variable user-supplied data | Placeholders the user fills at invocation time |
| `<examples>` | Multi-example container | Wrapping a set of `<example>` blocks |
| `<example>` | Single few-shot example | Each input/output pair in few-shot prompting |
| `<warning>` | Critical constraint | Non-negotiable rules; things that break silently if ignored |
| `<rules>` | Enumerated constraints | Ordered list of constraints applied uniformly |
| `<output_format>` | Expected output shape | Describes what the final response must look like |

## Type-specific canonical tags

### Knowledge / Reference skills

```markdown
<context>

[Background the agent needs before applying any rule in this skill]
</context>

<rules>

- [Rule 1 — stated with the reason it exists]
- [Rule 2]
</rules>

<gotchas>

- [Behavior that defies reasonable assumptions]
- [Edge case that breaks the happy path]
</gotchas>

<examples>
<example>

Input: [...]
Output: [...]
</example>
</examples>
```

### Workflow / Process skills

```markdown
<prerequisites>

- [ ] [Thing that must be true before starting]
</prerequisites>

<steps>
<step n="1">
<instructions>

[Exact action to take]
</instructions>
<validation>

[How to confirm the step succeeded]
</validation>
<recovery>

If this fails: [corrective action]
</recovery>
</step>

<step n="2">

...
</step>
</steps>

<checkpoint>

Pause and confirm with the user before proceeding:
- [Question 1]
- [Question 2]
</checkpoint>
```

### Tool-augmented skills

````markdown
<command>

```bash
[exact command with <placeholder> for variable parts]
```

</command>

<example_run>

Input: [sample input]
Output: [expected output indicating success]
</example_run>

<error_handling>

If the command fails with "[common error message]":
[resolution steps]
</error_handling>
````

### Code generation / Template skills

````markdown
<template>

[The exact output structure the agent fills in.
Use [FILL: description] for parts the agent writes.
Keep everything else verbatim.]
</template>

<constraints>

- [Non-obvious constraint — stated with reason]
- [What to never change in the template]
</constraints>

<output_format>

[Description of the final file/artifact produced]
</output_format>

<validation>

After generating, verify:
- [ ] [Check 1]
- [ ] [Check 2]
</validation>
````

### Analysis / Review skills

````markdown
<criteria>
<category name="[Category 1]">

- **[Criterion]:** [What to check. Pass = [X]. Fail = [Y].]
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
````

## Nesting patterns

Nest tags when content has a natural hierarchy. Follow the Anthropic convention for multi-document
inputs:

````markdown
<documents>
<document index="1">

<source>[URL or file path]</source>
<document_content>

[Full text of document]
</document_content>
</document>

<document index="2">
...
</document>
</documents>
````

For few-shot examples, always wrap the set in `<examples>` and each item in `<example>`:

````markdown
<examples>
<example>

<input>Analyze this function for security issues: [code]</input>
<output>

## Security analysis report

### Findings
| Severity | Finding | Location | Recommendation |
| --- | --- | --- | --- |
| High | SQL injection via string concat | line 12 | Use parameterized queries |
</output>
</example>
</examples>
````

## Anti-patterns

| Anti-pattern | Problem | Fix |
| --- | --- | --- |
| Wrapping every line | XML overhead with no disambiguation gain | Only wrap content types that would be ambiguous without tags |
| Generic tag names (`<text>`, `<data>`, `<info>`) | Meaningless to Claude — no semantic signal | Use domain-specific names: `<criteria>`, `<constraints>`, `<command>` |
| HTML tag names | Stripped or mis-rendered by markdown parsers | Use non-HTML semantic names |
| Mixing XML structure with markdown headers | Creates two parallel structure systems; Claude has to reconcile both | Choose one: use XML for structure inside a section, markdown headers for top-level section boundaries |
| Over-nesting (4+ levels deep) | Hard to read; Claude may misparse deep nesting | Keep nesting to 2–3 levels maximum |

## When XML tags are NOT needed

- Short, single-purpose instructions with no mixed content types
- Skills that consist entirely of enumerated rules (a plain markdown list is cleaner)
- Simple command references where the structure is obvious from markdown code fencing

> [!TIP]
> If a colleague reading the raw text could confuse whether a sentence is an instruction, an
> example, or input data — add XML tags. If the structure is obvious without them, don't.
