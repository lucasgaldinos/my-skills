---
title: "Diagram Type Routing Guide"
description: "Full decision framework for selecting the right Mermaid diagram type. Use when the correct type is ambiguous, types appear interchangeable, or the user has not specified one."
tags:
  - mermaid
  - diagram-selection
  - routing
---

# Diagram Type Routing Guide

Use this guide when the correct diagram type is ambiguous, two types seem interchangeable, or the user has not specified one. For quick routing, see the intent table in `SKILL.md` first.

## Decision Framework

Answer these questions in order. Stop at the first match.

### 0. Is the target renderer constrained?

- **Portable Markdown / GitHub / unknown renderer** → avoid beta-only or renderer-sensitive choices unless the semantic match is strong and you include a rendering note.
- **Mermaid Live / latest Mermaid / controlled static build** → beta diagrams and advanced layouts are acceptable after validation.
- **VS Code or Obsidian** → confirm the Mermaid extension/plugin version before relying on advanced layout config.

### 1. Are multiple actors/entities communicating?

- **Yes, ≥2 actors exchanging messages over time** → `sequenceDiagram`
- **No, one entity changing condition over time** → `stateDiagram-v2`
- **No, one actor executing a process with decisions** → `flowchart`

### 2. Is this static structure or dynamic behavior?

- **Static** (blueprints, schemas, topology at rest):
  + OOP classes + methods → `classDiagram`
  + Database tables + keys → `erDiagram`
  + System architecture (formal, multi-level) → `C4Context` / `C4Container` / `C4Component`
  + Cloud infra / network zones → `architecture-beta`
  + Module wiring / component blocks → `block-beta`
  + Protocol packet structure → `packet-beta`
  + Requirements traceability → `requirementDiagram`
- **Dynamic** (what happens, in what order) → continue to next question

### 3. Is measured data the primary content?

- **Part-to-whole proportions** → `pie`
- **Time-series or categorical bar/line data** → `xychart-beta`
- **Flow volume between nodes** → `sankey-beta`
- **Hierarchical data sized by volume** → `treemap`
- **Multi-axis strength/weakness comparison** → `radar`

### 4. Is absolute time or duration the primary concern?

- **Project schedule with durations** → `gantt`
- **Qualitative user sentiment over phases** → `journey`
- **Chronological historical milestones** → `timeline`
- **Parallel version histories / branches** → `gitGraph`

### 5. Is the output a decision/evaluation or conceptual grouping?

- **2-axis strategic evaluation** (e.g., effort vs impact, BCG matrix) → `quadrantChart`
- **Multi-axis strength/weakness comparison** → `radar`
- **Concept clusters / brainstorming / hierarchy** → `mindmap`
- **Task board** → `kanban`

### 6. Is this mainly a layout or styling request?

- **Nodes are cramped** → keep the current semantic type and use spacing config where documented.
- **Edges cross heavily in a flowchart** → keep `flowchart`; consider `layout: elk` if the renderer supports it.
- **Graph is a dense relationship map** → prefer a semantic diagram type (`mindmap`, `classDiagram`, `erDiagram`) or keep `flowchart` with default layout and spacing.
- **Hierarchy or mindmap needs cleaner placement** → consider `layout: tidy-tree`, mainly for mindmaps.

See [layout-configuration-guide.md](layout-configuration-guide.md) for practical config recipes.

### Fallback

If no question produces a clear match and the user has not specified a type: **ask one clarifying question** before generating. Example: *"Should each box represent a status/condition, an action, or a system component?"* Use `flowchart` only as a last resort — it loses semantic precision compared to purpose-built types.

When available, use a structured question tool such as `vscode_askQuestions` for choices that change the output direction. If no such tool is available, ask directly in chat.

Good fallback question set:

- Should nodes represent actions, states, actors, data entities, deployed systems, concepts, or measurements?
- Must this render on GitHub or another constrained Markdown renderer?
- Is the problem semantic choice or only layout/readability?

