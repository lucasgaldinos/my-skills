---
# === tikz-figure.md — self-documenting template ===
# Demonstrates: native TikZ/pgfplots figure in a thesis-style document,
# with \label/\ref via raw LaTeX (no pandoc-crossref required).
title: "TikZ Figure Template"
author: "Template Author"
date: 2026-04-22
lang: en-US
documentclass: article
geometry: margin=2.5cm
fontsize: 11pt
header-includes:                     # injected into the LaTeX preamble
  - \usepackage{tikz}                # base TikZ
  - \usepackage{pgfplots}            # axis environment used below
  - \pgfplotsset{compat=1.18}        # pin pgfplots behavior; silences compat warnings
---

# About this template

This document draws a native TikZ/pgfplots figure inside a floating `figure`
environment and references it with raw LaTeX `\ref{fig:parabola}`. No
`pandoc-crossref` filter is required.

# TikZ via pgfplots

See Figure \ref{fig:parabola} for a parabola rendered natively by pgfplots.

```{=latex}
\begin{figure}[ht]
  \centering
  \begin{tikzpicture}
    \begin{axis}[
        width=10cm, height=6cm,
        xlabel={$x$}, ylabel={$y$},
        grid=major,
        domain=-3:3, samples=80,
    ]
      \addplot[blue, thick] {x^2};
      \addplot[red, dashed] {2*x};
    \end{axis}
  \end{tikzpicture}
  \caption{Parabola $y = x^2$ (blue) with its derivative $y = 2x$ (red).}
  \label{fig:parabola}
\end{figure}
```

# Plain TikZ

A minimal TikZ picture without pgfplots, for completeness:

```{=latex}
\begin{figure}[ht]
  \centering
  \begin{tikzpicture}
    \draw[->] (0,0) -- (3,0) node[right] {$x$};
    \draw[->] (0,0) -- (0,2) node[above] {$y$};
    \draw[thick, blue] (0,0) -- (2,1.5);
  \end{tikzpicture}
  \caption{Basic TikZ axes with a vector.}
  \label{fig:tikz-basic}
\end{figure}
```

See also Figure \ref{fig:tikz-basic}.

## Notes

- `{=latex}` raw blocks are preserved verbatim when targeting LaTeX/PDF; they
  are dropped for HTML output (that is intentional — see `strip-raw-latex-for-html.lua`
  if HTML+TikZ becomes a requirement).
- `\pgfplotsset{compat=1.18}` freezes pgfplots' internal behavior; bump the
  version if newer features are needed.
- TikZ compiles with `xelatex`. For very heavy TikZ jobs, `lualatex` is an
  acceptable fallback (CON-002).

## Compile

```bash
pandoc tikz-figure.md \
  --pdf-engine=xelatex \
  -o tikz-figure.pdf
```
