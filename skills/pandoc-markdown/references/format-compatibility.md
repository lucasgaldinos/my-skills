# Pandoc format compatibility matrix

Source of truth: <https://pandoc.org/MANUAL.html#general-options>, `pandoc --list-input-formats`,
`pandoc --list-output-formats`. This file is a curated summary for academic workflows —
not an exhaustive list of the 50+ formats pandoc supports.

---

## 1. Reader / writer capability

Legend: `R` = can read, `W` = can write, `R/W` = round-trip (with the caveats noted below).

| Format                       | Read | Write | Common use                                                   |
| ---------------------------- | :--: | :---: | ------------------------------------------------------------ |
| `markdown` (pandoc-flavored) |  R   |   W   | Primary authoring source                                     |
| `gfm`                        |  R   |   W   | GitHub READMEs, issues. **No native math**; avoid for academic content. |
| `commonmark` / `commonmark_x`|  R   |   W   | Stricter markdown flavors; `commonmark_x` adds pandoc extensions |
| `latex`                      |  R   |   W   | PDF pipeline intermediate; also reads existing `.tex`         |
| `pdf`                        |      |   W   | **Write-only** (via `--pdf-engine`). No `-f pdf`.              |
| `beamer`                     |      |   W   | Write-only. Input is still markdown.                          |
| `html` / `html4` / `html5`   |  R   |   W   | Web output; arXiv / journal pre-prints often ship as HTML     |
| `docx`                       |  R   |   W   | Microsoft Word. Styling via `--reference-doc=template.docx`.  |
| `odt`                        |  R   |   W   | LibreOffice.                                                  |
| `rtf`                        |      |   W   | Legacy. Write-only in recent pandoc.                          |
| `epub` / `epub2` / `epub3`   |  R   |   W   | E-books. See `references/epubs.md`.                           |
| `ipynb`                      |  R   |   W   | Jupyter notebooks. See `references/jupyter-notebooks.md`.      |
| `rst`                        |  R   |   W   | reStructuredText (Sphinx).                                    |
| `org`                        |  R   |   W   | Emacs org-mode.                                               |
| `typst`                      |  R   |   W   | Newer markup / PDF pipeline (pandoc ≥ 3.1).                    |
| `revealjs` / `slidy` / `dzslides` |    |   W   | HTML slide writers.                                            |
| `asciidoc`                   |  R   |   W   | Technical docs.                                               |
| `opml`                       |  R   |   W   | Outlines.                                                     |
| `csv` / `tsv`                |  R   |       | **Read-only**, converts to a single pandoc `Table`.           |
| `bibtex` / `biblatex` / `csljson` / `ris` |  R |  W  | Bibliography formats; read for `--bibliography=`, write for export. |
| `native` / `json`            |  R   |   W   | Pandoc AST. Useful for inter-filter debugging.                |

## 2. Feature × output-format support

This is the table academic authors actually want — "will my citation / figure / math / cross-ref
survive when I switch the `-t` target?".

| Feature                                  | PDF (XeLaTeX) | Beamer  | HTML    | DOCX   | EPUB    |
| ---------------------------------------- | :-----------: | :-----: | :-----: | :----: | :-----: |
| YAML `bibliography:` + `--citeproc`      | ✅            | ✅      | ✅      | ✅     | ✅      |
| `[@key]` citations                       | ✅            | ✅      | ✅      | ✅     | ✅      |
| ABNT / CSL styles                        | ✅            | ✅      | ✅      | ✅     | ✅      |
| Math `$…$` / `$$…$$`                     | ✅ (native)   | ✅      | ✅ (KaTeX / MathJax / MathML) | ⚠️ (OMML — some loss) | ✅ (MathML) |
| Raw LaTeX (`\textbf{}`, envs)            | ✅            | ✅      | ❌ (silently dropped) | ❌ | ❌ |
| Raw HTML (`<div>`, `<span>`)             | ❌ (dropped)  | ❌      | ✅      | ⚠️     | ✅      |
| Figures with captions (`![cap](img){}`)  | ✅            | ✅      | ✅      | ✅     | ✅      |
| `pandoc-crossref` `@fig:`/`@tbl:`/`@eq:` | ✅            | ✅      | ✅      | ✅     | ✅      |
| Pipe tables                              | ✅            | ✅ (see `beamer-table-fix.lua`) | ✅ | ✅ | ✅ |
| Longtable (auto-emitted)                 | ✅            | ❌ (needs filter) | ✅ | ✅ | ✅ |
| TikZ                                     | ✅            | ⚠️ (`[fragile]` frames silently fail) | ❌ | ❌ | ❌ |
| Mermaid via `pandoc-ext/diagram`         | ✅            | ⚠️ (pre-render recommended) | ✅ | ✅ | ✅ |
| PlantUML via `pandoc-ext/diagram`        | ✅            | ⚠️ (pre-render recommended) | ✅ | ✅ | ✅ |
| `header-includes:` (LaTeX preamble)      | ✅            | ✅      | ❌      | ❌     | ❌      |
| CSS via `--css=`                         | ❌            | ❌      | ✅      | ❌     | ✅      |
| Syntax highlighting (`--highlight-style=`) | ✅         | ✅      | ✅      | ✅     | ✅      |
| Footnotes `[^1]`                         | ✅            | ⚠️ (break frames) | ✅ | ✅ | ✅ |
| `lang=…` spans (polyglossia / CSS)       | ✅            | ✅      | ✅      | ✅     | ✅      |

Legend: ✅ works, ⚠️ works with caveats, ❌ silently lost / unsupported.

## 3. Portability rules of thumb

<rules>

- **Target LaTeX-only features only when the document is LaTeX-only.** Raw `\env{}` is
  silently dropped in HTML/DOCX. If you need multi-format output, keep everything in
  portable Markdown + Pandoc attribute syntax; use filters (e.g. `strip-raw-latex-for-html.lua`)
  to bridge the gap.
- **Never target `gfm` for academic content.** GFM has no citations, no math, no cross-refs.
  Use `markdown` (pandoc-flavored) as the intermediate and convert from there.
- **DOCX is for reviewers, not for archive.** Citations, figures, and math survive but
  styling is mapped to Word styles via `--reference-doc=template.docx`. Treat DOCX as an
  exchange format, not a source of truth.
- **EPUB3 + MathML is the accessible-math pathway.** EPUB2 falls back to images. For
  thesis archives where accessibility matters, produce both PDF and EPUB3.
</rules>

## 4. Cross-references

- `pandoc --list-input-formats` and `pandoc --list-output-formats` — authoritative and
  matches the installed version.
- `references/pandocs-markdown.md` — pandoc markdown syntax (`tex_math_dollars`, raw blocks).
- `references/diagrams-and-filters.md` — diagram stack details and filter order.
- `references/epubs.md` — EPUB-specific options.
- `references/jupyter-notebooks.md` — `ipynb` round-trip.
