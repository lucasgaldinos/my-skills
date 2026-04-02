---
title: "LaTeX environments decision guide"
tags: [katex, latex, environments, math, markdown]
date_created: 2026-04-01
date_changed: 2026-04-01
---

# LaTeX environments decision guide

This file governs environment selection inside `$$\begin{...}\end{...}$$` display-math
blocks. Every display-math block in markdown MUST use an explicit environment — never
bare `$$expression$$`. Choose the environment based on content using this guide.

> [!IMPORTANT]
> Display math (`$$...$$`) MUST always wrap its content in `\begin{...}\end{...}`.
> Bare `$$x = y$$` is forbidden. See [math-katex-reference.md](math-katex-reference.md) for the delimiter rule.

---

## Decision flowchart

Use this outline top-to-bottom. Stop at the first match.

> [!NOTE]
> "Equation number" means the auto-label `(1)`, `(2)`, `(3)` … that KaTeX adds to numbered environments. KaTeX always produces simple sequential labels; chapter-prefix labels such as `2.1` are not available — use `\tag{2.1}` to assign one manually.

```text
──────────────────────────────────────────────────────────────────
 Single expression (one logical equation)
──────────────────────────────────────────────────────────────────
  ├─ Fits on one line:
  │   ├─ Want an equation number (N)?   → equation
  │   └─ No equation number?            → equation*
  └─ Too long for one line (split):
      ├─ Want an equation number (N)?   → split inside equation
      └─ No equation number?            → split inside equation*

──────────────────────────────────────────────────────────────────
 Multiple equations WITH column alignment (on &)
──────────────────────────────────────────────────────────────────
  ├─ Equation number on every row?      → align
  ├─ No equation numbers?               → align*
  └─ Explicit multi-column layout?      → alignat{n} or alignat*{n}

──────────────────────────────────────────────────────────────────
 Multiple equations WITHOUT alignment (just centered)
──────────────────────────────────────────────────────────────────
  ├─ Equation number on every row?      → gather
  └─ No equation numbers?               → gather*

──────────────────────────────────────────────────────────────────
 Matrix or array
──────────────────────────────────────────────────────────────────
  ├─ No delimiters?                     → matrix
  ├─ Parentheses ( )?                   → pmatrix
  ├─ Brackets [ ]?                      → bmatrix
  ├─ Braces { }?                        → Bmatrix
  ├─ Single bars | |?                   → vmatrix
  ├─ Double bars ‖ ‖?                   → Vmatrix
  ├─ General tabular (mixed cols)?      → array{colspec}
  └─ Inline-sized matrix?               → smallmatrix (inside $...$)

──────────────────────────────────────────────────────────────────
 Piecewise or conditional definition
──────────────────────────────────────────────────────────────────
  ├─ Normal size branches?              → cases
  ├─ Display-size branches?             → dcases
  └─ Brace on the right?               → rcases

──────────────────────────────────────────────────────────────────
 Nested / helper block (no own equation number)
──────────────────────────────────────────────────────────────────
  ├─ Multi-line content sharing ONE outer number?
  │   └─ Prefer: equation + aligned    (NOT: align + aligned per row)
  ├─ Centered block inside align?       → gathered
  └─ Multi-line limit subscript?        → subarray
```

> [!TIP]
> `aligned`, `gathered`, and `alignedat` are nestable helpers — they carry no
> auto-numbering themselves. Wrap them inside `equation`, `align`, or `$$...$$`.

---

## Numbering guide

Prefer **numbered** variants (`equation`, `align`, `gather`, `alignat`) by default — equations are more useful when they carry a reference label for prose citations.

Use **starred** variants (`equation*`, `align*`, `gather*`) only when you explicitly
want no numbers, such as for intermediate derivation steps or decorative examples.

### Chapter-prefixed numbering

