---
# === minimal-article.md — self-documenting template ===
# Demonstrates: article class, abstract, two sections, inline + display math,
# two citations rendered via citeproc + ABNT CSL, one pipe table.
title: "A Minimal Article Template"
author: "Template Author"            # default pandoc LaTeX template expects a string; list-of-objects renders as "true"
date: 2026-04-22
lang: en-US                          # English for journal-style output
documentclass: article               # short paper format; no \chapter
geometry: margin=2.5cm
fontsize: 11pt
linestretch: 1.15                    # journals typically allow tighter spacing than theses
abstract: |
  This short template demonstrates the minimum pandoc setup required to
  compile a journal-style article with citations, math, and tables.
bibliography:
  - /home/lucas_galdino/chimera/gpu_accelerated/documents_tcc/refs.bib
csl: /home/lucas_galdino/chimera/gpu_accelerated/documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl
link-citations: true
linkcolor: blue
urlcolor: blue
---

# About this template

This article demonstrates the minimal YAML required for a journal-style
submission using `pandoc` + `xelatex` + `citeproc`.

# Introduction

Parallel metaheuristics for routing problems span GPU and CPU backends
[@schulz2013gpu]. Guided local search remains a classical baseline
[@voudouris1999tsp].

Inline math renders naturally: the cost of a tour is
$C(\pi) = \sum_{i=1}^{n-1} d(\pi_i, \pi_{i+1}) + d(\pi_n, \pi_1)$.

# Results

Display math works equally well:

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

- `abstract:` in YAML emits `\begin{abstract}…\end{abstract}` automatically for LaTeX output.
- Two citations exercise the bibliography pipeline (a single citation would not).
- Switching to `lang: pt-BR` activates Portuguese hyphenation (see `minimal-thesis.md`).

## Compile

```bash
pandoc minimal-article.md \
  --pdf-engine=xelatex \
  --citeproc \
  -o minimal-article.pdf
```
