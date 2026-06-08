---
name: target-audience
description: 'Use when the sensei tutor adapts vocabulary, analogy depth, and scaffolding amount. Routes to: intern (everyday analogies, very small examples), junior (default — coding analogies, concise examples), mid (brief definitions, focus on nuance/trade-offs), senior (assume adjacent knowledge, edge cases and integration).'
argument-hint: 'Set audience level — intern, junior, mid, or senior'
user-invocable: false
---

<router>

  Target Audience Router — routes to the correct vocabulary and scaffolding level based on the `<target-audience>` value.
</router>

<scope>

  This tag controls vocabulary complexity, analogy depth, example size, and assumed prior knowledge. It does not affect the teaching method (see [active-mode](../active-mode/SKILL.md)) or response pacing (see [urgency-level](../urgency-level/SKILL.md)).
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | intern | [intern.md](./intern.md) | | Everyday analogies (cooking, building blocks). Very small examples (3-5 lines). Define all terms. |
  | junior | [junior.md](./junior.md) | ★ | Coding analogies (arrays as shelves, functions as recipes). Concise examples (5-15 lines). Assume basic programming. |
  | mid | [mid.md](./mid.md) | | Brief definitions, focus on nuance and trade-offs. Assume familiarity with common patterns. |
  | senior | [senior.md](./senior.md) | | Assume adjacent knowledge. Focus on edge cases, integration points, performance, specs, and RFCs. |
</modes>

<dispatch>

  1. Read the current `<target-audience>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its behavioral-instructions section
  4. When no value is set, use the default (★) junior mode
</dispatch>

<example>

  User sets `<target-audience>senior</target-audience>`.
  → Match "senior" in modes table
  → Read [senior.md](./senior.md)
  → Apply: assume adjacent knowledge, discuss edge cases and architectural trade-offs, reference specs
</example>

<memory-contract>

  Entity prefix: `sensei:audience:`
  Common observations: detected/set audience level per student, whether level was accurate
  Relation types: `calibrated_at` (student→audience level)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - When `intern`, `<active-mode>` intro uses everyday analogies; `<pseudocode-style>` freeform may be more appropriate
  - When `senior`, `<active-mode>` fast-path is the typical pairing; `<pseudocode-style>` language-adapted is common
  - Audience level affects analogy complexity in all modes, example length, and assumed prior knowledge
  - `<learning-framework>` Freire methods work well at all levels but use different generative themes per audience
</cross-tag-interactions>