Chapter-prefixed labels such as 2.1, 2.2 … require `\numberwithin{equation}{chapter}` from the `amsmath` LaTeX package. This is **not available in KaTeX or any markdown renderer**. KaTeX always produces simple sequential labels `(1)`, `(2)`, `(3)` — there is no way to reset or prefix the counter per chapter.

If chapter-scoped labels are essential, assign them manually with `\tag{2.1}`.

> [!WARNING]
> `\tag` rendering is inconsistent on GitHub. Chapter-tagged equations are only
> reliable in VS Code, Jupyter, or PDF output.

### Controlling per-row numbering

`\notag` suppresses the equation number on a specific row inside a numbered
environment, without adding a custom label:

```latex
$$\begin{align}
  x &= r\cos\theta \notag \\
  y &= r\sin\theta
\end{align}$$
```

`\tag{label}` assigns a custom label to a specific row, overriding the automatic
counter. Works in both starred **and** numbered environments:

```latex
$$\begin{align*}
  f(x) &= \int_0^x t^2\,dt    \tag{I.1} \\
  g(x) &= f'(x) = x^2         \tag{I.2}
\end{align*}$$
```

> [!WARNING]
> `\tag` may not render on GitHub. Use only in VS Code or Jupyter targets.
> See [math-katex-reference.md](math-katex-reference.md) §3 for GitHub limitations.

---

## Single-equation environments

### `equation`

**Purpose:** single, numbered equation — use when the equation will be cited in text.

**Syntax:**

```latex
$$\begin{equation}
  E = mc^2
\end{equation}$$
```

**When to use:** you write "as shown in equation (1)" or cross-reference it.

**When NOT to use:** throwaway equations not cited anywhere — use `equation*` instead.

**Example — energy-momentum relation:**

```latex
$$\begin{equation}
  E^2 = (pc)^2 + (m_0 c^2)^2
\end{equation}$$
```

---

### `equation*`

**Purpose:** single, unnumbered equation.

**Syntax:**

```latex
$$\begin{equation*}
  a^2 + b^2 = c^2
\end{equation*}$$
```

**When to use:** any standalone single expression that does not need a number.
This is the default choice for one-line display math.

**When NOT to use:** when you need to cite the equation by number.

**Example — quadratic formula:**

```latex
$$\begin{equation*}
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation*}$$
```

---

### `split`

**Purpose:** split one logical equation across multiple lines with alignment, nested
inside `equation` or `equation*`. The whole block shares one number (or none).

**Syntax** (nested inside `equation*`):

```latex
$$\begin{equation*}
  \begin{split}
    f(x) &= (x+1)^3 \\
         &= x^3 + 3x^2 + 3x + 1
  \end{split}
\end{equation*}$$
```

**When to use:** a single equation is too long to fit on one line, or you want to
show derivation steps that are part of one expression.

**When NOT to use:** you have multiple distinct equations — use `align*` instead.
Do not use `split` at the top level; it must always be nested.

**Example — polynomial expansion:**

```latex
$$\begin{equation}
  \begin{split}
    \mathbf{A}^{-1} &= \frac{1}{\det(\mathbf{A})} \,\text{adj}(\mathbf{A}) \\
                    &= \frac{1}{ad - bc}
                       \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
  \end{split}
\end{equation}$$
```

---

## Multi-equation alignment environments

### `align`

**Purpose:** multiple equations aligned at `&` markers, numbered per row.

**Syntax:**

```latex
$$\begin{align}
  f(x) &= x^2 + 2x + 1 \\
  g(x) &= (x+1)^2
\end{align}$$
```

**When to use:** a derivation sequence or system of equations where each line should
be numbered and columns must be aligned.

**When NOT to use:** when you don't need numbers on every row — use `align*`.
When there is only one equation — use `equation`.

**Example — Newton's equations of motion:**

```latex
$$\begin{align}
  v   &= v_0 + at \\
  x   &= x_0 + v_0 t + \tfrac{1}{2}at^2 \\
  v^2 &= v_0^2 + 2a(x - x_0)
\end{align}$$
```

