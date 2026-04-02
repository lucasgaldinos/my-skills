# Extended Markdown Syntax Reference

Source: <https://www.markdownguide.org/extended-syntax/>

## Tables

- Use `---` for column headers, `|` to separate columns
- Alignment: `:---` left, `:---:` center, `---:` right
- Can format text inside cells (links, code, emphasis) but not block elements
- Escape `|` with `&#124;`

## Fenced code blocks

- Use 3 or more backticks (not tildes), as requested.
- Specify language for syntax highlighting:

  ````python
  '''some python code'''
  ````

- No indentation needed

## Footnotes

- Reference: `[^identifier]`
- Definition: `[^identifier]: content`
- Identifiers can be numbers or words (no spaces/tabs)
- Can go anywhere except inside lists, blockquotes, tables
- Multi-paragraph footnotes: indent continuation paragraphs

## Heading IDs

- Custom: `### Heading {#custom-id}`
- Link to: `[text](#custom-id)`

## Definition lists

- Term on first line, `: definition` on next line
- Not universally supported

## Strikethrough

- `~~strikethrough~~`

## Task lists

- `- [x] completed`
- `- [ ] incomplete`

## Emoji

- Copy/paste Unicode or use shortcodes: `:tent:`

## Highlight

- `==highlighted==` (limited support; use `<mark>` as fallback)

## Subscript / Superscript

- Sub: `H~2~O` (or `<sub>`)
- Super: `X^2^` (or `<sup>`)

## Automatic URL linking

- Bare URLs are auto-linked in many processors
- Disable with backticks: `` `http://example.com` ``

---

# Markdown Hacks Reference

Source: <https://www.markdownguide.org/hacks/>

## Underline

- `<ins>underlined text</ins>`

## Indent

- `&nbsp;&nbsp;&nbsp;&nbsp;` for manual indentation (last resort)

## Center

- `<center>text</center>` (deprecated) or `<p style="text-align:center">`

## Color

- `<font color="red">text</font>` (deprecated) or `<p style="color:blue">`

## Comments

- `[comment text]: #` — invisible in rendered output
- Surround with blank lines

## Image size

- `<img src="image.png" width="200" height="100">`

## Image captions

- `<figure>` + `<figcaption>` or italic text below image

## Link targets

- `<a href="url" target="_blank">text</a>`

## Symbols

- Use HTML entities: `&copy;`, `&reg;`, `&trade;`, `&euro;`, `&larr;`, etc.

## Table hacks

- Line breaks in cells: `<br>`
- Lists in cells: `<ul><li>item</li></ul>`

## Table of contents

- Manual list of `[heading](#heading-id)` links

## Videos

- Link image to video: `[![alt](thumbnail-url)](video-url)`
