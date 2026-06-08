---
name: progressive-clues
description: 'Use when the sensei tutor provides hints through the progressive clue system. Routes to 4 escalating levels: explain (default — conceptual hint), pseudocode (algorithmic hint with ??? placeholders), blank-fill (partial solution with strategic gaps), guided-steps (step-by-step walkthrough). Auto-escalates after 2-3 exchanges per level. Loaded when student is stuck or progressive-clues XML tag is set.'
argument-hint: 'Set clue level — explain (conceptual), pseudocode (algorithmic), blank-fill (partial solution), or guided-steps (walkthrough)'
user-invocable: false
---

<router>

  Progressive Clues Router — routes to the correct help level based on the `<progressive-clues>` value.
</router>

<scope>

  This tag controls the help intensity when the student is stuck. It operates as a 4-level escalation ladder. It does not control the teaching method (see [active-mode](../active-mode/SKILL.md)) — rather, it activates when the current method isn't sufficient. After exhausting Level 4, the [escalation-protocol](../escalation-protocol/SKILL.md) takes over.
</scope>

<modes>

  | Mode | File | Default | Level | Summary |
  |---|---|---|---|---|
  | explain | [explain.md](./explain.md) | ★ | 1 | Conceptual hint without revealing implementation. Use askQuestions to check if sufficient. |
  | pseudocode | [pseudocode.md](./pseudocode.md) | | 2 | Algorithmic hint in pseudocode with ??? for key logic. Follows active `<pseudocode-style>`. |
  | blank-fill | [blank-fill.md](./blank-fill.md) | | 3 | Partial solution with strategic blanks. Use askQuestions with blanks as prompts. |
  | guided-steps | [guided-steps.md](./guided-steps.md) | | 4 | Step-by-step walkthrough. Maximum help. Still pseudocode, not real code. |
</modes>

<dispatch>

  1. Read the current `<progressive-clues>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its hint-delivery instructions
  4. When no value is set, use the default (★) explain level (Level 1)
</dispatch>

<auto-escalation>

  - Spend 2-3 exchanges at each level before moving up
  - Never skip levels unless `<urgency-level>` is `high`
  - After Level 4 (guided-steps), if student is still stuck → trigger `<escalation-protocol>`
  - Track which level was needed per concept for memory
</auto-escalation>

<example>

  Student is stuck after 3 exchanges at Level 1 (explain).
  → Auto-escalate to Level 2
  → Read [pseudocode.md](./pseudocode.md)
  → Apply: show algorithmic structure with ??? placeholders, following the active `<pseudocode-style>` format
</example>

<memory-contract>

  Entity prefix: `sensei:clue:`
  Common observations: which clue level was needed for which concept, whether hint was sufficient
  Relation types: `required_help_at` (concept→clue level)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - `<urgency-level>` `high` allows skipping levels to reach guided-steps faster
  - `<pseudocode-style>` determines the format of Level 2 (pseudocode) and Level 4 (guided-steps) hints
  - After Level 4, triggers `<escalation-protocol>` — the two tags form a continuous help pipeline
  - `<active-mode>` socratic uses explain level most often; validation uses blank-fill for gap-checking
</cross-tag-interactions>
