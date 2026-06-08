# External research diff — pandoc-markdown skill

Generated: 2026-04-22 • Phase 0 of `plan/feature-pandoc-markdown-skill-1.md`

## Sources fetched

| id  | URL                                                                                                                     | Local stage                                                                 |
|-----|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| S1  | <https://raw.githubusercontent.com/plinde/claude-plugins/refs/heads/main/pandoc/skills/pandoc/SKILL.md>                   | `tmp/pandoc-skill-research/plinde-pandoc.md`                                |
| S2  | <https://raw.githubusercontent.com/jrajasekera/jr-agent-skills/main/skills/pandoc-converter/SKILL.md> (+tree listing)     | `tmp/pandoc-skill-research/jrajasekera-pandoc-converter/SKILL.md`           |
| S3  | <https://raw.githubusercontent.com/raghur/mermaid-filter/refs/heads/master/README.md>                                     | `tmp/pandoc-skill-research/raghur-mermaid-filter.md`                        |

## Gap candidates

Legend — `risk`: Low = additive text-only; Med = new file or new script, no build-break; High = edits core compile recipe. Answers filled after Phase-0 `vscode_askQuestions` round.

| gap_id   | source | description                                                                                               | proposed_destination                                              | rationale                                                                                     | risk | answer |
|----------|--------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------|--------|
| G-PL-01  | S1     | Markdown→DOCX workflow incl. `--reference-doc=template.docx` for styling                                  | new `references/format-conversions.md`                            | Current SKILL.md is PDF/beamer/HTML only; DOCX is a common academic output (journals)         | Low  | Skip   |
| G-PL-02  | S1     | DOCX→Markdown extraction (`pandoc input.docx -o output.md [--atx-headers]`)                               | new `references/format-conversions.md`                            | Useful for ingesting reviewer edits back into the source                                      | Low  | Skip   |
| G-PL-03  | S1     | HTML print-to-PDF fallback when LaTeX unavailable (`--embed-resources --standalone` + browser print)      | new subsection "Fallback compile paths" in SKILL.md               | Safety net for machines without TeX; keeps skill usable offline                               | Low  | Skip   |
| G-PL-04  | S1     | Explicit `-f gfm` vs `-f markdown` rule for HTML line-breaks/lists (paragraph-merge pitfall)              | expand existing "Known failure modes" in SKILL.md                 | SKILL.md already has the gfm-math warning; the list-merge pitfall is distinct and unrecorded  | Low  | Add    |
| G-PL-05  | S1     | `--embed-resources --standalone` flag for self-contained HTML (images+CSS inlined)                        | SKILL.md "Compile commands" → HTML recipe                         | Single-file HTML is often needed for sharing preprints                                        | Low  | Skip   |
| G-PL-06  | S1     | Google Docs round-trip workflow (md → docx → Drive upload → Open with Docs)                               | `references/format-conversions.md`                                | Advisors/reviewers often comment in Google Docs; round-trip is a real workflow                | Low  | Skip   |
| G-PL-07  | S1     | Self-test snippet (`pandoc --version \| head -1`; echo-pipe smoke test)                                   | future `scripts/pandoc-preflight.sh` (Phase 4 check mode)         | Gives check mode a cheap first probe before expensive compile                                 | Med  | Skip   |
| G-PL-08  | S1     | PDF-engine selection matrix table (pdflatex/xelatex/lualatex, with "use when")                            | SKILL.md "Compile commands" → new inline table                    | Currently scattered across prose; a table is easier to scan                                   | Low  | Add    |
| G-JR-01  | S2     | python wrapper script pattern (`convert.py --check`, `--formats`, auto-detect from extension)             | new `scripts/pandoc-preflight.py`                                 | Gives the skill a deterministic, testable preflight binary; reusable in CI                    | Med  | Skip   |
| G-JR-02  | S2     | Format-compatibility table (read vs read/write; CSV/TSV/XLSX read-only; EPUB/RTF/PPTX noted)              | new `references/format-compatibility.md`                          | Pandoc's format matrix is non-obvious; a reference file avoids repeated web lookups           | Low  | Add    |
| G-JR-03  | S2     | Per-OS install instructions (brew / apt-get / texlive-xetex) incl. PDF-engine LaTeX install              | add short "Prerequisites" subsection to SKILL.md or new ref file  | The current skill assumes tools are installed; new users hit install pain first               | Low  | Skip   |
| G-MF-01  | S3     | Add `raghur/mermaid-filter` as alternative diagram stack + env-var config (`MERMAID_FILTER_*`)            | `references/diagrams-and-filters.md` + diagram decision table     | Complements `pandoc-ext/diagram`; env vars enable CI overrides without editing the `.md`      | Low  | **Add with modification** — wrap new content in XML tags (`<rules>` / `<gotchas>`) per skill convention. User quote: "Add, but rememeber to route it using xml tags" |
| G-MF-02  | S3     | Mermaid filter config discovery: `.mermaid-config.json`, `.mermaid.css`, `.puppeteer.json` in CWD         | `references/diagrams-and-filters.md`                              | Offline/sandbox builds need `.puppeteer.json` to point at a local Chromium                    | Low  | Add    |
| G-MF-03  | S3     | Promote "`mermaid-filter` must run before `pandoc-crossref`" from implicit to an explicit rule            | SKILL.md "Diagrams" or "Cross-references" section                 | Violating filter order silently breaks cross-refs — a top-tier gotcha worth a bullet          | Low  | **Defer** — log to `fix/TODO.md` for later review. User quote: "I don't really know, add in `fix/TODO.md` later" |
| G-MF-04  | S3     | `{.mermaid #fig:example}` attribute syntax so `pandoc-crossref` can reference the rendered image          | `references/diagrams-and-filters.md` with a worked example        | Explicit example beats discovery; currently the skill only mentions `pandoc-crossref` broadly | Low  | Add    |

## Notes on omitted candidates

Deliberately NOT listed (judgement call — flag if you disagree):

- plinde §"PSI document conversion" — domain-specific to plinde's use, not academic.
- plinde Homebrew-only install hints — Linux-first repo; captured in G-JR-03 instead.
- mermaid-filter Windows 8.1 `mermaid-filter.cmd` workaround — not applicable to this Linux workflow.
- jrajasekera CSV→HTML table on its own — subsumed by G-JR-02 (format matrix).

## Decision legend

- **Add** — integrate into the proposed destination during Phase 1–5.
- **Skip** — record here as "Skip" and do not revisit.
- **Modify** — user provides freeform text describing a different destination / scope.

No files outside `tmp/pandoc-skill-research/` and `~/.agents/skills/pandoc-markdown/fix/` were edited in this phase.
