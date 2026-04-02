---
name: skills-best-practices
description: Use this skill when creating, reviewing, or improving any Agent Skill (SKILL.md) for GitHub Copilot, Claude Code, or any compatible agent. Triggers on "create a skill", "write a SKILL.md", "improve this skill", "fix my skill description", "skill isn't triggering", "agent keeps ignoring my skill", "make Claude always do X", "build a reusable workflow for Y", or any request to package a capability into an agent skill. Also triggers when the user wants to teach the agent something domain-specific and doesn't know how.
argument-hint: "[domain or goal for the skill] [any existing docs, code, or examples]"
user-invocable: true
---

# Build an Agent Skill

This is a **workflow meta-skill** — it produces a working SKILL.md. Follow the steps in order.
The key insight: getting the skill type right before writing anything saves every rewrite later.
Skills that don't match their type produce agents that are either too rigid (fails on edge cases) or too vague (misses the point entirely).

## Step 1: Interview the user

Before writing anything, use #tool:vscode/askQuestions to ask:

1. "What should this skill help you do? What's missing today that you want the agent to do automatically?"
2. "Do you have existing documentation, code, or examples I can base this on — or should I research the domain?"
3. "Who uses this skill?" → [Just me, My team, I'll share it publicly]
4. "Should the agent use this skill automatically when relevant, or only when you explicitly invoke it?"

If the user gave a one-liner like "make a skill for X", also ask:

- "What does success look like — what should the agent produce or do differently?"
- "Is there a specific sequence of steps, or is it more about 'knowing things'?"

Why this matters: without these answers, the skill type is guesswork. A workflow skill written as a reference skill (or vice versa) will fail the user even if every individual instruction is correct.

## Step 2: Classify the skill type

Read [references/skill-types.md](references/skill-types.md) to classify what the user needs. The classification determines everything about structure.

Use the quick table:

| The user wants...                                                   | Type                |
| ------------------------------------------------------------------- | ------------------- |
| Agent to "know" domain-specific facts, conventions, or API behavior | Knowledge/Reference |
| Agent to follow an exact multi-step process with order that matters | Workflow/Process    |
| Agent to use a specific tool, command, or API in a specific way     | Tool-augmented      |
| Agent to generate code/docs in a specific format consistently       | Code generation     |
| Agent to review/grade/check things against criteria                 | Analysis/Review     |
| Help building another skill                                         | Meta (this skill)   |

If unsure between two types, ask one clarifying question. Never guess and proceed — the wrong type produces a structurally wrong skill that requires a full rewrite.

## Step 3: Research the domain

If the user lacks documentation or says "I'm not sure how it works":

1. Use #tool:web/fetch to retrieve any official docs, API references, or specification pages the user provides.
2. If the user has no URL, ask: "Can you share a link to the documentation, or should I search for it?"
3. Read the fetched content and summarize what you found in a markdown file `[domain](?/skills/skill_name/references/gathered_knowledge.md)`, where the `gathered_knowledge.md` contains relevant information and the sources URL for it.
4. Present the content: "Here's what I found about `[domain](?/skills/skill_name/references/gathered_knowledge.md)` summarized and referenced.Does this match what you need the skill to know?"

Why this matters: a skill built on guessed domain knowledge will confidently give wrong instructions. The user came to you because they want better-than-improvised results. A skill that just restates general knowledge is worthless.

## Step 4: Draft the skill

Read [assets/skill-templates.md](assets/skill-templates.md) and use the template matching the classified skill type.

**Structural rules (apply to all types):**

- Keep `SKILL.md` body under 500 lines. Move anything not needed on every invocation to `references/` or `assets/`.
- Reference external files with an explicit condition: "Read references/X.md when `[specific situation](path/to/file)`" — not "see references/ for more."
- The `description` frontmatter is the only trigger mechanism. Write it imperatively: "Use this skill when..." and name actual user phrases, not internal mechanics.
- Tools are referenced by instruction, not called directly: "Use #tool:web/fetch to retrieve [URL] before answering any questions about..."

**For each skill type, what to emphasize:**

- **Knowledge/Reference**: The non-obvious facts. Not what the domain is — what the agent would get wrong without being told. Include a Gotchas section.
- **Workflow**: Step sequence with an explicit WHY for each step. Validation gate after each step. Explicit human checkpoints. Fallback if a step fails.
- **Tool-augmented**: Exact command with `<placeholders>`. One working example. Most likely error mode and recovery.
- **Code generation**: Template inline (or in `assets/`) that the agent fills in literally. Constraints annotated in the template itself.
- **Analysis/Review**: Rubric with pass/fail criteria for each item. Output report format as a concrete template.

**Explaining the why — the most important instruction:**
Don't just write rules. Explain why each rule matters. "Never use the `--force` flag" is weaker than "Never use `--force` — it bypasses the migration integrity check and can leave the schema in a partially migrated state that is difficult to recover from." The agent understands reasoning and can generalize it to edge cases not in the rule list. Rules without reasoning produce brittle skills.

## Step 5: Show the draft and get feedback

Show the complete draft to the user. Ask:

- "Does this match what you had in mind?"
- "Is there anything missing, wrong, or that you'd phrase differently?"
- "Can you try asking me something that should trigger this skill and tell me if it works?"

Revise based on feedback. Repeat until the user confirms it's correct.

## Step 6: Set up the folder structure

Create the skill directory and any needed subdirectories:

```
.github/skills/[skill-name]/
├── SKILL.md          ← required
├── references/       ← if you have domain docs or detailed criteria
└── assets/           ← if you have templates the agent fills in
```

If tool scripts are needed (e.g., validators, formatters), create `scripts/` and write them there. Reference from SKILL.md with explicit invocation instructions.

## Step 7: Validate the description

Ask the user to try 3–5 prompts that should trigger the skill and 2–3 that should not. If the skill fails to activate on "should trigger" prompts, read [references/optimizing-descriptions.md](references/optimizing-descriptions.md) for the description optimization loop.

Common description failures:

- Too narrow: skill should trigger on "deploy" but description only says "deployment pipeline"
- Too broad: skill triggers on everything code-related
- Mechanic-focused: description says what the skill does, not when to use it
- Missing indirect triggers: user asks for X without naming the skill's domain

## Stop conditions

Stop iterating when:

- The user confirms the skill does what they want
- The skill activates correctly on representative prompts
- The skill does NOT activate on unrelated prompts

---

## References

| File                                                                           | Load when                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| [references/skill-types.md](references/skill-types.md)                         | Classifying skill type in Step 2                                    |
| [references/vscode-agent-skills.md](references/vscode-agent-skills.md)         | Questions about VS Code frontmatter, tool access, or slash commands |
| [references/best-practices.md](references/best-practices.md)                   | Deep dive on progressive disclosure, calibration, and patterns      |
| [references/optimizing-descriptions.md](references/optimizing-descriptions.md) | Skill isn't triggering; need to test and improve description        |
| [assets/skill-templates.md](assets/skill-templates.md)                         | Getting the correct template for a skill type in Step 4             |
| [references/links.md](references/links.md)                                     | Pointers to official agentskills.io spec and VS Code docs           |
