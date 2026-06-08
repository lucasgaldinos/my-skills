---
# === multi-language.md — self-documenting template ===
# Demonstrates: Portuguese primary language with an inline English section,
# routed via polyglossia (XeLaTeX) through pandoc lang spans.
title: "Documento Multi-idioma"
author: "Template Author"
date: 2026-04-22
lang: pt-BR                          # primary language → polyglossia \setmainlanguage{portuguese}
otherlangs: [en-US]                  # secondary languages → \setotherlanguages{english}
documentclass: article
geometry: margin=2.5cm
fontsize: 11pt
# Note: pandoc auto-loads polyglossia when `lang:` is set and --pdf-engine=xelatex.
# Do NOT re-include \usepackage{polyglossia} in header-includes — that re-runs
# \setmainlanguage with an empty argument and triggers "Undefined control sequence
# \familytype" errors.
---

# Sobre este template

Este documento usa **português** como idioma principal e demonstra como
embutir um trecho em **inglês** via atributo de idioma do pandoc
(`[texto]{lang=en}` ou `<div lang="en-US">…</div>`).

# Trecho em inglês

[This paragraph is written in English and should be rendered with English
hyphenation and "curly quotes"]{lang=en-US}

Um bloco inteiro em inglês usa `<div>`:

::: {lang=en-US}
This block of text is entirely in English. Hyphenation rules switch here
accordingly. Use this form when a whole subsection is in another language.
:::

Voltamos ao português para continuar a discussão normalmente.

## Notes

- **polyglossia vs babel**: prefer `polyglossia` with XeLaTeX/LuaLaTeX
  (better Unicode, active maintenance). Use `babel` only when stuck on
  pdfLaTeX — which is forbidden by CON-002 in this repo.
- Pandoc's `[…]{lang=en-US}` spans map to `\foreignlanguage{english}{…}`
  automatically with `polyglossia` and `lang:` set.
- `otherlangs:` emits `\setotherlanguage{english}` in the preamble. Without
  it, inline language switches degrade silently.
- Hyphenation is the primary visible effect; quote glyphs and some
  typographic spacing also change with the language.

## Compile

```bash
pandoc multi-language.md \
  --pdf-engine=xelatex \
  -o multi-language.pdf
```
