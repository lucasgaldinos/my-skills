# Self-update protocol — worked examples

Companion to the `## Self-update protocol` section in `SKILL.md`. The classification
rules and workflow live in `SKILL.md`; only the worked transcripts live here so
`SKILL.md` stays under its 500-line budget.

## Example 1 — missing bib key (major)

Stderr: `[WARNING] Citeproc: citation goldberg1989 not found` plus exit code 0 *but* the
rendered PDF shows `[?]` for that citation. Classification: **major** (missing bib entry,
even though pandoc exited 0).

Ask → user picks `Yes — propose patch` → diff adds a new gotcha row:

> "`--citeproc` emits WARNING, not ERROR, for missing keys — grep stderr for
> `citation .* not found` in CI."

User picks `Apply` → SKILL.md updated.

## Example 2 — LaTeX fatal from unclosed math (major)

Stderr tail:

```text
! Missing $ inserted.
! Emergency stop.
Fatal error occurred, no output PDF file produced!
```

Classification: **major** (LaTeX Fatal). Ask → user picks `No — log to fix/TODO.md` →
row appended:

> `2026-04-22 | "Fatal error occurred, no output PDF file produced!" |
> templates/article.md | declined | unclosed $ reported; user will fix source
> rather than extend skill.`

No SKILL.md change.

## Example 3 — overfull hbox only (minor)

Stderr: `Overfull \hbox (12.3pt too wide) in paragraph at lines 45--47`, exit 0,
`pdfinfo` reports 42 pages. Classification: **minor**. No prompt, no log, *unless* the
user explicitly says "the PDF is wrong". If they do, re-classify as user-driven and
follow the `<workflow>` starting at step 2.

## Example 4 — orchestrator-executed dry-run (real, 2026-04-22)

Trigger: `pandoc fix/staging/scratch-broken.md --pdf-engine=xelatex --citeproc -o /tmp/scratch-broken.pdf`
with `bibliography: nonexistent.bib` in the YAML.

- Exit code: 99
- Stderr: `File nonexistent.bib not found in resource path`
- Classification: **major** (categories *a* exit ≠ 0 + *d* missing bibliography)
- User chose: `No — log to fix/TODO.md`
- Outcome: row appended to `fix/TODO.md`; `fix/staging/scratch-broken.md` retained as
  a regression fixture for future check-mode tests.
