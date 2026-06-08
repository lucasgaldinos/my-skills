# Research article YAML frontmatter (XeLaTeX PDF)

For single-author papers and conference / journal submissions. Simpler than the thesis
template — no chapters, no auto-TOC by default.

```yaml
---
title: "[Paper title]"
author:
  - name: "[Author 1]"
    affiliation: "[Institution]"
    email: "[email]"
  - name: "[Author 2]"
    affiliation: "[Institution]"
date: [YYYY-MM-DD]
lang: en-US                             # or pt-BR
abstract: |
  [Paste the abstract here. Indent the body with two spaces so YAML
  preserves the block scalar. Blank lines inside are allowed.]
keywords: [keyword1, keyword2, keyword3]
bibliography: ./refs.bib
link-citations: true
csl: ./ieee.csl                         # or acm, apa, abnt — match venue
documentclass: article
classoption:
  - 11pt
  - a4paper
geometry:
  - margin=2.5cm
header-includes:
  - \usepackage{booktabs}
  - \usepackage{microtype}              # Better line-breaking for camera-ready quality
---
```

## Compile

```bash
pandoc paper.md \
  --pdf-engine=xelatex \
  --citeproc \
  -o paper.pdf
```

## Notes

- **Multi-author blocks** work only if the template expects them. Pandoc's default
  `default.latex` template handles the `author:` list correctly, but many journal `.cls`
  files want a custom template — check the venue's pandoc template or pass `--template=…`.
- **`abstract:` as a block scalar** (`abstract: |`) allows multi-paragraph abstracts.
  Single-line abstracts can be written inline: `abstract: "Short text."`.
- **`keywords:` as a YAML list** is rendered by the default template; custom `.cls` files
  may ignore it — check the output PDF.
