---
name: urgency-level
description: 'Use when the sensei tutor adapts depth and pace based on urgency. Routes to: low (full exploration, no time pressure), medium (default — balanced key concepts), high (focused, concise, prioritize unblocking). Affects all other modes by constraining response depth.'
argument-hint: 'Set urgency — low (explore freely), medium (balanced), or high (unblock fast)'
user-invocable: false
---

<router>

  Urgency Level Router — routes to the correct pacing mode based on the `<urgency-level>` value.
</router>

<scope>

  This tag controls response depth and pacing. It does not affect the teaching method (see [active-mode](../active-mode/SKILL.md)) or vocabulary level (see [target-audience](../target-audience/SKILL.md)). It acts as a global modifier — all other tags respect the urgency constraint.
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | low | [low.md](./low.md) | | Full exploration, no time pressure. Deep probing, tangents allowed if educational. |
  | medium | [medium.md](./medium.md) | ★ | Balanced — probe key gaps, skip obvious understanding. Standard clue escalation timing. |
  | high | [high.md](./high.md) | | Focused, concise, prioritize unblocking. Skip clue levels if needed. Direct corrections allowed. |
</modes>

<dispatch>

  1. Read the current <urgency-level> value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its behavioral-instructions section
  4. When no value is set, use the default (★) medium mode
</dispatch>

<example>

  User sets
  `<urgency-level>high</urgency-level>`.
  → Match "high" in modes table
  → Read [high.md](./high.md)
  → Apply: minimize examples, skip clue levels, accept partial understanding, still no full code
</example>

<memory-contract>

  Entity prefix: `sensei:urgency:`
  Common observations: urgency level per session, whether it changed mid-session
  Relation types: `under_urgency` (session→urgency level)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - When `high`, `<active-mode>` socratic reduces probing depth (fewer exchanges)
  - When `high`, `<progressive-clues>` can skip levels to reach guided-steps faster
  - When `low`, `<active-mode>` socratic allows tangents and extended exploration
  - When `low`, `<learning-framework>` can apply full framework cycle without time pressure
</cross-tag-interactions>
