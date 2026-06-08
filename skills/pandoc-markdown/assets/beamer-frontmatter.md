# Beamer slide deck YAML frontmatter (PDF slides)

Based on this repo's working thesis presentation (see repo memory). Known-good against
Pandoc 3.x + XeLaTeX + beamer table fix filter.

```yaml
---
title: "[Presentation title]"
subtitle: "[Optional subtitle]"
author: "[Author]"
date: [YYYY]
institute: "[Institution — one line]"
theme: "Madrid"                         # Any beamer theme: Madrid, Berlin, Warsaw, …
colortheme: "dolphin"
fonttheme: "structurebold"
fontsize: 11pt
aspectratio: 169                        # 169 = 16:9 widescreen; 43 = 4:3
lang: pt-BR                             # or en-US
bibliography: ./refs.bib                # Optional — only if slides cite
link-citations: true
header-includes:
  - \usepackage{booktabs}
  - \setbeamertemplate{footline}{\hfill\insertframenumber/\inserttotalframenumber\hspace{2mm}\vspace{2mm}}
# DO NOT set:
#   toc: true              → produces duplicate TOC + section-divider slides
#   reference-section-title: "…"  → breaks {.allowframebreaks} on the refs heading
---
```

## Slide structure rules

- **Level-1 heading (`#`)** = section divider (title-only slide).
- **Level-2 heading (`##`)** = slide title. This is the default *slide level* when `##` is
  the deepest heading followed by content.
- **Level-3 heading (`###`)** inside a slide = block header (creates a `\begin{block}`).
  Classes `.example` and `.alert` produce `exampleblock` and `alertblock`.
- **Horizontal rule (`---`)** always starts a new slide — useful for splitting a long `##`
  section into multiple slides with the same title.

## Compile (this repo's working command)

```bash
pandoc slides.md \
  -t beamer \
  -o slides.pdf \
  --pdf-engine=xelatex \
  --citeproc \
  --lua-filter=scripts/beamer-table-fix.lua \
  --resource-path=.:assets
```

## Notes / gotchas

- **Mermaid diagrams fail inside beamer frames** (pandoc 3.x + mermaid-filter). Pre-render
  to PNG: `mmdc -i diagram.mmd -o diagram.png`, then `![](assets/diagram.png){width=80%}`.
- **Long tables break in beamer frames.** The `beamer-table-fix.lua` filter in `scripts/`
  rewrites `longtable` → `tabular`.
- **`## Referências {.allowframebreaks}`** must be written manually (not via
  `reference-section-title:`) for the bibliography to span multiple slides.
- **Code blocks need `\begin{frame}[fragile]`.** Pandoc adds this automatically when it
  detects a verbatim block — do not set it yourself.
