-- abstract-to-latex.lua
--
-- Purpose: When a top-level Div has class `abstract`, emit the LaTeX
-- `abstract` environment for LaTeX/PDF/Beamer outputs. Lets authors
-- write `::: {.abstract} ... :::` in markdown without setting the
-- `abstract:` YAML field (which some templates ignore) and keeps the
-- same source portable to HTML (the Div is kept as a plain block).
--
-- Invocation (opt-in — NOT loaded by default):
--   pandoc article.md --lua-filter=../../scripts/abstract-to-latex.lua -o article.pdf
--
-- Limits:
--   * Only activates when FORMAT is a latex-family writer (latex, beamer).
--     For other formats the Div passes through unchanged (and HTML output
--     can be styled via `div.abstract { ... }` in CSS).
--   * Expects a single `abstract` Div per document (the LaTeX `abstract`
--     environment itself allows only one). Multiple Divs become multiple
--     environments — the second is silently ignored by most classes.
--   * Does not handle attributes like `{.abstract lang=en}` specially;
--     use `scripts/lang-span.lua` for language routing.
--
-- Filter order / interaction:
--   Run BEFORE citeproc (so any [@key] inside the abstract is still
--   resolved). Run AFTER other Div-rewriting filters that might strip
--   or re-class the abstract.

local function is_latex(format)
  return format == "latex" or format == "beamer"
end

function Div(el)
  if not is_latex(FORMAT) then return nil end
  if not el.classes:includes("abstract") then return nil end
  local out = {}
  table.insert(out, pandoc.RawBlock("latex", "\\begin{abstract}"))
  for _, blk in ipairs(el.content) do
    table.insert(out, blk)
  end
  table.insert(out, pandoc.RawBlock("latex", "\\end{abstract}"))
  return out
end
