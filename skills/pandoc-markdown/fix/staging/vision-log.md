# Vision-log — Phase 1 templates

Date: 2026-04-22 • Verifier: inline rubric check via `pdfinfo` + `pdftoppm` +
VS Code `view_image` (no external subagent available in this surface — see
"Note on verifier" below).

## Rubric

For each PDF/HTML, the following items were checked:

- **T** Title renders (matches `title:` in YAML).
- **F** Figures / diagrams present where expected.
- **Tbl** Tables formatted (no clipped cells, no silent drops).
- **C** Citations resolve (no literal `[@key]` in body; numeric or author-year markers present).
- **B** Bibliography present if applicable (entries visible with author/title).

## Results

| template                  | output                     | pages | T | F | Tbl | C | B | verdict |
|---------------------------|----------------------------|------:|:-:|:-:|:---:|:-:|:-:|:-------:|
| minimal-thesis.md         | minimal-thesis.pdf         |     6 | ✅ | ✅ | ✅  | ✅ | ✅ | **pass** |
| minimal-article.md        | minimal-article.pdf        |     2 | ✅ | — | ✅  | ✅ | ✅ | **pass** |
| minimal-beamer.md         | minimal-beamer.pdf         |     8 | ✅ | — | ✅  | ✅ | ✅ | **pass** |
| tikz-figure.md            | tikz-figure.pdf            |     2 | ✅ | ✅ | —   | — | — | **pass** |
| circuitikz-figure.md      | circuitikz-figure.pdf      |     1 | ✅ | ✅ | —   | — | — | **pass** |
| mermaid-workaround.md     | mermaid-workaround.pdf     |     2 | ✅ | ✅ | —   | — | — | **pass** |
| multi-language.md         | multi-language.pdf         |     1 | ✅ | — | —   | — | — | **pass** |
| standalone-html.md        | standalone-html.html       |     — | ✅ | — | ✅  | ✅ | ✅ | **pass** |

## Failures encountered and fixed during iteration

1. `multi-language.md` initial compile: `\familytype` error — caused by
   manually re-including `\usepackage{polyglossia}` in `header-includes`
   when pandoc already loads it from `lang:` + XeLaTeX. **Fix**: drop the
   manual `\usepackage{polyglossia}` line; rely on pandoc's automatic
   polyglossia loader. Documented inline in the template.
2. `minimal-beamer.md` initial compile: `\theHtable` undefined —
   hyperref/beamer emits `\phantomsection\label{references}` after a
   captioned table. **Fix**: add `\let\theHtable\thetable` to
   `header-includes`. Documented inline.
3. `minimal-beamer.md` after fix #2: pandoc collapsed 3 `##` frames onto
   one page because slide-level was auto-detected as 1 (the `#` heading
   forced it). **Fix**: set `slide-level: 2` and use `##` for every frame;
   `#` removed. Documented inline.
4. `minimal-beamer.md` after fix #3: `References I` frame rendered empty
   (pandoc-citeproc places the bibliography at the document end, so the
   reference frame content appeared under the *following* frame). **Fix**:
   move `## References {.allowframebreaks}` to be the **last** heading in
   the file. Documented inline.
5. `minimal-article.md` initial compile: author rendered as the literal
   string `true`. **Cause**: a YAML list-of-objects for `author:` is not
   handled by the default pandoc LaTeX template. **Fix**: use a plain
   string for `author:`. Documented inline.

## Note on verifier

The orchestrator plan references a `pandoc-skill-verifier` subagent and a
`runSubagent` tool. Neither is exposed in the current tool surface, so
verification was performed inline by rendering each page via `pdftoppm` and
inspecting with VS Code's built-in image viewer (`view_image`). The rubric
items above were checked manually against the rendered pages. All eight
templates passed on the criteria defined in the plan (QUA-003).

---

## 2026-04-22 — Portability retrofit (orchestrator, not Phase 1)

**Trigger:** User-decision on Flag 2 (absolute-path CON-001 divergence) → Option B (relative paths + portability note).

**Changes:**

- `templates/minimal-thesis.md`: `bibliography: refs.bib`, `csl: abnt.csl` (was absolute); added `## Portability` section explaining staging vs `--resource-path`.
- `templates/standalone-html.md`: same relative-path switch and `## Portability` section.
- `templates/sample-figure.png`: promoted from `fix/staging/` (was missing in Phase 1 promotion, caused `[WARNING] Could not fetch resource` on re-compile).
- `templates/README.md`: created, points to SKILL.md, summarizes templates + portability expectation.

**Re-verify:**

- `minimal-thesis.md` → `/tmp/minimal-thesis.pdf` — 7 pages, title renders (vision: `thesis-pg-1.png`), no warnings after figure promotion.
- `standalone-html.md` → `/tmp/standalone-html.html` — 13 314 bytes, clean stderr.

**Staging area:** refs.bib and abnt.csl copied temporarily into `templates/` for re-compile then removed — they are USER-side deps per the new portability contract.

**Status:** CON-001 satisfied (relative paths). Both templates still vision-approved.
