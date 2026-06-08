---
title: "Mermaid Arrow Semantics Guide"
description: "Practical rules for choosing Mermaid arrows and relationship operators by diagram type."
tags:
  - mermaid
  - arrows
  - relationships
  - semantics
---

# Mermaid Arrow Semantics Guide

Use arrow and relationship operators to carry meaning after choosing the correct diagram type. Do not use one arrow shape for every relationship.

## Flowchart Arrows

- `-->`: normal directed control/data flow.
- `-- text -->` or `-->|text|`: directed flow with a short edge label.
- `-.->` or `-. text .->`: optional path, retry, dependency, feedback, or non-primary influence.
- `==>` or `== text ==>`: main path, critical path, or emphasized happy path.
- `---`: undirected association in relationship maps where order does not matter.
- `<-->`: bidirectional exchange or mutual relationship.
- `--x`: rejected, cancelled, failed, or blocked path when the target node carries the label.
- `--o`: open/optional endpoint only when the target renderer is tested and the meaning is explicit.

Avoid accidental circle or cross edges: Mermaid treats `A---oB` and `A---xB` specially. Add a space or capitalize node IDs that start with `o` or `x` after a link.

## Sequence Arrows

- `->>`: request, call, command, or active message.
- `-->>`: return value, response, result, or acknowledgement.
- `-)`: asynchronous notification or fire-and-forget message.
- `--x` / `-x`: failure, destruction, or terminated participant message.

Do not use request arrows for returns. That makes temporal logic look like wishful thinking wearing a tie.

## State Transitions

State diagrams normally use `-->` for transitions. Put the meaning in the transition label, not in decorative arrow variants.

Use `[*] --> State` for initial states and `State --> [*]` for terminal states.

## Class Relationships

- `<|--`: inheritance / generalization.
- `*--`: composition / strong ownership.
- `o--`: aggregation / weak whole-part relationship.
- `-->`: navigable association.
- `..>`: dependency / uses / returns / creates.
- `..|>`: realization / interface implementation.
- `--` / `..`: generic solid/dashed links only when a more specific UML relationship does not fit.

## Entity Relationships

Use ER cardinality markers instead of flowchart arrows.

- `||`: exactly one.
- `|o` / `o|`: zero or one.
- `}|` / `|{`: one or more.
- `}o` / `o{`: zero or more.
- `--`: identifying relationship.
- `..`: non-identifying relationship.

If the child cannot exist independently of the parent, prefer solid identifying relationships. If both entities have independent identity, use dashed non-identifying relationships.
