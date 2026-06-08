-- strip-raw-latex-for-html.lua
--
-- Purpose: When the output format is HTML (or EPUB), replace common
-- inline raw-LaTeX commands with equivalent Pandoc inlines instead of
-- dropping them silently. Covers the three most common offenders:
-- `\textbf{...}`, `\emph{...}`/`\textit{...}`, `\texttt{...}`.
-- Solves the "multi-format silent drop" gotcha documented in SKILL.md.
--
-- Invocation (opt-in — NOT loaded by default):
--   pandoc input.md -s --lua-filter=../../scripts/strip-raw-latex-for-html.lua -o out.html
--
-- Limits:
--   * Only runs when FORMAT starts with `html` or is `epub*`. Pass-through
--     otherwise (so the filter is safe to leave in a defaults file that
--     also builds PDFs).
--   * Only maps the three command families above. Environments, math,
--     and commands with optional arguments are NOT rewritten — use
--     pandoc-native markup (`**bold**`, `*italic*`, `` `code` ``) for
--     real multi-format work.
--   * Nested commands (e.g. `\textbf{foo \emph{bar}}`) are rewritten
--     greedily; the outer match is converted first, then the rewritten
--     inline is re-scanned on the next pandoc pass — prefer Markdown.
--
-- Filter order / interaction:
--   Run AFTER other filters that emit raw LaTeX (e.g. diagram.lua for
--   TikZ). Order-independent with citeproc since citeproc does not emit
--   these commands.

local function is_web(format)
  return format:match("^html") ~= nil or format:match("^epub") ~= nil
end

-- Pattern table: LaTeX command → function that wraps matched text in
-- the appropriate pandoc Inlines list.
local mappings = {
  { pattern = "\\textbf%s*{(.-)}",  build = function(s) return pandoc.Strong(pandoc.Str(s))  end },
  { pattern = "\\emph%s*{(.-)}",    build = function(s) return pandoc.Emph(pandoc.Str(s))   end },
  { pattern = "\\textit%s*{(.-)}",  build = function(s) return pandoc.Emph(pandoc.Str(s))   end },
  { pattern = "\\texttt%s*{(.-)}",  build = function(s) return pandoc.Code(s)                end },
}

function RawInline(el)
  if not is_web(FORMAT) then return nil end
  if el.format ~= "latex" and el.format ~= "tex" then return nil end
  for _, m in ipairs(mappings) do
    local captured = el.text:match(m.pattern)
    if captured then
      return m.build(captured)
    end
  end
  return nil
end
