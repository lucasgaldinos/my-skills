:::::::: {#description .section .level1}
# [](#description){.anchor aria-hidden="true"}Description

Pandoc is a [Haskell](https://www.haskell.org) library for converting from one markup format to another, and a command-line tool that uses this library.

Pandoc can convert between numerous markup and word processing formats, including, but not limited to, various flavors of [Markdown](https://daringfireball.net/projects/markdown/), [HTML](https://www.w3.org/html/), [LaTeX](https://www.latex-project.org/) and [Word docx](https://en.wikipedia.org/wiki/Office_Open_XML). For the full lists of input and output formats, see the [`--from`](#option--from){.option} and [`--to`](#option--to){.option} [options below](#general-options). Pandoc can also produce [PDF](https://www.adobe.com/pdf/) output: see [creating a PDF](#creating-a-pdf), below.

Pandoc's enhanced version of Markdown includes syntax for [tables](#tables), [definition lists](#definition-lists), [metadata blocks](#metadata-blocks), [footnotes](#footnotes), [citations](#citations), [math](#math), and much more. See below under [Pandoc's Markdown](#pandocs-markdown).

Pandoc has a modular design: it consists of a set of readers, which parse text in a given format and produce a native representation of the document (an *abstract syntax tree* or AST), and a set of writers, which convert this native representation into a target format. Thus, adding an input or output format requires only adding a reader or writer. Users can also run custom [pandoc filters](https://pandoc.org/filters.html) to modify the intermediate AST.

Because pandoc's intermediate representation of a document is less expressive than many of the formats it converts between, one should not expect perfect conversions between every format and every other. Pandoc attempts to preserve the structural elements of a document, but not formatting details such as margin size. And some document elements, such as complex tables, may not fit into pandoc's simple document model. While conversions from pandoc's Markdown to all formats aspire to be perfect, conversions from formats more expressive than pandoc's Markdown can be expected to be lossy.

::: {#using-pandoc .section .level2}
## [](#using-pandoc){.anchor aria-hidden="true"}Using pandoc

If no *input-files* are specified, input is read from *stdin*. Output goes to *stdout* by default. For output to a file, use the [`-o`](#option--output){.option}/[`--output`](#option--output){.option} option:

    pandoc -o output.html input.txt

By default, pandoc produces a document fragment. To produce a standalone document (e.g. a valid HTML file including `<head>` and `<body>`), use the [`-s`](#option--standalone){.option} or [`--standalone`](#option--standalone){.option} flag:

    pandoc -s -o output.html input.txt

For more information on how standalone documents are produced, see [Templates](#templates) below.

If multiple input files are given, pandoc will concatenate them all (with blank lines between them) before parsing. (Use [`--file-scope`](#option--file-scope%5B){.option} to parse files individually.)
:::

::: {#specifying-formats .section .level2}
## [](#specifying-formats){.anchor aria-hidden="true"}Specifying formats

The format of the input and output can be specified explicitly using command-line options. The input format can be specified using the [`-f/--from`](#option--from){.option} option, the output format using the [`-t/--to`](#option--to){.option} option. Thus, to convert `hello.txt` from Markdown to LaTeX, you could type:

    pandoc -f markdown -t latex hello.txt

To convert `hello.html` from HTML to Markdown:

    pandoc -f html -t markdown hello.html

Supported input and output formats are listed below under [Options](#options) (see [`-f`](#option--from){.option} for input formats and [`-t`](#option--to){.option} for output formats). You can also use `pandoc --list-input-formats` and `pandoc --list-output-formats` to print lists of supported formats.

If the input or output format is not specified explicitly, pandoc will attempt to guess it from the extensions of the filenames. Thus, for example,

    pandoc -o hello.tex hello.txt

will convert `hello.txt` from Markdown to LaTeX. If no output file is specified (so that output goes to *stdout*), or if the output file's extension is unknown, the output format will default to HTML. If no input file is specified (so that input comes from *stdin*), or if the input files' extensions are unknown, the input format will be assumed to be Markdown.
:::

::: {#character-encoding .section .level2}
## [](#character-encoding){.anchor aria-hidden="true"}Character encoding

Pandoc uses the UTF-8 character encoding for both input and output. If your local character encoding is not UTF-8, you should pipe input and output through [`iconv`](https://www.gnu.org/software/libiconv/):

    iconv -t utf-8 input.txt | pandoc | iconv -f utf-8

Note that in some output formats (such as HTML, LaTeX, ConTeXt, RTF, OPML, DocBook, and Texinfo), information about the character encoding is included in the document header, which will only be included if you use the [`-s/--standalone`](#option--standalone){.option} option.
:::

::: {#creating-a-pdf .section .level2}
## [](#creating-a-pdf){.anchor aria-hidden="true"}Creating a PDF

To produce a PDF, specify an output file with a `.pdf` extension:

    pandoc test.txt -o test.pdf

By default, pandoc will use LaTeX to create the PDF, which requires that a LaTeX engine be installed (see [`--pdf-engine`](#option--pdf-engine){.option} below). Alternatively, pandoc can use ConTeXt, roff ms, or HTML as an intermediate format. To do this, specify an output file with a `.pdf` extension, as before, but add the [`--pdf-engine`](#option--pdf-engine){.option} option or [`-t context`](#option--to){.option}, [`-t html`](#option--to){.option}, or [`-t ms`](#option--to){.option} to the command line. The tool used to generate the PDF from the intermediate format may be specified using [`--pdf-engine`](#option--pdf-engine){.option}.

You can control the PDF style using variables, depending on the intermediate format used: see [variables for LaTeX](#variables-for-latex), [variables for ConTeXt](#variables-for-context), [variables for `wkhtmltopdf`](#variables-for-wkhtmltopdf), [variables for ms](#variables-for-ms). When HTML is used as an intermediate format, the output can be styled using [`--css`](#option--css){.option}.

To debug the PDF creation, it can be useful to look at the intermediate representation: instead of [`-o test.pdf`](#option--output){.option}, use for example [`-s -o test.tex`](#option--standalone){.option} to output the generated LaTeX. You can then test it with `pdflatex test.tex`.

When using LaTeX, the following packages need to be available (they are included with all recent versions of [TeX Live](https://www.tug.org/texlive/)): [`amsfonts`](https://ctan.org/pkg/amsfonts), [`amsmath`](https://ctan.org/pkg/amsmath), [`lm`](https://ctan.org/pkg/lm), [`unicode-math`](https://ctan.org/pkg/unicode-math), [`iftex`](https://ctan.org/pkg/iftex), [`listings`](https://ctan.org/pkg/listings) (if the [`--listings`](#option--listings%5B){.option} option is used), [`fancyvrb`](https://ctan.org/pkg/fancyvrb), [`longtable`](https://ctan.org/pkg/longtable), [`booktabs`](https://ctan.org/pkg/booktabs), [`multirow`](https://ctan.org/pkg/multirow) (if the document contains a table with cells that cross multiple rows), [`graphicx`](https://ctan.org/pkg/graphicx) (if the document contains images), [`bookmark`](https://ctan.org/pkg/bookmark), [`xcolor`](https://ctan.org/pkg/xcolor), [`soul`](https://ctan.org/pkg/soul), [`geometry`](https://ctan.org/pkg/geometry) (with the `geometry` variable set), [`setspace`](https://ctan.org/pkg/setspace) (with `linestretch`), and [`babel`](https://ctan.org/pkg/babel) (with `lang`). If `CJKmainfont` is set, [`xeCJK`](https://ctan.org/pkg/xecjk) is needed if `xelatex` is used, else [`luatexja`](https://ctan.org/pkg/luatexja) is needed if `lualatex` is used. [`framed`](https://ctan.org/pkg/framed) is required if code is highlighted in a scheme that use a colored background. The use of `xelatex` or `lualatex` as the PDF engine requires [`fontspec`](https://ctan.org/pkg/fontspec). `lualatex` uses [`selnolig`](https://ctan.org/pkg/selnolig) and [`lua-ul`](https://ctan.org/pkg/lua-ul). `xelatex` uses [`bidi`](https://ctan.org/pkg/bidi) (with the `dir` variable set). If the `mathspec` variable is set, `xelatex` will use [`mathspec`](https://ctan.org/pkg/mathspec) instead of [`unicode-math`](https://ctan.org/pkg/unicode-math). The [`csquotes`](https://ctan.org/pkg/csquotes) package will be used for [typography](#typography) if the `csquotes` variable or metadata field is set to a true value. The [`natbib`](https://ctan.org/pkg/natbib), [`biblatex`](https://ctan.org/pkg/biblatex), [`bibtex`](https://ctan.org/pkg/bibtex), and [`biber`](https://ctan.org/pkg/biber) packages can optionally be used for [citation rendering](#citation-rendering). If math with `\cancel`, `\bcancel`, or `\xcancel` is used, the [`cancel`](https://ctan.org/pkg/cancel) package is needed. The following packages will be used to improve output quality if present, but pandoc does not require them to be present: [`upquote`](https://ctan.org/pkg/upquote) (for straight quotes in verbatim environments), [`microtype`](https://ctan.org/pkg/microtype) (for better spacing adjustments), [`parskip`](https://ctan.org/pkg/parskip) (for better inter-paragraph spaces), [`xurl`](https://ctan.org/pkg/xurl) (for better line breaks in URLs), and [`footnotehyper`](https://ctan.org/pkg/footnotehyper) or [`footnote`](https://ctan.org/pkg/footnote) (to allow footnotes in tables).
:::

::: {#reading-from-the-web .section .level2}
## [](#reading-from-the-web){.anchor aria-hidden="true"}Reading from the Web

Instead of an input file, an absolute URI may be given. In this case pandoc will fetch the content using HTTP:

    pandoc -f html -t markdown https://www.fsf.org

It is possible to supply a custom User-Agent string or other header when requesting a document from a URL:

    pandoc -f html -t markdown --request-header User-Agent:"Mozilla/5.0" \
      https://www.fsf.org
:::
::::::::
