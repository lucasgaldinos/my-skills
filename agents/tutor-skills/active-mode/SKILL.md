---
name: active-mode
description: 'Use when the sensei tutor selects a teaching method. Routes to: socratic (default — guided questioning via askQuestions), intro (concept introduction with analogies and scaffolding), validation (user explains understanding, agent probes for gaps), fast-path (skip scaffolding for demonstrated mastery), research (agent researches topic before teaching). Loaded when active-mode XML tag is active or teaching method needs selection.'
argument-hint: 'Describe the teaching method you want — guided questioning, concept intro, understanding validation, fast-track for experts, or research mode'
user-invocable: false
---

<router>

  Active Mode Router — routes to the correct teaching method based on the `<active-mode>` value.
</router>

<scope>

  This tag controls the teaching method used during the interaction. It does not affect response depth (see [urgency-level](../urgency-level/SKILL.md)), vocabulary level (see [target-audience](../target-audience/SKILL.md)), or pseudocode format (see [pseudocode-style](../pseudocode-style/SKILL.md)).
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | socratic | [socratic.md](./socratic.md) | ★ | Guided questioning using askQuestions tool. One question at a time, WHY over WHAT, build concrete→abstract. |
  | intro | [intro.md](./intro.md) | | Concept introduction with analogies and scaffolding. Start from anchor point, bridge via analogy, define, expand. |
  | validation | [validation.md](./validation.md) | | User explains their understanding first, agent probes for gaps and misconceptions without correcting directly. |
  | fast-path | [fast-path.md](./fast-path.md) | | Skip scaffolding for demonstrated mastery. Go directly to nuance, trade-offs, edge cases. Downshifts when needed. |
  | research | [research.md](./research.md) | | Agent researches topic before responding. Search codebase → web → docs → cross-reference → synthesize pedagogically. |
</modes>

<dispatch>

  1. Read the current `<active-mode>` value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its behavioral-instructions section
  4. When no value is set, use the default (★) socratic mode
</dispatch>

<example>

  User sets `<active-mode>validation</active-mode>`.
  → Match "validation" in modes table
  → Read [validation.md](./validation.md)
  → Apply its behavioral instructions: ask user to explain their understanding, probe for gaps, don't correct directly
</example>

<memory-contract>

  Entity prefix: `sensei:mode:`
  Common observations: which mode was used per session/concept, engagement quality, whether mode was effective
  Relation types: `taught_with` (concept→mode), `switched_from` (mode→mode when mid-session switch)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - When `<urgency-level>` is `high`, socratic probing depth is reduced — fewer exchanges before escalating clue levels
  - When `<target-audience>` is `intern`, intro mode uses everyday analogies; when `senior`, fast-path is the typical pairing
  - When active-mode is `research`, the agent uses web search and codebase tools before applying any other tag's behavior
  - `<progressive-clues>` integrate with socratic (clues offered when student is stuck) and validation (clues offered when gaps found)
</cross-tag-interactions>
