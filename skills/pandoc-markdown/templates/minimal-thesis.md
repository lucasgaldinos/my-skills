---
# === minimal-thesis.md — self-documenting template ===
# Demonstrates: report class, one chapter, one figure, one pipe table,
# one citation rendered via citeproc + ABNT CSL, one display-math block.
title: "Minimal Thesis Template"
author: "Template Author"
date: 2026-04-22
lang: pt-BR                          # polyglossia picks Portuguese; affects hyphenation and babel labels
documentclass: report                # 'report' gives \chapter; use 'book' for two-sided, 'article' for short papers
geometry: margin=2.5cm               # ABNT-friendly default; override per institution
fontsize: 12pt
linestretch: 1.5                     # 1.5 line spacing is standard for thesis bodies in PT-BR
toc: true                            # generate table of contents
toc-depth: 0                         # chapters only (LaTeX counter: chapter=0, section=1); template-meta stays out of TOC
number-sections: true                # number chapters/sections; required for \ref{sec:...}
bibliography:
  - refs.bib                           # relative: place refs.bib next to this file (or pass --resource-path)
csl: abnt.csl                         # CON-001: reuse the repo CSL by placing/symlinking it here as abnt.csl
link-citations: true                 # turns [@key] into clickable hyperlinks in the PDF
linkcolor: blue
urlcolor: blue
---

# Sobre este template

Este arquivo demonstra o mínimo necessário para compilar uma dissertação/tese
em PDF via `pandoc` + `xelatex` + `citeproc`, incluindo:

- Frontmatter YAML com `documentclass: report`.
- Uma figura PNG embutida.
- Uma tabela em sintaxe *pipe* do pandoc.
- Uma citação bibliográfica resolvida via `refs.bib` + CSL ABNT.
- Um bloco de matemática display.

# Capítulo de Exemplo

## Introdução

Trabalhos clássicos de otimização em GPU fornecem o pano de fundo teórico
para o restante desta demonstração [@tsp_gpu].

## Figura

![Curvas seno e cosseno gerradas para ilustração](sample-figure.png){#fig:sample width=70%}

A Figura apresenta duas funções trigonométricas para referência.

## Tabela

| Método   | Tempo (s) | Speedup |
|----------|----------:|--------:|
| CPU      |     120.0 |    1.0x |
| GPU      |      12.5 |    9.6x |

## Matemática

A distância euclidiana entre dois pontos no plano é

$$
d(p, q) = \sqrt{(p_x - q_x)^2 + (p_y - q_y)^2}.
$$

# Referências

<!-- citeproc injeta a bibliografia aqui -->

## Notes

- `lang: pt-BR` activates polyglossia (XeLaTeX) for Portuguese hyphenation.
- `{#fig:sample}` is a pandoc attribute; to get numbered figure references, add the `pandoc-crossref` filter (not loaded here to keep the template minimal).
- To switch engines to `lualatex`, change `--pdf-engine=xelatex` in the compile command below.

## Portability

The YAML uses **relative paths** (`refs.bib`, `abnt.csl`). Two equivalent ways to satisfy them:

1. **Stage the files next to the template** (simplest):

   ```bash
   cp /path/to/your/refs.bib ./refs.bib
   cp /path/to/abnt-numerico.csl ./abnt.csl
   pandoc minimal-thesis.md --pdf-engine=xelatex --citeproc -o minimal-thesis.pdf
   ```

2. **Point pandoc at an existing directory** via `--resource-path`:

   ```bash
   pandoc minimal-thesis.md \
     --resource-path=.:/path/to/documents_tcc \
     --pdf-engine=xelatex --citeproc -o minimal-thesis.pdf
   ```

   In this repo that directory is `documents_tcc/` and the CSL file is named:

   ```text
   documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl
   ```

   Symlink or rename it to `abnt.csl` inside your `--resource-path` root.

## Compile

```bash
# Assumes refs.bib and abnt.csl sit next to this file.
pandoc minimal-thesis.md \
  --pdf-engine=xelatex \
  --citeproc \
  -o minimal-thesis.pdf
```
