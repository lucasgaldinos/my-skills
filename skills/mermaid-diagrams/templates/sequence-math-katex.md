---
title: "Sequence Math KaTeX Template"
description: "Template for Mermaid-native KaTeX math in sequence participant aliases, messages, and notes."
tags:
  - mermaid
  - template
  - sequence-diagram
  - math/katex
---

# Sequence Math KaTeX Template

Use when a sequence diagram needs short Mermaid-native math expressions in participant aliases, messages, or notes.

Requirements:

- Mermaid v10.9.0 or newer.
- Target renderer tested for Mermaid math support.
- Single LaTeX backslashes in actual Mermaid source, for example `\sqrt` and `\alpha`.
- Unquoted messages and notes; local `mmdc` renders wrapping quotes visibly.
- Notes with math checked for excessive padding.

Do not use this for GitHub Markdown when exact math rendering is required; Mermaid issue `#5482` reports GitHub KaTeX rendering problems.

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f6f8fa"
    primaryTextColor: "#24292f"
    primaryBorderColor: "#d0d7de"
    lineColor: "#57606a"
    noteBkgColor: "#fff8c5"
    noteTextColor: "#24292f"
    noteBorderColor: "#9a6700"
  sequence:
    diagramMarginX: 40
    diagramMarginY: 18
    actorMargin: 90
    messageMargin: 52
    noteMargin: 14
    messageAlign: center
---
sequenceDiagram
    autonumber
    participant A as $$\alpha$$
    participant B as $$\beta$$

    A->>B: Solve $$\ \sqrt{2+2}$$
    B-->>A: Result $$\ 2$$
    Note right of B: $$\sqrt{2+2}=\sqrt{4}=2$$
```

>[!TIP] on `$$\ \sqrt{2+2}$$`
>the `\ ...` is necessary for spacing, otherwise it would be rendered altogether.
