---
title: "KaTeX Math Formatting Reference"
tags: [katex, math, latex, markdown, formatting]
date_created: 2026-04-01
date_changed: 2026-04-01
description: "Rules and quick reference for KaTeX math formatting in markdown documents rendered by GitHub and VS Code."
---

# KaTeX math formatting reference

This reference governs how to write math in markdown files processed by this skill.
Primary sources live in [katex-docs/docs/](katex-docs/docs/) (sparse-checkout of the
[KaTeX repository][katex-repo], `docs/` only). Run `git pull origin main` inside that
directory to update.

> [!IMPORTANT]
> The full canonical supported-functions list is at
> [katex-docs/docs/supported.md](katex-docs/docs/supported.md) and the alphabetical
> support table is at [katex-docs/docs/support_table.md](katex-docs/docs/support_table.md).
> When in doubt, consult those files before writing a math expression.

## 1. Delimiters: inline vs display

| Delimiter | Mode | Renders as |
|-----------|------|-----------|
| `$...$` | Inline | Math embedded in text flow |
| `$$...$$` | Display | Centered block on its own line |

- Use `$...$` for short expressions embedded in a sentence: "the cost is $O(n^2)$".
- Use `$$...$$` for standalone equations that deserve their own line.
- **Display math (`$$...$$`) MUST always contain an explicit environment.**
  Never write bare `$$x + y = z$$`. Always wrap with `\begin{...}\end{...}`:

  ```latex
  $$\begin{equation}
  x + y = z
  \end{equation}$$
  ```

  Rationale: bare display math behaves inconsistently across renderers (GitHub,
  VS Code, Jupyter). An explicit environment communicates intent unambiguously
  and unlocks alignment, numbering, and multi-line capabilities.

- Do not use `\[...\]` or `\(...\)` delimiters — they are **not** supported
  by GitHub's markdown renderer.

## 2. Choosing the right display environment

See [latex-environments.md](latex-environments.md) for the full decision guide.
Quick summary:

| Environment | Use when |
|-------------|----------|
| `equation` | Single equation, numbered |
| `equation*` | Single equation, no number |
| `split` | Single equation split across lines (inside `equation`) |
| `align` | Multiple equations with column alignment, numbered |
| `align*` | Multiple equations with column alignment, no numbers |
| `aligned` | Alignment block nested inside another environment or inline |
| `gather` | Multiple equations centered, no alignment, numbered |
| `gather*` | Multiple equations centered, no alignment, no numbers |
| `gathered` | Like `gather` but nestable; no numbers |
| `array` | General tabular math; needs column spec `{lcr}` |
| `matrix` | Matrix without delimiters |
| `pmatrix` | Matrix in parentheses `( )` |
| `bmatrix` | Matrix in brackets `[ ]` |
| `Bmatrix` | Matrix in braces `{ }` |
| `vmatrix` | Matrix with single bars `\| \|` |
| `Vmatrix` | Matrix with double bars `\|\| \|\|` |
| `cases` | Piecewise / conditional definitions |
| `dcases` | Like `cases` but applies `\displaystyle` to each branch |
| `alignat` | Column-aligned equations with explicit column count |

> [!TIP]
> `aligned`, `gathered`, and `alignedat` do **not** need to be in display mode
> themselves — they can sit inside `$...$` or be nested in another `$$...$$`
> environment. Use them when you want alignment without triggering block layout.

## 3. GitHub rendering limitations

GitHub renders KaTeX with conservative defaults. Features that **do not work** on GitHub:

- **Macros** (`\def`, `\gdef`, `\newcommand`, `\let`, etc.) — silently ignored or
  rendered as red error text. Do not define or use custom macros in documents
  targeting GitHub rendering.
- **HTML extension commands** (`\href`, `\url`, `\htmlId`, `\htmlClass`,
  `\htmlStyle`, `\htmlData`, `\includegraphics`) — disabled because `trust: false`
  is the default. Avoid them; use standard markdown links instead.
- **`\color` switch behavior** — GitHub may render `\color{blue} text` differently
  than `\textcolor{blue}{text}`. Prefer `\textcolor{blue}{text}` for reliability.
- **`\tag`** — equation tags may not render on GitHub; use sparingly and only
  inside `align`, `gather`, or `equation`.

> [!WARNING]
> Do not use `\def`, `\gdef`, `\newcommand`, or any custom macro in documents
> that will be rendered on GitHub. They break silently or produce red error output.

## 4. VS Code rendering notes

VS Code uses the `markdown-it` + KaTeX pipeline (via extensions such as
`yzhang.markdown-all-in-one` or `vscode.markdown-math`). Behavior is close to
GitHub but with some differences:

- Most standard KaTeX functions work.
- `\tag` is generally supported.
- `displaystyle` coercion (`\displaystyle` inside inline math) works.
- Macros defined via `\def` within a single `$$` block are local and work within
  that block.
- Cross-block macro persistence (`\gdef`) is **not** reliable; do not rely on it.

## 5. Supported function categories (quick reference)

All of the following categories are safe to use in both GitHub and VS Code:

