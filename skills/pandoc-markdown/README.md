# pandoc-markdown skill

Agent skill for authoring/editing academic Pandoc Markdown (theses, articles, beamer
slide decks, standalone HTML) with citations, math, cross-references, and Mermaid /
TikZ / PlantUML diagrams.

**Humans:** read [`SKILL.md`](SKILL.md) — it is the single entry point. Everything
below is just an inventory of what lives in this folder.

## Folder layout

| Path             | Contents                                                                           |
| ---------------- | ---------------------------------------------------------------------------------- |
| `SKILL.md`       | The skill itself: rules, triggers, workflows, references and templates table.      |
| `templates/`     | 8 ready-to-compile starter documents (thesis, article, beamer, html, tikz, etc.).  |
| `scripts/`       | 5 Lua filters (`beamer-table-fix`, `abstract-to-latex`, `figure-numbering`, `strip-raw-latex-for-html`, `lang-span`). |
| `references/`    | Official Pandoc manual sections + synthesized notes (diagrams, format compatibility, quality rubric, check-mode and self-update playbooks). |
| `assets/`        | Shared LaTeX preambles, beamer themes, CSS, KDE highlight themes used by templates. |
| `fix/`           | Skill-maintenance log: `TODO.md`, deferred items, regression fixtures under `staging/`. |

## Modes

The skill has two opt-in modes (see `## Mode selection` in `SKILL.md`):

- **Self-update** — fix the skill when a compile fails in a way the skill should have prevented.
- **Check mode** — review an already-compiled PDF against a quality rubric.

Neither runs automatically; both require explicit user trigger phrases.
