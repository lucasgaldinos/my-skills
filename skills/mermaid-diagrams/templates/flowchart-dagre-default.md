---
title: "Flowchart Dagre Default Template"
description: "Stable default flowchart layout using portable spacing and curve controls."
tags:
  - mermaid
  - template
  - flowchart
  - layout/dagre
---

# Flowchart Dagre Default Template

Use this when the diagram is a normal layered process, pipeline, or decision flow. This is the safest default for portable Markdown.

Do not use this when the graph is a dense undirected relationship map or when edge crossings make the default layout unreadable.

```mermaid
---
config:
  layout: dagre
  flowchart:
    nodeSpacing: 60
    rankSpacing: 70
    diagramPadding: 16
    wrappingWidth: 180
    curve: "linear"
---
flowchart TD
  Collect[Collect input] ==> Clean[Clean data]
  Clean ==> Decide{Ready?}
  Decide == Yes ==> Run[Run analysis]
  Decide -. No .-> Repair[Repair input]
  Repair -. retry .-> Clean
  Run ==> Report[Write report]
```

Variables shown here are flowchart controls, not a separate dagre-specific object. Use them to tune fit before changing layout engines.
