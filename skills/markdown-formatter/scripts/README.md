---
title: "Markdown formatter scripts — design analysis"
tags: [markdown, scripts, validation, linting, markdown-it-py]
date_created: 2026-04-02
date_changed: 2026-04-02
metadata:
  Scripts:
    - check_frontmatter.py
    - check_math.py
    - check_admonitions.py
    - check_codeblocks.py
    - check_footnotes.py
    - format_table.py
    - check_xml_tags.py
    - validate_all.py
  Tests:
    - tests/valid_example.md
    - tests/invalid_example.md
  Behaviors:
    date_changed_before_date_created: warning  # not error — could be intentional during drafting
    footnote_size_threshold_chars: 200
    footnote_size_threshold_lines: 2
    many_footnotes_threshold: 3
    max_xml_nesting_depth: 3
---

# Markdown formatter scripts — design analysis

## Research findings

### markdown-it-py (v4.0.0)

`python` port of markdown-it. Parses markdown into a **flat token stream** (with nesting attributes) or a **syntax tree** (`SyntaxTreeNode`). Presets: `commonmark` (default), `gfm-like`, `zero`, `js-default`.

Key token types for our rules:

| Token type | Nesting | What it captures |
|---|---|---|
| `front_matter` | 0 | YAML preamble content (via plugin) |
| `blockquote_open` / `_close` | 1 / -1 | Blockquote boundaries |
| `fence` | 0 | Fenced code blocks (`info` = language + path) |
| `math_inline` / `math_block` | 0 | Dollar-delimited math (via dollarmath plugin) |
| `footnote_ref` | 0 | Footnote references `[^id]` (via footnote plugin) |
| `footnote_open` / `_close` | 1 / -1 | Footnote definition boundaries |
| `ordered_list_open` | 1 | Ordered lists (has `markup` for marker style) |

### mdit-py-plugins — relevant plugins

| Plugin | What it parses | Our rule |
|---|---|---|
| `front_matter_plugin` | YAML `---` blocks → `front_matter` token | Rule 0 |
| `dollarmath_plugin` | `$...$` and `$$...$$` → `math_inline` / `math_block` tokens | Rule 11 |
| `amsmath_plugin` | Bare `\begin{env}...\end{env}` without `$$` delimiters | Rule 11 |
| `footnote_plugin` | `[^id]` references and `[^id]:` definitions | Rule 7 |

### GitHub's parser (cmark-gfm)

GitHub uses cmark-gfm (a C library). No usable `python` binding exists, but markdown-it-py with `gfm-like` preset approximates it closely. Key difference: GitHub's math rendering uses its own dollar-sign parser with slightly different edge-case behavior for `$` adjacent to digits/spaces.

## What can be validated programmatically

### High confidence (AST-level checks)

1. **YAML front matter** — presence, required fields, date validation
2. **Blockquotes as admonitions** — every `blockquote_open` must contain `[!TYPE]` on its first inline content
3. **Math environments** — `$$` blocks must contain `\begin{env}...\end{env}`
4. **Forbidden LaTeX commands** — scan math tokens for `\def`, `\newcommand`, `\href`, `\url`, etc.
5. **Code block languages** — `fence` tokens must have non-empty `info` field
6. **Footnote size** — measure content length of `footnote_open..close` spans

### Medium confidence (content-level checks)

7. **Footnote placement** — verify `[^id]:` definitions appear after their referencing paragraph (line-based)
8. **Bare words in math** — detect words not wrapped in `\text{}` inside math tokens
9. **Reference labels** — count URL occurrences and flag when ≥3 without reference label

### Best-effort (heuristic)

10. **Table compactness** — detect padded/aligned tables (regex on `|` spacing)
11. **Consecutive admonitions** — verify blank line between consecutive blockquotes

## Proposed scripts

### Script 1: `validate_markdown.py` — unified linter

Parses with markdown-it-py + plugins, walks the token stream, checks rules 0, 3, 7, 9, 11. Single entry point with `--check` flags.

### Script 2: `check_math.py` — math-specific validator

Focused on rule 11. Extracts all math tokens, validates environments, forbidden commands, bare words.

### Script 3: `format_table.py` — table reformatter

Reads markdown, finds table blocks, reformats to compact style (rule 8). Outputs the fixed file.

### Script 4: `check_footnotes.py` — footnote validator

Validates footnote placement, size, identifier style (rule 7).

## Dependencies

