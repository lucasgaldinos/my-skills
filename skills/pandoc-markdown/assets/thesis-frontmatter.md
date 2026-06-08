# Thesis / monograph YAML frontmatter (XeLaTeX PDF)

Copy the block below to the top of the `.md` file. Fill every `[placeholder]`. Every field
has a reason — the annotations explain when it matters.

```yaml
---
title: "[Document title]"
subtitle: "[Optional subtitle]"
author: "[Full author name]"
date: [YYYY-MM-DD]                      # ISO date; localized by citeproc per `lang`
lang: pt-BR                             # REQUIRED: drives hyphenation + citeproc locale
bibliography:
  - ./refs.bib                          # Path relative to the .md file
reference-section-title: "Referências"  # Heading for the auto-generated bibliography
link-citations: true                    # In-text cites hyperlink to the bib entry
csl: ./associacao-brasileira-de-normas-tecnicas-numerico.csl  # ABNT numeric style
toc: true                               # Generate a table of contents
toc-depth: 3
numbersections: true                    # Number chapters/sections
documentclass: report                   # `report` = chapter-based; `article` = no chapters
geometry:                               # Passed to LaTeX `geometry` package
  - margin=2.5cm
fontsize: 12pt
linestretch: 1.5                        # 1.5 line spacing (ABNT requirement)
indent: true                            # Paragraph indentation instead of vertical skip
mainfont: "Latin Modern Roman"          # XeLaTeX-only; any system font name
header-includes:
  - \usepackage{booktabs}               # Better \toprule / \midrule / \bottomrule
  - \usepackage{longtable}
  - \usepackage[brazilian]{babel}
  - \newcommand{\standalonefiglabel}[1]{\refstepcounter{figure}\label{#1}}
---
```

## Notes

- **`documentclass: report`** is required for `# Chapter` headings. For articles without
  chapters, use `article` and treat `#` as section.
- **`csl:`** overrides the default citeproc style. The repo ships
  `documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl` — use a relative path
  so the document is portable.
- **`mainfont:`** only works with `xelatex` or `lualatex`. With `pdflatex` it is silently
  ignored and the default Computer Modern is used.
- **`header-includes:`** is raw LaTeX. Typos here fail the *LaTeX* build, not the YAML parse —
  errors look like "Undefined control sequence" from `latexmk`, not pandoc.

## Compile

```bash
pandoc thesis.md \
  --pdf-engine=xelatex \
  --citeproc \
  --resource-path=.:assets \
  -o thesis.pdf
```

With a defaults file: `pandoc -d defaults-academic.yaml thesis.md -o thesis.pdf`.
