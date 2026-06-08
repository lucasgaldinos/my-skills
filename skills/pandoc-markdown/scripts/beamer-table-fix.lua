-- beamer-table-fix.lua
--
-- Purpose: Pandoc 3.x generates `longtable` for any markdown table with more than ~1 row group. Beamer frames cannot hold a longtable (the package is incompatible with frame pagination), so the resulting PDF either fails to build or silently drops the table.
--
-- This filter intercepts the raw-LaTeX `longtable` block produced by the pandoc writer and rewrites it as a plain `tabular` inside a `\begin{center}...\end{center}`.
--
-- Invocation:
--   `pandoc slides.md -t beamer --lua-filter=scripts/beamer-table-fix.lua -o slides.pdf`
--
-- Limitations:
--   * Only handles the default pandoc longtable output shape. If you customize the table template, re-check the regex.
--   * Tables that are genuinely longer than one frame will still be clipped — split them into multiple `##` slides manually.

function RawBlock(el)
  if el.format == "latex" or el.format == "tex" then
    local text = el.text
    if text:find("\\begin{longtable}", 1, true) then
      text = text:gsub("\\begin{longtable}%[?[^%]]*%]?{([^}]*)}", "\\begin{center}\\begin{tabular}{%1}")
      text = text:gsub("\\endfirsthead", "")
      text = text:gsub("\\endhead", "")
      text = text:gsub("\\endfoot", "")
      text = text:gsub("\\endlastfoot", "")
      text = text:gsub("\\end{longtable}", "\\end{tabular}\\end{center}")
      return pandoc.RawBlock(el.format, text)
    end
  end
  return nil
end
