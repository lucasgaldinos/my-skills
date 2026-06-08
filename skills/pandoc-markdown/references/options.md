:::::::::: {#options .section .level1}
# [](#options){.anchor aria-hidden="true"}Options

::: {#general-options .section .level2 .options}
## [](#general-options){.anchor aria-hidden="true"}General options {.options}

[`-f`{.option-def} *FORMAT*, `-r`{.option-def} *FORMAT*, `--from=`{.option-def}*FORMAT*, `--read=`{.option-def}*FORMAT*]{#option--from .option-anchor}

:   Specify input format. *FORMAT* can be:

    ::: {#input-formats}
    -   `asciidoc` ([AsciiDoc](https://asciidoc.org/) markup)
    -   `bibtex` ([BibTeX](https://ctan.org/pkg/bibtex) bibliography)
    -   `biblatex` ([BibLaTeX](https://ctan.org/pkg/biblatex) bibliography)
    -   `bits` ([BITS](https://jats.nlm.nih.gov/extensions/bits/) XML, alias for `jats`)
    -   `commonmark` ([CommonMark](https://commonmark.org) Markdown)
    -   `commonmark_x` ([CommonMark](https://commonmark.org) Markdown with extensions)
    -   `creole` ([Creole 1.0](http://www.wikicreole.org/wiki/Creole1.0))
    -   `csljson` ([CSL JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html) bibliography)
    -   `csv` ([CSV](https://tools.ietf.org/html/rfc4180) table)
    -   `tsv` ([TSV](https://www.iana.org/assignments/media-types/text/tab-separated-values) table)
    -   `djot` ([Djot markup](https://djot.net))
    -   `docbook` ([DocBook](https://docbook.org))
    -   `docx` ([Word docx](https://en.wikipedia.org/wiki/Office_Open_XML))
    -   `dokuwiki` ([DokuWiki markup](https://www.dokuwiki.org/dokuwiki))
    -   `endnotexml` ([EndNote XML bibliography](https://support.clarivate.com/Endnote/s/article/EndNote-XML-Document-Type-Definition))
    -   `epub` ([EPUB](http://idpf.org/epub))
    -   `fb2` ([FictionBook2](http://www.fictionbook.org/index.php/Eng:XML_Schema_Fictionbook_2.1) e-book)
    -   `gfm` ([GitHub-Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)), or the deprecated and less accurate `markdown_github`; use [`markdown_github`](#markdown-variants) only if you need extensions not supported in [`gfm`](#markdown-variants).
    -   `haddock` ([Haddock markup](https://www.haskell.org/haddock/doc/html/ch03s08.html))
    -   `html` ([HTML](https://www.w3.org/html/))
    -   `ipynb` ([Jupyter notebook](https://nbformat.readthedocs.io/en/latest/))
    -   `jats` ([JATS](https://jats.nlm.nih.gov) XML)
    -   `jira` ([Jira](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all)/Confluence wiki markup)
    -   `json` (JSON version of native AST)
    -   `latex` ([LaTeX](https://www.latex-project.org/))
    -   `markdown` ([Pandoc's Markdown](#pandocs-markdown))
    -   `markdown_mmd` ([MultiMarkdown](https://fletcherpenney.net/multimarkdown/))
    -   `markdown_phpextra` ([PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/))
    -   `markdown_strict` (original unextended [Markdown](https://daringfireball.net/projects/markdown/))
    -   `mediawiki` ([MediaWiki markup](https://www.mediawiki.org/wiki/Help:Formatting))
    -   `man` ([roff man](https://man.cx/groff_man(7)))
    -   `mdoc` ([mdoc](https://mandoc.bsd.lv/man/mdoc.7.html) manual page markup)
    -   `muse` ([Muse](https://amusewiki.org/library/manual))
    -   `native` (native Haskell)
    -   `odt` ([OpenDocument text document](https://en.wikipedia.org/wiki/OpenDocument))
    -   `opml` ([OPML](https://opml.org/spec2.opml))
    -   `org` ([Emacs Org mode](https://orgmode.org))
    -   `pod` (Perl's [Plain Old Documentation](https://perldoc.perl.org/perlpod))
    -   `pptx` ([PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint))
    -   `ris` ([RIS](https://en.wikipedia.org/wiki/RIS_(file_format)) bibliography)
    -   `rtf` ([Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format))
    -   `rst` ([reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/introduction.html))
    -   `t2t` ([txt2tags](https://txt2tags.org))
    -   `textile` ([Textile](https://textile-lang.com))
    -   `tikiwiki` ([TikiWiki markup](https://doc.tiki.org/Wiki-Syntax-Text#The_Markup_Language_Wiki-Syntax))
    -   `twiki` ([TWiki markup](https://twiki.org/cgi-bin/view/TWiki/TextFormattingRules))
    -   `typst` ([typst](https://typst.app))
    -   `vimwiki` ([Vimwiki](https://vimwiki.github.io))
    -   `xlsx` ([Excel spreadsheet](https://en.wikipedia.org/wiki/Microsoft_Excel#File_formats))
    -   `xml` (XML version of native AST)
    -   the path of a custom Lua reader, see [Custom readers and writers](#custom-readers-and-writers) below
    :::

    Extensions can be individually enabled or disabled by appending `+EXTENSION` or `-EXTENSION` to the format name. See [Extensions](#extensions) below, for a list of extensions and their names. See [`--list-input-formats`](#option--list-input-formats){.option} and [`--list-extensions`](#option--list-extensions){.option}, below.

[`-t`{.option-def} *FORMAT*, `-w`{.option-def} *FORMAT*, `--to=`{.option-def}*FORMAT*, `--write=`{.option-def}*FORMAT*]{#option--to .option-anchor}

:   Specify output format. *FORMAT* can be:

    ::: {#output-formats}
    -   `ansi` (text with [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code), for terminal viewing)
    -   `asciidoc` (modern [AsciiDoc](https://asciidoc.org/) as interpreted by [AsciiDoctor](https://asciidoctor.org/))
    -   `asciidoc_legacy` ([AsciiDoc](https://asciidoc.org/) as interpreted by [`asciidoc-py`](https://github.com/asciidoc-py/asciidoc-py)).
    -   `asciidoctor` (deprecated synonym for `asciidoc`)
    -   `bbcode` [BBCode](https://www.bbcode.org/reference.php)
    -   `bbcode_fluxbb` [BBCode (FluxBB)](https://web.archive.org/web/20210623155046/https://fluxbb.org/forums/help.php#bbcode)
    -   `bbcode_phpbb` [BBCode (phpBB)](https://www.phpbb.com/community/help/bbcode)
    -   `bbcode_steam` [BBCode (Steam)](https://steamcommunity.com/comment/ForumTopic/formattinghelp)
    -   `bbcode_hubzilla` [BBCode (Hubzilla)](https://hubzilla.org/help/member/bbcode)
    -   `bbcode_xenforo` [BBCode (xenForo)](https://www.xenfocus.com/community/help/bb-codes/)
    -   `beamer` ([LaTeX beamer](https://ctan.org/pkg/beamer) slide show)
    -   `bibtex` ([BibTeX](https://ctan.org/pkg/bibtex) bibliography)
    -   `biblatex` ([BibLaTeX](https://ctan.org/pkg/biblatex) bibliography)
    -   `chunkedhtml` (zip archive of multiple linked HTML files)
    -   `commonmark` ([CommonMark](https://commonmark.org) Markdown)
    -   `commonmark_x` ([CommonMark](https://commonmark.org) Markdown with extensions)
    -   `context` ([ConTeXt](https://www.contextgarden.net/))
    -   `csljson` ([CSL JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html) bibliography)
    -   `djot` ([Djot markup](https://djot.net))
    -   `docbook` or `docbook4` ([DocBook](https://docbook.org) 4)
    -   `docbook5` (DocBook 5)
    -   `docx` ([Word docx](https://en.wikipedia.org/wiki/Office_Open_XML))
    -   `dokuwiki` ([DokuWiki markup](https://www.dokuwiki.org/dokuwiki))
    -   `epub` or `epub3` ([EPUB](http://idpf.org/epub) v3 book)
    -   `epub2` (EPUB v2)
    -   `fb2` ([FictionBook2](http://www.fictionbook.org/index.php/Eng:XML_Schema_Fictionbook_2.1) e-book)
    -   `gfm` ([GitHub-Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)), or the deprecated and less accurate `markdown_github`; use [`markdown_github`](#markdown-variants) only if you need extensions not supported in [`gfm`](#markdown-variants).
    -   `haddock` ([Haddock markup](https://www.haskell.org/haddock/doc/html/ch03s08.html))
    -   `html` or `html5` ([HTML](https://www.w3.org/html/), i.e. [HTML5](https://html.spec.whatwg.org/)/XHTML [polyglot markup](https://www.w3.org/TR/html-polyglot/))
    -   `html4` ([XHTML](https://www.w3.org/TR/xhtml1/) 1.0 Transitional)
    -   `icml` ([InDesign ICML](https://web.archive.org/web/20211006210211/https://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/idml/idml-cookbook.pdf))
    -   `ipynb` ([Jupyter notebook](https://nbformat.readthedocs.io/en/latest/))
    -   `jats_archiving` ([JATS](https://jats.nlm.nih.gov) XML, Archiving and Interchange Tag Set)
    -   `jats_articleauthoring` ([JATS](https://jats.nlm.nih.gov) XML, Article Authoring Tag Set)
    -   `jats_publishing` ([JATS](https://jats.nlm.nih.gov) XML, Journal Publishing Tag Set)
    -   `jats` (alias for `jats_archiving`)
    -   `jira` ([Jira](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all)/Confluence wiki markup)
    -   `json` (JSON version of native AST)
    -   `latex` ([LaTeX](https://www.latex-project.org/))
    -   `man` ([roff man](https://man.cx/groff_man(7)))
    -   `markdown` ([Pandoc's Markdown](#pandocs-markdown))
    -   `markdown_mmd` ([MultiMarkdown](https://fletcherpenney.net/multimarkdown/))
    -   `markdown_phpextra` ([PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/))
    -   `markdown_strict` (original unextended [Markdown](https://daringfireball.net/projects/markdown/))
    -   `markua` ([Markua](https://leanpub.com/markua/read))
    -   `mediawiki` ([MediaWiki markup](https://www.mediawiki.org/wiki/Help:Formatting))
    -   `ms` ([roff ms](https://man.cx/groff_ms(7)))
    -   `muse` ([Muse](https://amusewiki.org/library/manual))
    -   `native` (native Haskell)
    -   `odt` ([OpenDocument text document](https://en.wikipedia.org/wiki/OpenDocument))
    -   `opml` ([OPML](https://opml.org/spec2.opml))
    -   `opendocument` ([OpenDocument XML](https://www.oasis-open.org/2021/06/16/opendocument-v1-3-oasis-standard-published/))
    -   `org` ([Emacs Org mode](https://orgmode.org))
    -   `pdf` ([PDF](https://www.adobe.com/pdf/))
    -   `plain` (plain text)
    -   `pptx` ([PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) slide show)
    -   `rst` ([reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/introduction.html))
    -   `rtf` ([Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format))
    -   `texinfo` ([GNU Texinfo](https://www.gnu.org/software/texinfo/))
    -   `textile` ([Textile](https://textile-lang.com))
    -   `slideous` ([Slideous](https://goessner.net/articles/slideous/) HTML and JavaScript slide show)
    -   `slidy` ([Slidy](https://www.w3.org/Talks/Tools/Slidy2/) HTML and JavaScript slide show)
    -   `dzslides` ([DZSlides](https://paulrouget.com/dzslides/) HTML5 + JavaScript slide show)
    -   `revealjs` ([reveal.js](https://revealjs.com/) HTML5 + JavaScript slide show)
    -   `s5` ([S5](https://meyerweb.com/eric/tools/s5/) HTML and JavaScript slide show)
    -   `tei` ([TEI Simple](https://github.com/TEIC/TEI-Simple))
    -   `typst` ([typst](https://typst.app))
    -   `vimdoc` ([Vimdoc](https://vimhelp.org/helphelp.txt.html#help-writing))
    -   `xml` (XML version of native AST)
    -   `xwiki` ([XWiki markup](https://www.xwiki.org/xwiki/bin/view/Documentation/UserGuide/Features/XWikiSyntax/))
    -   `zimwiki` ([ZimWiki markup](https://zim-wiki.org/manual/Help/Wiki_Syntax.html))
    -   the path of a custom Lua writer, see [Custom readers and writers](#custom-readers-and-writers) below
    :::

    Note that `odt`, `docx`, `epub`, and `pdf` output will not be directed to *stdout* unless forced with [`-o -`](#option--output){.option}.

    Extensions can be individually enabled or disabled by appending `+EXTENSION` or `-EXTENSION` to the format name. See [Extensions](#extensions) below, for a list of extensions and their names. See [`--list-output-formats`](#option--list-output-formats){.option} and [`--list-extensions`](#option--list-extensions){.option}, below.

[`-o`{.option-def} *FILE*, `--output=`{.option-def}*FILE*]{#option--output .option-anchor}

:   Write output to *FILE* instead of *stdout*. If *FILE* is `-`, output will go to *stdout*, even if a non-textual format (`docx`, `odt`, `epub2`, `epub3`) is specified. If the output format is `chunkedhtml` and *FILE* has no extension, then instead of producing a `.zip` file pandoc will create a directory *FILE* and unpack the zip archive there (unless *FILE* already exists, in which case an error will be raised).

[`--data-dir=`{.option-def}*DIRECTORY*]{#option--data-dir .option-anchor}

:   Specify the user data directory to search for pandoc data files. If this option is not specified, the default user data directory will be used. On \*nix and macOS systems this will be the `pandoc` subdirectory of the XDG data directory (by default, `$HOME/.local/share`, overridable by setting the `XDG_DATA_HOME` environment variable). If that directory does not exist and `$HOME/.pandoc` exists, it will be used (for backwards compatibility). On Windows the default user data directory is `%APPDATA%\pandoc`. You can find the default user data directory on your system by looking at the output of `pandoc --version`. Data files placed in this directory (for example, `reference.odt`, `reference.docx`, `epub.css`, `templates`) will override pandoc's normal defaults. (Note that the user data directory is not created by pandoc, so you will need to create it yourself if you want to make use of it.)

[`-d`{.option-def} *FILE*, `--defaults=`{.option-def}*FILE*]{#option--defaults .option-anchor}

:   Specify a set of default option settings. *FILE* is a YAML or JSON file whose fields correspond to command-line option settings. All options for document conversion, including input and output files, can be set using a defaults file. The file will be searched for first in the working directory, and then in the `defaults` subdirectory of the user data directory (see [`--data-dir`](#option--data-dir){.option}). The `.yaml` extension will be added if *FILE* lacs an extension. See the section [Defaults files](#defaults-files) for more information on the file format. Settings from the defaults file may be overridden or extended by subsequent options on the command line.

[`--bash-completion`{.option-def}]{#option--bash-completion .option-anchor}

:   Generate a bash completion script. To enable bash completion with pandoc, add this to your `.bashrc`:

        eval "$(pandoc --bash-completion)"

[`--verbose`{.option-def}]{#option--verbose .option-anchor}

:   Give verbose debugging output.

[`--quiet`{.option-def}]{#option--quiet .option-anchor}

:   Suppress warning messages.

[`--fail-if-warnings[=true|false]`{.option-def}]{#option--fail-if-warnings[ .option-anchor}

:   Exit with error status if there are any warnings.

[`--log=`{.option-def}*FILE*]{#option--log .option-anchor}

:   Write log messages in machine-readable JSON format to *FILE*. All messages above DEBUG level will be written, regardless of verbosity settings ([`--verbose`](#option--verbose){.option}, [`--quiet`](#option--quiet){.option}).

[`--list-input-formats`{.option-def}]{#option--list-input-formats .option-anchor}

:   List supported input formats, one per line.

[`--list-output-formats`{.option-def}]{#option--list-output-formats .option-anchor}

:   List supported output formats, one per line.

[`--list-extensions`{.option-def}\[`=`*FORMAT*\]]{#option--list-extensions .option-anchor}

:   List supported extensions for *FORMAT*, one per line, preceded by a `+` or `-` indicating whether it is enabled by default in *FORMAT*. If *FORMAT* is not specified, defaults for pandoc's Markdown are given.

[`--list-highlight-languages`{.option-def}]{#option--list-highlight-languages .option-anchor}

:   List supported languages for syntax highlighting, one per line.

[`--list-highlight-styles`{.option-def}]{#option--list-highlight-styles .option-anchor}

:   List supported styles for syntax highlighting, one per line. See [`--syntax-highlighting`](#option--syntax-highlighting){.option}.

[`-v`{.option-def}, `--version`{.option-def}]{#option--version .option-anchor}

:   Print version.

[`-h`{.option-def}, `--help`{.option-def}]{#option--help .option-anchor}

:   Show usage message.
:::

::: {#reader-options .section .level2 .options}
## [](#reader-options){.anchor aria-hidden="true"}Reader options {.options}

[`--shift-heading-level-by=`{.option-def}*NUMBER*]{#option--shift-heading-level-by .option-anchor}

:   Shift heading levels by a positive or negative integer. For example, with [`--shift-heading-level-by=-1`](#option--shift-heading-level-by){.option}, level 2 headings become level 1 headings, and level 3 headings become level 2 headings. Headings cannot have a level less than 1, so a heading that would be shifted below level 1 becomes a regular paragraph. Exception: with a shift of -N, a level-N heading at the beginning of the document replaces the metadata title. [`--shift-heading-level-by=-1`](#option--shift-heading-level-by){.option} is a good choice when converting HTML or Markdown documents that use an initial level-1 heading for the document title and level-2+ headings for sections. [`--shift-heading-level-by=1`](#option--shift-heading-level-by){.option} may be a good choice for converting Markdown documents that use level-1 headings for sections to HTML, since pandoc uses a level-1 heading to render the document title.

[`--base-header-level=`{.option-def}*NUMBER*]{#option--base-header-level .option-anchor}

:   *Deprecated. Use [`--shift-heading-level-by`](#option--shift-heading-level-by){.option}=X instead, where X = NUMBER - 1.* Specify the base level for headings (defaults to 1).

[`--indented-code-classes=`{.option-def}*CLASSES*]{#option--indented-code-classes .option-anchor}

:   Specify classes to use for indented code blocks---for example, `perl,numberLines` or `haskell`. Multiple classes may be separated by spaces or commas.

[`--default-image-extension=`{.option-def}*EXTENSION*]{#option--default-image-extension .option-anchor}

:   Specify a default extension to use when image paths/URLs have no extension. This allows you to use the same source for formats that require different kinds of images. Currently this option only affects the Markdown and LaTeX readers.

[`--file-scope[=true|false]`{.option-def}]{#option--file-scope[ .option-anchor}

:   Parse each file individually before combining for multifile documents. This will allow footnotes in different files with the same identifiers to work as expected. If this option is set, footnotes and links will not work across files. Reading binary files (docx, odt, epub) implies [`--file-scope`](#option--file-scope%5B){.option}.

    If two or more files are processed using [`--file-scope`](#option--file-scope%5B){.option}, prefixes based on the filenames will be added to identifiers in order to disambiguate them, and internal links will be adjusted accordingly. For example, a header with identifier `foo` in `subdir/file1.txt` will have its identifier changed to `subdir__file1.txt__foo`.

[`-F`{.option-def} *PROGRAM*, `--filter=`{.option-def}*PROGRAM*]{#option--filter .option-anchor}

:   Specify an executable to be used as a filter transforming the pandoc AST after the input is parsed and before the output is written. The executable should read JSON from stdin and write JSON to stdout. The JSON must be formatted like pandoc's own JSON input and output. The name of the output format will be passed to the filter as the first argument. Hence,

        pandoc --filter ./caps.py -t latex

    is equivalent to

        pandoc -t json | ./caps.py latex | pandoc -f json -t latex

    The latter form may be useful for debugging filters.

    Filters may be written in any language. `Text.Pandoc.JSON` exports `toJSONFilter` to facilitate writing filters in Haskell. Those who would prefer to write filters in python can use the module [`pandocfilters`](https://github.com/jgm/pandocfilters), installable from PyPI. There are also pandoc filter libraries in [PHP](https://github.com/vinai/pandocfilters-php), [perl](https://metacpan.org/pod/Pandoc::Filter), and [JavaScript/node.js](https://github.com/mvhenderson/pandoc-filter-node).

    In order of preference, pandoc will look for filters in

    1.  a specified full or relative path (executable or non-executable),

    2.  `$DATADIR/filters` (executable or non-executable) where `$DATADIR` is the user data directory (see [`--data-dir`](#option--data-dir){.option}, above),

    3.  `$PATH` (executable only).

    Filters, Lua-filters, and citeproc processing are applied in the order specified on the command line.

[`-L`{.option-def} *SCRIPT*, `--lua-filter=`{.option-def}*SCRIPT*]{#option--lua-filter .option-anchor}

:   Transform the document in a similar fashion as JSON filters (see [`--filter`](#option--filter){.option}), but use pandoc's built-in Lua filtering system. The given Lua script is expected to return a list of Lua filters which will be applied in order. Each Lua filter must contain element-transforming functions indexed by the name of the AST element on which the filter function should be applied.

    The `pandoc` Lua module provides helper functions for element creation. It is always loaded into the script's Lua environment.

    See the [Lua filters documentation](https://pandoc.org/lua-filters.html) for further details.

    In order of preference, pandoc will look for Lua filters in

    1.  a specified full or relative path,

    2.  `$DATADIR/filters` where `$DATADIR` is the user data directory (see [`--data-dir`](#option--data-dir){.option}, above).

    Filters, Lua filters, and citeproc processing are applied in the order specified on the command line.

[`-M`{.option-def} *KEY*\[`=`*VAL*\], `--metadata=`{.option-def}*KEY*\[`:`*VAL*\]]{#option--metadata .option-anchor}

:   Set the metadata field *KEY* to the value *VAL*. A value specified on the command line overrides a value specified in the document using [YAML metadata blocks](#extension-yaml_metadata_block). Values will be parsed as YAML boolean or string values. If no value is specified, the value will be treated as Boolean true. Like [`--variable`](#option--variable){.option}, [`--metadata`](#option--metadata){.option} causes template variables to be set. But unlike [`--variable`](#option--variable){.option}, [`--metadata`](#option--metadata){.option} affects the metadata of the underlying document (which is accessible from filters and may be printed in some output formats) and metadata values will be escaped when inserted into the template.

[`--metadata-file=`{.option-def}*FILE*]{#option--metadata-file .option-anchor}

:   Read metadata from the supplied YAML (or JSON) file. This option can be used with every input format, but string scalars in the metadata file will always be parsed as Markdown. (If the input format is Markdown or a Markdown variant, then the same variant will be used to parse the metadata file; if it is a non-Markdown format, pandoc's default Markdown extensions will be used.) This option can be used repeatedly to include multiple metadata files; values in files specified later on the command line will be preferred over those specified in earlier files. Metadata values specified inside the document, or by using [`-M`](#option--metadata){.option}, overwrite values specified with this option. The file will be searched for first in the working directory, and then in the `metadata` subdirectory of the user data directory (see [`--data-dir`](#option--data-dir){.option}).

[`-p`{.option-def}, `--preserve-tabs[=true|false]`{.option-def}]{#option--preserve-tabs[ .option-anchor}

:   Preserve tabs instead of converting them to spaces. (By default, pandoc converts tabs to spaces before parsing its input.) Note that this will only affect tabs in literal code spans and code blocks. Tabs in regular text are always treated as spaces.

[`--tab-stop=`{.option-def}*NUMBER*]{#option--tab-stop .option-anchor}

:   Specify the number of spaces per tab (default is 4).

[`--track-changes=accept`{.option-def}\|`reject`\|`all`]{#option--track-changes .option-anchor}

:   Specifies what to do with insertions, deletions, and comments produced by the MS Word "Track Changes" feature. `accept` (the default) processes all the insertions and deletions. `reject` ignores them. Both `accept` and `reject` ignore comments. `all` includes all insertions, deletions, and comments, wrapped in spans with `insertion`, `deletion`, `comment-start`, and `comment-end` classes, respectively. The author and time of change is included. `all` is useful for scripting: only accepting changes from a certain reviewer, say, or before a certain date. If a paragraph is inserted or deleted, `track-changes=all` produces a span with the class `paragraph-insertion`/`paragraph-deletion` before the affected paragraph break. This option only affects the docx reader.

[`--extract-media=`{.option-def}*DIR*\|*FILE*`.zip`]{#option--extract-media .option-anchor}

:   Extract images and other media contained in or linked from the source document to the path *DIR*, creating it if necessary, and adjust the images references in the document so they point to the extracted files. Media are downloaded, read from the file system, or extracted from a binary container (e.g. docx), as needed. The original file paths are used if they are relative paths not containing `..`. Otherwise filenames are constructed from the SHA1 hash of the contents.

    If the path given ends in `.zip`, then instead of creating a directory, pandoc will create a zip archive containing the media files.

[`--abbreviations=`{.option-def}*FILE*]{#option--abbreviations .option-anchor}

:   Specifies a custom abbreviations file, with abbreviations one to a line. If this option is not specified, pandoc will read the data file `abbreviations` from the user data directory or fall back on a system default. To see the system default, use `pandoc --print-default-data-file=abbreviations`. The only use pandoc makes of this list is in the Markdown reader. Strings found in this list will be followed by a nonbreaking space, and the period will not produce sentence-ending space in formats like LaTeX. The strings may not contain spaces.

[`--trace[=true|false]`{.option-def}]{#option--trace[ .option-anchor}

:   Print diagnostic output tracing parser progress to stderr. This option is intended for use by developers in diagnosing performance issues.
:::

::: {#general-writer-options .section .level2 .options}
## [](#general-writer-options){.anchor aria-hidden="true"}General writer options {.options}

[`-s`{.option-def}, `--standalone`{.option-def}]{#option--standalone .option-anchor}

:   Produce output with an appropriate header and footer (e.g. a standalone HTML, LaTeX, TEI, or RTF file, not a fragment). This option is set automatically for `pdf`, `epub`, `epub3`, `fb2`, `docx`, and `odt` output. For `native` output, this option causes metadata to be included; otherwise, metadata is suppressed.

[`--template=`{.option-def}*FILE*\|*URL*]{#option--template .option-anchor}

:   Use the specified file as a custom template for the generated document. Implies [`--standalone`](#option--standalone){.option}. See [Templates](#templates), below, for a description of template syntax. If the template is not found, pandoc will search for it in the `templates` subdirectory of the user data directory (see [`--data-dir`](#option--data-dir){.option}). If no extension is specified and an extensionless template is not found, pandoc will look for a template with an extension corresponding to the writer, so that [`--template=special`](#option--template){.option} looks for `special.html` for HTML output. If this option is not used, a default template appropriate for the output format will be used (see [`-D/--print-default-template`](#option--print-default-template){.option}).

[`-V`{.option-def} *KEY*\[`=`*VAL*\], `--variable=`{.option-def}*KEY*\[`=`*VAL*\]]{#option--variable .option-anchor}

:   Set the template variable *KEY* to the string value *VAL* when rendering the document in standalone mode. Either `:` or `=` may be used to separate *KEY* from *VAL*. If no *VAL* is specified, the key will be given the value `true`. Structured values (lists, maps) cannot be assigned using this option, but they can be assigned in the `variables` section of a [defaults file](#defaults-files) or using the [`--variable-json`](#option--variable-json){.option} option. If the variable already has a *list* value, the value will be added to the list. If it already has another kind of value, it will be made into a list containing the previous and the new value. For example, [`-V keyword=Joe -V author=Sue`](#option--variable){.option} makes `author` contain a list of strings: `Joe` and `Sue`.

[`--variable-json=`{.option-def}*KEY*\[`=`:*JSON*\]]{#option--variable-json .option-anchor}

:   Set the template variable *KEY* to the value specified by a JSON string (this may be a boolean, a string, a list, or a mapping; a number will be treated as a string). For example, [`--variable-json foo=false`](#option--variable-json){.option} will give `foo` the boolean false value, while [`--variable-json foo='"false"'`](#option--variable-json){.option} will give it the string value `"false"`. Either `:` or `=` may be used to separate *KEY* from *VAL*. If the variable already has a value, this value will be replaced.

[`--sandbox[=true|false]`{.option-def}]{#option--sandbox[ .option-anchor}

:   Run pandoc in a sandbox, limiting IO operations in readers and writers to reading the files specified on the command line. Note that this option does not limit IO operations by filters or in the production of PDF documents. But it does offer security against, for example, disclosure of files through the use of `include` directives. Anyone using pandoc on untrusted user input should use this option.

    Note: some readers and writers (e.g., `docx`) need access to data files. If these are stored on the file system, then pandoc will not be able to find them when run in [`--sandbox`](#option--sandbox%5B){.option} mode and will raise an error. For these applications, we recommend using a pandoc binary compiled with the `embed_data_files` option, which causes the data files to be baked into the binary instead of being stored on the file system.

[`-D`{.option-def} *FORMAT*, `--print-default-template=`{.option-def}*FORMAT*]{#option--print-default-template .option-anchor}

:   Print the system default template for an output *FORMAT*. (See [`-t`](#option--to){.option} for a list of possible *FORMAT*s.) Templates in the user data directory are ignored. This option may be used with [`-o`](#option--output){.option}/[`--output`](#option--output){.option} to redirect output to a file, but [`-o`](#option--output){.option}/[`--output`](#option--output){.option} must come before [`--print-default-template`](#option--print-default-template){.option} on the command line.

    Note that some of the default templates use partials, for example `styles.html`. To print the partials, use [`--print-default-data-file`](#option--print-default-data-file){.option}: for example, [`--print-default-data-file=templates/styles.html`](#option--print-default-data-file){.option}.

[`--print-default-data-file=`{.option-def}*FILE*]{#option--print-default-data-file .option-anchor}

:   Print a system default data file. Files in the user data directory are ignored. This option may be used with [`-o`](#option--output){.option}/[`--output`](#option--output){.option} to redirect output to a file, but [`-o`](#option--output){.option}/[`--output`](#option--output){.option} must come before [`--print-default-data-file`](#option--print-default-data-file){.option} on the command line.

[`--eol=crlf`{.option-def}\|`lf`\|`native`]{#option--eol .option-anchor}

:   Manually specify line endings: `crlf` (Windows), `lf` (macOS/Linux/UNIX), or `native` (line endings appropriate to the OS on which pandoc is being run). The default is `native`.

[`--dpi`{.option-def}=*NUMBER*]{#option--dpi .option-anchor}

:   Specify the default dpi (dots per inch) value for conversion from pixels to inch/centimeters and vice versa. (Technically, the correct term would be ppi: pixels per inch.) The default is 96dpi. When images contain information about dpi internally, the encoded value is used instead of the default specified by this option.

[`--wrap=auto`{.option-def}\|`none`\|`preserve`]{#option--wrap .option-anchor}

:   Determine how text is wrapped in the output (the source code, not the rendered version). With `auto` (the default), pandoc will attempt to wrap lines to the column width specified by [`--columns`](#option--columns){.option} (default 72). With `none`, pandoc will not wrap lines at all. With `preserve`, pandoc will attempt to preserve the wrapping from the source document (that is, where there are nonsemantic newlines in the source, there will be nonsemantic newlines in the output as well). In `ipynb` output, this option affects wrapping of the contents of Markdown cells.

[`--columns=`{.option-def}*NUMBER*]{#option--columns .option-anchor}

:   Specify length of lines in characters. This affects text wrapping in the generated source code (see [`--wrap`](#option--wrap){.option}). It also affects calculation of column widths for plain text tables (see [Tables](#tables) below).

[`--toc[=true|false]`{.option-def}, `--table-of-contents[=true|false]`{.option-def}]{#option--toc[ .option-anchor}

:   Include an automatically generated table of contents (or, in the case of `latex`, `context`, `docx`, `odt`, `opendocument`, `rst`, or `ms`, an instruction to create one) in the output document. This option has no effect unless [`-s/--standalone`](#option--standalone){.option} is used, and it has no effect on `man`, `docbook4`, `docbook5`, or `jats` output.

    Note that if you are producing a PDF via `ms` and using (the default) `pdfroff` as a [`--pdf-engine`](#option--pdf-engine){.option}, the table of contents will appear at the beginning of the document, before the title. If you would prefer it to be at the end of the document, use the option [`--pdf-engine-opt=--no-toc-relocation`](#option--pdf-engine-opt){.option}. If `groff` is used as the [`--pdf-engine`](#option--pdf-engine){.option}, the table of contents will always appear at the end of the document.

[`--toc-depth=`{.option-def}*NUMBER*]{#option--toc-depth .option-anchor}

:   Specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents).

[`--lof[=true|false]`{.option-def}, `--list-of-figures[=true|false]`{.option-def}]{#option--lof[ .option-anchor}

:   Include an automatically generated list of figures (or, in some formats, an instruction to create one) in the output document. This option has no effect unless [`-s/--standalone`](#option--standalone){.option} is used, and it only has an effect on `latex`, `context`, and `docx` output.

[`--lot[=true|false]`{.option-def}, `--list-of-tables[=true|false]`{.option-def}]{#option--lot[ .option-anchor}

:   Include an automatically generated list of tables (or, in some formats, an instruction to create one) in the output document. This option has no effect unless [`-s/--standalone`](#option--standalone){.option} is used, and it only has an effect on `latex`, `context`, and `docx` output.

[`--strip-comments[=true|false]`{.option-def}]{#option--strip-comments[ .option-anchor}

:   Strip out HTML comments in the Markdown or Textile source, rather than passing them on to Markdown, Textile or HTML output as raw HTML. This does not apply to HTML comments inside raw HTML blocks when the `markdown_in_html_blocks` extension is not set.

[`--syntax-highlighting=default|none|idiomatic|`{.option-def}*STYLE*`|`*FILE*]{#option--syntax-highlighting .option-anchor}

:   The method to use for code syntax highlighting. Setting a specific *STYLE* causes highlighting to be performed with the internal highlighting engine, using KDE syntax definitions and styles. The `idiomatic` method uses a format-specific highlighter if one is available, or the default style if the target format has no idiomatic highlighting method. Setting this option to `none` disables all syntax highlighting. The `default` method uses a format-specific default.

    The default for HTML, EPUB, Docx, Ms, Man, and LaTeX output is to use the internal highlighter with the default style; for Typst it is to use Typst's own syntax highlighting system.

    Style options are `pygments` (the default), `kate`, `monochrome`, `breezeDark`, `espresso`, `zenburn`, `haddock`, and `tango`. For more information on syntax highlighting in pandoc, see [Syntax highlighting](#syntax-highlighting), below. See also [`--list-highlight-styles`](#option--list-highlight-styles){.option}.

    Instead of a *STYLE* name, a JSON file with extension `.theme` may be supplied. This will be parsed as a KDE syntax highlighting theme and (if valid) used as the highlighting style.

    To generate the JSON version of an existing style, use [`--print-highlight-style`](#option--print-highlight-style){.option}.

[`--no-highlight`{.option-def}]{#option--no-highlight .option-anchor}

:   *Deprecated, use [`--syntax-highlighting=none`](#option--syntax-highlighting){.option} instead.*

    Disables syntax highlighting for code blocks and inlines, even when a language attribute is given.

[`--highlight-style=`{.option-def}*STYLE*\|*FILE*]{#option--highlight-style .option-anchor}

:   *Deprecated, use [`--syntax-highlighting=`](#option--syntax-highlighting){.option}*STYLE*\|*FILE* instead.*

    Specifies the coloring style to be used in highlighted source code.

[`--print-highlight-style=`{.option-def}*STYLE*\|*FILE*]{#option--print-highlight-style .option-anchor}

:   Prints a JSON version of a highlighting style, which can be modified, saved with a `.theme` extension, and used with [`--syntax-highlighting`](#option--syntax-highlighting){.option}. This option may be used with [`-o`](#option--output){.option}/[`--output`](#option--output){.option} to redirect output to a file, but [`-o`](#option--output){.option}/[`--output`](#option--output){.option} must come before [`--print-highlight-style`](#option--print-highlight-style){.option} on the command line.

[`--syntax-definition=`{.option-def}*FILE*]{#option--syntax-definition .option-anchor}

:   Instructs pandoc to load a KDE XML syntax definition file, which will be used for syntax highlighting of appropriately marked code blocks. This can be used to add support for new languages or to use altered syntax definitions for existing languages. This option may be repeated to add multiple syntax definitions.

[`-H`{.option-def} *FILE*, `--include-in-header=`{.option-def}*FILE*\|*URL*]{#option--include-in-header .option-anchor}

:   Include contents of *FILE*, verbatim, at the end of the header. This can be used, for example, to include special CSS or JavaScript in HTML documents. This option can be used repeatedly to include multiple files in the header. They will be included in the order specified. Implies [`--standalone`](#option--standalone){.option}.

[`-B`{.option-def} *FILE*, `--include-before-body=`{.option-def}*FILE*\|*URL*]{#option--include-before-body .option-anchor}

:   Include contents of *FILE*, verbatim, at the beginning of the document body (e.g. after the `<body>` tag in HTML, or the `\begin{document}` command in LaTeX). This can be used to include navigation bars or banners in HTML documents. This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies [`--standalone`](#option--standalone){.option}. Note that if the output format is `odt`, this file must be in OpenDocument XML format suitable for insertion into the body of the document, and if the output is `docx`, this file must be in appropriate OpenXML format.

[`-A`{.option-def} *FILE*, `--include-after-body=`{.option-def}*FILE*\|*URL*]{#option--include-after-body .option-anchor}

:   Include contents of *FILE*, verbatim, at the end of the document body (before the `</body>` tag in HTML, or the `\end{document}` command in LaTeX). This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies [`--standalone`](#option--standalone){.option}. Note that if the output format is `odt`, this file must be in OpenDocument XML format suitable for insertion into the body of the document, and if the output is `docx`, this file must be in appropriate OpenXML format.

[`--resource-path=`{.option-def}*SEARCHPATH*]{#option--resource-path .option-anchor}

:   List of paths to search for images and other resources. The paths should be separated by `:` on Linux, UNIX, and macOS systems, and by `;` on Windows. If [`--resource-path`](#option--resource-path){.option} is not specified, the default resource path is the working directory. Note that, if [`--resource-path`](#option--resource-path){.option} is specified, the working directory must be explicitly listed or it will not be searched. For example: [`--resource-path=.:test`](#option--resource-path){.option} will search the working directory and the `test` subdirectory, in that order. This option can be used repeatedly. Search path components that come later on the command line will be searched before those that come earlier, so [`--resource-path foo:bar --resource-path baz:bim`](#option--resource-path){.option} is equivalent to [`--resource-path baz:bim:foo:bar`](#option--resource-path){.option}. Note that this option only has an effect when pandoc itself needs to find an image (e.g., in producing a PDF or docx, or when [`--embed-resources`](#option--embed-resources%5B){.option} is used.) It will not cause image paths to be rewritten in other cases (e.g., when pandoc is generating LaTeX or HTML).

[`--request-header=`{.option-def}*NAME*`:`*VAL*]{#option--request-header .option-anchor}

:   Set the request header *NAME* to the value *VAL* when making HTTP requests (for example, when a URL is given on the command line, or when resources used in a document must be downloaded). If you're behind a proxy, you also need to set the environment variable `http_proxy` to `http://...`.

[`--no-check-certificate[=true|false]`{.option-def}]{#option--no-check-certificate[ .option-anchor}

:   Disable the certificate verification to allow access to unsecure HTTP resources (for example when the certificate is no longer valid or self signed).
:::

::: {#options-affecting-specific-writers .section .level2 .options}
## [](#options-affecting-specific-writers){.anchor aria-hidden="true"}Options affecting specific writers {.options}

[`--self-contained[=true|false]`{.option-def}]{#option--self-contained[ .option-anchor}

:   *Deprecated synonym for [`--embed-resources --standalone`](#option--embed-resources%5B){.option}.*

[`--embed-resources[=true|false]`{.option-def}]{#option--embed-resources[ .option-anchor}

:   Produce a standalone HTML file with no external dependencies, using `data:` URIs to incorporate the contents of linked scripts, stylesheets, images, and videos. The resulting file should be "self-contained," in the sense that it needs no external files and no net access to be displayed properly by a browser. This option works only with HTML output formats, including `html4`, `html5`, `html+lhs`, `html5+lhs`, `s5`, `slidy`, `slideous`, `dzslides`, and `revealjs`. Scripts, images, and stylesheets at absolute URLs will be downloaded; those at relative URLs will be sought relative to the working directory (if the first source file is local) or relative to the base URL (if the first source file is remote). Elements with the attribute `data-external="1"` will be left alone; the documents they link to will not be incorporated in the document. Limitation: resources that are loaded dynamically through JavaScript cannot be incorporated; as a result, fonts may be missing when [`--mathjax`](#option--mathjax){.option} is used, and some advanced features (e.g. zoom or speaker notes) may not work in an offline "self-contained" `reveal.js` slide show.

    For SVG images, `img` tags with `data:` URIs are used, unless the image has the class `inline-svg`, in which case an inline SVG element is inserted. This approach is recommended when there are many occurrences of the same SVG in a document, as `<use>` elements will be used to reduce duplication.

[`--link-images[=true|false]`{.option-def}]{#option--link-images[ .option-anchor}

:   Include links to images instead of embedding the images in ODT. (This option currently only affects ODT output.)

[`--html-q-tags[=true|false]`{.option-def}]{#option--html-q-tags[ .option-anchor}

:   Use `<q>` tags for quotes in HTML. (This option only has an effect if the `smart` extension is enabled for the input format used.)

[`--ascii[=true|false]`{.option-def}]{#option--ascii[ .option-anchor}

:   Use only ASCII characters in output. Currently supported for XML and HTML formats (which use entities instead of UTF-8 when this option is selected), CommonMark, gfm, and Markdown (which use entities), roff man and ms (which use hexadecimal escapes), and to a limited degree LaTeX (which uses standard commands for accented characters when possible).

[`--reference-links[=true|false]`{.option-def}]{#option--reference-links[ .option-anchor}

:   Use reference-style links, rather than inline links, in writing Markdown or reStructuredText. By default inline links are used. The placement of link references is affected by the [`--reference-location`](#option--reference-location){.option} option.

[`--reference-location=block`{.option-def}\|`section`\|`document`]{#option--reference-location .option-anchor}

:   Specify whether footnotes (and references, if `reference-links` is set) are placed at the end of the current (top-level) block, the current section, or the document. The default is `document`. Currently this option only affects the `markdown`, `muse`, `html`, `epub`, `slidy`, `s5`, `slideous`, `dzslides`, and `revealjs` writers. In slide formats, specifying [`--reference-location=section`](#option--reference-location){.option} will cause notes to be rendered at the bottom of a slide.

[`--figure-caption-position=above`{.option-def}\|`below`]{#option--figure-caption-position .option-anchor}

:   Specify whether figure captions go above or below figures (default is `below`). This option only affects HTML, LaTeX, Docx, ODT, and Typst output.

[`--table-caption-position=above`{.option-def}\|`below`]{#option--table-caption-position .option-anchor}

:   Specify whether table captions go above or below tables (default is `above`). This option only affects HTML, LaTeX, Docx, ODT, and Typst output.

[`--markdown-headings=setext`{.option-def}\|`atx`]{#option--markdown-headings .option-anchor}

:   Specify whether to use ATX-style (`#`-prefixed) or Setext-style (underlined) headings for level 1 and 2 headings in Markdown output. (The default is `atx`.) ATX-style headings are always used for levels 3+. This option also affects Markdown cells in `ipynb` output.

[`--list-tables[=true|false]`{.option-def}]{#option--list-tables[ .option-anchor}

:   Render tables as list tables in RST output.

[`--top-level-division=default`{.option-def}\|`section`\|`chapter`\|`part`]{#option--top-level-division .option-anchor}

:   Treat top-level headings as the given division type in LaTeX, ConTeXt, DocBook, and TEI output. The hierarchy order is part, chapter, then section; all headings are shifted such that the top-level heading becomes the specified type. The default behavior is to determine the best division type via heuristics: unless other conditions apply, `section` is chosen. When the `documentclass` variable is set to `report`, `book`, or `memoir` (unless the `article` option is specified), `chapter` is implied as the setting for this option. If `beamer` is the output format, specifying either `chapter` or `part` will cause top-level headings to become `\part{..}`, while second-level headings remain as their default type.

    In Docx output, this option adds section breaks before first-level headings if `chapter` is selected, and before first- and second-level headings if `part` is selected. Footnote numbers will restart with each section break unless the reference doc modifies this.

[`-N`{.option-def}, `--number-sections=[true|false]`{.option-def}]{#option--number-sections .option-anchor}

:   Number section headings in LaTeX, ConTeXt, HTML, Docx, ms, or EPUB output. By default, sections are not numbered. Sections with class `unnumbered` will never be numbered, even if [`--number-sections`](#option--number-sections){.option} is specified.

[`--number-offset=`{.option-def}*NUMBER*\[`,`*NUMBER*`,`*...*\]]{#option--number-offset .option-anchor}

:   Offsets for section heading numbers. The first number is added to the section number for level-1 headings, the second for level-2 headings, and so on. So, for example, if you want the first level-1 heading in your document to be numbered "6" instead of "1", specify [`--number-offset=5`](#option--number-offset){.option}. If your document starts with a level-2 heading which you want to be numbered "1.5", specify [`--number-offset=1,4`](#option--number-offset){.option}. [`--number-offset`](#option--number-offset){.option} only directly affects the number of the first section heading in a document; subsequent numbers increment in the normal way. Implies [`--number-sections`](#option--number-sections){.option}. Currently this feature only affects HTML and Docx output.

[`--listings[=true|false]`{.option-def}]{#option--listings[ .option-anchor}

:   \*Deprecated, use [`--syntax-highlighting=idiomatic`](#option--syntax-highlighting){.option} or [`--syntax-highlighting=default`](#option--syntax-highlighting){.option} instead.

    Use the [`listings`](https://ctan.org/pkg/listings) package for LaTeX code blocks. The package does not support multi-byte encoding for source code. To handle UTF-8 you would need to use a custom template. This issue is fully documented here: [Encoding issue with the listings package](https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings#Encoding_issue).

[`-i`{.option-def}, `--incremental[=true|false]`{.option-def}]{#option--incremental[ .option-anchor}

:   Make list items in slide shows display incrementally (one by one). The default is for lists to be displayed all at once.

[`--slide-level=`{.option-def}*NUMBER*]{#option--slide-level .option-anchor}

:   Specifies that headings with the specified level create slides (for `beamer`, `revealjs`, `pptx`, `s5`, `slidy`, `slideous`, `dzslides`). Headings above this level in the hierarchy are used to divide the slide show into sections; headings below this level create subheads within a slide. Valid values are 0-6. If a slide level of 0 is specified, slides will not be split automatically on headings, and horizontal rules must be used to indicate slide boundaries. If a slide level is not specified explicitly, the slide level will be set automatically based on the contents of the document; see [Structuring the slide show](#structuring-the-slide-show).

[`--section-divs[=true|false]`{.option-def}]{#option--section-divs[ .option-anchor}

:   Wrap sections in `<section>` tags (or `<div>` tags for `html4`), and attach identifiers to the enclosing `<section>` (or `<div>`) rather than the heading itself (see [Heading identifiers](#heading-identifiers), below). This option only affects HTML output (and does not affect HTML slide formats).

[`--email-obfuscation=none`{.option-def}\|`javascript`\|`references`]{#option--email-obfuscation .option-anchor}

:   Specify a method for obfuscating `mailto:` links in HTML documents. `none` leaves `mailto:` links as they are. `javascript` obfuscates them using JavaScript. `references` obfuscates them by printing their letters as decimal or hexadecimal character references. The default is `none`.

[`--id-prefix=`{.option-def}*STRING*]{#option--id-prefix .option-anchor}

:   Specify a prefix to be added to all identifiers and internal links in HTML and DocBook output, and to footnote numbers in Markdown and Haddock output. This is useful for preventing duplicate identifiers when generating fragments to be included in other pages.

[`-T`{.option-def} *STRING*, `--title-prefix=`{.option-def}*STRING*]{#option--title-prefix .option-anchor}

:   Specify *STRING* as a prefix at the beginning of the title that appears in the HTML header (but not in the title as it appears at the beginning of the HTML body). Implies [`--standalone`](#option--standalone){.option}.

[`-c`{.option-def} *URL*, `--css=`{.option-def}*URL*]{#option--css .option-anchor}

:   Link to a CSS style sheet. This option can be used repeatedly to include multiple files. They will be included in the order specified. This option only affects HTML (including HTML slide shows) and EPUB output. It should be used together with [`-s/--standalone`](#option--standalone){.option}, because the link to the stylesheet goes in the document header.

    A stylesheet is required for generating EPUB. If none is provided using this option (or the `css` or `stylesheet` metadata fields), pandoc will look for a file `epub.css` in the user data directory (see [`--data-dir`](#option--data-dir){.option}). If it is not found there, sensible defaults will be used.

[`--reference-doc=`*FILE*\|*URL*]{#option--reference-doc}

:   Use the specified file as a style reference in producing a docx or ODT file.

    Docx

    :   For best results, the reference docx should be a modified version of a docx file produced using pandoc. The contents of the reference docx are ignored, but its stylesheets and document properties (including margins, page size, header, and footer) are used in the new docx. If no reference docx is specified on the command line, pandoc will look for a file `reference.docx` in the user data directory (see [`--data-dir`](#option--data-dir){.option}). If this is not found either, sensible defaults will be used.

        To produce a custom `reference.docx`, first get a copy of the default `reference.docx`: `pandoc -o custom-reference.docx --print-default-data-file reference.docx`. Then open `custom-reference.docx` in Word, modify the styles as you wish, and save the file. For best results, do not make changes to this file other than modifying the styles used by pandoc:

        Paragraph styles:

        -   Normal
        -   Body Text
        -   First Paragraph
        -   Compact
        -   Title
        -   Subtitle
        -   Author
        -   Date
        -   Abstract
        -   AbstractTitle
        -   Bibliography
        -   Heading 1
        -   Heading 2
        -   Heading 3
        -   Heading 4
        -   Heading 5
        -   Heading 6
        -   Heading 7
        -   Heading 8
        -   Heading 9
        -   Block Text \[for block quotes\]
        -   Footnote Block Text \[for block quotes in footnotes\]
        -   Source Code
        -   Footnote Text
        -   Definition Term
        -   Definition
        -   Caption
        -   Table Caption
        -   Image Caption
        -   Figure
        -   Captioned Figure
        -   TOC Heading

        Character styles:

        -   Default Paragraph Font
        -   Verbatim Char
        -   Footnote Reference
        -   Hyperlink
        -   Section Number

        Table style:

        -   Table

    ODT

    :   For best results, the reference ODT should be a modified version of an ODT produced using pandoc. The contents of the reference ODT are ignored, but its stylesheets are used in the new ODT. If no reference ODT is specified on the command line, pandoc will look for a file `reference.odt` in the user data directory (see [`--data-dir`](#option--data-dir){.option}). If this is not found either, sensible defaults will be used.

        To produce a custom `reference.odt`, first get a copy of the default `reference.odt`: `pandoc -o custom-reference.odt --print-default-data-file reference.odt`. Then open `custom-reference.odt` in LibreOffice, modify the styles as you wish, and save the file.

    PowerPoint

    :   Templates included with Microsoft PowerPoint 2013 (either with `.pptx` or `.potx` extension) are known to work, as are most templates derived from these.

        The specific requirement is that the template should contain layouts with the following names (as seen within PowerPoint):

        -   Title Slide
        -   Title and Content
        -   Section Header
        -   Two Content
        -   Comparison
        -   Content with Caption
        -   Blank

        For each name, the first layout found with that name will be used. If no layout is found with one of the names, pandoc will output a warning and use the layout with that name from the default reference doc instead. (How these layouts are used is described in [PowerPoint layout choice](#powerpoint-layout-choice).)

        All templates included with a recent version of MS PowerPoint will fit these criteria. (You can click on `Layout` under the `Home` menu to check.)

        You can also modify the default `reference.pptx`: first run `pandoc -o custom-reference.pptx --print-default-data-file reference.pptx`, and then modify `custom-reference.pptx` in MS PowerPoint (pandoc will use the layouts with the names listed above).

[`--split-level=`{.option-def}*NUMBER*]{#option--split-level .option-anchor}

:   Specify the heading level at which to split an EPUB or chunked HTML document into separate files. The default is to split into chapters at level-1 headings. In the case of EPUB, this option only affects the internal composition of the EPUB, not the way chapters and sections are displayed to users. Some readers may be slow if the chapter files are too large, so for large documents with few level-1 headings, one might want to use a chapter level of 2 or 3. For chunked HTML, this option determines how much content goes in each "chunk."

[`--chunk-template=`{.option-def}*PATHTEMPLATE*]{#option--chunk-template .option-anchor}

:   Specify a template for the filenames in a `chunkedhtml` document. In the template, `%n` will be replaced by the chunk number (padded with leading 0s to 3 digits), `%s` with the section number of the chunk, `%h` with the heading text (with formatting removed), `%i` with the section identifier. For example, `section-%s-%i.html` might be resolved to `section-1.1-introduction.html`. The characters `/` and `\` are not allowed in chunk templates and will be ignored. The default is `%s-%i.html`.

[`--epub-chapter-level=`{.option-def}*NUMBER*]{#option--epub-chapter-level .option-anchor}

:   *Deprecated synonym for [`--split-level`](#option--split-level){.option}.*

[`--epub-cover-image=`{.option-def}*FILE*]{#option--epub-cover-image .option-anchor}

:   Use the specified image as the EPUB cover. It is recommended that the image be less than 1000px in width and height. Note that in a Markdown source document you can also specify `cover-image` in a YAML metadata block (see [EPUB Metadata](#epub-metadata), below).

[`--epub-title-page=true`{.option-def}\|`false`]{#option--epub-title-page .option-anchor}

:   Determines whether a the title page is included in the EPUB (default is `true`).

[`--epub-metadata=`{.option-def}*FILE*]{#option--epub-metadata .option-anchor}

:   Look in the specified XML file for metadata for the EPUB. The file should contain a series of [Dublin Core elements](https://www.dublincore.org/specifications/dublin-core/dces/). For example:

         <dc:rights>Creative Commons</dc:rights>
         <dc:language>es-AR</dc:language>

    By default, pandoc will include the following metadata elements: `<dc:title>` (from the document title), `<dc:creator>` (from the document authors), `<dc:date>` (from the document date, which should be in [ISO 8601 format](https://www.w3.org/TR/NOTE-datetime)), `<dc:language>` (from the `lang` variable, or, if is not set, the locale), and `<dc:identifier id="BookId">` (a randomly generated UUID). Any of these may be overridden by elements in the metadata file.

    Note: if the source document is Markdown, a YAML metadata block in the document can be used instead. See below under [EPUB Metadata](#epub-metadata).

[`--epub-embed-font=`{.option-def}*FILE*]{#option--epub-embed-font .option-anchor}

:   Embed the specified font in the EPUB. This option can be repeated to embed multiple fonts. Wildcards can also be used: for example, `DejaVuSans-*.ttf`. However, if you use wildcards on the command line, be sure to escape them or put the whole filename in single quotes, to prevent them from being interpreted by the shell. To use the embedded fonts, you will need to add declarations like the following to your CSS (see [`--css`](#option--css){.option}):

        @font-face {
           font-family: DejaVuSans;
           font-style: normal;
           font-weight: normal;
           src:url("../fonts/DejaVuSans-Regular.ttf");
        }
        @font-face {
           font-family: DejaVuSans;
           font-style: normal;
           font-weight: bold;
           src:url("../fonts/DejaVuSans-Bold.ttf");
        }
        @font-face {
           font-family: DejaVuSans;
           font-style: italic;
           font-weight: normal;
           src:url("../fonts/DejaVuSans-Oblique.ttf");
        }
        @font-face {
           font-family: DejaVuSans;
           font-style: italic;
           font-weight: bold;
           src:url("../fonts/DejaVuSans-BoldOblique.ttf");
        }
        body { font-family: "DejaVuSans"; }

[`--epub-subdirectory=`{.option-def}*DIRNAME*]{#option--epub-subdirectory .option-anchor}

:   Specify the subdirectory in the OCF container that is to hold the EPUB-specific contents. The default is `EPUB`. To put the EPUB contents in the top level, use an empty string.

[`--ipynb-output=all|none|best`{.option-def}]{#option--ipynb-output .option-anchor}

:   Determines how ipynb output cells are treated. `all` means that all of the data formats included in the original are preserved. `none` means that the contents of data cells are omitted. `best` causes pandoc to try to pick the richest data block in each output cell that is compatible with the output format. The default is `best`.

[`--pdf-engine=`{.option-def}*PROGRAM*]{#option--pdf-engine .option-anchor}

:   Use the specified engine when producing PDF output. Valid values are `pdflatex`, `lualatex`, `xelatex`, `latexmk`, `tectonic`, `wkhtmltopdf`, `weasyprint`, `pagedjs-cli`, `prince`, `context`, `groff`, `pdfroff`, and `typst`. If the engine is not in your PATH, the full path of the engine may be specified here. If this option is not specified, pandoc uses the following defaults depending on the output format specified using [`-t/--to`](#option--to){.option}:

    -   [`-t latex`](#option--to){.option} or none: `pdflatex` (other options: `xelatex`, `lualatex`, `tectonic`, `latexmk`)
    -   [`-t context`](#option--to){.option}: `context`
    -   [`-t html`](#option--to){.option}: `weasyprint` (other options: `prince`, `wkhtmltopdf`, `pagedjs-cli`; see [print-css.rocks](https://print-css.rocks) for a good introduction to PDF generation from HTML/CSS)
    -   [`-t ms`](#option--to){.option}: `pdfroff`
    -   [`-t typst`](#option--to){.option}: `typst`

    This option is normally intended to be used when a PDF file is specified as [`-o/--output`](#option--output){.option}. However, it may still have an effect when other output formats are requested. For example, `ms` output will include `.pdfhref` macros only if a [`--pdf-engine`](#option--pdf-engine){.option} is selected, and the macros will be differently encoded depending on whether `groff` or `pdfroff` is specified.

[`--pdf-engine-opt=`{.option-def}*STRING*]{#option--pdf-engine-opt .option-anchor}

:   Use the given string as a command-line argument to the `pdf-engine`. For example, to use a persistent directory `foo` for `latexmk`'s auxiliary files, use [`--pdf-engine-opt=-outdir=foo`](#option--pdf-engine-opt){.option}. Note that no check for duplicate options is done.
:::

::: {#citation-rendering .section .level2 .options}
## [](#citation-rendering){.anchor aria-hidden="true"}Citation rendering {.options}

[`-C`{.option-def}, `--citeproc`{.option-def}]{#option--citeproc .option-anchor}

:   Process the citations in the file, replacing them with rendered citations and adding a bibliography. Citation processing will not take place unless bibliographic data is supplied, either through an external file specified using the [`--bibliography`](#option--bibliography){.option} option or the `bibliography` field in metadata, or via a `references` section in metadata containing a list of citations in CSL YAML format with Markdown formatting. The style is controlled by a [CSL](https://docs.citationstyles.org/en/stable/specification.html) stylesheet specified using the [`--csl`](#option--csl){.option} option or the `csl` field in metadata. (If no stylesheet is specified, the `chicago-author-date` style will be used by default.) The citation processing transformation may be applied before or after filters or Lua filters (see [`--filter`](#option--filter){.option}, [`--lua-filter`](#option--lua-filter){.option}): these transformations are applied in the order they appear on the command line. For more information, see the section on [Citations](#citations).

    Note: if this option is specified, the `citations` extension will be disabled automatically in the writer, to ensure that the citeproc-generated citations will be rendered instead of the format's own citation syntax.

[`--bibliography=`{.option-def}*FILE*]{#option--bibliography .option-anchor}

:   Set the `bibliography` field in the document's metadata to *FILE*, overriding any value set in the metadata. If you supply this argument multiple times, each *FILE* will be added to bibliography. If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see [`--resource-path`](#option--resource-path){.option}).

[`--csl=`{.option-def}*FILE*]{#option--csl .option-anchor}

:   Set the `csl` field in the document's metadata to *FILE*, overriding any value set in the metadata. (This is equivalent to [`--metadata csl=FILE`](#option--metadata){.option}.) If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see [`--resource-path`](#option--resource-path){.option}) and finally in the `csl` subdirectory of the pandoc user data directory.

[`--citation-abbreviations=`{.option-def}*FILE*]{#option--citation-abbreviations .option-anchor}

:   Set the `citation-abbreviations` field in the document's metadata to *FILE*, overriding any value set in the metadata. (This is equivalent to [`--metadata citation-abbreviations=FILE`](#option--metadata){.option}.) If *FILE* is a URL, it will be fetched via HTTP. If *FILE* is not found relative to the working directory, it will be sought in the resource path (see [`--resource-path`](#option--resource-path){.option}) and finally in the `csl` subdirectory of the pandoc user data directory.

[`--natbib`{.option-def}]{#option--natbib .option-anchor}

:   Use [`natbib`](https://ctan.org/pkg/natbib) for citations in LaTeX output. This option is not for use with the [`--citeproc`](#option--citeproc){.option} option or with PDF output. It is intended for use in producing a LaTeX file that can be processed with [`bibtex`](https://ctan.org/pkg/bibtex).

[`--biblatex`{.option-def}]{#option--biblatex .option-anchor}

:   Use [`biblatex`](https://ctan.org/pkg/biblatex) for citations in LaTeX output. This option is not for use with the [`--citeproc`](#option--citeproc){.option} option or with PDF output. It is intended for use in producing a LaTeX file that can be processed with [`bibtex`](https://ctan.org/pkg/bibtex) or [`biber`](https://ctan.org/pkg/biber).
:::

::: {#math-rendering-in-html .section .level2 .options}
## [](#math-rendering-in-html){.anchor aria-hidden="true"}Math rendering in HTML {.options}

The default is to render TeX math as far as possible using Unicode characters. Formulas are put inside a `span` with `class="math"`, so that they may be styled differently from the surrounding text if needed. However, this gives acceptable results only for basic math, usually you will want to use [`--mathjax`](#option--mathjax){.option} or another of the following options.

[`--mathjax`{.option-def}\[`=`*URL*\]]{#option--mathjax .option-anchor}

:   Use [MathJax](https://www.mathjax.org) to display embedded TeX math in HTML output. TeX math will be put between `\(...\)` (for inline math) or `\[...\]` (for display math) and wrapped in `<span>` tags with class `math`. Then the MathJax JavaScript will render it. The *URL* should point to the `MathJax.js` load script. If a *URL* is not provided, a link to the Cloudflare CDN will be inserted.

[`--mathml`{.option-def}]{#option--mathml .option-anchor}

:   Convert TeX math to [MathML](https://www.w3.org/Math/) (in `epub3`, `docbook4`, `docbook5`, `jats`, `html4` and `html5`). This is the default in `odt` output. MathML is supported natively by the main web browsers and select e-book readers.

[`--webtex`{.option-def}\[`=`*URL*\]]{#option--webtex .option-anchor}

:   Convert TeX formulas to `<img>` tags that link to an external script that converts formulas to images. The formula will be URL-encoded and concatenated with the URL provided. For SVG images you can for example use [`--webtex https://latex.codecogs.com/svg.latex?`](#option--webtex){.option}. If no URL is specified, the CodeCogs URL generating PNGs will be used (`https://latex.codecogs.com/png.latex?`). Note: the [`--webtex`](#option--webtex){.option} option will affect Markdown output as well as HTML, which is useful if you're targeting a version of Markdown without native math support.

[`--katex`{.option-def}\[`=`*URL*\]]{#option--katex .option-anchor}

:   Use [KaTeX](https://github.com/Khan/KaTeX) to display embedded TeX math in HTML output. The *URL* is the base URL for the KaTeX library. That directory should contain a `katex.min.js` and a `katex.min.css` file. If a *URL* is not provided, a link to the KaTeX CDN will be inserted.

[`--gladtex`{.option-def}]{#option--gladtex .option-anchor}

:   Enclose TeX math in `<eq>` tags in HTML output. The resulting HTML can then be processed by [GladTeX](https://humenda.github.io/GladTeX/) to produce SVG images of the typeset formulas and an HTML file with these images embedded.

        pandoc -s --gladtex input.md -o myfile.htex
        gladtex -d image_dir myfile.htex
        # produces myfile.html and images in image_dir
:::

::: {#options-for-wrapper-scripts .section .level2 .options}
## [](#options-for-wrapper-scripts){.anchor aria-hidden="true"}Options for wrapper scripts {.options}

[`--dump-args[=true|false]`{.option-def}]{#option--dump-args[ .option-anchor}

:   Print information about command-line arguments to *stdout*, then exit. This option is intended primarily for use in wrapper scripts. The first line of output contains the name of the output file specified with the [`-o`](#option--output){.option} option, or `-` (for *stdout*) if no output file was specified. The remaining lines contain the command-line arguments, one per line, in the order they appear. These do not include regular pandoc options and their arguments, but do include any options appearing after a `--` separator at the end of the line.

[`--ignore-args[=true|false]`{.option-def}]{#option--ignore-args[ .option-anchor}

:   Ignore command-line arguments (for use in wrapper scripts). Regular pandoc options are not ignored. Thus, for example,

        pandoc --ignore-args -o foo.html -s foo.txt -- -e latin1

    is equivalent to

        pandoc -o foo.html -s
:::
::::::::::
