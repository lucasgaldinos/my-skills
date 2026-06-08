---
title: "Flowchart Math KaTeX Template"
description: "Template for Mermaid-native KaTeX math inside flowchart node labels and edge labels."
tags:
  - mermaid
  - template
  - flowchart
  - math/katex
---

# Flowchart Math KaTeX Template

Use when a flowchart needs Mermaid-native math expressions in nodes or edge labels.

Requirements:

- Mermaid v10.9.0 or newer.
- Target renderer tested for Mermaid math support.
- One short `$$...$$` expression per edge label when possible.
- Dedicated formula nodes for long expressions that would crowd an edge.

Do not use this for GitHub Markdown when exact math rendering is required; Mermaid issue `#5482` reports GitHub KaTeX rendering problems.

## Short Edge-Label Pattern

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f6f8fa"
    primaryTextColor: "#24292f"
    primaryBorderColor: "#57606a"
    lineColor: "#57606a"
    edgeLabelBackground: "#ffffff"
  flowchart:
    nodeSpacing: 70
    rankSpacing: 80
    diagramPadding: 16
    curve: "linear"
---
flowchart LR
  Input["$$x$$"] ==> Model["$$f_\theta(x)$$"]
    Model -->|"$$\hat{y}=f_\theta(x)$$"| Loss["$$L(\theta)$$"]
  Loss -. gradient .-> Grad["$$\nabla_\theta L$$"]
  Grad -. update .-> Model
```

## Formula-Node Pattern

Use this when an edge label becomes too long. Mermaid does not provide a portable below-edge label option, so a dedicated node is usually clearer.

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f6f8fa"
    primaryTextColor: "#24292f"
    primaryBorderColor: "#57606a"
    lineColor: "#57606a"
    edgeLabelBackground: "#ffffff"
  flowchart:
    nodeSpacing: 85
    rankSpacing: 90
    diagramPadding: 24
    curve: "linear"
---
flowchart LR
  Input["$$x$$"] ==> Model["$$f_\theta$$"]
  Model ==> Prediction["$$\hat{y}=f_\theta(x)$$"]
  Prediction --> LossFormula["$$L(\theta)=\frac{1}{n}\sum_i(y_i-\hat{y}_i)^2$$"]
  LossFormula ==> Loss["$$L$$"]
  LossFormula -. update .-> Model

    classDef formula fill:#fff8c5,stroke:#9a6700,color:#24292f;
    class Prediction,LossFormula formula;
```
