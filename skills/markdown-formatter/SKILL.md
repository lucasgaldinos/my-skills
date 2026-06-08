---
name: markdown-formatter
description: "Use this skill before generating any new markdown file, or when explicitly invoked via /markdown-formatter for existing markdown. Enforces formatting rules, markdownlint compliance, GitHub-style admonitions, reference labels, footnotes, and code block source citations."
argument-hint: '"format markdown", "write a README", "create documentation", "fix markdown formatting", "generate .md file", or any task producing markdown output."'
metadata:
  References:
    - references/math-katex-reference.md
    - references/latex-environments.md
    - references/style-guide-summary.md
    - references/extended-syntax-and-hacks.md
    - scripts/README.md
    - https://github.com/KaTeX/KaTeX/blob/main/docs/supported.md#style-color-size-and-font
    - https://github.com/KaTeX/KaTeX/blob/main/docs/support_table.md
    - references/yaml-cheat-sheet.md
---

# Markdown Formatter

<context>

Produce markdown that is readable in source, portable across renderers, diff-friendly, and fully compliant with the project's markdownlint configuration.

- [1. Markdown Formatter](#1-markdown-formatter)
  + [1.1. When this skill activates](#11-when-this-skill-activates)
  + [1.2. Core rules](#12-core-rules)
    - [1.2.1. YAML front matter (preamble)](#121-yaml-front-matter-preamble)
    - [1.2.2. Structure and whitespace](#122-structure-and-whitespace)
    - [1.2.3. Lists](#123-lists)
    - [1.2.4. Code blocks](#124-code-blocks)
    - [1.2.5. Admonitions — GitHub style ONLY](#125-admonitions-github-style-only)
    - [1.2.6. Emphasis and bold — not for section structure](#126-emphasis-and-bold-not-for-section-structure)
    - [1.2.7. Links — reference labels for repeated URLs](#127-links-reference-labels-for-repeated-urls)
    - [1.2.8. Footnotes](#128-footnotes)
    - [1.2.9. Tables](#129-tables)
    - [1.2.10. Blockquotes](#1210-blockquotes)
    - [1.2.11. HTML in markdown](#1211-html-in-markdown)
  + [1.3. Markdownlint configuration](#13-markdownlint-configuration)
  + [1.4. Quick checklist](#14-quick-checklist)
  + [1.5. References](#15-references)

## 1.1. When this skill activates

- **New markdown files:** automatically, before any generation begins.
- **Existing markdown:** only when explicitly invoked (`/markdown-formatter`).
  </context>

<rules>

## Core rules

Every markdown file MUST follow these rules. Violations are formatting errors.

### 0. YAML front matter (preamble)

Every markdown file MUST begin with a YAML front matter block containing at minimum:

```yaml
---
title: "Document title matching the top-level header"
tags: [relevant, topic, tags]
description: "Brief summary of the document's purpose and content"
date_created: YYYY-MM-DD
date_changed: YYYY-MM-DD
---
```

**Rules:**

- `title`: required. Must match or closely correspond to the document's `# H1` header.
- `tags`: required. Lowercase, comma-separated list of relevant topics. Use existing tags from the project when possible.
- `date_created`: `[str]` required. ISO 8601 date (`YYYY-MM-DD`) of initial creation.
- `date_changed`: `[str]` required. ISO 8601 date (`YYYY-MM-DD`), updated whenever content changes. Must be `>=` `date_created`.
- `description`: `[str]` required. Concise summary of the document's purpose and content, ideally under 200 characters.
- `author`: `[list]` required. By default, "Lucas Galdino" or the agent's name.
- Additional fields are allowed and encouraged when relevant (e.g., `version`, `status`).
- The front matter block must be the very first thing in the file — no blank lines or content before the opening `---`.
- Use double-quoted strings for titles containing colons, special characters, or leading/trailing spaces.

**More info can be found in the [yaml-cheat-sheet](./references/yaml-cheat-sheet.md)**

### Structure and whitespace

- ATX headers only (`# Header`). One space after `#`. No closing `#`.
- Don't skip header levels. Use `<h1>, ..., <h6>`. Surround headers with exactly one blank line.
- Sentence case for headers (capitalize first word only, except proper nouns).
- No trailing punctuation on headers (no `:` or `.`). — **MD026, MD036**
- End every file with exactly one newline. — **MD047**
- No consecutive blank lines. — **MD012**
- No trailing whitespace (except 2 spaces for intentional line breaks). — **MD009**
- Single space after sentences.
- **line-length is disabled. Do not wrap lines.** — **disable MD013**

### 2. Lists

- Unordered: hyphen `-` marker. — **MD004**
- Ordered: sequential numbering (`1.`, `2.`, `3.`). — **MD029** (`style: "ordered"`)
- One space after list markers.
- Surround lists with blank lines. — **MD032**
- No empty lines between single-line list items; blank lines between multi-line items.

### 3. Code blocks

- Always fenced (triple backticks). Never indented. — **MD046**
- Use backtick fence style, never tildes. — **MD048**
- **Always specify the language.** — **MD040**
- When code is extracted from or destined for a known file, add the source path and line range in the info string:

  ````markdown
  ```python src/utils/parser.py#L15-L30
  def parse(data):
      return json.loads(data)
  ```
  ````

  Format: `` `language filepath#L<start>-L<end>` ``

  This applies whenever a source file exists or will exist. For purely illustrative snippets with no file association, language alone is sufficient.

- When nesting code blocks or showing markdown-inside-markdown, increase the fence length. Use 4+ backticks for the outer fence:

  `````markdown
  ````markdown
  ```bash
  echo "nested"
  ```
  ````
  `````

  Add more backticks as nesting depth increases.

### 4. Admonitions — GitHub style ONLY

Always use GitHub's blockquote-based admonition syntax. Never use emoji-based or bold-text admonitions.

```markdown
> [!note]
> Highlights information that users should take into account, even when skimming.

> [!tip]
> Optional information to help a user be more successful.

> [!important]
> Crucial information necessary for users to succeed.

> [!warning]
> Critical content demanding immediate user attention due to potential risks.

> [!caution]
> Negative potential consequences of an action.
```

**Rules:**

- Only these five types exist: `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, `CAUTION`.
- Each admonition is a blockquote — every continuation line starts with `>`.
- Consecutive admonitions MUST be separated by a blank line (not just a `>` line). — **custom: admonition-separation** (MD028 disabled — replaced by this rule)
- Important observations go inside admonitions. Minor notes, references, or tangential remarks go in footnotes instead (see rule 7).

### 5. Emphasis and bold — not for section structure

- Bold: `**bold**`. Italic: `*italic*`. — **MD049, MD050** (`style: "consistent"`)
- Never use bold/italic as a substitute for a header to introduce a multi-line section. — **MD036**
- Never use UPPERCASE for emphasis.

### 6. Links — reference labels for repeated URLs

- When a URL appears **3 or more times** in a document, convert all occurrences to a reference-style label:

  ```markdown
  See the [markdownlint docs][mdlint] for details.

  [mdlint]: https://github.com/DavidAnson/markdownlint
  ```

- Reference definitions go at the end of the file, sorted alphabetically by label.
- Labels use lowercase and hyphens only.
- Use double quotes for link titles.
- No bare URLs in prose. — **MD034**
- Descriptive link text — never "click here", "here", "link", or "more". — **MD059**

### 7. Footnotes

Classify footnotes by **content-type** first, then by **size**.

**Content-type routing:**

| Content type| Where it goes|
| ----------------------------------------------- | ---------------------------------------------- |
| Citations / references (papers, specs, URLs)| Footnote|
| Tangential observations or minor clarifications | Footnote (if short) or admonition (if complex) |
| Definitions / explanations of terms or concepts | Admonition (rule 4) — never a footnote|
| Important warnings or instructions| Admonition (rule 4) — never a footnote|

**Size threshold — when a footnote is too large:**

A footnote is "short" when it fits in ~2 lines and ~200 characters. Beyond that, convert to an admonition or a dedicated subsection. Long footnotes break readability at the bottom of the rendered page.

**Placement:** each `[^id]:` definition goes immediately after the paragraph that references it, separated by a blank line.

```markdown
This approach was first described in the CommonMark spec[^commonmark].

[^commonmark]: [CommonMark Spec §6.1](https://spec.commonmark.org/0.31.2/#code-spans) — accessed 2026-03-23.

The next paragraph continues here.
```

**GFM multi-line footnotes:** footnotes CAN contain lists, tables, blockquotes, and code blocks — indent continuation content by 4 spaces:

```markdown
[^detailed]: First line of the footnote.

    - Indented list item insid**MD013**e the footnote
    - Another item

    > Indented blockquote inside the footnote

| Col A | Col B |
| ----- | ----- |
| data  | data  |
```

**Identifiers:** prefer descriptive words (`[^commonmark]`, `[^euler-formula]`) over numbers for documents with many footnotes. Numbers are acceptable for documents with few footnotes.

For more info on footnotes, check the [extended syntax reference](references/extended-syntax-and-hacks.md#footnotes).

### 8. Tables

- Surround with blank lines. — **MD058**
- Leading and trailing pipes on every row. — **MD055**
- Do NOT pad or align columns — use compact style with minimal spacing. — **MD060** (`style: "compact"`, `aligned_delimiter: false`)
- Consistent column count across rows. — **MD056**

### 9. Blockquotes — admonitions only

All blockquotes MUST use admonition syntax (rule 4). Plain blockquotes without an admonition marker (`[!TYPE]`) are not allowed.

- One space after `>`.
- Use `>` on every line including wrapped continuations.
- No empty lines inside a single admonition blockquote.
- Consecutive admonitions separated by a blank line.

If you need to quote external text, place it inside a `[!NOTE]` or `[!TIP]` admonition with attribution.

### 10. HTML in markdown

- Avoid raw HTML unless necessary for features markdown doesn't support (image sizing, underline, complex table cells). — **MD033**
- Separate consecutive elements (lists, code blocks, blockquotes) with `<!-- -->` when needed.
- Use `<!-- comment -->` or `[hidden comment]: #` for invisible comments.
- `<mark>text</mark>` is an accepted use of raw HTML for highlighting annotations — preserve it.

### 11. KaTeX math

> [!important]
> When writing any math expression, consult [references/math-katex-reference.md](references/math-katex-reference.md) for platform limitations and [references/latex-environments.md](references/latex-environments.md) for choosing the right environment. The full supported-function list is at [references/katex-docs/docs/supported.md](references/katex-docs/docs/supported.md).

**Delimiters:** inline math uses `$expression$`; display math uses `$$...$$` for
standalone block equations.

Display math must always use an explicit environment:

```latex
$$\begin{equation}
E = mc^{2}
\end{equation}$$
```

Never write bare `$$expression$$`. Choose from:

|Situation| Environment|
|---|---|
|Single equation (numbered, cite-able)| `equation`|
| Single equation (no number)| `equation*`|
| Single equation split across lines| `split` inside `equation` |
| Multiple equations, aligned, numbered| `align`|
| Multiple equations, aligned, no numbers  | `align*`|
| Multiple equations, centered, numbered   | `gather`|
| Multiple equations, centered, no numbers | `gather*`|
| Piecewise/conditional definition| `cases` or `dcases`|
| Matrix — parentheses| `pmatrix`|
| Matrix — brackets| `bmatrix`|
| General tabular math| `array{colspec}`|

Platform constraints:

- Do NOT use `\def`, `\gdef`, `\newcommand`, or any custom macros — they break
  on GitHub and are unreliable across renderers.
- Do NOT use `\href`, `\url`, `\includegraphics`, or `\html*` commands —
  disabled by default (`trust: false`).
- Do NOT use `\[...\]` or `\(...\)` delimiters — unsupported on GitHub.
- Prefer `\textcolor{color}{…}` over the `\color` switch form.
- Text inside math: always use `\text{…}`. Never write bare words in math mode.
- `\tag{}` is supported inside `align`, `align*`, `gather`, `gather*`, `equation`.
- `aligned`, `gathered`, `alignedat` are nestable and do not auto-number;
  they must remain inside math delimiters.

### 12. XML tags in agent files

When writing markdown for agent customization files (`.instructions.md`, `.prompt.md`, SKILL.md, AGENTS.md, `.agent.md`), use semantic XML tags to separate content types — instructions, context, constraints, and examples.

**Formatting rules:**

- Always insert a blank line after an opening tag and before a closing tag.
- Use semantic, domain-specific tag names — never standard HTML tag names (`<div>`, `<p>`, `<span>`, `<code>`, etc.) which get stripped by markdown renderers.
- Keep nesting to 2–3 levels maximum.

**Canonical tags:** `<instructions>`, `<context>`, `<rules>`, `<constraints>`, `<examples>`, `<example>`, `<input>`, `<output>`, `<warning>`, `<output_format>`, `<gotchas>`, `<validation>`, `<checkpoint>`, `<recovery>`, `<command>`, `<template>`, `<criteria>`, `<prerequisites>`, `<error_handling>`.

```markdown
<rules>

- Rule one with its reason.
- Rule two with its reason.
</rules>

<examples>
<example>

Input: realistic user request
Output: correct agent behavior
</example>
</examples>
```

Do NOT wrap every line — only wrap content where the type would be ambiguous without tags. If the structure is obvious from markdown headers and formatting alone, XML tags are unnecessary.

### 13. Math symbol notation table

When a document uses mathematical symbols or notation, include a **symbol notation table** near the beginning of the math-heavy section so readers can decode the expressions.

```markdown
| Symbol| Meaning|
|---|---|
| $x$| Input variable|
| $\hat{y}$| Predicted output  |
| $\theta$| Model parameters  |
| $\nabla$| Gradient operator |
| $\mathcal{L}$ | Loss function|
```

**Rules:**

- Place the table before the first equation that uses the symbols.
- Only include symbols that are non-obvious or domain-specific — skip universally known notation like $+$, $=$, $\sum$.
- Update the table when new symbols are introduced later in the document.

### 14. Importing from external tools (Google Docs, Word, etc.)

Files imported from rich-text editors frequently carry structural artifacts. Detect and fix all of the following before treating the file as compliant.

**Headers:**

- Google Docs exports bold numbered headers: `## **1\. The Evolution of...**`. Strip the bold markers AND the backslash escape: `## 1. The Evolution of...`.
- MS Word exports may produce similar patterns or use `===`/`---` underline-style headers — convert to ATX.

**Paragraph breaks:**

- Google Docs sometimes uses a hard line break (`  ` — two trailing spaces) within what should be separate paragraphs. Replace `  \n` with `\n\n` (blank line) on prose lines.
- When each Google Doc paragraph is a single long line with no blank separator between consecutive prose lines, add blank lines between them.

**Academic citations (numbered inline):**

A common Google Docs export artifact — particularly from AI-generated academic articles — is bare numeric inline citations: the text ends with a superscript number (appears as `.3`, ` 18:`, or just `21` at sentence ends) and the document has a numbered Works Cited list at the bottom.

To fix:

1. Map each citation number to a descriptive label (e.g., `3` → `[^combining-framenet-verbnet-wordnet]`).
2. Replace each occurrence in the text with `[^label]`.
3. Convert the Works Cited entries to GFM `[^label]: [Title](url) — accessed YYYY-MM-DD.` definitions.
4. Place the definitions in a `## References` header section at the **end** of the document (acceptable exception to rule 7 for large academic documents with many citations — placing 67 definitions inline would be unreadable).
5. Use the same label for repeated citations; define only once.

Example conversion:

```markdown
<!-- Before -->

...fundamental shift in the field.12
Logical positivism emerged as a response.13

...12. Philosophy of language - Wikipedia, https://en.wikipedia.org/...

<!-- After -->

...fundamental shift in the field.[^philosophy-of-language]

Logical positivism emerged as a response.[^analytic-philosophy]

## References

[^philosophy-of-language]: [Philosophy of language — Wikipedia](https://en.wikipedia.org/wiki/Philosophy_of_language) — accessed 2026-03-31.

[^analytic-philosophy]: [Analytic Philosophy — IEP](https://iep.utm.edu/analytic-philosophy/) — accessed 2026-03-31.
```

</rules>

## Markdownlint configuration

The full markdownlint config lives at [~/.markdown_lint/.markdownlint.jsonc](~/.markdown_lint/.markdownlint.jsonc).
Custom rules (GitHub admonitions enforcement, code block source citations, admonition separation) are at [~/.markdown_lint/rules/](~/.markdown_lint/rules/).

When the user asks about a specific markdownlint rule, read the corresponding file from [references/markdownlint-rules/](references/markdownlint-rules/) — for example, [`references/markdownlint-rules/Rules.md`](references/markdownlint-rules/Rules.md#md040---fenced-code-blocks-should-have-a-language-specified) for MD040.

## Validation scripts

Self-contained Python scripts (PEP 723, run with `uv run`). Each validates a specific rule domain. See [scripts/README.md](scripts/README.md) for full design analysis and edge cases.

| Script| Rule   | What it checks|
|---|---|---|
| `uv run scripts/validate_all.py <files>`| all| **Orchestrator** — runs all checks below in one command|
| `uv run scripts/check_frontmatter.py <file>`| 0| YAML fields, dates, title↔H1 match|
| `uv run scripts/check_math.py <file>`| 11, 13 | `$$` environments, forbidden commands, notation table duplicates |
| `uv run scripts/check_admonitions.py <file>`| 4, 9   | All blockquotes are admonitions, type validation, separation|
| `uv run scripts/check_codeblocks.py <file>`| 3| Language specifier, backtick-only fences|
| `uv run scripts/check_footnotes.py <file>`| 7| Placement, size threshold, orphaned refs/defs, identifier style  |
| `uv run scripts/format_table.py <file> [--fix]` | 8| Compact style, column count; `--fix` reformats in-place|
| `uv run scripts/check_xml_tags.py <file>`| 12| No HTML tags, blank lines, nesting depth, unclosed tags|

All scripts support `--json` for machine-readable output. `validate_all.py` supports `--check <name>` to run a subset.

<validation>

## Quick checklist

Before finalizing any markdown output, verify:

- [ ] YAML front matter present with `title`, `tags`, `date_created`, `date_changed`
- [ ] Every fenced code block has a language specifier
- [ ] Code extracted from files has `filepath#L<start>-L<end>` in the info string
- [ ] Admonitions use `> [!TYPE]` syntax (not emoji or bold)
- [ ] Consecutive admonitions are separated by blank lines
- [ ] No bold/italic used as section headers
- [ ] Use any level of headers available. Do not skip to bold for lower-level sections.
- [ ] URLs appearing 3+ times use reference labels
- [ ] All headers are ATX, sentence case, no trailing punctuation
- [ ] File ends with exactly one newline
- [ ] Descriptive link text (no "click here", "here", "link", "more")
- [ ] Footnote definitions placed inline (after referencing paragraph)
- [ ] No plain blockquotes — all use `> [!TYPE]` admonition syntax
- [ ] Tables use compact style (no column padding or alignment)
- [ ] Agent files use semantic XML tags where content type is ambiguous
- [ ] Math-heavy sections include a symbol notation table
- [ ] Inline math uses `$...$`, display math uses `$$\begin{env}...\end{env}$$`
- [ ] No bare `$$expression$$` — every display block has an environment
- [ ] No custom macros (`\def`, `\newcommand`) in documents targeting GitHub
- [ ] Text in math wrapped in `\text{…}`, not written bare
- [ ] Headers are plain ATX — no `**bold**` wrapping, no `1\.` backslash escapes
- [ ] No bare numeric inline citations (`.3`, `.12`) — all citations use `[^label]` footnotes
- [ ] Google Docs paragraph artifacts cleaned: trailing `  ` → blank lines; consecutive prose lines have blank separators

</validation>

## References

|File|Load when|
|---|---|
| [references/style-guide-summary.md](references/style-guide-summary.md)| Deep style questions beyond this skill's rules|
| [references/extended-syntax-and-hacks.md](references/extended-syntax-and-hacks.md)| Using advanced features: footnotes, definition lists, task lists, HTML hacks |
| [references/markdownlint-rules/](references/markdownlint-rules/)| User asks about a specific MD### rule — read `md###.md`|
| [references/markdownlint-rules/CustomRules.md](references/markdownlint-rules/CustomRules.md) | Writing or debugging custom markdownlint rules|
| [scripts/custom-rules.md](scripts/custom-rules.md)| Understanding, installing, or modifying the custom js lint rules|
| [references/math-katex-reference.md](references/math-katex-reference.md)| Any math expression — platform rules, supported functions, color, spacing|
| [references/latex-environments.md](references/latex-environments.md)| Choosing the right `$$\begin{env}...\end{env}$$` environment|
| [references/katex-docs/docs/supported.md](references/katex-docs/docs/supported.md)| Full KaTeX supported-function reference (update with `git pull`)|
| [references/katex-docs/docs/support_table.md](references/katex-docs/docs/support_table.md)   | Alphabetical KaTeX support table including unsupported functions|
| [scripts/README.md](scripts/README.md)| Design analysis, edge cases, and architecture for validation scripts|
| [references/yaml-cheat-sheet.md](references/yaml-cheat-sheet.md)| YAML syntax, data types, and formatting rules|