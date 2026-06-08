---
# === minimal-beamer.md — self-documenting template ===
# Demonstrates: title slide, 3 content slides (bullets, math, table),
# one citation, use of scripts/beamer-table-fix.lua to avoid longtable-in-frame bug.
title: "Minimal Beamer Deck"
subtitle: "Pandoc Skill Template"
author: "Template Author"
date: 2026-04-22
lang: en-US
theme: Madrid                        # any stock beamer theme works; Madrid is a safe default
colortheme: default
aspectratio: 169                     # 16:9 widescreen; use 43 for 4:3
bibliography:
  - /home/lucas_galdino/chimera/gpu_accelerated/documents_tcc/refs.bib
csl: /home/lucas_galdino/chimera/gpu_accelerated/documents_tcc/associacao-brasileira-de-normas-tecnicas-numerico.csl
link-citations: true
slide-level: 2                       # each "##" heading starts a new frame; "#" becomes a section divider
header-includes:
  # beamer + hyperref workaround: pandoc emits \phantomsection\label{...}
  # after a captioned table, which triggers "Undefined control sequence \theHtable".
  # Providing the missing hyperref counter alias silences it.
  - \let\theHtable\thetable
---

## About this deck

A minimum working beamer template. Key workaround: `--lua-filter=beamer-table-fix.lua`
is required because pandoc 3.x emits `longtable` for any markdown table, and
`longtable` is incompatible with beamer frame pagination (tables silently disappear
otherwise).

## Bullet Slide

- Pandoc maps `##` to individual frames.
- Use `###` for frame subtitles if needed.
- Inline math works here too: $e^{i\pi} + 1 = 0$.

## Math Slide

Display math inside a frame:

$$
\text{Speedup}(n) = \frac{T_\text{CPU}(n)}{T_\text{GPU}(n)}.
$$

Citations also resolve on slides [@tsp_gpu].

## Table Slide

| Variant | Time (s) | Speedup |
|:--------|---------:|--------:|
| CPU     |    120.0 |    1.0x |
| GPU     |     12.5 |    9.6x |

## Notes

- `theme:` and `colortheme:` map directly to `\usetheme{}` / `\usecolortheme{}`.
- `aspectratio: 169` sets widescreen 16:9; omit for the beamer default 4:3.
- Without the Lua filter, the "Table Slide" renders as an empty frame.
- `## References {.allowframebreaks}` **must be the last heading** so citeproc
  places the bibliography inside that frame; otherwise pandoc attaches the
  bib to whatever heading happens to come last.

## Compile

```bash
pandoc minimal-beamer.md \
  -t beamer \
  --pdf-engine=xelatex \
  --citeproc \
  --lua-filter=$HOME/.agents/skills/pandoc-markdown/scripts/beamer-table-fix.lua \
  -o minimal-beamer.pdf
```

## References {.allowframebreaks}

<!-- .allowframebreaks lets the bibliography flow across multiple frames; must be the last section -->
