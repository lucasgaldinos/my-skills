# Check mode — workflow & auto-fix catalogue

Companion to the `## Check mode` section in `SKILL.md`. The trigger phrases and
opt-in policy live in `SKILL.md`; the operational workflow and the symptom-to-fix
table live here so `SKILL.md` stays under its 500-line budget.

The full scoring sheet is in [quality-rubric.md](quality-rubric.md).

## Workflow (7 steps)

1. **Locate the PDF.** Ask the user for the path if unclear; otherwise infer from the
   most recent compile or the `argument-hint`.
2. **Re-run the last pandoc command with verbose logging.** Append
   `--verbose 2>&1 | tee fix/last-compile.log`. Run pandoc directly — there is no
   preflight wrapper.
3. **Load PDF inspection capability.** Load the `pdf` skill plus a vision-capable
   rubric scorer; supply [quality-rubric.md](quality-rubric.md) as the scoring sheet.
4. **Classify each rubric item PASS / FAIL / UNKNOWN.** Combine stderr signals from
   `fix/last-compile.log` with vision observations of the PDF.
5. **For each FAIL, ask the user.** Call `vscode_askQuestions` with options
   `Fix: yes` / `Fix: no` / `Fix: <freeform suggestion>`. One question per FAIL —
   never batch.
6. **On `Fix: yes`,** propose a minimal patch (compile flag, frontmatter field, or
   filter change) and call `vscode_askQuestions` a second time with options
   `Apply` / `Revise` / `Cancel`. Only on `Apply` do you write changes.
7. **On `Fix: no`,** append a row to `fix/TODO.md` tagged `check-declined` with the
   rubric item, the FAIL evidence, and a one-sentence rationale.

## Auto-fix catalogue

When a FAIL maps cleanly to one of the symptoms below, propose the listed fix at step 6.

| Symptom (in stderr / PDF)                                       | Recommended fix                                                          | Confidence |
|-----------------------------------------------------------------|--------------------------------------------------------------------------|------------|
| Literal `[@key]` in body; no bibliography                       | Add `--citeproc`                                                         | high       |
| `pandoc-crossref` runs but `??` persists; bib keys not resolved | Reorder filters: `pandoc-crossref` BEFORE `--citeproc`                   | high       |
| LaTeX error mentions `inputenc` / non-ASCII char on `pdflatex`  | Switch to `--pdf-engine=xelatex`                                         | high       |
| Unicode source compiles on `xelatex`, fails on `pdflatex`       | Switch to `--pdf-engine=xelatex`                                         | high       |
| Beamer frame error referencing `longtable`                      | Add `--lua-filter=scripts/beamer-table-fix.lua`                          | high       |
| `Citeproc` / pandoc: `<name>.bib not found in resource path`    | Fix `bibliography:` path or add `--resource-path=<dir>`                  | medium     |
