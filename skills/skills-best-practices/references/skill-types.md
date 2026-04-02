# Skill Type Taxonomy

Skills are not all the same. Choosing the wrong type produces a skill that is either too brittle (over-specified for the wrong task) or too vague (generic instructions that don't help). Classify before you build.

---

## Type 1: Knowledge / Reference skill

**What it is:** Provides specialized knowledge the agent wouldn't reliably have — domain-specific APIs, project conventions, non-obvious configuration, version-specific changes.

**When to choose it:** The user knows what they want done. They just want the agent to know things it doesn't already know. No multi-step coordination needed.

**Signs you're in this type:**
- "I want Claude to know how our API works"
- "I want it to always use library X, not Y"
- "I want to teach it the conventions for this project"

**Structure:**
- SKILL.md body: short, declarative, declarative. No steps unless the knowledge itself has an order.
- No `scripts/`, rarely needs `assets/`
- `references/` only if there is a large amount of reference material (e.g., full API schema)
- `user-invocable: false` is common here — let the agent load it automatically when relevant

**Frontmatter description:** Must specify the *domain* and *what knowledge it contains*, not what the skill does. Example: `"Use when working with the Stripe API (v3), interacting with webhooks, or handling payment errors. Contains the project's API key patterns, idempotency conventions, and common error codes."`

**Body style:** Reference cards, tables, code examples. Concise. Trust the agent to apply knowledge intelligently — don't specify step-by-step how to use the knowledge.

**Gotcha — common mistake:** Writing a knowledge skill as if it's a workflow skill, adding numbered steps like "1. Read the API key from env. 2. Call the endpoint." Those steps are obvious to the agent. The skill's value is the non-obvious domain knowledge (e.g., "idempotency keys must be UUIDs, not arbitrary strings; the API rejects dashes").

**Example:** `claude-prompting-best-practices` (this repo) — provides Claude API behavior knowledge the agent wouldn't reliably recall.

---

## Type 2: Workflow / Process skill

**What it is:** Guides the agent through a multi-step process with decision points, validation gates, and feedback loops. The value is *sequence and coordination*, not knowledge.

**When to choose it:** The task has a correct order of operations. Skipping or reordering steps produces bad outcomes. There are multiple decision points where the agent needs to branch.

**Signs you're in this type:**
- "I want Claude to follow our exact deployment process"
- "I want it to go through a checklist before submitting code"
- "The process has back-and-forth with the user or tool results"

**Structure:**
- SKILL.md body: numbered steps, explicit decision points, validation gates
- `scripts/` for automated validators or formatters run between steps
- `assets/` for checklists, templates used during the workflow
- `references/` for domain knowledge loaded on demand
- Consider `user-invocable: true` so users can deliberately start the workflow

**Frontmatter description:** Specify the *workflow*, what triggers it, and what it produces. Example: `"Use when deploying a service, running a pre-release checklist, or doing a code review cycle. Guides through a step-by-step process with validation at each stage."`

**Body style:** Imperative steps. Tell the agent WHY each step matters, especially for steps that seem redundant. Use `- [ ]` checklists for multi-step workflows. Include a fallback ("if X fails, do Y before proceeding"). Explicit human-in-the-loop checkpoints.

**Feedback loop pattern:**
```
Step N: [action]
Step N+1: Validate — run [script] or ask the user: "[question]"
If validation fails: [corrective action], then return to Step N+1.
Only proceed when validation passes.
```

**Gotcha — common mistake:** Making the workflow so rigid it can't handle state variations (e.g., "run migration.py" without handling the case where the DB is already migrated). Give the agent enough context to handle the most common failure modes.

**Example:** `skill-creator` in anthropics/skills — multi-step process: interview → draft → test → review → improve → repeat.

---

## Type 3: Tool-augmented skill

**What it is:** Primary purpose is to leverage specific tools (terminal commands, web search, file system operations, APIs). The value is telling the agent *which tools to use and how*, including non-obvious flags, required permissions, and failure modes.

**When to choose it:** The task requires specific tools the agent might not reach for, or might use incorrectly without guidance.

**Signs you're in this type:**
- "I want it to use our internal CLI tool"
- "It should always use `grep -P` not `grep -E` for this"
- "It needs to fetch from this specific API endpoint"

**Structure:**
- SKILL.md: specify the exact tools, commands, flags to use. Give one complete working example. Include the most likely error modes and how to handle them.
- `scripts/` for wrapper scripts that standardize tool invocation
- Specify tools in frontmatter `allowed-tools` if needed (VS Code experimental feature)

**Frontmatter description:** Name the tools. Example: `"Use when searching the internal knowledge base (uses kb-search CLI), fetching API documentation (uses fetch_webpage), or running benchmarks (uses bench.sh). Do not use default search or web search for these tasks."`

**Body style:** Exact commands. Replace parameters explicitly with `<placeholder>`. One worked example. Error handling for the most likely failure mode.

**Tool reference in VS Code Copilot skills:**
Skills don't directly call tools — they instruct the agent to use them. Reference tools by how the user describes them:
```
Use fetch_webpage to retrieve [URL] before answering any questions about the API.
```
```
Run the following terminal command (request permission if needed):
bash scripts/validate.sh [input]
```

**Gotcha — common mistake:** Listing 5 possible tools and letting the agent choose. Pick one default, give the others as fallback only.

---

## Type 4: Code generation / Template skill

**What it is:** Produces code, documents, or structured output in a specific format. The value is the template and format constraints that make the output consistent and usable without editing.

**When to choose it:** There is a specific output format that is either non-obvious, critical to get right, or repetitive to specify each time.

**Signs you're in this type:**
- "I want it to generate tests that match our test file structure"
- "I want PRs to always be formatted this way"
- "I want components generated with our exact boilerplate"

**Structure:**
- SKILL.md: describe the output format and constraints. Link to template files.
- `assets/` for template files the agent fills in (primary use of assets/)
- `scripts/` if there is post-generation validation or formatting

**Frontmatter description:** Specify output format and when to generate it. Example: `"Use when generating React components, custom hooks, or context providers. Produces components with TypeScript types, barrel exports, and test stubs matching the project's structure."`

**Body style:** Template-first. Show, don't just tell — provide the template inline for short outputs, reference `assets/template.md` for long ones. Add constraints as annotated comments in the template itself. Short explanation of which parts to adapt vs. keep fixed.

**Wrong approach:**
> "Generate components with props, TypeScript types, tests, and barrel exports."

**Right approach:**
> "Use this template exactly, filling in `[ComponentName]`, `[Props]`, and `[behavior]`:"
> (then: full template)

---

## Type 5: Analysis / Review skill

**What it is:** Evaluates something against criteria. Produces structured findings, grades, or recommendations. The value is the evaluation rubric — criteria the agent would otherwise have to improvise.

**When to choose it:** The task is subjective enough that without criteria, the agent will miss important things or be inconsistent across runs.

**Signs you're in this type:**
- "I want it to review PRs for security issues"
- "I want it to grade outputs for quality"
- "I want a consistent code review process"

**Structure:**
- SKILL.md: the rubric. What to look for, how to score/classify, output format.
- `references/` for large criteria sets (e.g., OWASP checklist, accessibility guidelines)
- `assets/` for output report templates

**Frontmatter description:** Specify what is being analyzed and what criteria apply. Example: `"Use when reviewing code for security vulnerabilities. Checks for OWASP Top 10, injection risks, and insecure defaults. Produces a structured report with severity ratings."`

**Body style:** Rubric sections. For each criterion: what to check, what pass/fail looks like, what to report. One worked example of a finding. Output format template.

---

## Type 6: Meta-skill (skill that builds skills)

**What it is:** A workflow skill whose output is another skill. Requires understanding the user's intent, classifying what they need, researching the domain, and guiding through an iterative build-test-refine cycle.

**When to choose it:** The user wants to create a skill but may not know what type, how to structure it, or whether their domain knowledge is sufficient.

**Characteristics that make it different from other types:**
- Requires upfront user interview (use `vscode_askQuestions`) — without this, all downstream choices are guesses
- Must classify the output skill type before writing (use this reference)
- Must research the domain if the user lacks expertise (use `fetch_webpage` or web search)
- Iterative: draft → user reviews → refine → repeat
- Final validation: test description triggering behavior

**This skill (`skills-best-practices`) is this type.**

---

## Quick classification table

| User says... | Type |
|---|---|
| "Teach it how [library/API/project] works" | Knowledge/Reference |
| "Make it follow our [process/workflow/checklist]" | Workflow/Process |
| "Make it use [specific tool/command]" | Tool-augmented |
| "Generate [code/doc/output] in [specific format]" | Code generation |
| "Review/grade/check [thing] against [criteria]" | Analysis/Review |
| "I want to create a skill for X" | Meta (this skill) → classify X |

## Hybrid skills

Most real skills are hybrids. A deployment skill might be: Workflow (step sequence) + Tool-augmented (specific CLI tools) + Code generation (generates config files). When building hybrids:
1. Identify the primary type — it determines the SKILL.md body structure
2. Layers add sections: e.g., tool references as a "Tools" section within a workflow skill
3. Keep `SKILL.md` under 500 lines — use `references/` for the secondary type's detail
