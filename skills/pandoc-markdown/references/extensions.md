:::::::::::::::::::::::::::::: {#extensions .section .level1}
# [](#extensions){.anchor aria-hidden="true"}Extensions

The behavior of some of the readers and writers can be adjusted by enabling or disabling various extensions.

An extension can be enabled by adding `+EXTENSION` to the format name and disabled by adding `-EXTENSION`. For example, [`--from markdown_strict+footnotes`](#option--from){.option} is strict Markdown with footnotes enabled, while [`--from markdown-footnotes-pipe_tables`](#option--from){.option} is pandoc's Markdown without footnotes or pipe tables.

The Markdown reader and writer make by far the most use of extensions. Extensions only used by them are therefore covered in the section [Pandoc's Markdown](#pandocs-markdown) below (see [Markdown variants](#markdown-variants) for `commonmark` and `gfm`). In the following, extensions that also work for other formats are covered.

Note that Markdown extensions added to the `ipynb` format affect Markdown cells in Jupyter notebooks (as do command-line options like [`--markdown-headings`](#option--markdown-headings){.option}).

:::: {#typography .section .level2}
## [](#typography){.anchor aria-hidden="true"}Typography

::: {#extension-smart .section .level3}
### [](#extension-smart){.anchor aria-hidden="true"}Extension: `smart` [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + beamer
      + commonmark_x
      + context
      + dokuwiki
      + latex
      + markdown
      + opml
      + textile
      + typst

      disabled by default for:
      - commonmark
      - epub
      - epub2
      - epub3
      - gfm
      - html
      - html4
      - html5
      - ipynb
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - mediawiki
      - org
      - plain
      - rst
      - twiki
      "}

Interpret straight quotes as curly quotes, `---` as em-dashes, `--` as en-dashes, and `...` as ellipses. Nonbreaking spaces are inserted after certain abbreviations, such as "Mr."

This extension can be enabled/disabled for the following formats:

input formats
:   `markdown`, `commonmark`, `latex`, `mediawiki`, `org`, `rst`, `twiki`, `html`

output formats
:   `markdown`, `latex`, `context`, `org`, `rst`

enabled by default in
:   `markdown`, `latex`, `context` (both input and output)

Note: If you are *writing* Markdown, then the `smart` extension has the reverse effect: what would have been curly quotes comes out straight.

In LaTeX, `smart` means to use the standard TeX ligatures for quotation marks (``` `` ``` and `''` for double quotes, `` ` `` and `'` for single quotes) and dashes (`--` for en-dash and `---` for em-dash). If `smart` is disabled, then in reading LaTeX pandoc will parse these characters literally. In writing LaTeX, enabling `smart` tells pandoc to use the ligatures when possible; if `smart` is disabled pandoc will use unicode quotation mark and dash characters.
:::
::::

:::::: {#headings-and-sections .section .level2}
## [](#headings-and-sections){.anchor aria-hidden="true"}Headings and sections

::: {#extension-auto_identifiers .section .level3}
### [](#extension-auto_identifiers){.anchor aria-hidden="true"}Extension: `auto_identifiers` [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + asciidoc
      + beamer
      + context
      + docx
      + html
      + html4
      + html5
      + ipynb
      + jats
      + jats_archiving
      + jats_articleauthoring
      + jats_publishing
      + latex
      + markdown
      + markdown_github
      + markdown_mmd
      + mediawiki
      + muse
      + odt
      + opml
      + org
      + rst
      + textile
      + tikiwiki
      + twiki
      + vimwiki

      disabled by default for:
      - dokuwiki
      - epub
      - epub2
      - epub3
      - markdown_phpextra
      - markdown_strict
      - plain
      "}

A heading without an explicitly specified identifier will be automatically assigned a unique identifier based on the heading text.

This extension can be enabled/disabled for the following formats:

input formats
:   `markdown`, `latex`, `rst`, `mediawiki`, `textile`

output formats
:   `markdown`, `muse`

enabled by default in
:   `markdown`, `muse`

The default algorithm used to derive the identifier from the heading text is:

-   Remove all formatting, links, etc.
-   Remove all footnotes.
-   Remove all non-alphanumeric characters, except underscores, hyphens, and periods.
-   Replace all spaces and newlines with hyphens.
-   Convert all alphabetic characters to lowercase.
-   Remove everything up to the first letter (identifiers may not begin with a number or punctuation mark).
-   If nothing is left after this, use the identifier `section`.

Thus, for example,

  Heading                         Identifier
  ------------------------------- -------------------------------
  `Heading identifiers in HTML`   `heading-identifiers-in-html`
  `Maître d'hôtel`                `maître-dhôtel`
  `*Dogs*?--in *my* house?`       `dogs--in-my-house`
  `[HTML], [S5], or [RTF]?`       `html-s5-or-rtf`
  `3. Applications`               `applications`
  `33`                            `section`

These rules should, in most cases, allow one to determine the identifier from the heading text. The exception is when several headings have the same text; in this case, the first will get an identifier as described above; the second will get the same identifier with `-1` appended; the third with `-2`; and so on.

(However, a different algorithm is used if `gfm_auto_identifiers` is enabled; see below.)

These identifiers are used to provide link targets in the table of contents generated by the [`--toc|--table-of-contents`](#option--toc%5B){.option} option. They also make it easy to provide links from one section of a document to another. A link to this section, for example, might look like this:

    See the section on
    [heading identifiers](#heading-identifiers-in-html-latex-and-context).

Note, however, that this method of providing links to sections works only in HTML, LaTeX, and ConTeXt formats.

If the [`--section-divs`](#option--section-divs%5B){.option} option is specified, then each section will be wrapped in a `section` (or a `div`, if `html4` was specified), and the identifier will be attached to the enclosing `<section>` (or `<div>`) tag rather than the heading itself. This allows entire sections to be manipulated using JavaScript or treated differently in CSS.
:::

::: {#extension-ascii_identifiers .section .level3}
### [](#extension-ascii_identifiers){.anchor aria-hidden="true"}Extension: `ascii_identifiers` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - asciidoc
      - beamer
      - commonmark
      - commonmark_x
      - context
      - docx
      - dokuwiki
      - epub
      - epub2
      - epub3
      - gfm
      - html
      - html4
      - html5
      - ipynb
      - latex
      - markdown
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - mediawiki
      - muse
      - odt
      - opml
      - org
      - plain
      - rst
      - textile
      - tikiwiki
      - twiki
      - vimwiki
      "}

Causes the identifiers produced by `auto_identifiers` to be pure ASCII. Accents are stripped off of accented Latin letters, and non-Latin letters are omitted.
:::

::: {#extension-gfm_auto_identifiers .section .level3}
### [](#extension-gfm_auto_identifiers){.anchor aria-hidden="true"}Extension: `gfm_auto_identifiers` [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + commonmark_x
      + gfm
      + ipynb
      + markdown_github

      disabled by default for:
      - asciidoc
      - beamer
      - commonmark
      - context
      - docx
      - dokuwiki
      - epub
      - epub2
      - epub3
      - html
      - html4
      - html5
      - latex
      - markdown
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - mediawiki
      - muse
      - odt
      - opml
      - org
      - plain
      - rst
      - textile
      - tikiwiki
      - twiki
      - vimwiki
      "}

Changes the algorithm used by `auto_identifiers` to conform to GitHub's method. Spaces are converted to dashes (`-`), uppercase characters to lowercase characters, and punctuation characters other than `-` and `_` are removed. Emojis are replaced by their names.
:::
::::::

::: {#math-input .section .level2}
## [](#math-input){.anchor aria-hidden="true"}Math Input

The extensions [`tex_math_dollars`](#extension-tex_math_dollars), [`tex_math_gfm`](#extension-tex_math_gfm), [`tex_math_single_backslash`](#extension-tex_math_single_backslash), and [`tex_math_double_backslash`](#extension-tex_math_double_backslash) are described in the section about Pandoc's Markdown.

However, they can also be used with HTML input. This is handy for reading web pages formatted using MathJax, for example.
:::

::: {#raw-htmltex .section .level2}
## [](#raw-htmltex){.anchor aria-hidden="true"}Raw HTML/TeX

The following extensions are described in more detail in their respective sections of [Pandoc's Markdown](#pandocs-markdown):

-   [`raw_html`](#extension-raw_html) allows HTML elements which are not representable in pandoc's AST to be parsed as raw HTML. By default, this is disabled for HTML input.

-   [`raw_tex`](#extension-raw_tex) allows raw LaTeX, TeX, and ConTeXt to be included in a document. This extension can be enabled/disabled for the following formats (in addition to `markdown`):

    input formats
    :   `latex`, `textile`, `html` (environments, `\ref`, and `\eqref` only), `ipynb`

    output formats
    :   `textile`, `commonmark`

    Note: as applied to `ipynb`, `raw_html` and `raw_tex` affect not only raw TeX in Markdown cells, but data with mime type `text/html` in output cells. Since the `ipynb` reader attempts to preserve the richest possible outputs when several options are given, you will get best results if you disable `raw_html` and `raw_tex` when converting to formats like `docx` which don't allow raw `html` or `tex`.

-   [`native_divs`](#extension-native_divs) causes HTML `div` elements to be parsed as native pandoc Div blocks. If you want them to be parsed as raw HTML, use [`-f html-native_divs+raw_html`](#option--from){.option}.

-   [`native_spans`](#extension-native_spans) causes HTML `span` elements to be parsed as native pandoc Span inlines. If you want them to be parsed as raw HTML, use [`-f html-native_spans+raw_html`](#option--from){.option}. If you want to drop all `div`s and `span`s when converting HTML to Markdown, you can use `pandoc -f html-native_divs-native_spans -t markdown`.
:::

:::: {#literate-haskell-support .section .level2}
## [](#literate-haskell-support){.anchor aria-hidden="true"}Literate Haskell support

::: {#extension-literate_haskell .section .level3}
### [](#extension-literate_haskell){.anchor aria-hidden="true"}Extension: `literate_haskell` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - beamer
      - epub
      - epub2
      - epub3
      - html
      - html4
      - html5
      - ipynb
      - latex
      - markdown
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - opml
      - plain
      - rst
      "}

Treat the document as literate Haskell source.

This extension can be enabled/disabled for the following formats:

input formats
:   `markdown`, `rst`, `latex`

output formats
:   `markdown`, `rst`, `latex`, `html`

If you append `+lhs` (or `+literate_haskell`) to one of the formats above, pandoc will treat the document as literate Haskell source. This means that

-   In Markdown input, "bird track" sections will be parsed as Haskell code rather than block quotations. Text between `\begin{code}` and `\end{code}` will also be treated as Haskell code. For ATX-style headings the character '=' will be used instead of '#'.

-   In Markdown output, code blocks with classes `haskell` and `literate` will be rendered using bird tracks, and block quotations will be indented one space, so they will not be treated as Haskell code. In addition, headings will be rendered setext-style (with underlines) rather than ATX-style (with '#' characters). (This is because ghc treats '#' characters in column 1 as introducing line numbers.)

-   In restructured text input, "bird track" sections will be parsed as Haskell code.

-   In restructured text output, code blocks with class `haskell` will be rendered using bird tracks.

-   In LaTeX input, text in `code` environments will be parsed as Haskell code.

-   In LaTeX output, code blocks with class `haskell` will be rendered inside `code` environments.

-   In HTML output, code blocks with class `haskell` will be rendered with class `literatehaskell` and bird tracks.

Examples:

    pandoc -f markdown+lhs -t html

reads literate Haskell source formatted with Markdown conventions and writes ordinary HTML (without bird tracks).

    pandoc -f markdown+lhs -t html+lhs

writes HTML with the Haskell code in bird tracks, so it can be copied and pasted as literate Haskell source.

Note that GHC expects the bird tracks in the first column, so indented literate code blocks (e.g. inside an itemized environment) will not be picked up by the Haskell compiler.
:::
::::

::::::::::::::::::: {#other-extensions .section .level2}
## [](#other-extensions){.anchor aria-hidden="true"}Other extensions

::: {#extension-empty_paragraphs .section .level3}
### [](#extension-empty_paragraphs){.anchor aria-hidden="true"}Extension: `empty_paragraphs` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - beamer
      - docx
      - epub
      - epub2
      - epub3
      - html
      - html4
      - html5
      - latex
      - odt
      - opendocument
      "}

Allows empty paragraphs. By default empty paragraphs are omitted.

This extension can be enabled/disabled for the following formats:

input formats
:   `docx`, `html`

output formats
:   `docx`, `odt`, `opendocument`, `html`, `latex`
:::

::: {#extension-native_numbering .section .level3}
### [](#extension-native_numbering){.anchor aria-hidden="true"}Extension: `native_numbering` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - docx
      - odt
      - opendocument
      "}

Enables native numbering of figures and tables. Enumeration starts at 1.

This extension can be enabled/disabled for the following formats:

output formats
:   `odt`, `opendocument`, `docx`
:::

::: {#extension-xrefs_name .section .level3}
### [](#extension-xrefs_name){.anchor aria-hidden="true"}Extension: `xrefs_name` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - odt
      - opendocument
      "}

Links to headings, figures and tables inside the document are substituted with cross-references that will use the name or caption of the referenced item. The original link text is replaced once the generated document is refreshed. This extension can be combined with `xrefs_number` in which case numbers will appear before the name.

Text in cross-references is only made consistent with the referenced item once the document has been refreshed.

This extension can be enabled/disabled for the following formats:

output formats
:   `odt`, `opendocument`
:::

::: {#extension-xrefs_number .section .level3}
### [](#extension-xrefs_number){.anchor aria-hidden="true"}Extension: `xrefs_number` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - odt
      - opendocument
      "}

Links to headings, figures and tables inside the document are substituted with cross-references that will use the number of the referenced item. The original link text is discarded. This extension can be combined with `xrefs_name` in which case the name or caption numbers will appear after the number.

For the `xrefs_number` to be useful heading numbers must be enabled in the generated document, also table and figure captions must be enabled using for example the `native_numbering` extension.

Numbers in cross-references are only visible in the final document once it has been refreshed.

This extension can be enabled/disabled for the following formats:

output formats
:   `odt`, `opendocument`
:::

::: {#ext-styles .section .level3}
### [](#ext-styles){.anchor aria-hidden="true"}Extension: `styles` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - docx
      "}

When converting from docx, add `custom-styles` attributes for all docx styles, regardless of whether pandoc understands the meanings of these styles. Because attributes cannot be added directly to paragraphs or text in the pandoc AST, paragraph styles will cause Divs to be created and character styles will cause Spans to be created to hold the attributes. (Table styles will be added to the Table elements directly.) This extension can be used with [docx custom styles](#custom-styles).

input formats
:   `docx`
:::

::: {#extension-amuse .section .level3}
### [](#extension-amuse){.anchor aria-hidden="true"}Extension: `amuse` [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + muse
      "}

In the `muse` input format, this enables Text::Amuse extensions to Emacs Muse markup.
:::

::: {#extension-raw_markdown .section .level3}
### [](#extension-raw_markdown){.anchor aria-hidden="true"}Extension: `raw_markdown` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - ipynb
      "}

In the `ipynb` input format, this causes Markdown cells to be included as raw Markdown blocks (allowing lossless round-tripping) rather than being parsed. Use this only when you are targeting `ipynb` or a Markdown-based output format.
:::

::: {#typst-citations .section .level3}
### [](#typst-citations){.anchor aria-hidden="true"}Extension: `citations` (typst) [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + markdown
      + opml
      + org
      + typst

      disabled by default for:
      - docx
      - ipynb
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - plain
      "}

When the `citations` extension is enabled in `typst` (as it is by default), `typst` citations will be parsed as native pandoc citations, and native pandoc citations will be rendered as `typst` citations.
:::

::: {#org-citations .section .level3}
### [](#org-citations){.anchor aria-hidden="true"}Extension: `citations` (org) [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + markdown
      + opml
      + org
      + typst

      disabled by default for:
      - docx
      - ipynb
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - plain
      "}

When the `citations` extension is enabled in `org`, org-cite and org-ref style citations will be parsed as native pandoc citations, and org-cite citations will be used to render native pandoc citations.
:::

::: {#docx-citations .section .level3}
### [](#docx-citations){.anchor aria-hidden="true"}Extension: `citations` (docx) [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + markdown
      + opml
      + org
      + typst

      disabled by default for:
      - docx
      - ipynb
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - plain
      "}

When `citations` is enabled in `docx`, citations inserted by Zotero or Mendeley or EndNote plugins will be parsed as native pandoc citations. (Otherwise, the formatted citations generated by the bibliographic software will be parsed as regular text.)
:::

::: {#org-fancy-lists .section .level3}
### [](#org-fancy-lists){.anchor aria-hidden="true"}Extension: `fancy_lists` (org) [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + commonmark_x
      + markdown
      + opml
      + plain

      disabled by default for:
      - commonmark
      - gfm
      - ipynb
      - markdown_github
      - markdown_mmd
      - markdown_phpextra
      - markdown_strict
      - org
      "}

Some aspects of [Pandoc's Markdown fancy lists](#extension-fancy_lists) are also accepted in `org` input, mimicking the option `org-list-allow-alphabetical` in Emacs. As in Org Mode, enabling this extension allows lowercase and uppercase alphabetical markers for ordered lists to be parsed in addition to arabic ones. Note that for Org, this does not include roman numerals or the `#` placeholder that are enabled by the extension in Pandoc's Markdown.
:::

::: {#extension-element_citations .section .level3}
### [](#extension-element_citations){.anchor aria-hidden="true"}Extension: `element_citations` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - jats
      - jats_archiving
      - jats_articleauthoring
      - jats_publishing
      "}

In the `jats` output formats, this causes reference items to be replaced with `<element-citation>` elements. These elements are not influenced by CSL styles, but all information on the item is included in tags.
:::

::: {#extension-ntb .section .level3}
### [](#extension-ntb){.anchor aria-hidden="true"}Extension: `ntb` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - context
      "}

In the `context` output format this enables the use of [Natural Tables (TABLE)](https://wiki.contextgarden.net/TABLE) instead of the default [Extreme Tables (xtables)](https://wiki.contextgarden.net/xtables). Natural tables allow more fine-grained global customization but come at a performance penalty compared to extreme tables.
:::

::: {#extension-smart_quotes-org .section .level3}
### [](#extension-smart_quotes-org){.anchor aria-hidden="true"}Extension: `smart_quotes` (org) [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - org
      "}

Interpret straight quotes as curly quotes during parsing. When *writing* Org, then the `smart_quotes` extension has the reverse effect: what would have been curly quotes comes out straight.

This extension is implied if `smart` is enabled.
:::

::: {#extension-special_strings-org .section .level3}
### [](#extension-special_strings-org){.anchor aria-hidden="true"}Extension: `special_strings` (org) [±]{.extension-checkbox aria-hidden="true" title="enabled by default for:
      + org
      "}

Interpret `---` as em-dashes, `--` as en-dashes, `\-` as shy hyphen, and `...` as ellipses.

This extension is implied if `smart` is enabled.
:::

::: {#extension--tagging .section .level3}
### [](#extension--tagging){.anchor aria-hidden="true"}Extension: `tagging` [±]{.extension-checkbox aria-hidden="true" title="disabled by default for:
      - context
      "}

Enabling this extension with `context` output will produce markup suitable for the production of tagged PDFs. This includes additional markers for paragraphs and alternative markup for emphasized text. The `emphasis-command` template variable is set if the extension is enabled.
:::
:::::::::::::::::::
::::::::::::::::::::::::::::::