**Suppress a single row's number with `\notag`:**

```latex
$$\begin{align}
  x  &= r\cos\theta \notag \\
  y  &= r\sin\theta
\end{align}$$
```

---

### `align*`

**Purpose:** same as `align` but no auto-numbering on any row.

**Syntax:**

```latex
$$\begin{align*}
  \nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
  \nabla \cdot \mathbf{B} &= 0
\end{align*}$$
```

**When to use:** multi-line derivations or systems where numbers would clutter.
This is the most common multi-line environment for prose documents.

**When NOT to use:** when you need to cite individual equation numbers.

**Example — completing the square:**

```latex
$$\begin{align*}
  x^2 + bx &= x^2 + bx + \left(\tfrac{b}{2}\right)^2 - \left(\tfrac{b}{2}\right)^2 \\
            &= \left(x + \tfrac{b}{2}\right)^2 - \tfrac{b^2}{4}
\end{align*}$$
```

---

### `aligned`

**Purpose:** alignment block nestable inside another environment or inside `$$...$$`
without producing its own display math. No auto-numbering.

**Syntax** (nested inside `equation`):

```latex
$$\begin{equation}
  \begin{aligned}
    \dot{x} &= Ax + Bu \\
    y       &= Cx + Du
  \end{aligned}
\end{equation}$$
```

**When to use:**

- Inside `equation` (or `equation*`) when a multi-line expression should share
  **one** equation number (or no number) — this is the most common use case for
  `aligned`.
- Inside one specific row of `align` when **that row alone** needs internal
  multi-line alignment across its own sub-lines.

**When NOT to use:**

- Do not use `aligned` inside `align` as a general substitute for outer alignment.
  The typical patterns are:  
  multiple aligned equations, each numbered → `align`  
  multiple aligned equations, no numbers → `align*`  
  one multi-line expression with one number → `equation` + `aligned`
- As a standalone top-level environment — must live inside math delimiters.

**Example — state-space form beside a label:**

```latex
$$\begin{equation}
  \text{State space:} \quad
  \begin{aligned}
    \dot{\mathbf{x}} &= A\mathbf{x} + B\mathbf{u} \\
    \mathbf{y}       &= C\mathbf{x}
  \end{aligned}
\end{equation}$$
```

---

### `alignat{n}`

**Purpose:** multi-column alignment with an explicit column-pair count `n`. Gives
fine-grained spacing control for structured systems (e.g., linear equation tables).

**Syntax:**

```latex
$$\begin{alignat}{2}
  2x &+ 3y &= 5 \\
   x &-  y &= 1
\end{alignat}$$
```

`n` = number of `rl` column pairs. Each pair uses two `&` separators (one before the
operator, one before the right-hand side).

**When to use:** displaying a structured system of linear equations where you want
operators and constants to align in separate columns.

**When NOT to use:** you just want equations left-aligned on `=` — use `align*`.

**Example — 3×3 linear system:**

```latex
$$\begin{alignat*}{3}
   x &+ 2y &- z &= 1 \\
  2x &-  y &+ z &= 3 \\
   x &+  y &+ z &= 6
\end{alignat*}$$
```

---

### `alignat*{n}`

**Purpose:** unnumbered version of `alignat{n}`. Identical behavior, no row numbers.

Use the same syntax as `alignat{n}` with `\begin{alignat*}{n}`.

---

## Gather environments

### `gather`

**Purpose:** multiple centered equations, each on its own line, numbered per row.
No alignment between rows.

**Syntax:**

```latex
$$\begin{gather}
  a + b = c \\
  d + e = f
\end{gather}$$
```

**When to use:** a list of independent equations that should each be numbered but
do not share a common alignment point.

**When NOT to use:** equations that should share an alignment column — use `align`.

**Example — Maxwell's equations in integral form:**

```latex
$$\begin{gather}
  \oint \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} \\
  \oint \mathbf{B} \cdot d\mathbf{A} = 0 \\
  \oint \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}
\end{gather}$$
```

