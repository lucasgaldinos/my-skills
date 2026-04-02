---
name: markdown-formatter
description: >-
  Use this skill before generating any new markdown file, or when explicitly
  invoked via /markdown-formatter for existing markdown. Enforces formatting
  rules, markdownlint compliance, GitHub-style admonitions, reference labels,
  footnotes, code block source citations, and KaTeX math formatting. Triggers
  on: "format markdown", "write a README", "create documentation", "fix
  markdown formatting", "generate .md file", "write math", "add equation",
  or any task producing markdown output.
argument-hint: "markdown formatting instructions"
references:
  - references/math-katex-reference.md
  - references/latex-environments.md
  - https://github.com/KaTeX/KaTeX/blob/main/docs/supported.md#style-color-size-and-font
  - https://github.com/KaTeX/KaTeX/blob/main/docs/support_table.md
---

# Markdown Formatter

Produce markdown that is readable in source, portable across renderers, diff-friendly, and fully compliant with the project's markdownlint configuration.

## When this skill activates

- **New markdown files:** automatically, before any generation begins.
- **Existing markdown:** only when explicitly invoked (`/markdown-formatter`).

## Core rules

Every markdown file MUST follow these rules. Violations are formatting errors.

### 0. YAML front matter (preamble)

Every markdown file MUST begin with a YAML front matter block containing at minimum:

```yaml
---
title: "Document title matching the top-level header"
tags: [relevant, topic, tags]
date_created: YYYY-MM-DD
date_changed: YYYY-MM-DD
---
```

**Rules:**

- `title`: required. Must match or closely correspond to the document's `# H1` header.
- `tags`: required. Lowercase, comma-separated list of relevant topics. Use existing tags from the project when possible.
- `date_created`: required. ISO 8601 date (`YYYY-MM-DD`) of initial creation.
- `date_changed`: required. ISO 8601 date (`YYYY-MM-DD`), updated whenever content changes. Must be `>=` `date_created`.
- Additional fields are allowed and encouraged when relevant (e.g., `author`, `description`, `version`, `status`).
- The front matter block must be the very first thing in the file — no blank lines or content before the opening `---`.
- Use double-quoted strings for titles containing colons, special characters, or leading/trailing spaces.

### 1. Structure and whitespace

- ATX headers only (`# Header`). One space after `#`. No closing `#`.
- Don't skip header levels. Use `<h1>, ..., <h6>`. Surround headers with exactly one blank line. 
- Sentence case for headers (capitalize first word only, except proper nouns).
- No trailing punctuation on headers (no `:` or `.`). — **MD026, MD036**
- End every file with exactly one newline. — **MD047**
- No consecutive blank lines. — **MD012**
- No trailing whitespace (except 2 spaces for intentional line breaks). — **MD009**
- Single space after sentences.
- line-length is disabled. Do not wrap lines. — **MDD013**

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
> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
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

Use footnotes for:

- Minor references or attributions that would interrupt reading flow.
- Tangential observations not directly tied to the main content.
- Source citations for non-code content (papers, articles, specifications).

Do NOT use footnotes for important warnings or instructions — those belong in admonitions (rule 4).

```markdown
This approach was first described in the CommonMark spec[^1].

[^1]: [CommonMark Spec §6.1](https://spec.commonmark.org/0.31.2/#code-spans) — accessed 2026-03-23.
```

Footnote identifiers: prefer descriptive words (`[^commonmark]`) over numbers for documents with many footnotes.

### 8. Tables

- Surround with blank lines. — **MD058**
- Leading and trailing pipes on every row. — **MD055**
- Do NOT pad or align columns — use compact style with minimal spacing. — **MD060** (`style: "compact"`, `aligned_delimiter: false`)
- Consistent column count across rows. — **MD056**

### 9. Blockquotes

- One space after `>`.
- Use `>` on every line including wrapped continuations.
- No empty lines inside a single blockquote.
- Consecutive blockquotes separated by a blank line. — **MD028**

### 10. HTML in markdown

- Avoid raw HTML unless necessary for features markdown doesn't support (image sizing, underline, complex table cells). — **MD033**
- Separate consecutive elements (lists, code blocks, blockquotes) with `<!-- -->` when needed.
- Use `<!-- comment -->` or `[hidden comment]: #` for invisible comments.

### 11. KaTeX math

> [!IMPORTANT]
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

| Situation | Environment |
|-----------|-------------|
| Single equation (numbered, cite-able) | `equation` |
| Single equation (no number) | `equation*` |
| Single equation split across lines | `split` inside `equation` |
| Multiple equations, aligned, numbered | `align` |
| Multiple equations, aligned, no numbers | `align*` |
| Multiple equations, centered, numbered | `gather` |
| Multiple equations, centered, no numbers | `gather*` |
| Piecewise/conditional definition | `cases` or `dcases` |
| Matrix — parentheses | `pmatrix` |
| Matrix — brackets | `bmatrix` |
| General tabular math | `array{colspec}` |

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

## Markdownlint configuration

The full markdownlint config lives at `~/.markdown_lint/.markdownlint.jsonc`.
Custom rules (GitHub admonitions enforcement, code block source citations, admonition separation) are at `~/.markdown_lint/rules/`.

When the user asks about a specific markdownlint rule, read the corresponding file from [references/markdownlint-rules/](references/markdownlint-rules/) — for example, `references/markdownlint-rules/md040.md` for MD040.

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
- [ ] Inline math uses `$...$`, display math uses `$$\begin{env}...\end{env}$$`
- [ ] No bare `$$expression$$` — every display block has an environment
- [ ] No custom macros (`\def`, `\newcommand`) in documents targeting GitHub
- [ ] Text in math wrapped in `\text{…}`, not written bare

## References

| File | Load when |
|------|-----------|
| [references/style-guide-summary.md](references/style-guide-summary.md) | Deep style questions beyond this skill's rules |
| [references/extended-syntax-and-hacks.md](references/extended-syntax-and-hacks.md) | Using advanced features: footnotes, definition lists, task lists, HTML hacks |
| [references/markdownlint-rules/](references/markdownlint-rules/) | User asks about a specific MD### rule — read `md###.md` |
| [references/markdownlint-rules/CustomRules.md](references/markdownlint-rules/CustomRules.md) | Writing or debugging custom markdownlint rules |
| [scripts/custom-rules.md](scripts/custom-rules.md) | Understanding, installing, or modifying the custom js lint rules |
| [references/math-katex-reference.md](references/math-katex-reference.md) | Any math expression — platform rules, supported functions, color, spacing |
| [references/latex-environments.md](references/latex-environments.md) | Choosing the right `$$\begin{env}...\end{env}$$` environment |
| [references/katex-docs/docs/supported.md](references/katex-docs/docs/supported.md) | Full KaTeX supported-function reference (update with `git pull`) |
| [references/katex-docs/docs/support_table.md](references/katex-docs/docs/support_table.md) | Alphabetical KaTeX support table including unsupported functions |
