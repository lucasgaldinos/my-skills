# Templates

Self-documenting, compile-verified pandoc templates for academic writing.

> [!note]
> The thesis/article/html templates reference `refs.bib` and `abnt.csl` by
> **relative path**. Stage your own copies next to the template (or pass
> `--resource-path`) before compiling. See each template's **Portability**
> section for exact commands.

See [../SKILL.md](../SKILL.md) for the full skill description.

| Template | Purpose |
|---|---|
| `minimal-thesis.md`   | Thesis/dissertation skeleton (report class, chapter, figure, table, citation, math). |
| `minimal-article.md`  | Short academic article (abstract, 2 sections, citations, table, math). |
| `minimal-beamer.md`   | Academic slide deck (title + 3 content frames, beamer-table-fix filter). |
| `tikz-figure.md`      | Native TikZ figure (axis + curve) inside a thesis skeleton. |
| `circuitikz-figure.md`| RC-circuit TikZ figure via circuitikz package. |
| `mermaid-workaround.md`| Pre-render Mermaid → PNG workflow (beamer-safe). |
| `multi-language.md`   | pt-BR base with English span via polyglossia. |
| `standalone-html.md`  | Standalone HTML target with KaTeX + citeproc. |
