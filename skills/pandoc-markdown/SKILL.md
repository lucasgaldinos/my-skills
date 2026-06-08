---
name: pandoc-markdown
description: >
  Use when authoring/editing academic Pandoc Markdown (theses, articles, beamer decks,
  standalone HTML) with YAML frontmatter, `--citeproc`+`.bib` citations, LaTeX math,
  cross-refs, or Mermaid/TikZ/PlantUML diagrams via XeLaTeX/Beamer. Triggers: pandoc,
  `refs.bib`, `xelatex`, `beamer`, ABNT/CSL, Lua filters, compile debugging.
  <self-update>Loads a `self-update trigger` when: "results are not good", "the PDF is
  wrong", "the skill missed something", "fix the skill".</self-update>
argument-hint: "[target format: pdf | beamer | html] [source `.md` file] | self-update [advise-only]"
user-invocable: true
---

# Pandoc Markdown for Academic Writing

<context>

Pandoc is the authoring target for this repo's thesis, articles, and slide decks. This skill
encodes the non-obvious conventions and failure modes that make academic Pandoc output
*actually render correctly* — correct math, citations, cross-references, diagrams, and
beamer frames — rather than the common cases already in the agent's training data.

Primary outputs covered: **PDF (XeLaTeX)**, **Beamer slides (PDF)**, **standalone HTML**.
Citation stack: **`--citeproc` + BibTeX `.bib` + ABNT CSL**. Diagrams: **Mermaid**, **TikZ**,
**PlantUML** via Lua filters.

