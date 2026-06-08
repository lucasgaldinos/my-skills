-- lang-span.lua
--
-- Purpose: Map pandoc Spans and Divs that carry a `lang` attribute to
-- `\foreignlanguage{<babel_name>}{...}` in LaTeX output, so XeLaTeX +
-- polyglossia switches hyphenation rules correctly. Complements pandoc's
-- built-in behaviour, which only sets `lang` on the outermost
-- environment — this filter covers inline switches inside paragraphs.
--
-- Invocation (opt-in — NOT loaded by default):
--   pandoc multi-language.md \
--     --lua-filter=../../scripts/lang-span.lua \
--     --pdf-engine=xelatex -o out.pdf
--
-- Limits:
--   * Only rewrites for LaTeX-family writers (`latex`, `beamer`). For
--     HTML output, pandoc already emits `<span lang="...">` natively.
--   * Known BCP-47 → polyglossia name map covers the common cases
--     (`pt`, `pt-BR`, `pt-PT`, `en`, `en-US`, `en-GB`, `es`, `fr`, `de`,
--     `it`). Unknown codes fall through as the raw code — compilation
--     will fail loudly if the language is not registered via
--     `otherlangs:` in the frontmatter.
--   * Assumes polyglossia (XeLaTeX/LuaLaTeX). babel users should replace
--     `\foreignlanguage` with the babel equivalent (same name in most
--     cases but e.g. `portuges` vs `portuguese`).
--
-- Filter order / interaction:
--   Run BEFORE citeproc so that citations inside a span inherit the
--   correct locale. Order-independent with diagram.lua.

local function is_latex(format)
  return format == "latex" or format == "beamer"
end

local lang_map = {
  ["pt"]    = "portuguese", ["pt-br"] = "portuguese", ["pt-pt"] = "portuguese",
  ["en"]    = "english",    ["en-us"] = "english",    ["en-gb"] = "english",
  ["es"]    = "spanish",    ["fr"]    = "french",
  ["de"]    = "german",     ["it"]    = "italian",
}

local function resolve(code)
  if not code then return nil end
  return lang_map[code:lower()] or code:lower()
end

function Span(el)
  if not is_latex(FORMAT) then return nil end
  local lang = el.attributes.lang
  if not lang then return nil end
  local name = resolve(lang)
  local out = pandoc.List()
  out:insert(pandoc.RawInline("latex", "\\foreignlanguage{" .. name .. "}{"))
  out:extend(el.content)
  out:insert(pandoc.RawInline("latex", "}"))
  return out
end

function Div(el)
  if not is_latex(FORMAT) then return nil end
  local lang = el.attributes.lang
  if not lang then return nil end
  local name = resolve(lang)
  local out = {}
  table.insert(out, pandoc.RawBlock("latex", "\\begin{otherlanguage}{" .. name .. "}"))
  for _, blk in ipairs(el.content) do
    table.insert(out, blk)
  end
  table.insert(out, pandoc.RawBlock("latex", "\\end{otherlanguage}"))
  return out
end
