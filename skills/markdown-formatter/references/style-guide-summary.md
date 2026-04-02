# Markdown Style Guide Summary

Source: <https://cirosantilli.com/markdown-style-guide/>

## File conventions

- Extension: `.md`
- File names: lowercase, hyphen-separated, derived from top-level header
- End files with a newline; no trailing empty lines

## Whitespace

- No consecutive blank lines (max one empty line between elements)
- Single space after sentences (not double)
- No trailing whitespace unless it indicates a line break

## Line wrapping

- Try to keep lines under 80 characters
- Break at sentence boundaries or clause boundaries (after `,`, `and`, `which`)
- Acceptable to exceed 80 chars for single long sentences

## Headers

- Use ATX style (`# Header`) — not Setext
- Single space between `#` and text
- No closing `#` characters
- No leading spaces before `#`
- Don't skip header levels
- Surround headers with one blank line
- Sentence case (capitalize first word only, except proper nouns)
- No trailing punctuation (`:` or `.`)
- Keep headers short; expand in the first paragraph

## Blockquotes

- One space after `>`
- Use `>` on every line (including wrapped lines)
- No empty lines inside a single blockquote

## Lists

- **Unordered:** use hyphen `-` marker
- **Ordered:** use `1.` for all items (unless referencing by number)
- No extra spaces before list markers
- One space after list marker for single-line items
- Content indentation must align with first item's text
- No empty lines between single-line items; empty lines between multi-line items
- Surround lists with one blank line
- Case of first letter matches what it would be mid-sentence
- Punctuation: period only if item has multiple sentences or starts uppercase

## Definition lists

- Avoid the extension; use bold term + colon format instead:
  `- **term**: definition`

## Code

- Use fenced code blocks (triple backticks), not indented
- Always specify the language
- Don't prefix shell code with `$` unless showing output
- Mark as code: executables, file paths, version numbers, abbreviation expansions
- Don't mark as code: project names, library names

## Tables

- Surround with one blank line
- Don't indent tables
- Surround every row with pipes `|`
- Align border pipes vertically
- Column width matches longest cell

## Links

- Use trailing `[]` on implicit reference links: `[text][]`
- Reference definitions: last in file, alphabetically sorted, aligned
- Use double quotes for titles

## Emphasis

- Bold: `**bold**` (not `__bold__`)
- Italic: `*italic*` (not `_italic_`)
- Don't use UPPERCASE for emphasis
- Don't use emphasis where a header is appropriate

## Separate consecutive elements

- Use `<!-- -->` HTML comment to separate consecutive lists, code blocks, or blockquotes
