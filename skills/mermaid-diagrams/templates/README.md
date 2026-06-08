---
title: "Mermaid Template Gallery"
description: "Index of reusable Mermaid templates for common diagram types and readable light or dark palettes."
tags:
  - mermaid
  - templates
  - gallery
  - palettes
---

# Mermaid Template Gallery

Use these templates as starting points. Copy the closest file, then change labels and relationships while keeping the semantic diagram type intact.

## Theme and Palette Templates

| Template | Use when |
| --- | --- |
| [flowchart-github-light.md](flowchart-github-light.md) | Fixed GitHub-like light background |
| [flowchart-github-dark.md](flowchart-github-dark.md) | Fixed GitHub-like dark background |
| [flowchart-dark-slide.md](flowchart-dark-slide.md) | Presentations or dark exported images |
| [flowchart-print-friendly.md](flowchart-print-friendly.md) | Papers, reports, and black-and-white printing |

## Core Diagram Templates

| Template | Use when |
| --- | --- |
| [state-lifecycle.md](state-lifecycle.md) | One entity changes status over time |
| [sequence-service-call.md](sequence-service-call.md) | Multiple actors exchange messages over time |
| [entity-relationship.md](entity-relationship.md) | Tables, keys, and cardinality |
| [class-model.md](class-model.md) | Classes, methods, and inheritance |

## Math Templates

These require Mermaid v10.9.0+ and should be validated in the target renderer.

| Template | Use when |
| --- | --- |
| [flowchart-math-katex.md](flowchart-math-katex.md) | Flowchart nodes, short edge labels, or dedicated formula nodes need Mermaid-native KaTeX math |
| [sequence-math-katex.md](sequence-math-katex.md) | Sequence participants, messages, or notes need short Mermaid-native KaTeX math |

## Layout Templates

Ask before using non-default layouts when more than one layout may fit.

| Template | Use when |
| --- | --- |
| [flowchart-dagre-default.md](flowchart-dagre-default.md) | Stable layered flow with portable spacing controls |
| [flowchart-elk-complex-routing.md](flowchart-elk-complex-routing.md) | Complex directed flowcharts with crossing edges |
| [mindmap-tidy-tree-hierarchy.md](mindmap-tidy-tree-hierarchy.md) | Mindmaps and hierarchical concept trees |

## Notes

- New templates use YAML frontmatter `config:` inside the Mermaid fence.
- Legacy `%%{ init: ... }%%` directives are intentionally not used.
- Templates use semantic arrows: thick flowchart links for primary paths, dotted links for retries/dependencies/feedback, cross links for rejected paths, sequence returns with `-->>`, and UML/ER operators for structural diagrams. See [../docs/arrow-semantics-guide.md](../docs/arrow-semantics-guide.md).
- Palette templates force colors for fixed-background contexts. For normal GitHub Markdown, Mermaid defaults may adapt better to viewer theme.
- Layout templates include renderer caveats. Prefer the default layout unless the user chooses another option or the diagram has a clear routing/placement problem.
- Validate uncommon config keys against [../docs/mermaid-config-variables.md](../docs/mermaid-config-variables.md) before publishing.
- Math templates use Mermaid-native `$$...$$` syntax and are limited to flowcharts and sequence diagrams unless another renderer is tested.
- Use single LaTeX backslashes in actual Mermaid source. Do not wrap sequence messages or notes in quotes unless the target renderer proves it needs that.
- Validate advanced config in the target renderer before publishing.