---

## What Each Type Shows That Others Cannot

This is the clearest way to resolve interchangeability conflicts: identify the **unique metadata** each type captures.

| Type | Unique capability — what it shows that no other type can |
| --- | --- |
| `flowchart` | Decision branching (if/then/else) and step-by-step algorithm execution verbs |
| `sequenceDiagram` | Multi-actor temporal communication with sync vs. async message distinction and activation bars |
| `stateDiagram-v2` | Exact event triggers for transitions; concurrent states via fork/join; composite states |
| `classDiagram` | Method visibility (public/private/protected), inheritance hierarchy, OOP polymorphism |
| `erDiagram` | Mathematical cardinality (1:1, 1:N, N:M) and PK/FK constraint notation |
| `C4Context` / `C4Container` | Multi-level abstraction zoom: context → container → component → code |
| `architecture-beta` | Cloud service icons (AWS/Azure/GCP), network boundary zones, infrastructure topology |
| `gantt` | Absolute calendar duration, parallel task tracks, task dependency critical path |
| `journey` | Qualitative Y-axis (frustration/satisfaction score), emotional sentiment across phases |
| `gitGraph` | Parallel timeline divergence and convergence — branches that split and merge |
| `mindmap` | Radial, non-linear conceptual clustering with no execution dependency implied |
| `quadrantChart` | Continuous 2-axis spatial evaluation with strategic quadrant labels and named data points |
| `requirementDiagram` | Traceability chain: requirement → system element → verification test |
| `sankey-beta` | Proportional flow volume between nodes — the width of edges encodes quantity |
| `radar` | Simultaneous multi-axis strength/weakness comparison on a single chart |
| `treemap` | Hierarchical containment where area encodes volume/size |
| `timeline` | Strictly linear, single-thread chronological narrative (unlike gitGraph, no branches) |
| `zenuml` | Sequence diagrams written in a programming-language-like syntax (code-first teams) |

---

## Common Interchangeability Traps

### Flowchart vs. State Diagram

They both use boxes and arrows — but they model opposite things.

- **Use `flowchart`** when boxes represent *actions*: "Process payment", "Validate input", "Send email"
- **Use `stateDiagram-v2`** when boxes represent *conditions*: "Active", "Pending", "Rejected", "Fulfilled"

State diagrams focus on the entity's **resting phase** and the **event that changes it**. Flowcharts focus on **what happens** during execution. Forcing a flowchart to show states clutters it with transient action blocks; forcing a state diagram to show actions loses the "what triggers the change" semantic.

### Flowchart vs. Sequence Diagram

Both show A→B→C chains — the difference is the number of actors.

- **Use `flowchart`** for single-actor logic or simple pipelines
- **Use `sequenceDiagram`** when ≥2 participants exchange messages

A flowchart with 4+ systems communicating becomes unreadable spaghetti without vertical lifelines. The lifeline is the core value of `sequenceDiagram` — it makes parallel async/sync communication readable.

### Class Diagram vs. ER Diagram

They look structurally similar but capture fundamentally different information.

- **Use `classDiagram`** for OOP code design — supports methods, visibility markers (`+`/`-`/`#`), and inheritance (`<|--`)
- **Use `erDiagram`** for database schema — supports cardinality (`||--o{`), and FK/PK notation

Using ER for classes strips behavioral methods. Using Class for databases adds meaningless methods and obscures cardinality. If the consumer is a database engineer, use ER. If it's a software engineer reading code, use Class.

### C4 vs. Architecture vs. Flowchart (system design)

All three can show "boxes with arrows" for systems — but at very different abstraction levels and formality.

- **Use `C4Context` / `C4Container` / `C4Component`** for formal documentation at multiple abstraction levels. C4 has explicit semantics for Person, System, Container, Component, and boundary types. Use when audience is architects or stakeholders reviewing system boundaries.
- **Use `architecture-beta`** for cloud infrastructure layout with provider-specific service icons (AWS Lambda, S3, Azure functions, etc.) and explicit network zone boundaries.
- **Use `flowchart`** for informal, ad-hoc component wiring, simple service dependency maps, or when C4/architecture formality is overkill.

