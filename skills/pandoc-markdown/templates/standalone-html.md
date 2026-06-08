---
# === standalone-html.md — self-documenting template ===
# Demonstrates: standalone HTML target with KaTeX math and citeproc bibliography.
title: "Standalone HTML Template"
author: "Template Author"
date: 2026-04-22
lang: en-US
bibliography:
  - refs.bib                           # relative: stage refs.bib next to this file
csl: abnt.csl                         # relative: stage/symlink the ABNT CSL as abnt.csl
link-citations: true
---

# About this template

This file mirrors `minimal-article.md` but targets HTML instead of PDF.
Differences from the PDF target:

- `-s` (`--standalone`) wraps the body in a full `<html>` document.
- `--katex` loads KaTeX from a CDN for fast client-side math rendering.
- `--citeproc` resolves citations from `refs.bib` using the ABNT CSL.
- No LaTeX engine is needed.

# Introduction

Parallel metaheuristics for routing problems span GPU and CPU backends
[@schulz2013gpu]. Guided local search remains a classical baseline
[@voudouris1999tsp].

Inline math: $C(\pi) = \sum_{i=1}^{n-1} d(\pi_i, \pi_{i+1}) + d(\pi_n, \pi_1)$.

# Results

Display math:

$$
\text{Speedup} = \frac{T_\text{CPU}}{T_\text{GPU}}.
$$

| Problem size | CPU time (s) | GPU time (s) |
|-------------:|-------------:|-------------:|
|          100 |          2.0 |          0.3 |
|          400 |         35.0 |          1.8 |

# References

<!-- citeproc inserts the bibliography here -->

## Notes

- `--katex` renders math client-side; for offline HTML use `--mathml` or
  `--mathjax` (MathJax can also be self-hosted).
- `--embed-resources --standalone` (not used here) would inline images and
  CSS to produce a single self-contained `.html` file.
- An optional `--css=assets/styles/academic.css` (added in Phase 2) would
  apply academic typography.

## Portability

The YAML uses **relative paths** (`refs.bib`, `abnt.csl`). Either stage
both files next to the template, or pass `--resource-path` so pandoc can
find them:

```bash
pandoc standalone-html.md \
  --resource-path=.:/path/to/documents_tcc \
  -s --katex --citeproc -o standalone-html.html
```

In this repo: `documents_tcc/refs.bib` and
`documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl`
(symlink or rename the CSL to `abnt.csl`).

## Compile

```bash
# Assumes refs.bib and abnt.csl sit next to this file.
pandoc standalone-html.md \
  -s --katex --citeproc \
  -o standalone-html.html
```
