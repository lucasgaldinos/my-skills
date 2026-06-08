---
name: escalation-protocol
description: 'Use when the sensei tutor has exhausted progressive clues and student still needs help. Routes to: suggest-resources (default — recommend docs, tutorials, articles), pair-programming (agent codes alongside student), draft-pr (agent drafts a PR for student to review), human-mentor (recommend seeking human help). Loaded when escalation-protocol XML tag is set or after progressive-clues Level 4.'
argument-hint: 'Set escalation action — suggest-resources, pair-programming, draft-pr, or human-mentor'
user-invocable: false
---

<router>

  Escalation Protocol Router — routes to the correct escalation action based on the `<escalation-protocol>` value.
</router>

<scope>

  This tag controls what happens after the student exhausts all progressive clue levels. It is the final help mechanism. It does not replace progressive clues (see [progressive-clues](../progressive-clues/SKILL.md)) — it activates after them. The escalation should feel supportive, never punitive.
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | suggest-resources | [suggest-resources.md](./suggest-resources.md) | ★ | Recommend external docs, tutorials, articles, videos. Use web search. Curate, don't dump. |
  | pair-programming | [pair-programming.md](./pair-programming.md) | | Agent codes alongside student. Ping-pong pseudocode. Agent writes more than usual. |
  | draft-pr | [draft-pr.md](./draft-pr.md) | | Agent drafts a PR (pseudocode/skeleton) for student to review and learn from. |
  | human-mentor | [human-mentor.md](./human-mentor.md) | | Recommend seeking human help. Provide specific guidance on what to ask and what gap exists. |
</modes>

<dispatch>

  1. Read the current `<escalation-protocol>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its escalation instructions
  4. When no value is set, use the default (★) suggest-resources mode
</dispatch>

<example>

  Student exhausts progressive-clues Level 4 and is still stuck.
  → Escalation triggered, default to suggest-resources
  → Read [suggest-resources.md](./suggest-resources.md)
  → Apply: search web for current resources on the topic, curate 2-3 relevant links with explanation of why each helps
</example>

<memory-contract>

  Entity prefix: `sensei:escalation:`
  Common observations: which escalation was triggered, for what concept, whether it resolved the block
  Relation types: `escalated_to` (concept→escalation action)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - Activated after `<progressive-clues>` Level 4 is exhausted — the two tags form a pipeline
  - pair-programming and draft-pr still follow `<pseudocode-style>` rules (no real code)
  - suggest-resources uses web search — same workflow as `<active-mode>` research mode
  - human-mentor should reference the specific concept and gap identified during the session
</cross-tag-interactions>
