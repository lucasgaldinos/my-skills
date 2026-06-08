---
name: learning-framework
description: 'Use when the sensei tutor selects or applies a pedagogical framework. Routes to 10 frameworks: 5w2h (default — structured analysis), pear-loop (Plan-Explore-Analyze-Rewrite), five-whys, rubber-duck, red-green-refactor, and 5 Paulo Freire methods (dialogical, praxis, problem-posing, generative, critical). Loaded when learning-framework XML tag is active.'
argument-hint: 'Set learning framework — 5w2h, pear-loop, five-whys, rubber-duck, red-green-refactor, or a Freire method (dialogical, praxis, problem-posing, generative, critical)'
user-invocable: false
---

<router>

  Learning Framework Router — routes to the correct pedagogical framework based on the `<learning-framework>` value.
</router>

<scope>

  This tag controls the pedagogical structure applied to the learning interaction. It does not affect the teaching method itself (see [active-mode](../active-mode/SKILL.md)) — rather, it provides the analytical lens through which concepts are explored. A framework can be combined with any active-mode.
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | 5w2h | [5w2h.md](./5w2h.md) | ★ | Structured analysis: What, Why, When, Where, Who, How, How much — applied to code comprehension. |
  | pear-loop | [pear-loop.md](./pear-loop.md) | | Plan → Explore → Analyze → Rewrite cycle. Track which phase the student is in. |
  | five-whys | [five-whys.md](./five-whys.md) | | Root cause analysis via repeated "why" questions. Stop when actionable root cause reached. |
  | rubber-duck | [rubber-duck.md](./rubber-duck.md) | | Student explains code line-by-line to the agent. Agent stays mostly silent, only probing contradictions. |
  | red-green-refactor | [red-green-refactor.md](./red-green-refactor.md) | | TDD cycle applied to learning: predict (red) → confirm (green) → improve mental model (refactor). |
  | freire-dialogical | [freire-dialogical.md](./freire-dialogical.md) | | Bidirectional knowledge building through dialogue. Teacher and student co-create understanding. |
  | freire-praxis | [freire-praxis.md](./freire-praxis.md) | | Reflect → Act → Reflect cycle. Think through approach → code it → review what was learned. |
  | freire-problem-posing | [freire-problem-posing.md](./freire-problem-posing.md) | | Present problems from student's real context. Opposed to "banking model" of abstract knowledge dump. |
  | freire-generative | [freire-generative.md](./freire-generative.md) | | Identify themes from student's real experience to generate learning springboards. |
  | freire-critical | [freire-critical.md](./freire-critical.md) | | Develop awareness of structural factors: tech debt, framework lock-in, architectural power dynamics. |
</modes>

<dispatch>

  1. Read the current `<learning-framework>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its pedagogical structure
  4. When no value is set, use the default (★) 5w2h framework
</dispatch>

<example>

  User sets `<learning-framework>freire-problem-posing</learning-framework>`.
  → Match "freire-problem-posing" in modes table
  → Read [freire-problem-posing.md](./freire-problem-posing.md)
  → Apply: ground all examples in the student's actual codebase and project context, never use abstract toy problems
</example>

<memory-contract>

  Entity prefix: `sensei:framework:`
  Common observations: which framework was effective for which concept, student engagement level
  Relation types: `applied_framework` (concept→framework)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - Frameworks apply on top of the `<active-mode>` — socratic + 5w2h = questioning through the 7 W/H lenses
  - When `<urgency-level>` is `high`, simplify framework application (e.g., 5w2h → focus on What + How only)
  - When `<urgency-level>` is `low`, allow full framework cycle with all phases
  - Freire methods work especially well with `<active-mode>` validation (student reflects on their own context)
  - `<target-audience>` affects framework vocabulary: intern gets everyday examples, senior gets architectural analysis
</cross-tag-interactions>
