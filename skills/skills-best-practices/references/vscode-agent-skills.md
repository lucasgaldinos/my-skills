# VS Code Agent Skills — Quick Reference

Source: https://code.visualstudio.com/docs/copilot/customization/agent-skills (fetched March 2026)

---

## Skill discovery locations

VS Code looks for skills in these paths (in priority order):

| Type | Path options |
|---|---|
| Project skills | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| Personal skills | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` |

Additional locations can be configured with `chat.agentSkillsLocations`.
For monorepos: enable `chat.useCustomizationsInParentRepositories`.

---

## Frontmatter fields (VS Code specifics)

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Max 64 chars, lowercase, hyphens only, must match parent directory name |
| `description` | Yes | Max 1024 chars. Primary trigger mechanism. |
| `argument-hint` | No | Shown in chat input when skill is invoked as slash command |
| `user-invocable` | No | Defaults `true`. Set `false` to hide from `/` menu but still allow auto-loading |
| `disable-model-invocation` | No | Defaults `false`. Set `true` to require manual `/skillname` invocation only |

**Visibility matrix:**

| Config | In `/` menu | Auto-loaded by agent |
|---|---|---|
| default (both omitted) | Yes | Yes |
| `user-invocable: false` | No | Yes |
| `disable-model-invocation: true` | Yes | No |
| both set | No | No |

---

## Tools available to skills in VS Code Copilot

Skills don't directly call tools — they instruct the agent to call them. The agent has access to these tools in agent mode:

**File operations:** Read, write, create, rename, delete files via Copilot's file tools.

**Terminal:** Bash commands. User is prompted for approval (or set auto-approve with `chat.tools.terminalCommandAutoApproval`). Always tell the user what a terminal command does when asking for permission.

**fetch_webpage:** Retrieve content from a URL. Use for fetching documentation, API specs, or any web resource. Reference in skill body as:
```
Use fetch_webpage to retrieve [URL] before answering questions about...
```

**Web search:** Agent can search the web when needed. Reference as:
```
Search the web for the latest [topic] documentation if you are unsure of the current syntax.
```

**Code editing:** Read, write, and modify files in the workspace.

**VS Code-specific tools:** `vscode_askQuestions` (ask the user questions in a structured multi-choice or free-text form).

---

## How tools should be referenced in a skill

Don't say "use the fetch tool." Say exactly what to fetch and why:

```markdown
## Before answering any API questions
Use fetch_webpage to retrieve https://example.com/api/docs. This is the authoritative 
reference — do not rely on training knowledge since the API may have changed.
```

```markdown
## Validation step
Run this terminal command to validate (ask the user for permission first):
bash scripts/validate.sh output/
If the command fails, do not proceed to the next step.
```

```markdown
## When the user's intent is unclear
Use vscode_askQuestions to clarify before proceeding:
- "What type of skill do you want to create?" [Reference/Knowledge, Workflow, Code generation, Analysis/Review, Other]
- "Do you have existing documentation or code to base this on?"
- "Is this for VS Code Copilot only, or should it work in Claude Code and other agents too?"
```

---

## Skill as slash command

When `user-invocable: true` (default), users can type `/skill-name` in chat to explicitly invoke the skill. Use `argument-hint` to tell users what to add after the slash command:

```yaml
argument-hint: "[domain to build skill for] [any existing docs or code to base it on]"
```

---

## Project vs. personal skills — when to use which

**Project skill** (`.github/skills/`): Tied to the codebase. For workflows, conventions, and API knowledge specific to this project. Checked into source control — teammates share it.

**Personal skill** (`~/.copilot/skills/`): Tied to you, not a project. For general-purpose capabilities you use across projects. Stays private.

This skill (`skills-best-practices`) is a personal or general-purpose skill — it helps build other skills, regardless of which project is open.

---

## Progressive disclosure — what loads when

1. **Startup (always):** `name` + `description` from frontmatter (~100 tokens). Loaded for ALL skills at once.
2. **On activation:** Full `SKILL.md` body. Loaded when agent decides the skill is relevant, or when user types `/skill-name`.
3. **On demand:** Files in `scripts/`, `references/`, `assets/`. Loaded only when the SKILL.md body instructs the agent to read them.

**Implication:** Files in sub-directories cost zero context until referenced. Use this aggressively. Only put content in SKILL.md that is needed on every single invocation.

---

## Bundled resources — standard structure

```
skill-name/
├── SKILL.md          ← required
├── scripts/          ← executable code (bash, python, node)
│   └── *.sh, *.py, *.js
├── references/       ← docs loaded on demand
│   └── *.md
└── assets/           ← templates, data files
    └── templates/
```

Reference files from SKILL.md with explicit load conditions:
```markdown
If the API returns a non-200 status, read references/error-codes.md for the full error catalog.
```
Not:
```markdown
See references/ for more information.
```
Generic "see references" directives are ignored by the agent because there's no signal about when to load what.

---

## Security note

Always review shared skills before installing. Terminal commands run with user permissions. The VS Code terminal tool has auto-approve options — only enable for commands you understand and trust.