---

### `gather*`

**Purpose:** multiple centered equations, unnumbered.

**When to use:** same as `gather` but you do not need to cite individual rows.

**Example — Fourier series terms:**

```latex
$$\begin{gather*}
  a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\cos(nx)\,dx \\
  b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x)\sin(nx)\,dx
\end{gather*}$$
```

---

### `gathered`

**Purpose:** nestable `gather` — centered rows, no auto-numbering, must live inside
math delimiters or another environment.

**Syntax** (nested inside `equation`):

```latex
$$\begin{equation}
  \begin{gathered}
    \nabla^2 \phi = 0 \\
    \phi\big|_{\partial\Omega} = g
  \end{gathered}
\end{equation}$$
```

**When to use:** you want multiple centered lines as part of a single numbered block,
or nested inside an `align` column alongside other content.

**When NOT to use:** as a standalone top-level environment.

---

## Matrix environments

Matrix environments go inside display math. Rows are separated by `\\`; columns by
`&`. All matrix environments have the same internal syntax — only the delimiters differ.

**Common pattern:**

```latex
$$\begin{equation*}
  \begin{pmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
  \end{pmatrix}
\end{equation*}$$
```

### `matrix`

No delimiters. Use when you supply your own delimiters with `\left(\right)`, or for
building blocks inside larger expressions.

```latex
$$\begin{equation*}
  \left[\begin{matrix} 1 & 0 \\ 0 & 1 \end{matrix}\right]
\end{equation*}$$
```

---

### `pmatrix`

Parentheses `( )`. Default choice for general matrices.

```latex
$$\begin{equation*}
  A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
\end{equation*}$$
```

---

### `bmatrix`

Brackets `[ ]`. Common for vectors in physics and for augmented matrices.

```latex
$$\begin{equation*}
  \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
\end{equation*}$$
```

---

### `Bmatrix`

Braces `{ }`. Used when braces carry semantic meaning (e.g., set notation in a display).

```latex
$$\begin{equation*}
  S = \begin{Bmatrix} 1 & 2 \\ 3 & 4 \end{Bmatrix}
\end{equation*}$$
```

---

### `vmatrix`

Single bars `| |`. Use for determinants.

```latex
$$\begin{equation*}
  \det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
\end{equation*}$$
```

---

### `Vmatrix`

Double bars `‖ ‖`. Use for norms or double-bar determinants.

```latex
$$\begin{equation*}
  \|\mathbf{A}\| = \begin{Vmatrix} a & b \\ c & d \end{Vmatrix}
\end{equation*}$$
```

---

### `smallmatrix`

Inline-sized matrix, intended for use inside `$...$` inline math or inside text-flow.
Must be wrapped in manually provided delimiters.

```latex
The matrix $\left(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\right)$ is 2×2.
```

**When NOT to use:** inside display-math `$$...$$`. Use the full matrix variants there.

---

## Case and piecewise environments

### `cases`

**Purpose:** piecewise/conditional definitions. Left brace, two columns: expression
and condition. Use `\text{...}` for the condition text.

**Syntax:**

```latex
$$\begin{equation*}
  f(x) = \begin{cases}
    x^2   & \text{if } x \geq 0 \\
    -x^2  & \text{if } x < 0
  \end{cases}
\end{equation*}$$
```

**When to use:** any piecewise function or conditional definition where normal-sized
fractions in conditions are acceptable.

**When NOT to use:** when the branch expressions contain large fractions or sums that
need display-size rendering — use `dcases`.

---

### `dcases`

**Purpose:** like `cases` but applies `\displaystyle` to both columns automatically,
so fractions and sums in branches render at display size.

```latex
$$\begin{equation*}
  g(n) = \begin{dcases}
    \dfrac{n}{2}   & \text{if } n \text{ is even} \\
    \dfrac{n+1}{2} & \text{if } n \text{ is odd}
  \end{dcases}
\end{equation*}$$
```