All reference files under `references/` are the *official Pandoc manual sections* — treat
them as authoritative. Load one only when the current task needs its content (see the
[References](#references) table).
</context>

## When to use this skill vs. plain markdown

<rules>

- Load this skill the moment a `.md` file has a **YAML frontmatter with `bibliography:`,
  `title:` + `author:`, `header-includes:`, `theme:` (beamer), or `reference-section-title:`**.
  Those fields only make sense under Pandoc.
- Load it when the user mentions **compiling** a `.md` — pandoc's CLI flags, engines, and
  filters are the most error-prone surface.
- Do **not** load it for plain GitHub-flavored Markdown (READMEs, issues, PR descriptions)
  unless the user explicitly asks to target Pandoc. For those, prefer `markdown-formatter`.
</rules>

## Core rules for academic Pandoc markdown

<rules>

- **Every academic document starts with a YAML frontmatter.** Minimum fields: `title`,
  `author`, `date`, `lang`, and (for citations) `bibliography`. Templates live in
  [assets/](assets/).
- **Math uses `$…$` and `$$…$$`.** This is the `tex_math_dollars` extension, enabled by
  default in `markdown`. Inline: the opening `$` must have a non-space char to its right,
  the closing `$` must have a non-space char to its left and NOT be followed by a digit —
  otherwise `$20,000 and $30,000` is parsed as math. Escape literal dollars with `\$`.
  Display math may be separated from the formula by whitespace but **no blank lines** between
  the `$$` delimiters. Source: [references/pandocs-markdown.md](references/pandocs-markdown.md).
- **Citations use `[@key]` syntax with `--citeproc`.** `[@goldberg1989]`, `[@smith2020, p. 42]`,
  `[-@smith2020]` (suppress author), `[@a; @b]` (multiple). The `.bib` file is declared in
  frontmatter (`bibliography: ./refs.bib`) — never hardcode the path in the compile command
  when the frontmatter already has it. See [references/citations.md](references/citations.md).
- **Cross-references use the same `@` prefix only with the `pandoc-crossref` filter.** Without
  that filter, use explicit `\ref{label}` inside raw LaTeX blocks for PDF output, or plain
  Markdown links (`[Figure 1](#fig:foo)`) for HTML. Do not promise cross-refs "just work" —
  they require a filter.
- **Raw LaTeX is allowed and preserved** when the output is `latex`/`pdf`/`beamer`. Wrap in
  `\begin{...}\end{...}` or use inline backslash commands. It will be **dropped silently** for
  HTML/DOCX output — do not mix raw LaTeX into a document that needs multi-format output
  without a fallback.
- **Heading levels drive structure.** For `beamer`, the *slide level* is auto-detected as the
  deepest heading followed immediately by content; override with `--slide-level=N`. For a
  thesis, level-1 headings are chapters only if the template expects it (ABNT-like templates
  do). See [references/slide-shows.md](references/slide-shows.md).
- **Language matters for hyphenation, quotes, and citeproc locale.** Always set `lang:` in
  frontmatter (`lang: pt-BR`, `lang: en-US`). XeLaTeX uses it to pick hyphenation patterns;
  citeproc uses it to localize "and"/"et al." and date formats.
- **Always use forward slashes in paths** inside the Markdown (`assets/figure.png`), even on
  Windows hosts — backslashes break on Unix builders.
</rules>

## YAML frontmatter by document type

<instructions>

Pick the matching template from `assets/` and adapt the placeholders. Do not invent fields —
unknown YAML keys are silently ignored by pandoc, which means typos produce wrong output
without errors.
</instructions>

| Document type   | Template                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Thesis / monograph (XeLaTeX PDF) | [assets/thesis-frontmatter.md](assets/thesis-frontmatter.md) |
| Research article / paper         | [assets/article-frontmatter.md](assets/article-frontmatter.md) |
| Beamer slide deck (PDF)          | [assets/beamer-frontmatter.md](assets/beamer-frontmatter.md)  |
| Pandoc defaults file (reusable compile config) | [assets/defaults-academic.yaml](assets/defaults-academic.yaml) |

<gotchas>

- **`bibliography:` must be a string or a YAML list of strings** — never bare YAML anchors.
  Multiple files: `bibliography: [./refs.bib, ./extra.bib]`.
- **`reference-section-title:`** creates the bibliography heading automatically. Without it,
  the refs list appears with no header in PDF output.
- **`link-citations: true`** makes in-text citations hyperlink to the bibliography — required
  for readable PDFs. Off by default.
- **`header-includes:`** is raw passthrough to the LaTeX preamble. A malformed entry breaks
  the whole build with a cryptic LaTeX error, not a YAML error.
- **Beamer-specific fields** (`theme`, `colortheme`, `fonttheme`, `aspectratio`) only apply
  when `-t beamer` is used. They are ignored for other outputs — safe to keep in a shared
  source file.
</gotchas>

## Compile commands

<command>

Academic PDF (thesis/article) with citations and Lua filters:

```bash
pandoc input.md \
  --from markdown \
  --to pdf \
  --pdf-engine=xelatex \
  --citeproc \
  --csl=path/to/abnt.csl \
  --lua-filter=scripts/diagram.lua \
  --resource-path=.:assets \
  -o output.pdf
```

Beamer slide deck (this repo's thesis presentation pattern):

```bash
pandoc slides.md \
  -t beamer \
  --pdf-engine=xelatex \
  --citeproc \
  --lua-filter=scripts/beamer-table-fix.lua \
  -o slides.pdf
```

Standalone HTML with math via KaTeX:

```bash
pandoc input.md \
  -s --katex \
  --citeproc \
  --toc \
  -o output.html
```

</command>

<rules>

- **`--citeproc` is required** if the document cites anything. Without it, `[@key]` is
  rendered as literal text in the output.
- **`--pdf-engine=xelatex`** is required for any document with non-ASCII text (Portuguese,
  emoji, small-caps, etc.). `pdflatex` will fail on Unicode. `lualatex` also works.
- **`--resource-path`** is a colon-separated (Unix) or semicolon-separated (Windows) list of
  directories pandoc searches for images and `\input{}`-ed files. When the source file is
  not in the repo root, always set it.
- **A defaults file ([assets/defaults-academic.yaml](assets/defaults-academic.yaml)) replaces
  all those flags** with `pandoc -d defaults-academic.yaml input.md`. Use it when the same
  command is run repeatedly. See [references/defaults-files.md](references/defaults-files.md).
</rules>

## Diagrams that render in the PDF

<instructions>

The user selected three diagram stacks: Mermaid, TikZ, PlantUML. Each has a different
integration path. Use the decision table below.
</instructions>

| Stack     | Invocation                                  | Filter / engine                                                | Best for                           |
| --------- | ------------------------------------------- | -------------------------------------------------------------- | ---------------------------------- |
| Mermaid   | fenced ` ```mermaid ` block                 | [`pandoc-ext/diagram`](https://github.com/pandoc-ext/diagram) Lua filter + `mmdc` CLI | Flowcharts, sequence, class, ER    |
| TikZ      | raw `\begin{tikzpicture}…\end{tikzpicture}` | Native XeLaTeX — no filter needed for PDF output               | Precise technical figures, math    |
| PlantUML  | fenced ` ```plantuml ` block                | Same `pandoc-ext/diagram` filter + `plantuml` CLI              | UML, component diagrams            |

See [references/diagrams-and-filters.md](references/diagrams-and-filters.md) for installation,
version constraints, and the full filter invocation pattern.

<gotchas>

- **Mermaid and PlantUML are pre-rendered to images by the filter** (PNG/SVG) and embedded;
  the raw source is not in the PDF. This means: (1) the `mmdc`/`plantuml` CLI must be on
  `PATH` at build time, (2) builds fail offline if Mermaid needs to download Chromium.
- **TikZ does NOT work in Beamer frames that use `\begin{frame}[fragile]`** without extra
  care — `[fragile]` is required for verbatim/code, but TikZ compilation inside `[fragile]`
  frames silently produces wrong output. If a slide has both code and TikZ, split into two
  frames.
- **Mermaid diagrams in Beamer are known to break** when the filter strips the block but
  doesn't render (version mismatch). Pre-render to a PNG and embed with
  `![](assets/class_diagram.png){width=80%}` — this repo's thesis presentation does exactly
  this. Documented in `scripts/beamer-table-fix.lua` comments.
- **TikZ output in HTML** requires a rasterization pipeline (`dvisvgm` or `tikz-to-svg`).
  Easier path: conditionally embed a pre-rendered SVG using raw HTML blocks with the
  `html` output format.
</gotchas>

## Known failure modes (and fixes)

<gotchas>

- **`[WARNING] Could not convert TeX math ... , rendering as TeX`** when converting
  HTML → markdown via `pandoc -f html -t gfm`. `gfm` has no native math; pandoc falls back
  to literal TeX. **Fix:** use `-t markdown` (pandoc-flavored) instead of `-t gfm`, and the
  math stays as `$…$` blocks. This was the failure in the user's `article-example.md` case.
- **HTML-to-markdown conversion produces raw HTML `<div>`/`<span>` noise.** Add
  `--wrap=none --strip-comments` and post-process. For arXiv HTML specifically, the cleanest
  route is `pandoc -f html -t markdown+smart --strip-comments input.html -o output.md` then
  manually add a YAML frontmatter. `gfm` was the wrong target for academic content.
- **Longtable breaks inside a Beamer frame.** Pandoc 3.x generates `longtable` for
  multi-row markdown tables; beamer frames can't hold a longtable. **Fix:** use the
  [scripts/beamer-table-fix.lua](scripts/beamer-table-fix.lua) filter that converts
  `longtable` → `tabular`. Pass `--lua-filter=scripts/beamer-table-fix.lua`.
- **`## Referências` loses `{.allowframebreaks}` when `reference-section-title` is set.**
  Remove `reference-section-title` from the YAML and write the heading manually with the
  attribute: `## Referências {.allowframebreaks}`.
- **`mermaid-filter` + Pandoc 3+ hides diagrams from `\listoffigures`.** `mermaid-filter` emits older Pandoc 2.x AST (`Para[Image]`) instead of a proper `Figure` node. LaTeX won't generate `\begin{figure}` environments for paragraphs. **Fix:** Use a custom lua interceptor script to convert them: `if #elem.content == 1 and elem.content[1].t == 'Image' then ... return pandoc.Figure(...)`. Reference the `scripts/fix-mermaid-figure.lua` script if available. Alternatively, migrate to `pandoc-ext/diagram` which bridges the AST correctly.
- **`mermaid-filter` diagrams squished (vertically crushed) in LaTeX.** LaTeX's default `\maxheight` constraint for images is `0.4\textheight`. Diagram images with tall aspect ratios get proportionally scaled down dramatically to fit. **Fix:** override it in the markdown header: `\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}`. For infinite scaling, formulate your blocks with `format=pdf` or `format=svg`.
- **`toc: true` + `\AtBeginSection` produces duplicate section divider slides.** Choose one;
  for beamer, prefer explicit `## Roteiro` slides over auto-generated ones.
- **Raw LaTeX in the document body is silently dropped in DOCX output.** If the document is
  multi-format, replace `\textbf{foo}` with `**foo**`, `\emph{foo}` with `*foo*`, and move
  genuinely LaTeX-only constructs into `header-includes:` macros used via Pandoc spans.
</gotchas>

## Writing conventions for academic Markdown

<rules>

- **Paragraphs separated by a blank line.** A lone newline inside a paragraph is just a
  space — do not rely on visual line breaks in the source.
- **Hard breaks:** end a line with two spaces or a backslash + newline (`escaped_line_breaks`).
  Needed inside multiline/grid table cells where trailing spaces are stripped.
- **Headings:** always leave a blank line before a heading (`blank_before_header` extension,
  on by default in `markdown`). Use ATX style (`##`) — setext style breaks on long titles.
- **Heading IDs are auto-generated** from the text (lowercased, non-alphanumerics stripped,
  spaces → hyphens). To pin a stable ID, use `## Section {#sec:intro}`. Required for any
  heading you want to cross-reference.
- **Figures with captions:** `![Caption text](path/fig.png){#fig:label width=80%}`. The
  `#fig:label` requires `pandoc-crossref`; without it, just write `\label{fig:label}` in
  raw LaTeX immediately after the image.
- **Tables:** pipe tables (`| a | b |`) for simple cases; grid tables for cell content with
  newlines. Always include a header row — pandoc cannot infer alignment otherwise.
- **Callouts / admonitions:** GitHub-style `> [!NOTE]` blocks are NOT pandoc-native. For
  PDF, use raw LaTeX environments (e.g., `\begin{tcolorbox}...\end{tcolorbox}`) defined in
  `header-includes:`. For HTML, a `<div class="note">...</div>` + CSS.
- **Footnotes:** `[^1]` inline and `[^1]: text` on its own line. Unlike citations, these
  work without any filter.
</rules>

## Workflow: starting a new academic document

<instructions>

1. **Pick the document type** — thesis, article, or beamer — and copy the matching YAML
   from `assets/`.
2. **Set the language and bibliography** in the frontmatter before writing any body.
   Forgetting this turns every citation into literal `[@key]` in the output.
3. **Write the body** following the rules above. Cite with `[@key]`, math with `$…$`,
   figures with `![caption](path){#fig:label}`.
4. **Add diagrams** per the decision table. If using Mermaid/PlantUML, verify `mmdc` or
   `plantuml` is on `PATH`: `which mmdc && which plantuml`.
5. **Compile** with one of the commands above, or with a defaults file.
6. **Read the first warning**, not the last. Pandoc emits warnings top-down, and an early
   YAML error cascades into dozens of downstream warnings.
</instructions>

<validation>

After each compile, verify:

- [ ] No `[WARNING] Could not convert TeX math` lines in stderr
- [ ] No `[WARNING] Citeproc: citation X not found` lines
- [ ] Bibliography appears in the output with the expected heading
- [ ] All figure numbers resolve (no `??` in PDF)
- [ ] Table of contents (if enabled) reflects the actual heading hierarchy
</validation>

<routing>

## References

Load only the file(s) matching the current task. All are the official Pandoc manual sections
verbatim — authoritative but long.

| File                                                                      | Load when                                                                               |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [references/pandocs-markdown.md](references/pandocs-markdown.md)          | Any question about syntax, extensions, math, tables, inline formatting                  |
| [references/citations.md](references/citations.md)                        | Configuring `.bib`, CSL, citation syntax edge cases, citeproc locale                    |
| [references/extensions.md](references/extensions.md)                      | Enabling/disabling a specific pandoc extension (`+smart`, `-raw_tex`, etc.)             |
| [references/templates.md](references/templates.md)                        | Customizing the LaTeX/HTML template, defining variables, overriding `default.latex`     |
| [references/slide-shows.md](references/slide-shows.md)                    | Beamer or reveal.js slide structure, slide levels, incremental lists                    |
| [references/defaults-files.md](references/defaults-files.md)              | Writing or debugging a `pandoc -d defaults.yaml` file                                   |
| [references/options.md](references/options.md)                            | CLI flag reference (`--from`, `--to`, `--pdf-engine`, `--lua-filter`, …)                |
| [references/syntax-highlighting.md](references/syntax-highlighting.md)    | Code block highlighting, `highlight-style`, custom KDE XML themes                       |
| [references/diagrams-and-filters.md](references/diagrams-and-filters.md)  | Installing/configuring mermaid/PlantUML/TikZ pipelines (synthesized, not official doc)  |
| [references/accessible-pdfs-and-pdf-archiving-standards.md](references/accessible-pdfs-and-pdf-archiving-standards.md) | PDF/A, tagged PDF, accessibility |
| [references/epubs.md](references/epubs.md)                                | EPUB output (not primary but supported)                                                 |
| [references/jupyter-notebooks.md](references/jupyter-notebooks.md)        | Converting to/from `.ipynb`                                                             |
| [references/reproducible-builds.md](references/reproducible-builds.md)    | Deterministic output for CI                                                             |
| [references/format-compatibility.md](references/format-compatibility.md)  | Which features survive which output formats (PDF/HTML/DOCX/EPUB cross-matrix)           |
| [references/quality-rubric.md](references/quality-rubric.md)              | Check-mode scoring sheet — items, PASS/FAIL criteria, severity                          |
| [references/self-update-examples.md](references/self-update-examples.md)  | Worked transcripts of the self-update protocol (missing bib, fatal LaTeX, dry-run)      |
| [references/check-mode.md](references/check-mode.md)                      | Full check-mode workflow + symptom→fix auto-fix catalogue                               |
| (all other files in `references/`)                                        | Rare edge cases — authors, custom readers, lua interpreter mode, web server, vimdoc     |

## Scripts bundled with this skill

<scripts>

All filters are **opt-in** — none load automatically. Pass them via `--lua-filter=…` on the
command line or list them under `lua-filters:` in a defaults file. Each file has a 4-part
header comment (purpose / invocation / limits / filter order) — read it before wiring the
filter into a pipeline.

| Script | Trigger / Condition | Mechanism / Purpose |
| --- |--- | --- |
| [scripts/beamer-table-fix.lua](scripts/beamer-table-fix.lua)| `--lua-filter beamer-table-fix.lua`| **Beamer specific.** Pandoc 3 multi-row tables generate `longtable` environments, which Beamer frames cannot natively support without crashing. Converts them to standard `tabular` so tables fit seamlessly in slide frames. |
| [scripts/fix-mermaid-figure.lua](scripts/fix-mermaid-figure.lua)| `--lua-filter fix-mermaid-figure.lua` with `--filter mermaid-filter` | **XeLaTeX diagram fix.** `mermaid-filter` emits older Pandoc 2.x `Para[Image]` nodes. This script intercepts these and upgrades them into block-level `Figure` nodes, guaranteeing that your diagrams appear natively inside `\listoffigures` and support `\ref`. |
| [scripts/abstract-to-latex.lua](scripts/abstract-to-latex.lua)| Top-level `::: {.abstract}` divs| **LaTeX specific.** Wraps content inside `\begin{abstract}…\end{abstract}`. Very useful for academic papers where Pandoc's default markdown abstract handles placement poorly.         |
| [scripts/figure-numbering.lua](scripts/figure-numbering.lua)| When `--filter pandoc-crossref` is unavailable| **Zero-dependency numbering.** Scans unlabeled images and assigns them sequential `fig:N` tags so you can do `\ref{fig:N}` without installing the heavy `pandoc-crossref` binary.|
| [scripts/strip-raw-latex-for-html.lua](scripts/strip-raw-latex-for-html.lua)| When compiling to `--to html*` or `epub*`| **HTML fallback.** LaTeX authors often use pure TeX commands like `\textbf{}`. This filter sanitizes them into pandoc semantic Markdown equivalents so styles aren't lost in HTML targets.   |
| [scripts/lang-span.lua](scripts/lang-span.lua)| Markdown spans defined as `[word]{lang=xx}` or `::: {lang=xx}`| **Polyglossia integration.** Converts the span into the LaTeX command `\foreignlanguage{xx}{word}`, ensuring correct hyphenation for mixed language terms in a document.|

</scripts>

<gotchas>

- **Beamer + `strip-raw-latex-for-html.lua` = no-op.** The filter only activates for
  `html*`/`epub*` targets; safe to leave in a shared defaults file.
- **`figure-numbering.lua` vs `pandoc-crossref`.** Do not load both — crossref already
  assigns `fig:N` identifiers. Use `figure-numbering.lua` only as a zero-dependency fallback.
- **`lang-span.lua` requires `otherlangs:` in the YAML.** The filter emits
  `\foreignlanguage{english}{…}`; that command fails at compile time if `english` was not
  registered via `otherlangs: [en-US]` (polyglossia) in the frontmatter.
</gotchas>

Diagram filters (`pandoc-ext/diagram`, `raghur/mermaid-filter`) are installed separately —
see [references/diagrams-and-filters.md](references/diagrams-and-filters.md).
</routing>

## Templates

<templates>

Copy a template from `templates/` into the document root and adapt the placeholders. Each
file is a complete, compilable starting point — frontmatter + a few body examples — not a
fragment.

| Template                                                                  | Purpose                                                                          |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [templates/minimal-thesis.md](templates/minimal-thesis.md)                | ABNT-style thesis skeleton (XeLaTeX PDF, citeproc, chapters)                     |
| [templates/minimal-article.md](templates/minimal-article.md)              | Single-file research article (XeLaTeX PDF, abstract, refs)                       |
| [templates/minimal-beamer.md](templates/minimal-beamer.md)                | Beamer slide deck skeleton matching this repo's thesis-presentation pattern      |
| [templates/standalone-html.md](templates/standalone-html.md)              | Self-contained HTML with KaTeX math + citeproc                                   |
| [templates/tikz-figure.md](templates/tikz-figure.md)                      | Inline TikZ figure block ready to drop into a XeLaTeX document                   |
| [templates/circuitikz-figure.md](templates/circuitikz-figure.md)          | CircuiTikZ schematic block (electrical/electronic diagrams)                      |
| [templates/mermaid-workaround.md](templates/mermaid-workaround.md)        | Pre-render Mermaid → PNG and embed (beamer-safe; avoids filter failure)          |
| [templates/multi-language.md](templates/multi-language.md)                | Polyglossia + `lang-span.lua` setup for mixed-language documents                 |

</templates>

## Self-update protocol

<context>

When a pandoc/LaTeX compile fails in a way that this skill's current guidance did not
prevent, the skill should offer to update itself (new rule, new gotcha, new trigger, or
new TODO row). The protocol below is *mandatory*: the agent must classify the failure,
ask the user before proposing changes, and ask again before applying them. Silent edits
to SKILL.md are forbidden.
</context>

<rules>

**Major failure — auto-propose self-update.** Any one of the following, observed while
this skill was loaded, counts as a major failure and triggers the classify→ask flow:

- pandoc process exit code ≠ 0
- `[ERROR]` (any case) present in pandoc stderr
- LaTeX log contains `Fatal error occurred, no output PDF file produced!`
- Citeproc reports one or more missing bib entries for keys cited in the source
- Output PDF exists but has zero pages (`pdfinfo` → `Pages: 0`)
</rules>

<rules>

**Minor failure — do NOT auto-trigger.** Record if the user asks, otherwise stay silent:

- `[WARNING]` lines without any `[ERROR]`
- `Underfull \hbox` / `Overfull \hbox` / `Underfull \vbox` messages
- Non-empty output PDF (`pdfinfo` → `Pages: ≥ 1`) even if it contains `??` placeholders
</rules>

<workflow>

1. **Classify.** On a major failure, quote the triggering stderr snippet and state the
   category from the major-failure list.
2. **First ask.** Call `vscode_askQuestions` with exactly these options:
   `Yes — propose patch` / `No — log to fix/TODO.md` / `No — ignore` /
   `Custom (freeform)`. One question, freeform input allowed.
3. **On `Yes`:** draft a minimal unified diff (new rule / new gotcha / new reference row /
   new TODO entry) and call `vscode_askQuestions` a second time with options
   `Apply` / `Revise` / `Cancel`. Only on `Apply` do you write to SKILL.md.
4. **On `No — log to fix/TODO.md`:** append a row to `fix/TODO.md` with today's date,
   the trigger snippet, the affected file, `declined` (or `deferred-for-review`), and a
   one-sentence rationale. Do not edit SKILL.md.
5. **On `No — ignore`:** take no action; do not log.
6. **On `Custom`:** treat the freeform text as the user's instruction. If it implies a
   patch, go to step 3; otherwise log as `custom` in `fix/TODO.md`.
7. **Advise-only mode.** When another phase/agent invokes this protocol with
   `mode=advise-only`, classify and return `{classification, category, suggested_fix,
   todo_row_draft}` as JSON. Do **not** edit SKILL.md or `fix/TODO.md` yourself.
</workflow>

<examples>

Four worked transcripts (missing bib key, LaTeX fatal, overfull-hbox-only, real
orchestrator dry-run) are kept in
[references/self-update-examples.md](references/self-update-examples.md) to keep this
file under its 500-line budget.
</examples>

<triggers>

User phrases that force a self-update evaluation even without a failing compile. When the
user says any of these verbatim (or very close), run the `<workflow>` starting at step 1
with the most recent compile output (or `N/A` if none) as the trigger snippet:

- "results are not good"
- "the PDF is wrong"
- "the skill missed something"
- "fix the skill"
</triggers>

## Mode selection

<rules>

The skill has two opt-in maintenance/QA modes. They never run automatically together; pick
based on what the user is asking to fix.

| Mode             | Activate when                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Self-update      | A compile failed in a way the skill *should have* prevented, OR the user uses a self-update trigger phrase ("fix the skill", "the skill missed something"). Edits SKILL.md / fix/TODO.md. |
| Check mode       | The compile succeeded but the user wants a quality review of the *output PDF*. Triggered only by check-mode phrases ("check the PDF", "review the output", `/pandoc-check`). Edits the document, not the skill. |
| Neither          | Default. Normal authoring/editing tasks; both modes stay dormant.                              |

</rules>

## Check mode

<context>

Check mode is an **opt-in PDF quality review**. The agent only runs it when the user
explicitly asks (see `<triggers>` below) — never automatically after a compile, never as
part of the self-update protocol. Check mode and self-update are complementary:
self-update edits the *skill*; check mode edits the *current document*. The full
scoring sheet lives in [references/quality-rubric.md](references/quality-rubric.md).
</context>

<triggers>

Run check mode only when the user says one of these (verbatim or close paraphrase):

- "check the PDF"
- "review the output"
- "did it render right"
- "run the quality check"
- explicit `/pandoc-check`
</triggers>

<workflow>

Seven steps (locate PDF → re-run with `--verbose` → load `pdf` skill + vision rubric →
classify each item PASS/FAIL/UNKNOWN → per-FAIL `vscode_askQuestions` → on `Fix: yes`
propose patch + second confirm → on `Fix: no` log to `fix/TODO.md` as `check-declined`).
Full workflow + the symptom→fix auto-fix catalogue live in
[references/check-mode.md](references/check-mode.md). No preflight wrapper —
`pandoc … --verbose` directly.
</workflow>
</auto-fix-catalogue>
