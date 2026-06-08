# refactoring-guru/ — local mirror placeholder

<context>

This folder is a placeholder for locally mirrored refactoring.guru content. It is
populated by a separate `quick-research` agent that fetches each pattern page using
`defuddle` and saves it as Markdown.

Until that agent is run, this folder is intentionally empty. The skill workflow
falls back to [../refactoring-guru-links.md](../refactoring-guru-links.md) for
canonical URLs.
</context>

## Expected naming convention

Files written by the quick-research agent should follow:

```text
<pattern-type>-<pattern-name>.md
```

Where `pattern-type` is one of `creational`, `structural`, `behavioral`, and
`pattern-name` is the kebab-case GoF name. Examples:

- `creational-factory-method.md`
- `structural-adapter.md`
- `behavioral-strategy.md`

## When this folder is populated

The `refactor-plan` SKILL.md routing table will direct loads here for deep
per-pattern detail. Until then, the skill relies on:

- [../design-patterns-intro.md](../design-patterns-intro.md) — prose summary of all 22 patterns
- [../design-problem-categories.md](../design-problem-categories.md) — taxonomy
- [../pattern-selection-guide.md](../pattern-selection-guide.md) — routing table
