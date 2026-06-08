---
name: pseudocode-style
description: 'Use when the sensei tutor produces or evaluates pseudocode. Routes to: strict-pdl (default — Cal Poly PDL standard, ALL CAPS keywords, indentation-based nesting), language-adapted (allow language idioms but keep structure), freeform (natural language with logic markers). Loaded when pseudocode-style XML tag is active or when pseudocode is being generated.'
argument-hint: 'Set pseudocode format — strict-pdl (Cal Poly standard), language-adapted, or freeform'
user-invocable: false
---

<router>

  Pseudocode Style Router — routes to the correct pseudocode format based on the `<pseudocode-style>` value.
</router>

<scope>

  This tag controls how pseudocode is written and formatted. It does not affect when pseudocode is produced (that depends on `<active-mode>` and `<progressive-clues>`) or the teaching method itself.
</scope>

<modes>

  | Mode | File | Default | Summary |
  |---|---|---|---|
  | strict-pdl | [strict-pdl.md](./strict-pdl.md) | ★ | Cal Poly PDL standard — ALL CAPS keywords (IF, THEN, ELSE, WHILE), indentation-based nesting, no language syntax. |
  | language-adapted | [language-adapted.md](./language-adapted.md) | | Language idioms allowed (list comprehensions, arrow functions) but keep structural rules. Useful for language-specific learning. |
  | freeform | [freeform.md](./freeform.md) | | Natural language with logic markers (→, ⇒, ∴). Most accessible for non-programmers. Minimal structure. |
</modes>

<dispatch>

  1. Read the current <pseudocode-style> value from the conversation
  2. Find the matching row in the modes table
  3. Read the linked mode file — follow its formatting rules for all pseudocode output
  4. When no value is set, use the default (★) strict-pdl mode
</dispatch>

<example>

  User sets `<pseudocode-style>language-adapted</pseudocode-style>`.
  → Match "language-adapted" in modes table
  → Read [language-adapted.md](./language-adapted.md)
  → Apply: allow Python list comprehensions in pseudocode but keep indentation structure and descriptive variable names
</example>

<memory-contract>

  Entity prefix: `sensei:pseudocode:`
  Common observations: which style student preferred, why a style was chosen
  Relation types: `preferred_style` (student→pseudocode style)

  Each mode file defines its own specific entity/relation patterns. Read the mode file for details.
</memory-contract>

<cross-tag-interactions>

  - When `<target-audience>` is `intern`, freeform may be more appropriate than strict-pdl
  - When `<target-audience>` is `senior`, language-adapted is common (they know the language)
  - `<progressive-clues>` pseudocode level (Level 2) uses whichever style is active in this tag
  - All pseudocode output across ALL modes must follow the active style — this tag is a global format rule
</cross-tag-interactions>
