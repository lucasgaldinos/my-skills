# Pandoc-markdown skill — Self-update TODO log

This log records (a) proposals the user declined when the self-update protocol was
triggered, and (b) known gaps deferred from planning for later review. See the
`## Self-update protocol` section of `SKILL.md` for the process that populates this file.

Columns:

- **timestamp** — ISO date (UTC) the row was added.
- **trigger_error_snippet** — short quote from the pandoc/LaTeX stderr that caused the
  trigger, or `N/A` for planning deferrals.
- **template_or_doc_affected** — path (relative to this skill) to the file most likely to
  change if the item is actioned.
- **user_decision** — one of `declined`, `deferred-for-review`, `ignored`, `custom`.
- **notes** — source citation, rule statement, and suggested follow-up action.

| timestamp | trigger_error_snippet | template_or_doc_affected | user_decision | notes |
|---|---|---|---|---|
| 2026-04-22 | N/A (Phase-0 deferral, not a compile error) | SKILL.md / references/diagrams-and-filters.md | deferred-for-review | Source: raghur/mermaid-filter README (G-MF-03). Rule: "`mermaid-filter` must run BEFORE `pandoc-crossref` in the `--lua-filter`/`--filter` chain, else diagram IDs aren't resolved by crossref." User quote: "I don't really know, add in fix/TODO.md later." Action item for future: decide whether to (a) bake the rule into SKILL.md's filter-ordering guidance, (b) add a guard to a future Lua filter, or (c) close as documentation-only in `references/diagrams-and-filters.md`. |
| 2026-04-22 (dry-run) | `File nonexistent.bib not found in resource path` (pandoc exit 99) | `fix/staging/scratch-broken.md` (deliberately broken dry-run doc, NOT a real template) | log-only | Phase-3 protocol dry-run executed by orchestrator. Major-failure category (a)+(d). User chose "No — log to fix/TODO.md". Outcome: protocol works end-to-end (classification → ask → log). No SKILL.md changes proposed. The broken scratch doc remains in `fix/staging/` for re-use as a regression fixture. |
| 2026-04-23 (check-mode live run) | 2 rubric FAILs on templates/minimal-thesis.pdf: (b) TOC listed Notes/Portability/Compile as thesis sections; (g) overfull hbox from long CSL filename | `templates/minimal-thesis.md` | Fix: yes → Apply (both patches) | Patch 1: added `toc-depth: 0` to YAML (required value `0` not `1`, since in LaTeX `report` class `chapter=0, section=1`; first attempt with `1` still showed sections, corrected on iteration). Patch 2: moved long CSL filename into its own `text` code block. Recompile: 7 pages, 10/10 rubric items PASS. This is the Phase-4 end-to-end proof (parallel to the Phase-3 self-update dry-run) — no TODO; row kept as audit record. |