All scripts use PEP 723 inline metadata (`uv run --script`):

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdown-it-py[plugins]>=4.0.0",
#   "pyyaml>=6.0",
# ]
# ///
```

## Architecture options

### ~~Option A: Single unified script~~

### Option B: Modular per-domain scripts (CHOSEN)

Separate scripts: `check_frontmatter.py`, `check_math.py`, `check_admonitions.py`, `check_codeblocks.py`, `check_footnotes.py`, `format_table.py`, `check_xml_tags.py`.

**Pros:** focused, independently runnable, easier to maintain, each script only loads the plugins it needs.

**Cons (minor):**

- Each script independently parses the file with markdown-it-py (~5ms per file per script). For running all 7 checks, ~35ms total — negligible in practice.
- ~~Running all checks requires 7 commands.~~ **Solved by `validate_all.py`**: imports all check functions via `sys.path.insert`, runs them in one command, aggregates findings. Individual scripts still work standalone because each has `if __name__ == "__main__"`.
- ~15 lines of boilerplate (`Finding` dataclass, output formatting, CLI parsing) is duplicated across scripts. This is the cost of PEP 723 self-contained scripts — no shared modules allowed. The `validate_all.py` orchestrator avoids this by normalizing findings via `dataclasses.asdict()` after the fact.

## Tests

Test fixtures are in `tests/`:

| File | Purpose |
|---|---|
| `tests/valid_example.md` | Passes all validation rules — canonical correct usage |
| `tests/invalid_example.md` | Intentionally violates rules 0 (date order), 3, 7, 8, 9, 11 |

Run all checks against both files:

```bash
uv run validate_all.py tests/valid_example.md tests/invalid_example.md
```

Expected: `valid_example.md` → zero errors, `invalid_example.md` → multiple errors and warnings.

### ~~Option C: Hybrid~~

## Edge case analysis

### YAML front matter (check_frontmatter.py)

| Edge case | Handling |
|---|---|
| File with no front matter | Error: "No YAML front matter found" |
| Invalid YAML (malformed syntax) | Error with yaml.YAMLError details |
| Missing required fields | Error per missing field |
| `date_changed` before `date_created` | Warning (not error — could be intentional during drafting) |
| Title doesn't match H1 exactly | Warning with case-insensitive comparison |
| Front matter not first in file | Error: "must be the very first thing" |
| Multiple `---` blocks | Parser handles: first valid `---..---` is front matter |
| `---` inside code blocks | Parser correctly ignores these |
| Empty/null required fields | Error: "field is empty" |

### Blockquote admonitions (check_admonitions.py)

| Edge case | Handling |
| --- | --- |
| Nested blockquotes (blockquote inside blockquote) | Only top-level blockquote checked for `[!TYPE]` |
| `> [!NOTE]` inside a fenced code block | Parser excludes — fence tokens are separate |
| Empty blockquote (just `>`) | Error: no admonition marker found |
| Valid admonition with wrong type (e.g., `[!INFO]`) | Error listing valid types |
| Blockquote inside list item | Checked — the parser still emits `blockquote_open` |
| Consecutive blockquotes without blank line | Error: "must be separated by a blank line" |

### Math environments (check_math.py)

| Edge case | Handling |
|---|---|
| `$` as currency (e.g., "\$100") | dollarmath_plugin with `allow_digits=True` may parse this — but typically `$100` without closing `$` won't match. No false positive in practice |
| `$$` inside a code block | Parser correctly ignores — fence tokens exclude math |
| Nested environments (e.g., `split` inside `equation`) | Valid — only outermost `$$` checked for `\begin` |
| Empty `$$..$$` block | Error: no environment found |
| `\[...\]` or `\(...\)` delimiters | Error: "unsupported on GitHub" (line-based check) |
| Duplicate symbols in notation table | Warning with line of first occurrence |
| Bare words in math (e.g., `x = value`) | Warning: heuristic check, skips known function names |

### Code blocks (check_codeblocks.py)

| Edge case | Handling |
|---|---|
| Info string with only spaces | Error: treated as no language |
| Tilde fences (`~~~`) | Warning: "use backtick fences" (MD048) |
| Nested fences (outer has 4+ backticks) | Parser handles correctly |
| Info string with file path (e.g., ```python src/file.py#L1-L10```) | Language is first word — valid |

### Footnote placement (check_footnotes.py)

| Edge case | Handling |
|---|---|
| Multiple references to same footnote | Checks against first reference only |
| Orphaned definition (no reference) | Warning |
| Orphaned reference (no definition) | Warning |
| Multi-line footnote with 4-space indent | Correctly gathered as single definition |
| Footnote > 200 chars or > 2 lines | Warning: "consider converting to admonition" |
| Numeric IDs in document with many footnotes | Info: "prefer descriptive words" |
| Definition appears before reference | Warning: "place definitions inline after the referencing paragraph" |

### XML tags (check_xml_tags.py)

| Edge case | Handling |
|---|---|
| XML tags inside code blocks | Skipped (code block detection) |
| HTML tag names as XML tags | Error: "will be stripped by markdown renderers" |
| Unclosed tags | Error at opening tag line |
| Mismatched close/open | Error with mismatch details |
| No blank line after opening tag | Warning |
| No blank line before closing tag | Warning |
| Nesting > 3 levels | Warning |
| Non-agent file | Skipped entirely (checks file extension/name) |

### Tables (format_table.py)

| Edge case | Handling |
|---|---|
| Table inside code block | Skipped (code block detection) |
| Alignment in delimiter row (`:---:`, `---:`) | Preserved during reformatting |
| Table with only 1 column | Reformatted normally |
| Irregular column count across rows | Reported as warning (MD056) |
| Empty cells | Preserved as empty (`||`) |
