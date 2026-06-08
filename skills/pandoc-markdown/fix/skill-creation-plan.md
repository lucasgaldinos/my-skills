---
goal: Enhance the pandoc-markdown agent skill with tested templates, styling assets, Lua filter library, self-update mode, and check mode
version: 1.0
date_created: 2026-04-22
last_updated: 2026-04-23
owner: lucas_galdino
status: 'Completed'
tags: [feature, skill, pandoc, agent-skills, tooling]
---

# Introduction

![Status: Completed](https://img.shields.io/badge/status-Completed-brightgreen)

This plan enhances the existing `pandoc-markdown` agent skill at
`~/.agents/skills/pandoc-markdown/` by (1) adding a `templates/` directory of
self-documenting, compile-verified example documents (thesis, article, beamer,
HTML, TikZ, circuitikz, Mermaid workaround, multi-language), (2) adding
styling assets (ABNT LaTeX header, beamer theme override, academic HTML CSS,
code highlight style), (3) adding a Lua filter library in `scripts/`, (4)
introducing a **self-update mode** triggered by major compile failures (with
confirmation via `vscode_askQuestions`, and a `fix/TODO.md` fallback), and
(5) introducing a **check mode** that reads the rendered PDF with the `pdf`
skill + vision, parses pandoc stderr, and asks the user one-by-one how to
proceed on each issue. The plan is strictly planning — no files are created
during the plan phase itself.

## 1. Requirements & Constraints

### Functional requirements

- **REQ-001** — All example templates in `templates/` must compile successfully on the target machine (Linux + TeX Live + `pandoc >= 3.0`).
- **REQ-002** — Each template file must be **self-documenting**: the first section explains what it demonstrates, the YAML frontmatter is annotated, and the exact compile command is shown as a fenced code block at the bottom.
- **REQ-003** — Templates must cover both target families: (a) standalone document PDFs (thesis, article, HTML), and (b) slide decks (beamer), and (c) specialized content (TikZ, circuitikz, Mermaid workaround, multi-language with `polyglossia`/`babel`).
- **REQ-004** — The skill must continue to work for both auto-load (description-triggered) and explicit `/pandoc-markdown` invocation.
- **REQ-005** — Self-update mode MUST ask the user via `vscode_askQuestions` before modifying `SKILL.md` or any reference file; it must never silently edit the skill.
- **REQ-006** — When the user declines a self-update, the issue MUST be appended to `~/.agents/skills/pandoc-markdown/fix/TODO.md` with timestamp, trigger error, and user's "no" decision noted.
- **REQ-007** — Check mode MUST re-read the produced PDF using the `pdf` skill and the vision API, then report visual issues (overflow, clipped figures, missing cross-refs rendered as `??`, absent bibliography) alongside stderr warnings.
- **REQ-008** — Check mode MUST ask the user, per issue, via `vscode_askQuestions` whether to fix (yes/no/custom suggestion) — no unattended modifications.
- **REQ-009** — Check mode MUST only run when the user **explicitly asks** to check outputs (phrases like "check the output", "review the PDF", "did it render right", or explicit `/pandoc-check` invocation).

### Security / safety requirements

- **SEC-001** — Neither self-update nor check mode may execute shell commands beyond `pandoc`, `which`, `pdfinfo`, `ls`, `cat`, and the diagram CLIs explicitly listed in `SKILL.md` (no `curl | sh`, no network fetches without `vscode_askQuestions` confirmation).
- **SEC-002** — When fetching external skills for comparison (TASK-003 to TASK-005), URLs must be fetched via `fetch_webpage` only, and the retrieved content must be staged in `tmp/pandoc-skill-research/` before being considered for integration.

### Quality / compliance requirements

- **QUA-001** — `SKILL.md` body must stay under 500 lines after all edits (current: ~320 lines; budget: ~180 lines for new content).
- **QUA-002** — Every new rule added to `SKILL.md` must include its *why* (per `skills-best-practices`).
- **QUA-003** — Every template PDF must be verified via the `pdf` skill + vision before being committed to `templates/`.
- **QUA-004** — Each Lua filter in `scripts/` must include a header comment explaining purpose, invocation, and known limits (same style as `beamer-table-fix.lua`).

### Constraints

- **CON-001** — The ABNT CSL file is already in the repo at `documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl`; templates MUST reference it by relative path, not re-download it.
- **CON-002** — Templates MUST compile with `xelatex` (default) and `lualatex` (fallback for TikZ-heavy docs) — no `pdflatex`, which fails on Unicode.
- **CON-003** — The skill lives at `~/.agents/skills/pandoc-markdown/`; no artifacts may be created inside the `chimera/gpu_accelerated` workspace except for transient compile outputs under `tmp/`.
- **CON-004** — This plan is **planning only** — the plan document itself is the deliverable for phase 0; execution of later phases requires explicit user go-ahead.

### Guidelines / patterns

- **GUD-001** — Follow the `skills-best-practices` skill for SKILL.md structure (XML tags, progressive disclosure).
- **GUD-002** — Follow the `create-implementation-plan` skill template for this document.
- **PAT-001** — Mirror the existing `beamer-table-fix.lua` style for all new Lua filters (function-per-node, comments at top, graceful `return nil` fallthrough).
- **PAT-002** — Mirror the `assets/*-frontmatter.md` annotation style (inline YAML comments + a "Notes" section below) for new templates.

## 2. Implementation Steps

### Implementation Phase 0 — External research & diff gathering (planning-adjacent, no skill edits)

- GOAL-000: Fetch the external reference skills the user cited, diff them against the current `pandoc-markdown` skill, and produce a machine-parseable gap report under `~/.agents/skills/pandoc-markdown/fix/external-diff.md`. Present each proposed integration via `vscode_askQuestions` one at a time. No edits to `SKILL.md` without explicit approval per gap.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-001 | `fetch_webpage` `https://raw.githubusercontent.com/plinde/claude-plugins/refs/heads/main/pandoc/skills/pandoc/SKILL.md` → save to `tmp/pandoc-skill-research/plinde-pandoc.md` | ✅ | 2026-04-23 |
| TASK-002 | `fetch_webpage` `https://github.com/jrajasekera/jr-agent-skills/tree/main/skills/pandoc-converter` and the individual raw files it links → `tmp/pandoc-skill-research/jrajasekera-pandoc-converter/` | ✅ | 2026-04-23 |
| TASK-003 | `fetch_webpage` `https://raw.githubusercontent.com/raghur/mermaid-filter/refs/heads/master/README.md` → `tmp/pandoc-skill-research/raghur-mermaid-filter.md` | ✅ | 2026-04-23 |
| TASK-004 | Produce diff report at `~/.agents/skills/pandoc-markdown/fix/external-diff.md` with one row per "gap candidate" — columns: `gap_id`, `source`, `description`, `proposed_destination` (SKILL.md section / new reference file / new asset), `rationale`, `risk` | ✅ | 2026-04-23 |
| TASK-005 | For each `gap_id`, call `vscode_askQuestions` with options `Add / Skip / Add with modification (freeform)`. Record the answer in the diff report. No edits yet. | ✅ | 2026-04-23 |

**Completion criterion:** `external-diff.md` exists and every `gap_id` has an `answer` column filled.

---

### Implementation Phase 1 — Templates directory (self-documenting, compile-verified examples)

- GOAL-001: Create `~/.agents/skills/pandoc-markdown/templates/` containing 7 compilable examples. Each is self-documenting (frontmatter + notes + embedded compile command). Verify each compiles, then use the `pdf` skill + vision to confirm the visual output matches intent before promoting from `fix/staging/` to `templates/`.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-006 | Create `templates/` and `fix/staging/` directories (staging is the compile scratch area; files are only copied to `templates/` after vision approval) | ✅ | 2026-04-23 |
| TASK-007 | `templates/minimal-thesis.md` — `documentclass: report`, 1 chapter, 1 figure (PNG), 1 pipe table, 1 citation from `refs.bib`, 1 display-math block; compile with `xelatex + citeproc`. Self-document compile command at bottom. | ✅ | 2026-04-23 |
| TASK-008 | `templates/minimal-article.md` — `documentclass: article`, abstract, 2 sections, inline + display math, 2 citations, 1 pipe table. | ✅ | 2026-04-23 |
| TASK-009 | `templates/minimal-beamer.md` — title slide, 3 content slides (bullets, math, table), 1 citation, `--lua-filter=scripts/beamer-table-fix.lua`, no Mermaid. | ✅ | 2026-04-23 |
| TASK-010 | `templates/tikz-figure.md` — thesis-style doc with a native TikZ figure (axis + curve) in `\begin{figure}…\end{figure}`, `\usepackage{tikz,pgfplots}` in `header-includes`. Also demonstrates `\ref{fig:…}` via raw LaTeX (no `pandoc-crossref` required). | ✅ | 2026-04-23 |
| TASK-011 | `templates/circuitikz-figure.md` — same skeleton as TASK-010 but using `\usepackage{circuitikz}` to draw a simple RC circuit; documents the extra package and `\draw` syntax. | ✅ | 2026-04-23 |
| TASK-012 | `templates/mermaid-workaround.md` — demonstrates the **pre-render workflow**: a `.mmd` source file lives next to the template, a shell one-liner (commented in the template) generates `.png` via `mmdc`, and the markdown embeds the image with `![](path){width=80%}`. Self-documents both the failure mode and the workaround. | ✅ | 2026-04-23 |
| TASK-013 | `templates/multi-language.md` — thesis frontmatter with `lang: pt-BR` and a section in English wrapped in `<div lang="en">…</div>` (or `[…]{lang=en}` inline). Documents `polyglossia` vs `babel` and when to choose each. | ✅ | 2026-04-23 |
| TASK-014 | `templates/standalone-html.md` — same content shape as `minimal-article.md` but targeting `-s --katex --citeproc -o output.html`; includes reference to `assets/academic.css`. | ✅ | 2026-04-23 |
| TASK-015 | For each template, run `pandoc … -o fix/staging/<name>.pdf` (or `.html`). Capture stderr. If stderr has `[ERROR]`, mark the template "failed" and invoke the self-update flow (Phase 3). | ✅ | 2026-04-23 |
| TASK-016 | For each successfully compiled PDF, load the `pdf` skill and call vision to verify: (a) title renders, (b) figures appear, (c) table formatting is clean, (d) citations resolve (no literal `[@key]` text), (e) bibliography present if applicable. Record result in `fix/staging/vision-log.md`. | ✅ | 2026-04-23 |
| TASK-017 | Promote only the PDFs that pass vision inspection: copy the `.md` source from `fix/staging/` to `templates/`. Leave failed attempts in `fix/staging/` for the self-update loop. | ✅ | 2026-04-23 |

**Completion criterion:** Every `templates/*.md` has (a) a corresponding approved PDF in `fix/staging/`, (b) a positive vision-log entry, (c) a self-documented compile command in its own body.

---

### Implementation Phase 2 — Styling assets & Lua filter library

- GOAL-002: Add styling assets covering LaTeX (ABNT header), beamer theme, HTML CSS, and code-highlighting theme. Add general-purpose Lua filters. Reference them from `SKILL.md` and from the templates of Phase 1.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-018 | `references/diagrams-and-filters.md` — add the `raghur/mermaid-filter` vs `pandoc-ext/diagram` comparison table (the one from this chat reply) as a new subsection. Update SKILL.md's diagram table to mention both. | ✅ | 2026-04-23 |
| TASK-019 | `assets/styles/abnt-header.tex` — ABNT-compliant `header-includes` content: margins (`geometry`), `linestretch=1.5`, `indent=1.25cm`, `titlesec` formatting for chapter/section, `caption` configuration, `hyperref` setup with `colorlinks=false`. Loadable via `header-includes: - \input{assets/styles/abnt-header.tex}`. | ✅ | 2026-04-23 |
| TASK-020 | `assets/styles/beamer-thesis-theme.tex` — custom footline (author + title + frame count), sectionpage override, color palette (blue/gray, academic), `\setbeamertemplate{caption}[numbered]`. Paste-in via `header-includes`. | ✅ | 2026-04-23 |
| TASK-021 | `assets/styles/academic.css` — standalone HTML CSS: serif body font (Charter stack), justified paragraphs, numbered figure captions via `:has()`/counter, bibliography block styled, responsive max-width. Loadable via `--css=assets/styles/academic.css`. | ✅ | 2026-04-23 |
| TASK-022 | `assets/styles/highlight-academic.theme` — KDE syntax-highlighting XML theme (muted, print-friendly); loadable via `--highlight-style=assets/styles/highlight-academic.theme`. | ✅ | 2026-04-23 |
| TASK-023 | `scripts/abstract-to-latex.lua` — Lua filter: when a top-level Div has class `abstract`, emit `\begin{abstract}…\end{abstract}` for LaTeX output. Useful for articles whose frontmatter doesn't carry `abstract:`. | ✅ | 2026-04-23 |
| TASK-024 | `scripts/figure-numbering.lua` — Lua filter: auto-assign `\label{fig:N}` to every unlabeled image, so raw `\ref{fig:N}` references work without `pandoc-crossref`. | ✅ | 2026-04-23 |
| TASK-025 | `scripts/strip-raw-latex-for-html.lua` — Lua filter: when the output format is `html`, convert common raw LaTeX (`\emph{}`, `\textbf{}`, `\textit{}`) to equivalent Pandoc inline nodes instead of dropping them. Solves the "multi-format silent drop" gotcha in SKILL.md. | ✅ | 2026-04-23 |
| TASK-026 | `scripts/lang-span.lua` — Lua filter: map `[text]{lang=en}` spans to `\foreignlanguage{english}{text}` in LaTeX output; used by `templates/multi-language.md`. | ✅ | 2026-04-23 |
| TASK-027 | Update `SKILL.md` §"Scripts bundled with this skill" to list the new filters with one-line purpose each. | ✅ | 2026-04-23 |
| TASK-028 | Update `assets/defaults-academic.yaml` to reference the new styles optionally (commented-out by default). | ✅ | 2026-04-23 |

**Completion criterion:** Templates of Phase 1 that depend on these assets/filters now compile with them (re-run TASK-015 verification).

---

### Implementation Phase 3 — Self-update mode

- GOAL-003: Encode in `SKILL.md` a workflow that detects **major** compile failures, asks the user whether to update the skill, and either patches the skill (with confirmation) or logs to `fix/TODO.md`. The mode is a documented protocol the agent follows — no daemon, no runtime state.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-029 | Create `~/.agents/skills/pandoc-markdown/fix/TODO.md` with a header template: columns `timestamp`, `trigger_error_snippet`, `template_or_doc_affected`, `user_decision`, `notes`. | ✅ | 2026-04-23 |
| TASK-030 | Add new section `## Self-update protocol` to `SKILL.md`. Define **major failure** as any of: (a) pandoc exit code ≠ 0, (b) `[ERROR]` in stderr, (c) LaTeX `Fatal error occurred`, (d) missing bibliography entries for cited keys, (e) output PDF has zero pages. | ✅ | 2026-04-23 |
| TASK-031 | In the same section, define **minor failure** (skill does NOT auto-trigger): (a) `[WARNING]` lines only, (b) underfull/overfull hbox warnings, (c) pdfinfo shows output exists and has > 0 pages. | ✅ | 2026-04-23 |
| TASK-032 | Document the self-update call flow: (1) agent classifies failure; (2) if major, agent calls `vscode_askQuestions` with question "A major compile failure happened: <category>. Self-update the skill?" options: `Yes — propose patch / No — log to fix/TODO.md / No — ignore / Custom (freeform)`; (3) on "Yes", agent drafts a patch as a diff and asks again via `vscode_askQuestions` with options `Apply / Revise / Cancel`; (4) on "No", agent writes the row to `fix/TODO.md`. | ✅ | 2026-04-23 |
| TASK-033 | Add 3 worked examples inline in the same section showing the full turn-by-turn flow (stderr → classification → ask → outcome). | ✅ | 2026-04-23 |
| TASK-034 | Add trigger phrases the user can say to **force** self-update evaluation: "results are not good", "the PDF is wrong", "the skill missed something", "fix the skill". List them verbatim in `SKILL.md` so the description can surface them. | ✅ | 2026-04-23 |
| TASK-035 | Update the skill `description:` frontmatter to mention self-update triggers (stay under 500 chars total). | ✅ | 2026-04-23 |

**Completion criterion:** A dry-run with an intentionally broken template (e.g., unclosed `$`) triggers the documented flow end-to-end, and the final state matches (either patched skill + user approval, or a new row in `fix/TODO.md`).

---

### Implementation Phase 4 — Check mode

- GOAL-004: Add an opt-in check mode. When the user explicitly asks to check a rendered PDF, the skill parses stderr, reads the PDF via the `pdf` skill + vision, scores against `references/quality-rubric.md`, and asks per-issue whether to fix.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-036 | Create `references/quality-rubric.md` with checkboxes: (a) title + author render, (b) TOC present and matches headings, (c) no literal `[@key]` in body, (d) bibliography present, (e) no `??` for cross-refs, (f) figures have captions and numbers, (g) tables not clipped, (h) no math-rendering warnings, (i) language-specific quotes correct (Portuguese « » vs English " ", etc.), (j) page count matches expected for the content. | ✅ | 2026-04-23 |
| TASK-037 | Add `## Check mode` section to `SKILL.md`. Define invocation triggers (verbatim phrases): "check the PDF", "review the output", "did it render right", "run the quality check", explicit `/pandoc-check`. | ✅ | 2026-04-23 |
| TASK-038 | Document the check flow: (1) locate the PDF; (2) re-run the last pandoc command with `--verbose 2>&1 | tee fix/last-compile.log`; (3) load`pdf` skill and call vision on the PDF; (4) classify each rubric item as pass/fail/unknown; (5) for each fail, call `vscode_askQuestions` — options `Fix: yes / Fix: no / Fix: <freeform suggestion>`; (6) on "yes", produce a patch and confirm again via`vscode_askQuestions`; (7) on "no", append the fail to`fix/TODO.md` marked `check-declined`. | ✅ | 2026-04-23 |
| TASK-039 | Document the **auto-fix catalogue** (short list of fixes the skill can offer with high confidence): missing `--citeproc`, wrong filter order, missing `--pdf-engine=xelatex`, Unicode in `pdflatex`, `longtable` in beamer (suggest `beamer-table-fix.lua`), bibliography path typo. | ✅ | 2026-04-23 |
| TASK-040 | Add an example transcript in `references/quality-rubric.md` showing one full check run on a deliberately broken PDF (e.g., missing `--citeproc`). | ✅ | 2026-04-23 |

**Completion criterion:** Running check mode on one of the Phase-1 `templates/*.pdf` outputs produces a rubric report with ≥ 80% items auto-classified and no unattended edits.

---

### Implementation Phase 5 — SKILL.md consolidation & README

- GOAL-005: Fold all new subsystems into `SKILL.md` cleanly, keep the body under 500 lines, and regenerate the `## References` / `## Scripts` / new `## Templates` tables.

| Task     | Description | Completed | Date |
| -------- | ----------- | --------- | ---- |
| TASK-041 | Add new table `## Templates` to `SKILL.md` pointing into `templates/*.md` with one-line purpose each. | ✅ | 2026-04-23 |
| TASK-042 | Update the `## References` table to include `quality-rubric.md` and any new reference files from Phase 0 diff integration. | ✅ | 2026-04-23 |
| TASK-043 | Update the `## Scripts bundled with this skill` table with the 4 new Lua filters from Phase 2. | ✅ | 2026-04-23 |
| TASK-044 | Add `<rules>`-wrapped "When the skill activates check mode vs self-update mode" decision table. | ✅ | 2026-04-23 |
| TASK-045 | Add a short `README.md` inside `~/.agents/skills/pandoc-markdown/` (for humans browsing the skill folder) pointing to `SKILL.md`. | ✅ | 2026-04-23 |
| TASK-046 | Run `wc -l ~/.agents/skills/pandoc-markdown/SKILL.md` — must be < 500. If over budget, move the longest subsection into a `references/` file with a pointer. | ✅ | 2026-04-23 |
| TASK-047 | Invoke the skill via two trigger prompts ("help me compile my thesis" and "this beamer has broken tables") and confirm the skill loads; invoke two anti-triggers ("write a GitHub README", "explain python decorators") and confirm it does NOT load. | ✅ | 2026-04-23 |

**Completion criterion:** All tables in SKILL.md are self-consistent, body ≤ 500 lines, trigger/anti-trigger tests pass.

---

## 3. Alternatives

- **ALT-001** — Build a pandoc "defaults file repository" instead of templates. Rejected: defaults files are not self-documenting and don't exercise the full authoring surface (math, figures, tables, citations) in one place.
- **ALT-002** — Make self-update mode automatic on every warning. Rejected per user direction: minor warnings often produce "well-enough" output, and unconditional prompting is noisy.
- **ALT-003** — Use `raghur/mermaid-filter` as the primary Mermaid path instead of the pre-render workaround. Rejected for beamer (same fragile-frame failure mode) and kept as a documented alternative for non-beamer PDFs.
- **ALT-004** — Embed template `.md` files as fenced code blocks inside `SKILL.md`. Rejected: violates the < 500-line body budget (`skills-best-practices`) and loses compilation verifiability.
- **ALT-005** — Replace the check-mode rubric with pytest-style assertions. Rejected: rubric items are visual and require vision to evaluate; a text-only test suite cannot catch clipped figures or wrong quote glyphs.

## 4. Dependencies

- **DEP-001** — `pandoc >= 3.0` installed on the host.
- **DEP-002** — TeX Live with `xelatex` (verified via `which xelatex`).
- **DEP-003** — `mmdc` (mermaid-cli) on `PATH` — only required to exercise TASK-012's pre-render step.
- **DEP-004** — `pdfinfo` (from poppler-utils) for page-count verification in check mode.
- **DEP-005** — The `pdf` skill at `/home/lucas_galdino/.agents/skills/pdf/` — used by TASK-016 and TASK-038 to read compiled PDFs with vision.
- **DEP-006** — The ABNT CSL already in the repo at `documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl`.
- **DEP-007** — Access to `fetch_webpage` for TASK-001 to TASK-003.
- **DEP-008** — `vscode_askQuestions` for every user confirmation step in Phases 0, 3, 4.

## 5. Files

### New directories

- **FILE-001** — `~/.agents/skills/pandoc-markdown/templates/` — compiled + vision-approved example documents (Phase 1).
- **FILE-002** — `~/.agents/skills/pandoc-markdown/assets/styles/` — LaTeX / CSS / highlight-theme styling assets (Phase 2).
- **FILE-003** — `~/.agents/skills/pandoc-markdown/fix/` — self-update staging, TODO log, diff reports (Phases 0, 3, 4).
- **FILE-004** — `~/.agents/skills/pandoc-markdown/fix/staging/` — scratch area for compile + vision verification (Phase 1).

### New files (per task)

- **FILE-005** — `templates/minimal-thesis.md` (TASK-007) + its verified `fix/staging/minimal-thesis.pdf`.
- **FILE-006** — `templates/minimal-article.md` (TASK-008) + PDF.
- **FILE-007** — `templates/minimal-beamer.md` (TASK-009) + PDF.
- **FILE-008** — `templates/tikz-figure.md` (TASK-010) + PDF.
- **FILE-009** — `templates/circuitikz-figure.md` (TASK-011) + PDF.
- **FILE-010** — `templates/mermaid-workaround.md` + `templates/assets/mermaid-source.mmd` + pre-rendered PNG (TASK-012).
- **FILE-011** — `templates/multi-language.md` (TASK-013) + PDF.
- **FILE-012** — `templates/standalone-html.md` (TASK-014) + HTML.
- **FILE-013** — `assets/styles/abnt-header.tex` (TASK-019).
- **FILE-014** — `assets/styles/beamer-thesis-theme.tex` (TASK-020).
- **FILE-015** — `assets/styles/academic.css` (TASK-021).
- **FILE-016** — `assets/styles/highlight-academic.theme` (TASK-022).
- **FILE-017** — `scripts/abstract-to-latex.lua` (TASK-023).
- **FILE-018** — `scripts/figure-numbering.lua` (TASK-024).
- **FILE-019** — `scripts/strip-raw-latex-for-html.lua` (TASK-025).
- **FILE-020** — `scripts/lang-span.lua` (TASK-026).
- **FILE-021** — `fix/TODO.md` (TASK-029).
- **FILE-022** — `fix/external-diff.md` (TASK-004).
- **FILE-023** — `references/quality-rubric.md` (TASK-036).
- **FILE-024** — `README.md` (TASK-045).

### Files modified

- **FILE-025** — `SKILL.md` — new sections `## Self-update protocol`, `## Check mode`, `## Templates`; updated `## References`, `## Scripts bundled with this skill`, `description:` frontmatter.
- **FILE-026** — `assets/defaults-academic.yaml` (TASK-028) — optional style-asset references.
- **FILE-027** — `references/diagrams-and-filters.md` (TASK-018) — mermaid-filter vs pandoc-ext/diagram comparison.

## 6. Testing

- **TEST-001** — Every `templates/*.md` compiles to PDF (or HTML) with exit code 0 and zero `[ERROR]` lines in stderr. Automated via `for f in templates/*.md; do pandoc -d assets/defaults-academic.yaml "$f" -o "fix/staging/$(basename $f .md).pdf"; done`.
- **TEST-002** — Every produced PDF passes the `quality-rubric.md` checklist with ≥ 80% `pass` items, verified via the `pdf` skill + vision, logged in `fix/staging/vision-log.md`.
- **TEST-003** — Trigger-phrase test: prompts "help me compile my thesis", "this beamer has broken tables", "fix the pandoc build" cause the skill to load. Prompts "write a GitHub README", "explain python decorators" do NOT load it. Pass ≥ 4/5.
- **TEST-004** — Self-update dry run: feed the skill a deliberately broken template (stray `$`). Verify `vscode_askQuestions` is called exactly once (classification prompt), and a decline writes a correctly-formatted row to `fix/TODO.md`.
- **TEST-005** — Check-mode dry run: run check mode on a known-good `templates/minimal-article.pdf`. Verify no user prompts fire (nothing to fix). Run check mode on a deliberately miscompiled version (missing `--citeproc`). Verify one prompt fires and the suggested fix matches the auto-fix catalogue.
- **TEST-006** — `wc -l SKILL.md` < 500 (QUA-001).
- **TEST-007** — `grep -c "^- \*\*" SKILL.md` rules each have a *why* sentence in the same bullet (manual spot check on 10 random bullets; QUA-002).
- **TEST-008** — Each `scripts/*.lua` has the 4-part header comment (purpose / invocation / limits / filter order) (QUA-004).

## 7. Risks & Assumptions

- **RISK-001** — `mmdc` not installed on the host → TASK-012 template cannot be pre-rendered automatically. **Mitigation:** ship a placeholder PNG and a `pre-render.sh` script so users who install `mmdc` can refresh it.
- **RISK-002** — `circuitikz` is a separate LaTeX package not in minimal TeX Live. **Mitigation:** include install hint `tlmgr install circuitikz` in the template notes; skip TASK-011 if not installed and document the skip in `fix/TODO.md`.
- **RISK-003** — Vision misreads a rendered PDF (e.g., rotated figures). **Mitigation:** TASK-016 logs the vision verdict alongside `pdfinfo` metadata so humans can spot-check. A user can always override with a `freeform` answer.
- **RISK-004** — `vscode_askQuestions` is unavailable in a given client surface → self-update mode cannot prompt. **Mitigation:** fall back to "write proposed patch to `fix/TODO.md` marked `pending-review`" — never silent edit.
- **RISK-005** — Style asset changes break existing thesis build. **Mitigation:** all style assets are opt-in (loaded via explicit `header-includes: - \input{…}` or `--css=…`); `defaults-academic.yaml` keeps them commented.
- **RISK-006** — Plan scope creep beyond 500-line SKILL.md budget. **Mitigation:** TASK-046 enforces the budget; overflow automatically spills into `references/`.
- **ASSUMPTION-001** — The user has a working TeX Live installation verified via `which xelatex` before starting Phase 1.
- **ASSUMPTION-002** — The `pdf` skill in this session exposes a vision-capable PDF reader that accepts local PDF file paths.
- **ASSUMPTION-003** — The user's TSP thesis bibliography (`documents_tcc/refs.bib`) has at least 2 valid entries usable as citation sources in test templates.
- **ASSUMPTION-004** — Future major pandoc versions (≥ 4.0) will keep the `longtable` output shape — if they change, `beamer-table-fix.lua` regex must be updated (logged as a standing watch in `fix/TODO.md`).

## 8. Related Specifications / Further Reading

- Current skill: `~/.agents/skills/pandoc-markdown/SKILL.md`
- Supporting skills: `~/.agents/skills/skills-best-practices/SKILL.md`, `~/.agents/skills/create-implementation-plan/SKILL.md`, `~/.agents/skills/pdf/SKILL.md`, `~/.agents/skills/markdown-formatter/SKILL.md`
- Pandoc manual: <https://pandoc.org/MANUAL.html>
- Pandoc Lua filters: <https://pandoc.org/lua-filters.html>
- Pandoc generic filter architecture: <https://pandoc.org/filters.html>
- Diagram filter (generic): <https://github.com/pandoc-ext/diagram>
- Mermaid filter (specialist): <https://github.com/raghur/mermaid-filter> — README at <https://raw.githubusercontent.com/raghur/mermaid-filter/refs/heads/master/README.md>
- External comparable skills: <https://raw.githubusercontent.com/plinde/claude-plugins/refs/heads/main/pandoc/skills/pandoc/SKILL.md>, <https://github.com/jrajasekera/jr-agent-skills/tree/main/skills/pandoc-converter>
- Repo artifacts referenced: `documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl`, `documents_tcc/refs.bib`, `documentation/analysis/presentations/thesis_presentation.md` (existing working beamer build as reference)
- Repo memories relevant to this plan: thesis beamer build command + workarounds (see stored repo memory dated 2025-11-23).
