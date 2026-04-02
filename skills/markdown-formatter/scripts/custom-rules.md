---
title: "Custom markdownlint rules"
tags: [markdownlint, custom-rules, linting, javascript]
date_created: 2026-03-23
date_changed: 2026-03-23
---

# Custom markdownlint rules

These are custom markdownlint rules written in javascript. They live at
`~/.markdown_lint/rules/` and extend the built-in rule set for this project's
markdown conventions.

## Installation

Add these rules to VS Code via settings:

```jsonc
"markdownlint.customRules": [
  "~/.markdown_lint/rules/github-admonitions.js",
  "~/.markdown_lint/rules/code-block-source-citation.js",
  "~/.markdown_lint/rules/admonition-separation.js"
]
```

Or pass them via CLI using a `.markdownlint-cli2.jsonc` config:

```jsonc
{
  "config": { "extends": "~/.markdown_lint/.markdownlint.jsonc" },
  "customRules": [
    "~/.markdown_lint/rules/github-admonitions.js",
    "~/.markdown_lint/rules/code-block-source-citation.js",
    "~/.markdown_lint/rules/admonition-separation.js"
  ]
}
```

```bash
markdownlint-cli2 --config .markdownlint-cli2.jsonc file.md
```

## Rules

### `github-admonitions`

**File:** `github-admonitions.js`

**Purpose:** Enforces GitHub-style `> [!TYPE]` admonition syntax. Flags
blockquotes that use emoji-based or bold-text patterns instead of the
standardized format.

**What it catches:**

```markdown
> **Note:** This is wrong.
> :memo: **Note:** Also wrong.
> :warning: **Warning:** Nope.
```

**What it expects:**

```markdown
> [!NOTE]
> This is correct.

> [!WARNING]
> Also correct.
```

**Valid types:** `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`.

**How it works:** Two regex patterns — one detects admonition-like blockquotes
(bold keywords, emoji prefixes), the other validates the GitHub `> [!TYPE]`
format. If the first matches but the second doesn't, it's flagged.

```javascript github-admonitions.js#L10-L11
const admonitionPattern = /^\s*>\s*(?::[\w]+:\s*)?(?:\*{2}|_{2})?\s*(?:Note|Tip|Important|Warning|Caution)\s*:?\s*(?:\*{2}|_{2})?\s/i;
const githubAdmonitionPattern = /^\s*>\s*\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/;
```

---

### `code-block-source-citation`

**File:** `code-block-source-citation.js`

**Purpose:** Validates that when a fenced code block's info string includes a
file path reference, it follows the format `language filepath#L<start>-L<end>`.

**What it catches:**

````markdown
```bash install.sh
#!/bin/bash
echo hello
```
````

````markdown
```python some_file.py:5
def foo():
    pass
```
````

**What it expects:**

````markdown
```bash install.sh#L5-L20
#!/bin/bash
echo hello
```
````

**When it does NOT trigger:** If the info string contains only a language
(e.g., `` ```python ``), no citation is required. The rule only activates when a
second token in the info string looks like a file reference (contains `.` or
`/`).

**How it works:** Matches info strings with 2+ tokens. If the second token
looks like a filepath, validates it against `filename#L<n>` or
`filename#L<n>-L<n>`.

```javascript code-block-source-citation.js#L16-L17
const infoStringPattern = /^(`{3,})\s*(\S+)\s+(\S+)/;
const validCitationPattern = /^[^\s#]+#L\d+(-L\d+)?$/;
```

---

### `admonition-separation`

**File:** `admonition-separation.js`

**Purpose:** Ensures consecutive blockquotes (including admonitions) are
separated by at least one blank line. This complements the built-in MD028 rule
with stricter detection for adjacent admonitions that might visually merge.

**What it catches:**

```markdown
> [!NOTE]
> Some note.
> [!WARNING]
> Some warning.
```

**What it expects:**

```markdown
> [!NOTE]
> Some note.

> [!WARNING]
> Some warning.
```

**How it works:** Tracks blockquote boundaries and admonition starts. Detects
two cases: (1) a new blockquote starting immediately after a previous one ended
with no blank line, and (2) multiple `> [!TYPE]` admonitions within a single
continuous blockquote (no blank line between them).

```javascript admonition-separation.js#L29-L41
const isBlockquoteLine = /^\s*>/.test(line);
const isAdmonitionLine = admonitionStart.test(line);

if (isBlockquoteLine && !inBlockquote) {
  if (blockquoteEndLine === index) {
    // Previous blockquote ended on the immediately preceding line
  }
} else if (isBlockquoteLine && inBlockquote) {
  // Inside a blockquote — check for a second admonition start
  if (isAdmonitionLine && sawAdmonition) {
    // Multiple admonitions merged into one blockquote
  }
}
```
