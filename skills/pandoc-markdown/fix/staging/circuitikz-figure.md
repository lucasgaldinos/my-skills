---
# === circuitikz-figure.md — self-documenting template ===
# Demonstrates: a simple RC circuit drawn with circuitikz in a floating figure.
title: "CircuiTikZ Figure Template"
author: "Template Author"
date: 2026-04-22
lang: en-US
documentclass: article
geometry: margin=2.5cm
fontsize: 11pt
header-includes:
  - \usepackage{circuitikz}          # requires `tlmgr install circuitikz` on minimal TeX Live
  - \ctikzset{bipoles/length=0.9cm}  # tweak component sizes globally
---

# About this template

This document renders an RC circuit (one resistor, one capacitor) using the
`circuitikz` LaTeX package, inside a pandoc-managed LaTeX document. If
`tlmgr install circuitikz` has not been run, this template will fail to
compile — see the Notes section for the install hint.

# Simple RC Low-Pass Filter

Figure \ref{fig:rc} shows the canonical passive RC low-pass filter topology.

```{=latex}
\begin{figure}[ht]
  \centering
  \begin{circuitikz}
    \draw (0,0) to [V, l=$V_\text{in}$] (0,3)
                to [R=$R$]              (3,3)
                to [C=$C$]              (3,0) -- (0,0);
    \draw (3,3) -- (4.5,3) node[right] {$V_\text{out}^+$};
    \draw (3,0) -- (4.5,0) node[right] {$V_\text{out}^-$};
  \end{circuitikz}
  \caption{Passive RC low-pass filter with cutoff $f_c = 1 / (2\pi R C)$.}
  \label{fig:rc}
\end{figure}
```

## Notes

- **Install requirement**: on a minimal TeX Live, run
  `tlmgr install circuitikz pgf` before first compile.
- `\ctikzset{bipoles/length=0.9cm}` in `header-includes` is a project-wide
  component-size preference; remove it to keep circuitikz defaults.
- `circuitikz` is TikZ-heavy; if compile time becomes an issue, try
  `--pdf-engine=lualatex` (CON-002 allows lualatex as a TikZ fallback).

## Compile

```bash
pandoc circuitikz-figure.md \
  --pdf-engine=xelatex \
  -o circuitikz-figure.pdf
```
