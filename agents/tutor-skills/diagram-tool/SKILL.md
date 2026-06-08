---
name: diagram-tool
description: 'Use when the sensei tutor creates visual explanations using diagrams. Routes to: mermaid (default — use renderMermaidDiagram tool), excalidraw (generate .excalidraw JSON), drawio (generate .drawio XML), plantuml (generate .puml text), all (agent selects best tool per diagram type). Loaded when diagram-tool XML tag is active or when visual explanation is needed.'
argument-hint: 'Set diagram tool — mermaid, excalidraw, drawio, plantuml, or all (auto-select)'
user-invocable: false
---

<router>

  Diagram Tool Router — routes to the correct diagramming tool based on the `<diagram-tool>` value.
</router>

<scope>

  This tag controls which diagramming tool produces visual explanations. It does not affect when diagrams are created (that depends on context and the teaching method). For diagram syntax and capabilities, each mode file delegates to an existing diagram skill and adds a pedagogical wrapper.
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | mermaid | [mermaid.md](./mermaid.md) | ★ | Use renderMermaidDiagram MCP tool. Delegates to mermaid-diagrams skill. Fast inline rendering. |
  | excalidraw | [excalidraw.md](./excalidraw.md) | | Generate .excalidraw JSON files. Delegates to excalidraw-diagram-generator skill. Hand-drawn aesthetic. |
  | drawio | [drawio.md](./drawio.md) | | Generate .drawio mxGraph XML. Delegates to draw-io-diagram-generator skill. Formal/structured diagrams. |
  | plantuml | [plantuml.md](./plantuml.md) | | Generate .puml text files. Self-contained (no existing skill). Text-based diagram definition. |
  | all | [all.md](./all.md) | | Agent auto-selects the best tool per diagram type. Selection heuristic in mode file. |
</modes>

<dispatch>

  1. Read the current `<diagram-tool>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its tool instructions and delegation pattern
  4. When no value is set, use the default (★) mermaid mode
</dispatch>

<example>

  User sets `<diagram-tool>excalidraw</diagram-tool>`.
  → Match "excalidraw" in modes table
  → Read [excalidraw.md](./excalidraw.md)
  → Apply: delegate to excalidraw-diagram-generator skill, add pedagogical annotations (labels explaining WHY, not just WHAT)
</example>

<memory-contract>

  Entity prefix: `sensei:tool:`
  Common observations: which tool was used, diagram type generated, whether visual helped understanding
  Relation types: `used_tool` (concept→diagram tool)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - Diagrams are used across all `<active-mode>` values — intro uses them for anchoring, socratic for probing, research for presenting findings
  - When `<urgency-level>` is `high`, prefer mermaid (fastest rendering) unless another tool is explicitly set
  - When `<target-audience>` is `intern`, add more labels and annotations to diagrams
  - Diagram complexity scales with audience level: intern (simple flow), senior (full architecture)
</cross-tag-interactions>
