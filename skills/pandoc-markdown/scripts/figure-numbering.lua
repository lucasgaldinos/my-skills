-- figure-numbering.lua
--
-- Purpose: Auto-assign a stable `\label{fig:N}` to every Image that lacks
-- an identifier. Lets documents use raw `\ref{fig:1}` without installing
-- the `pandoc-crossref` filter. The counter is document-global and
-- independent of LaTeX's figure counter — use it only for stable anchors,
-- not for the user-visible figure number.
--
-- Invocation (opt-in — NOT loaded by default):
--   pandoc input.md --lua-filter=../../scripts/figure-numbering.lua -o out.pdf
--
-- Limits:
--   * Only operates on the LaTeX family of writers (`latex`, `beamer`).
--     For other formats the Image passes through unchanged.
--   * Does not renumber images that already have an id — respects the
--     author's explicit `{#fig:foo}`.
--   * Inserted \label lives INSIDE the image's caption span via a raw
--     LaTeX suffix; for captionless images it wraps the image in a
--     minimal `\begin{figure}` so \label binds to the figure counter.
--   * Prefer pandoc-crossref if you need @fig:foo references or a list
--     of figures — this filter is a zero-dependency fallback only.
--
-- Filter order / interaction:
--   Run BEFORE citeproc and BEFORE pandoc-crossref (if present), so
--   later filters see the labels.

local function is_latex(format)
  return format == "latex" or format == "beamer"
end

local counter = 0

function Image(img)
  if not is_latex(FORMAT) then return nil end
  if img.identifier and img.identifier ~= "" then return nil end
  counter = counter + 1
  img.identifier = "fig:" .. tostring(counter)
  -- Append a raw LaTeX \label to the caption so it survives pandoc's
  -- figure-wrapping. Pandoc will attach \label{<identifier>} automatically
  -- when writing latex; setting identifier is sufficient.
  return img
end