> [!NOTE]
> `dcases` requires the `mathtools` package in standard LaTeX. In KaTeX it is
> supported natively. Confirm support in your renderer before using.

---

### `rcases`

**Purpose:** piecewise definition with the brace on the **right** side instead of
the left. Used when labeling a group of conditions.

```latex
$$\begin{equation*}
  \begin{rcases}
    x + y  = 3 \\
    2x - y = 0
  \end{rcases}
  \implies x = 1,\; y = 2
\end{equation*}$$
```

---

## Array environment

### `array{colspec}`

**Purpose:** general tabular math layout. Requires an explicit column specification
string using the characters below.

| Specifier | Meaning |
|-----------|---------|
| `l` | left-aligned column |
| `c` | centered column |
| `r` | right-aligned column |
| `\|` | vertical rule between columns |
| `:` | dashed vertical rule (KaTeX extension) |

**Syntax:**

```latex
$$\begin{equation*}
  \begin{array}{l|cr}
    \text{Name} & \text{Count} & \text{Rate} \\
    \hline
    A & 10 & 0.5 \\
    B & 20 & 1.0
  \end{array}
\end{equation*}$$
```

**When to use:** truth tables, lookup tables, or any non-matrix tabular content that
needs mixed alignment columns or vertical rules.

**When NOT to use:** when all columns have the same alignment and no rules are needed
— use a matrix environment instead.

> [!WARNING]
> `\cline` and `\multicolumn` are **NOT supported** in KaTeX's `array`. Use `\hline`
> for full horizontal rules only. Do not attempt `\multicolumn`.

---

## Nested and special environments

### `subarray`

**Purpose:** multi-line text in subscripts or superscripts, typically for limits.
Takes a column-alignment argument (`l`, `c`, or `r`).

```latex
$$\begin{equation*}
  \sum_{\begin{subarray}{c} i=1 \\ j<i \end{subarray}}^{n} a_{ij}
\end{equation*}$$
```

**When to use:** `\underset`, `\sum`, `\int` limits that need two lines of text.

**When NOT to use:** as a standalone display environment — it must be inside a larger
expression.

---

### Nesting rules summary

| Outer environment | Can nest |
|------------------|---------|
| `equation` | `split`, `aligned`, `gathered`, `matrix`, `pmatrix`, `bmatrix`, `Bmatrix`, `vmatrix`, `Vmatrix`, `cases`, `dcases`, `rcases`, `array` |
| `equation*` | same as `equation` |
| `align` | `aligned`, `gathered`, `split` (one per row), all matrix and case environments |
| `align*` | same as `align` |
| `gather` | `aligned`, `gathered`, all matrix and case environments |
| `gather*` | same as `gather` |
| `aligned` | all matrix and case environments |
| `gathered` | all matrix and case environments |
| `split` | matrix environments only (no nested `aligned`/`gathered`) |

> [!NOTE]
> `split` inside `align` produces one row with internal line-breaks. Use `aligned`
> inside `align` when you need alignment points both inside and outside the block.

---

## Line separators

| Separator | Effect |
|-----------|--------|
| `\\` | new row (standard) |
| `\\[0.5em]` | new row with extra vertical space (KaTeX units: `em`, `pt`, `ex`, `cm`, `mm`) |
| `\cr` | same as `\\`; TeX primitive — prefer `\\` for clarity |

**Example with spacing:**

```latex
$$\begin{align*}
  f(x) &= x^2 \\[0.8em]
  g(x) &= x^3
\end{align*}$$
```

> [!NOTE]
> KaTeX supports length units `em`, `ex`, `pt`, `pc`, `in`, `cm`, `mm`, `mu`, `sp`
> inside `\\[length]`. Do not use `px` — it is not a valid TeX unit.

---

## `\tag{}` usage

`\tag{label}` places a custom label on a row instead of the automatic counter.
It works in: `align`, `align*`, `alignat`, `alignat*`, `gather`, `gather*`, `equation`.