| Category | Example functions |
|----------|------------------|
| Greek letters | `\alpha`, `\beta`, `\Gamma`, `\Omega` |
| Accents | `\hat`, `\bar`, `\tilde`, `\vec`, `\dot`, `\ddot` |
| Fractions | `\frac{}{}`, `\dfrac{}{}`, `\tfrac{}{}`, `\cfrac{}{}` |
| Roots | `\sqrt{}`, `\sqrt[n]{}` |
| Sums / integrals | `\sum`, `\int`, `\iint`, `\oint`, `\prod` |
| Limits | `\lim`, `\limsup`, `\min`, `\max`, `\sup`, `\inf` |
| Relations | `\leq`, `\geq`, `\neq`, `\approx`, `\sim`, `\cong`, `\equiv` |
| Arrows | `\to`, `\gets`, `\Rightarrow`, `\leftrightarrow` |
| Logic / sets | `\forall`, `\exists`, `\in`, `\notin`, `\subset`, `\cup`, `\cap` |
| Delimiters | `\left(`, `\right)`, `\left[`, `\big(`, `\bigg\|` |
| Layout | `\overbrace`, `\underbrace`, `\overline`, `\boxed` |
| Text in math | `\text{…}`, `\mathrm{…}`, `\mathbf{…}`, `\mathit{…}` |
| Color | `\textcolor{color}{…}`, `\colorbox{color}{…}` |
| Size | `\displaystyle`, `\textstyle`, `\small`, `\large`, `\Huge` |

## 6. Text in math mode

Use `\text{…}` to embed plain text inside a math expression:

```latex
$x \in \mathbb{R} \text{ such that } x > 0$
```

Renders as: $x \in \mathbb{R} \text{ such that } x > 0$

Nest `$…$` inside `\text{…}` to switch back to math mode:

```latex
$\text{if } n \text{ is even, then } n = 2k$
```

Renders as: $\text{if } n \text{ is even, then } n = 2k$

Do **not** write bare words in math mode — they render as italic math variables, not text.

## 7. Fonts and styling

| Command | Produces |
|---------|----------|
| `\mathbf{A}` or `\bf A` | Bold upright |
| `\mathit{A}` or `\it A` | Italic |
| `\mathrm{A}` or `\rm A` | Roman (upright) |
| `\mathsf{A}` or `\sf A` | Sans-serif |
| `\mathtt{A}` or `\tt A` | Monospace |
| `\mathbb{A}` | Blackboard bold (`ℝ`, `ℕ`, `ℤ`) |
| `\mathcal{A}` | Calligraphic |
| `\mathfrak{A}` | Fraktur |
| `\boldsymbol{A}` | Bold (works for Greek and symbols) |
| `\pmb{A}` | Poor man's bold (fallback when `\boldsymbol` has no glyph) |

Preferred blackboard bold shortcuts: `\R`, `\N`, `\Z`, `\mathbb{R}`, `\mathbb{N}`.

## 8. Color

Inline syntax and rendered result:

- `$\textcolor{blue}{F = ma}$` → $\textcolor{blue}{F = ma}$
- `$\textcolor{#228B22}{F = ma}$` → $\textcolor{#228B22}{F = ma}$

For background colors, `\colorbox` renders its argument in text mode; nest `$…$`
inside to render math. Use it inside display math to avoid `$` delimiter conflicts:

```latex
$$\begin{equation*}
  \colorbox{aqua}{$F = ma$}
\end{equation*}$$
```

- `\textcolor{color}{…}` — colored text; prefer this over `\color` (which is a switch).
- Accepts HTML color names and six-digit hex codes (with or without `#`).
- `\colorbox{color}{$math$}` — background color; nest `$…$` inside for math content.
- Avoid color in documents targeting black-and-white output.

## 9. Spacing and alignment fine-tuning

| Command | Width |
|---------|-------|
| `\,` | 3/18 em (thin space) |
| `\:` | 4/18 em (medium space) |
| `\;` | 5/18 em (thick space) |
| `\quad` | 1 em |
| `\qquad` | 2 em |
| `\!` | −3/18 em (negative thin space) |
| `~` | non-breaking space |

Use `\,` to separate `d` from the variable in integrals: `\int f(x)\,dx`.

## 10. Line separators inside environments

Inside any multi-row environment, use `\\` to end a row. Optional distance syntax:
`\\[0.5em]`. Accepted alternatives: `\cr`, `\\[distance]`, `\cr[distance]`.

## 11. Common pitfalls

| Pitfall | Correct form |
|---------|-------------|
| Bare display math | `$$\begin{equation}…\end{equation}$$` |
| Custom macros on GitHub | Expand inline; use standard KaTeX functions |
| `\[…\]` delimiters | Use `$$\begin{equation}…\end{equation}$$` instead |
| Text in math mode | Wrap in `\text{…}` |
| `\color` as a switch | Use `\textcolor{color}{…}` instead |
| HTML-extension commands | Use standard markdown/KaTeX alternatives |
| Missing `&` in `align` | Every `\\` row must have matching `&` alignment points |

## 12. Updating the KaTeX docs

```bash
cd ~/.agents/skills/markdown-formatter/references/katex-docs
git pull origin main
```

This updates only the `docs/` subdirectory (sparse checkout).

[katex-repo]: https://github.com/KaTeX/KaTeX
