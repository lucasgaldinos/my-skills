# Pandoc PDF Quality Rubric

This rubric is used by the [`## Check mode`](../SKILL.md#check-mode) workflow. The
scorer (the agent loads the `pdf` skill plus a vision-capable rubric pass) classifies
each item as **PASS**, **FAIL**, or **UNKNOWN**. Each item is phrased as an *observable
PDF property* so any vision-capable agent can score it without internal access to pandoc.

## How to score

- **PASS** — the property holds in the rendered PDF.
- **FAIL** — the property is observably violated in the PDF (or the PDF is missing /
  zero pages, in which case every layout-dependent item is also FAIL).
- **UNKNOWN** — the property cannot be evaluated (e.g. no bibliography expected for
  this document, the page where it would appear is missing, vision pass could not parse
  the page). UNKNOWN is *not* a pass — it surfaces in the report so the user can decide.

Scoring rules:

1. Read `fix/last-compile.log` first. If pandoc exited non-zero or no PDF exists,
   mark items (a)–(j) as FAIL or UNKNOWN per the definitions above and skip vision.
2. Otherwise, run the vision pass over every page, then mark each item.
3. Report each item with a one-line evidence quote (stderr line, page number, or
   "vision: …").

## Items

- [ ] **(a) Title and author render.** The first page (or title block) shows the
      `title:` and `author:` from the YAML frontmatter, not raw `$title$` placeholders.
- [ ] **(b) TOC present and matches headings.** If `toc: true` in YAML, a Table of
      Contents page exists, and every entry corresponds to an `##`/`###` heading in the
      source (no missing or extra entries).
- [ ] **(c) No literal `[@key]` in body.** Citations were resolved; no `[@goldberg1989]`
      or similar bracketed key appears as visible text.
- [ ] **(d) Bibliography present.** If the document cites at least one key, the
      bibliography section exists with a heading (`reference-section-title:` or manual
      `## Referências`) and at least one entry.
- [ ] **(e) No `??` for cross-refs.** No `??`, `Figure ??`, `Table ??`, or
      `Section ??` appears anywhere in the rendered text.
- [ ] **(f) Figures captioned and numbered.** Every embedded image has a caption line
      and a "Figure N" / "Figura N" prefix consistent with the document language.
- [ ] **(g) Tables not clipped.** No table column or row is cut off at the right or
      bottom margin; multi-page tables continue cleanly across pages.
- [ ] **(h) No math-rendering warnings in the PDF.** No literal `[WARNING] Could not
      convert TeX math` text in the body, no overlapping math glyphs, no missing-glyph
      tofu boxes inside `$…$` regions.
- [ ] **(i) Language-specific quotes correct.** Quotation marks match the `lang:`
      field: `« »` (or `“ ”`) for `pt-BR`, `" "` for `en-US`. No mixed conventions.
- [ ] **(j) Page count matches expectation.** The PDF page count is within ±20% of
      what the document asserts (e.g. a thesis declaring `~80 pages` should not be 4 or
      300 pages). UNKNOWN if no expectation is stated.

## Example transcript

The following transcript is the realistic check-mode run on the deliberately-broken
fixture [`fix/staging/scratch-broken.md`](../fix/staging/scratch-broken.md), which
declares a missing `nonexistent.bib`, cites `[@nobody2099]`, and contains an unclosed
`\begin{align}`. This is the same fixture that produced the dry-run row in
[`fix/TODO.md`](../fix/TODO.md).

```text
User: /pandoc-check

Agent (step 1 — locate):
  No PDF found at fix/staging/scratch-broken.pdf.

Agent (step 2 — recompile with --verbose):
  $ pandoc fix/staging/scratch-broken.md --pdf-engine=xelatex --citeproc \
      -o fix/staging/scratch-broken.pdf --verbose 2>&1 | tee fix/last-compile.log
  [WARNING] Could not find bibliography file nonexistent.bib
  pandoc: nonexistent.bib: openBinaryFile: does not exist (No such file or directory)
  Error producing PDF.
  ! LaTeX Error: \begin{align} on input line 12 ended by \end{document}.
  Fatal error occurred, no output PDF file produced!
  pandoc exited with code 43.

Agent (step 3 — load pdf + vision rubric):
  Skipped: no PDF artifact exists.

Agent (step 4 — classify):
  (a) title/author          FAIL  (no PDF produced)
  (b) TOC matches headings  UNKNOWN (no PDF)
  (c) no literal [@key]     FAIL  (stderr: missing bib → key would render literally)
  (d) bibliography present  FAIL  (stderr: bib file not found)
  (e) no ?? cross-refs      UNKNOWN (no PDF)
  (f) figures captioned     UNKNOWN (no figures in fixture)
  (g) tables not clipped    UNKNOWN (no tables in fixture)
  (h) no math warnings      FAIL  (LaTeX Fatal: unclosed \begin{align})
  (i) quotes correct        UNKNOWN (no PDF)
  (j) page count matches    FAIL  (0 pages produced)

Agent (step 5 — first FAIL → ask):
  vscode_askQuestions:
    "Item (d) bibliography missing: 'nonexistent.bib' not found.
     Auto-fix catalogue suggests fixing the bibliography path or
     using --resource-path. Fix?"
    Options: [Fix: yes] [Fix: no] [Fix: <freeform>]

User: Fix: no — this is a deliberate fixture, leave it broken.

Agent (step 7 — log decline):
  Appended to fix/TODO.md:
    | 2026-04-23 | "openBinaryFile: nonexistent.bib does not exist"
      | fix/staging/scratch-broken.md | check-declined
      | Quality-check rubric item (d). User confirmed fixture is intentionally
        broken; no SKILL.md or fixture change. |

Agent: Continuing to next FAIL (h)…
```

The takeaway: when no PDF is produced, layout items collapse to UNKNOWN/FAIL and the
stderr-derived items (c, d, h) are the actionable ones — exactly the auto-fix catalogue
entries in [`SKILL.md`](../SKILL.md#check-mode).