```latex
$$\begin{align*}
  f(x) &= \int_0^x t^2\,dt \tag{I.1} \\
  g(x) &= f'(x) = x^2     \tag{I.2}
\end{align*}$$
```

**Rules:**

- Place `\tag{...}` at the end of the row, after the last `&` column and before `\\`.
- `\tag` overrides auto-numbering for that row; other rows in a numbered environment
  still receive automatic numbers.
- `\notag` suppresses the number on one row without assigning a custom tag.
- Cross-block `\gdef` macros for reusable tags are **not reliable in KaTeX** — define
  tags inline per row.

> [!WARNING]
> `\tag` rendering on GitHub is inconsistent. Prefer it only in VS Code or Jupyter
> targets. For GitHub output, use starred environments (`align*`, `gather*`) and
> refer to equations descriptively in prose.

---

## KaTeX limitations

| Feature | Status |
|---------|--------|
| `\cline` in `array` | Not supported |
| `\multicolumn` in `array` | Not supported |
| `\gdef` cross-block macros | Unreliable — avoid |
| `\tag` in `align`, `align*`, `alignat`, `gather`, `gather*` | Supported |
| `\tag` on GitHub | Inconsistent — use with caution |
| `gathered`, `aligned`, `alignedat` auto-numbering | None — must nest inside delimiters |
| `dcases` | Supported in KaTeX natively |

---

## Quick reference table

|Environment|Numbering|Alignment|Nestable|When to use|
|---|---|---|---|---|
|`equation`|yes|no|no (outer)|Single numbered equation|
|`equation*`|no|no|no (outer)|Single unnumbered equation (default choice)|
|`split`|inherits outer|yes (`&`)|yes (inside `equation`)|One equation split across lines|
|`align`|yes (per row)|yes (`&`)|no (outer)|Multiple equations, column-aligned, numbered|
|`align*`|no|yes (`&`)|no (outer)|Multiple equations, column-aligned, unnumbered|
|`aligned`|no|yes (`&`)|yes|Alignment block nested inside another env|
|`alignat{n}`|yes (per row)|yes (n col-pairs)|no (outer)|Structured multi-column system, numbered|
|`alignat*{n}`|no|yes (n col-pairs)|no (outer)|Structured multi-column system, unnumbered|
|`gather`|yes (per row)|no (centered)|no (outer)|Multiple independent equations, numbered|
|`gather*`|no|no (centered)|no (outer)|Multiple independent equations, unnumbered|
|`gathered`|no|no (centered)|yes|Centered multi-line block nested inside another env|
|`matrix`|no|via `&`|yes|Matrix without delimiters|
|`pmatrix`|no|via `&`|yes|Matrix in parentheses|
|`bmatrix`|no|via `&`|yes|Matrix in brackets|
|`Bmatrix`|no|via `&`|yes|Matrix in braces|
|`vmatrix`|no|via `&`|yes|Determinant (single bars)|
|`Vmatrix`|no|via `&`|yes|Norm or double-bar determinant|
|`smallmatrix`|no|via `&`|yes (inline)|Inline-sized matrix inside `$...$`|
|`array{spec}`|no|per column spec|yes|General tabular math, mixed column alignment|
|`cases`|no|two columns|yes|Piecewise / conditional definitions|
|`dcases`|no|two columns (display-sized)|yes|Piecewise with display-size branches|
|`rcases`|no|two columns (right brace)|yes|Piecewise with right-side brace|
|`subarray`|no|l/c/r|yes (subscripts)|Multi-line subscript/limit labels|

---

## References

- [katex-docs/docs/supported.md](katex-docs/docs/supported.md) — full list of supported KaTeX functions
- [katex-docs/docs/support_table.md](katex-docs/docs/support_table.md) — alphabetical KaTeX support table
- [math-katex-reference.md](math-katex-reference.md) — KaTeX formatting rules for this skill