A flowchart can substitute for both, but loses the semantic types (Person vs. System) and provider-specific visual context.

### Module Map vs. Formal Architecture vs. Deployment Topology

- **Use `flowchart`** for quick dependency maps, pipelines, or informal module wiring when portability matters.
- **Use `block-beta`** for component/module blocks when the renderer supports beta diagrams.
- **Use C4** when the audience needs explicit people, systems, containers, components, and boundaries.
- **Use `architecture-beta`** when cloud/provider services, network zones, or deployment topology are the main subject.

If a formal architecture diagram must render on GitHub, prefer C4 only if the renderer supports it; otherwise use a portable flowchart and state the semantic compromise.

### Semantic Diagram Type vs. Layout Config

Layout problems should not change diagram semantics.

- **Use config** when nodes are too close, edges cross, or clusters are hard to read.
- **Change diagram type** only when the boxes mean a different kind of thing: action, state, actor, class, table, system, or measurement.
- **Ask first** when the user requests a layout engine whose target renderer is unknown.

### Gantt vs. User Journey

Both have a timeline X-axis — but the Y-axis measures completely different things.

- **Use `gantt`** when the Y-axis represents **tasks** with durations, dependencies, and parallel tracks
- **Use `journey`** when the Y-axis represents **qualitative sentiment** (score 1–5 of satisfaction/frustration)

You cannot interchange the Y-axis metric. A Gantt cannot encode "the user was frustrated at step 3." A Journey cannot encode "this task took 3 weeks and blocked two other tasks."

### Sequence Diagram vs. State Diagram

Both can show an object changing over time — but the scope differs.

- **Use `sequenceDiagram`** for **multi-object interactions**: "User sends → API processes → DB stores"
- **Use `stateDiagram-v2`** for **one object's lifecycle**: "Order: Draft → Submitted → Approved → Fulfilled"

State diagrams are **unary** (one entity). Sequence diagrams are **plural** (multiple actors). Trying to show multi-actor communication in a state diagram produces a confusing mess of parallel state tracks.

### Mindmap vs. Flowchart vs. Architecture

All three can show hierarchical relationships — but the semantics differ.

- **Use `mindmap`** for loose, non-linear conceptual clustering where no execution order is implied
- **Use `flowchart`** when the hierarchy implies a sequential execution order or dependency
- **Use `architecture-beta`** / `C4` when the hierarchy represents deployed systems with network boundaries

A mindmap says "these concepts are related to the center." A flowchart says "this step must happen before that step." Confusing them implies ordering where none exists (mindmap) or removes ordering where it matters (flowchart as mindmap).

---

## Diagram Family Map

```text
Behavioral (dynamic)
├── flowchart         → process logic, decisions, steps
├── sequenceDiagram   → multi-actor time-ordered messaging
├── stateDiagram-v2   → lifecycle of one entity
├── journey           → user sentiment across phases
└── zenuml            → sequence (code-style syntax)

Structural (static)
├── classDiagram      → OOP blueprints
├── erDiagram         → relational database schema
├── C4Context/Container/Component  → formal system architecture (multi-level)
├── architecture-beta → cloud infra topology
├── block-beta        → component/module wiring
├── packet-beta       → network protocol structure
└── requirementDiagram → compliance traceability

Temporal
├── gantt             → calendar schedule, task duration
├── timeline          → linear chronology
└── gitGraph          → branch/merge version history

Analytical / Conceptual
├── mindmap           → concept clusters
├── quadrantChart     → 2-axis evaluation
└── kanban            → task board

Quantitative
├── pie               → part-to-whole
├── xychart-beta      → line/bar series
├── sankey-beta       → flow volume
├── radar             → multi-axis comparison
└── treemap           → hierarchical volume
```
