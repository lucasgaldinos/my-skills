::::::::::::::::::::::::::::::::::: {#templates .section .level1}
# [](#templates){.anchor aria-hidden="true"}Templates

When the [`-s/--standalone`](#option--standalone){.option} option is used, pandoc uses a template to add header and footer material that is needed for a self-standing document. To see the default template that is used, just type

    pandoc -D *FORMAT*

where *FORMAT* is the name of the output format. A custom template can be specified using the [`--template`](#option--template){.option} option. You can also override the system default templates for a given output format *FORMAT* by putting a file `templates/default.*FORMAT*` in the user data directory (see [`--data-dir`](#option--data-dir){.option}, above). *Exceptions:*

-   For `odt` output, customize the `default.opendocument` template.
-   For `docx` output, customize the `default.openxml` template.
-   For `pdf` output, customize the `default.latex` template (or the `default.context` template, if you use [`-t context`](#option--to){.option}, or the `default.ms` template, if you use [`-t ms`](#option--to){.option}, or the `default.html` template, if you use [`-t html`](#option--to){.option}).
-   `pptx` has no template.

Note that `docx`, `odt`, and `pptx` output can also be customized using `--reference-doc`. Use a reference doc to adjust the styles in your document; use a template to handle variable interpolation and customize the presentation of metadata, the position of the table of contents, boilerplate text, etc.

Templates contain *variables*, which allow for the inclusion of arbitrary information at any point in the file. They may be set at the command line using the [`-V/--variable`](#option--variable){.option} option. If a variable is not set, pandoc will look for the key in the document's metadata, which can be set using either [YAML metadata blocks](#extension-yaml_metadata_block) or with the [`-M/--metadata`](#option--metadata){.option} option. In addition, some variables are given default values by pandoc. See [Variables](#variables) below for a list of variables used in pandoc's default templates.

If you use custom templates, you may need to revise them as pandoc changes. We recommend tracking the changes in the default templates, and modifying your custom templates accordingly. An easy way to do this is to fork the [pandoc-templates](https://github.com/jgm/pandoc-templates) repository and merge in changes after each pandoc release.

:::::::::::: {#template-syntax .section .level2}
## [](#template-syntax){.anchor aria-hidden="true"}Template syntax

::: {#comments .section .level3}
### [](#comments){.anchor aria-hidden="true"}Comments

Anything between the sequence `$--` and the end of the line will be treated as a comment and omitted from the output.
:::

::: {#delimiters .section .level3}
### [](#delimiters){.anchor aria-hidden="true"}Delimiters

To mark variables and control structures in the template, either `$`...`$` or `${`...`}` may be used as delimiters. The styles may also be mixed in the same template, but the opening and closing delimiter must match in each case. The opening delimiter may be followed by one or more spaces or tabs, which will be ignored. The closing delimiter may be preceded by one or more spaces or tabs, which will be ignored.

To include a literal `$` in the document, use `$$`.
:::

::: {#interpolated-variables .section .level3}
### [](#interpolated-variables){.anchor aria-hidden="true"}Interpolated variables

A slot for an interpolated variable is a variable name surrounded by matched delimiters. Variable names must begin with a letter and can contain letters, numbers, `_`, `-`, and `.`. The keywords `it`, `if`, `else`, `endif`, `for`, `sep`, and `endfor` may not be used as variable names. Examples:

    $foo$
    $foo.bar.baz$
    $foo_bar.baz-bim$
    $ foo $
    ${foo}
    ${foo.bar.baz}
    ${foo_bar.baz-bim}
    ${ foo }

Variable names with periods are used to get at structured variable values. So, for example, `employee.salary` will return the value of the `salary` field of the object that is the value of the `employee` field.

-   If the value of the variable is a simple value, it will be rendered verbatim. (Note that no escaping is done; the assumption is that the calling program will escape the strings appropriately for the output format.)
-   If the value is a list, the values will be concatenated.
-   If the value is a map, the string `true` will be rendered.
-   Every other value will be rendered as the empty string.
:::

::: {#conditionals .section .level3}
### [](#conditionals){.anchor aria-hidden="true"}Conditionals

A conditional begins with `if(variable)` (enclosed in matched delimiters) and ends with `endif` (enclosed in matched delimiters). It may optionally contain an `else` (enclosed in matched delimiters). The `if` section is used if `variable` has a true value, otherwise the `else` section is used (if present). The following values count as true:

-   any map
-   any array containing at least one true value
-   any nonempty string
-   boolean True

Note that in YAML metadata (and metadata specified on the command line using [`-M/--metadata`](#option--metadata){.option}), unquoted `true` and `false` will be interpreted as Boolean values. But a variable specified on the command line using [`-V/--variable`](#option--variable){.option} will always be given a string value. Hence a conditional `if(foo)` will be triggered if you use [`-V foo=false`](#option--variable){.option}, but not if you use [`-M foo=false`](#option--metadata){.option}.

Examples:

    $if(foo)$bar$endif$

    $if(foo)$
      $foo$
    $endif$

    $if(foo)$
    part one
    $else$
    part two
    $endif$

    ${if(foo)}bar${endif}

    ${if(foo)}
      ${foo}
    ${endif}

    ${if(foo)}
    ${ foo.bar }
    ${else}
    no foo!
    ${endif}

The keyword `elseif` may be used to simplify complex nested conditionals:

    $if(foo)$
    XXX
    $elseif(bar)$
    YYY
    $else$
    ZZZ
    $endif$
:::

::: {#for-loops .section .level3}
### [](#for-loops){.anchor aria-hidden="true"}For loops

A for loop begins with `for(variable)` (enclosed in matched delimiters) and ends with `endfor` (enclosed in matched delimiters).

-   If `variable` is an array, the material inside the loop will be evaluated repeatedly, with `variable` being set to each value of the array in turn, and concatenated.
-   If `variable` is a map, the material inside will be set to the map.
-   If the value of the associated variable is not an array or a map, a single iteration will be performed on its value.

Examples:

    $for(foo)$$foo$$sep$, $endfor$

    $for(foo)$
      - $foo.last$, $foo.first$
    $endfor$

    ${ for(foo.bar) }
      - ${ foo.bar.last }, ${ foo.bar.first }
    ${ endfor }

    $for(mymap)$
    $it.name$: $it.office$
    $endfor$

You may optionally specify a separator between consecutive values using `sep` (enclosed in matched delimiters). The material between `sep` and the `endfor` is the separator.

    ${ for(foo) }${ foo }${ sep }, ${ endfor }

Instead of using `variable` inside the loop, the special anaphoric keyword `it` may be used.

    ${ for(foo.bar) }
      - ${ it.last }, ${ it.first }
    ${ endfor }
:::

::: {#partials .section .level3}
### [](#partials){.anchor aria-hidden="true"}Partials

Partials (subtemplates stored in different files) may be included by using the name of the partial, followed by `()`, for example:

    ${ styles() }

Partials will be sought in the directory containing the main template. The file name will be assumed to have the same extension as the main template if it lacks an extension. When calling the partial, the full name including file extension can also be used:

    ${ styles.html() }

(If a partial is not found in the directory of the template and the template path is given as a relative path, it will also be sought in the `templates` subdirectory of the user data directory.)

Partials may optionally be applied to variables using a colon:

    ${ date:fancy() }

    ${ articles:bibentry() }

If `articles` is an array, this will iterate over its values, applying the partial `bibentry()` to each one. So the second example above is equivalent to

    ${ for(articles) }
    ${ it:bibentry() }
    ${ endfor }

Note that the anaphoric keyword `it` must be used when iterating over partials. In the above examples, the `bibentry` partial should contain `it.title` (and so on) instead of `articles.title`.

Final newlines are omitted from included partials.

Partials may include other partials.

A separator between values of an array may be specified in square brackets, immediately after the variable name or partial:

    ${months[, ]}

    ${articles:bibentry()[; ]}

The separator in this case is literal and (unlike with `sep` in an explicit `for` loop) cannot contain interpolated variables or other template directives.
:::

::: {#nesting .section .level3}
### [](#nesting){.anchor aria-hidden="true"}Nesting

To ensure that content is "nested," that is, subsequent lines indented, use the `^` directive:

    $item.number$  $^$$item.description$ ($item.price$)

In this example, if `item.description` has multiple lines, they will all be indented to line up with the first line:

    00123  A fine bottle of 18-year old
           Oban whiskey. ($148)

To nest multiple lines to the same level, align them with the `^` directive in the template. For example:

    $item.number$  $^$$item.description$ ($item.price$)
                   (Available til $item.sellby$.)

will produce

    00123  A fine bottle of 18-year old
           Oban whiskey. ($148)
           (Available til March 30, 2020.)

If a variable occurs by itself on a line, preceded by whitespace and not followed by further text or directives on the same line, and the variable's value contains multiple lines, it will be nested automatically.
:::

::: {#breakable-spaces .section .level3}
### [](#breakable-spaces){.anchor aria-hidden="true"}Breakable spaces

Normally, spaces in the template itself (as opposed to values of the interpolated variables) are not breakable, but they can be made breakable in part of the template by using the `~` keyword (ended with another `~`).

    $~$This long line may break if the document is rendered
    with a short line length.$~$
:::

::: {#pipes .section .level3}
### [](#pipes){.anchor aria-hidden="true"}Pipes

A pipe transforms the value of a variable or partial. Pipes are specified using a slash (`/`) between the variable name (or partial) and the pipe name. Example:

    $for(name)$
    $name/uppercase$
    $endfor$

    $for(metadata/pairs)$
    - $it.key$: $it.value$
    $endfor$

    $employee:name()/uppercase$

Pipes may be chained:

    $for(employees/pairs)$
    $it.key/alpha/uppercase$. $it.name$
    $endfor$

Some pipes take parameters:

    |----------------------|------------|
    $for(employee)$
    $it.name.first/uppercase/left 20 "| "$$it.name.salary/right 10 " | " " |"$
    $endfor$
    |----------------------|------------|

Currently the following pipes are predefined:

-   `pairs`: Converts a map or array to an array of maps, each with `key` and `value` fields. If the original value was an array, the `key` will be the array index, starting with 1.

-   `uppercase`: Converts text to uppercase.

-   `lowercase`: Converts text to lowercase.

-   `length`: Returns the length of the value: number of characters for a textual value, number of elements for a map or array.

-   `reverse`: Reverses a textual value or array, and has no effect on other values.

-   `first`: Returns the first value of an array, if applied to a non-empty array; otherwise returns the original value.

-   `last`: Returns the last value of an array, if applied to a non-empty array; otherwise returns the original value.

-   `rest`: Returns all but the first value of an array, if applied to a non-empty array; otherwise returns the original value.

-   `allbutlast`: Returns all but the last value of an array, if applied to a non-empty array; otherwise returns the original value.

-   `chomp`: Removes trailing newlines (and breakable space).

-   `nowrap`: Disables line wrapping on breakable spaces.

-   `alpha`: Converts textual values that can be read as an integer into lowercase alphabetic characters `a..z` (mod 26). This can be used to get lettered enumeration from array indices. To get uppercase letters, chain with `uppercase`.

-   `roman`: Converts textual values that can be read as an integer into lowercase roman numerals. This can be used to get lettered enumeration from array indices. To get uppercase roman, chain with `uppercase`.

-   `left n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the left, with an optional left and right border. Has no effect on other values. This can be used to align material in tables. Widths are positive integers indicating the number of characters. Borders are strings inside double quotes; literal `"` and `\` characters must be backslash-escaped.

-   `right n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the right, and has no effect on other values.

-   `center n "leftborder" "rightborder"`: Renders a textual value in a block of width `n`, aligned to the center, and has no effect on other values.
:::
::::::::::::

:::::::::::::::::::::::: {#variables .section .level2}
## [](#variables){.anchor aria-hidden="true"}Variables

::: {#metadata-variables .section .level3}
### [](#metadata-variables){.anchor aria-hidden="true"}Metadata variables

`title`, `author`, `date`

:   allow identification of basic aspects of the document. Included in PDF metadata through LaTeX and ConTeXt. These can be set through a [pandoc title block](#extension-pandoc_title_block), which allows for multiple authors, or through a [YAML metadata block](#extension-yaml_metadata_block):

        ---
        author:
        - Aristotle
        - Peter Abelard
        ...

    Note that if you just want to set PDF or HTML metadata, without including a title block in the document itself, you can set the `title-meta`, `author-meta`, and `date-meta` variables. (By default these are set automatically, based on `title`, `author`, and `date`.) The page title in HTML is set by `pagetitle`, which is equal to `title` by default.

`subtitle`
:   document subtitle, included in HTML, EPUB, LaTeX, ConTeXt, and docx documents

`abstract`
:   document summary, included in HTML, LaTeX, ConTeXt, AsciiDoc, and docx documents

`abstract-title`
:   title of abstract, currently used only in HTML, EPUB, docx, and Typst. This will be set automatically to a localized value, depending on `lang`, but can be manually overridden.

`keywords`
:   list of keywords to be included in HTML, PDF, ODT, pptx, docx and AsciiDoc metadata; repeat as for `author`, above

`subject`
:   document subject, included in ODT, PDF, docx, EPUB, and pptx metadata

`description`
:   document description, included in ODT, docx and pptx metadata. Some applications show this as `Comments` metadata.

`category`
:   document category, included in docx and pptx metadata

Additionally, any root-level string metadata, not included in ODT, docx or pptx metadata is added as a *custom property*. The following [YAML](https://yaml.org/spec/1.2/spec.html "YAML v1.2 Spec") metadata block for instance:

    ---
    title:  'This is the title'
    subtitle: "This is the subtitle"
    author:
    - Author One
    - Author Two
    description: |
        This is a long
        description.

        It consists of two paragraphs
    ...

will include `title`, `author` and `description` as standard document properties and `subtitle` as a custom property when converting to docx, ODT or pptx.
:::

::: {#language-variables .section .level3}
### [](#language-variables){.anchor aria-hidden="true"}Language variables

`lang`

:   identifies the main language of the document using IETF language tags (following the [BCP 47](https://tools.ietf.org/html/bcp47) standard), such as `en` or `en-GB`. The [Language subtag lookup](https://r12a.github.io/app-subtags/) tool can look up or verify these tags. This affects most formats, and controls hyphenation in PDF output when using LaTeX (through [`babel`](https://ctan.org/pkg/babel) and [`polyglossia`](https://ctan.org/pkg/polyglossia)) or ConTeXt. Use native pandoc [Divs and Spans](#divs-and-spans) with the `lang` attribute to switch the language:

        ---
        lang: en-GB
        ...

        Text in the main document language (British English).

        ::: {lang=fr-CA}
        > Cette citation est écrite en français canadien.
        :::

        More text in English. ['Zitat auf Deutsch.']{lang=de}

`dir`
:   the base script direction, either `rtl` (right-to-left) or `ltr` (left-to-right). For bidirectional documents, native pandoc `span`s and `div`s with the `dir` attribute (value `rtl` or `ltr`) can be used to override the base direction in some output formats. This may not always be necessary if the final renderer (e.g. the browser, when generating HTML) supports the [Unicode Bidirectional Algorithm](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics). When using LaTeX for bidirectional documents, only the `xelatex` engine is fully supported (use [`--pdf-engine=xelatex`](#option--pdf-engine){.option}).
:::

::: {#variables-for-html .section .level3}
### [](#variables-for-html){.anchor aria-hidden="true"}Variables for HTML

`document-css`
:   Enables inclusion of most of the [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS) in the `styles.html` [partial](#partials) (have a look with `pandoc --print-default-data-file=templates/styles.html`). Unless you use [`--css`](#option--css){.option}, this variable is set to `true` by default. You can disable it with e.g. `pandoc -M document-css=false`.

`mainfont`
:   sets the CSS `font-family` property on the `html` element.

`fontsize`
:   sets the base CSS `font-size`, which you'd usually set to e.g. `20px`, but it also accepts `pt` (12pt = 16px in most browsers).

`fontcolor`
:   sets the CSS `color` property on the `html` element.

`linkcolor`
:   sets the CSS `color` property on all links.

`monofont`
:   sets the CSS `font-family` property on `code` elements.

`monobackgroundcolor`
:   sets the CSS `background-color` property on `code` elements and adds extra padding.

`linestretch`
:   sets the CSS `line-height` property on the `html` element, which is preferred to be unitless.

`maxwidth`
:   sets the CSS `max-width` property (default is 36em).

`backgroundcolor`
:   sets the CSS `background-color` property on the `html` element.

`margin-left`, `margin-right`, `margin-top`, `margin-bottom`
:   sets the corresponding CSS `padding` properties on the `body` element.

To override or extend some [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS) for just one document, include for example:

    ---
    header-includes: |
      <style>
      blockquote {
        font-style: italic;
      }
      tr.even {
        background-color: #f0f0f0;
      }
      td, th {
        padding: 0.5em 2em 0.5em 0.5em;
      }
      tbody {
        border-bottom: none;
      }
      </style>
    ---
:::

::: {#variables-for-html-math .section .level3}
### [](#variables-for-html-math){.anchor aria-hidden="true"}Variables for HTML math

`classoption`
:   when using [`--katex`](#option--katex){.option}, you can render display math equations flush left using [YAML metadata](#layout) or with [`-M classoption=fleqn`](#option--metadata){.option}.
:::

::: {#variables-for-html-slides .section .level3}
### [](#variables-for-html-slides){.anchor aria-hidden="true"}Variables for HTML slides

These affect HTML output when [producing slide shows with pandoc](#slide-shows).

`institute`
:   author affiliations: can be a list when there are multiple authors

`revealjs-url`
:   base URL for reveal.js documents (defaults to `https://unpkg.com/reveal.js@^5`)

`s5-url`
:   base URL for S5 documents (defaults to `s5/default`)

`slidy-url`
:   base URL for Slidy documents (defaults to `https://www.w3.org/Talks/Tools/Slidy2`)

`slideous-url`
:   base URL for Slideous documents (defaults to `slideous`)

`title-slide-attributes`
:   additional attributes for the title slide of reveal.js slide shows. See [background in reveal.js, beamer, and pptx](#background-in-reveal.js-beamer-and-pptx) for an example.

`highlightjs-theme`
:   highlight.js theme for code highlighting when using [`--syntax-highlighting=idiomatic`](#option--syntax-highlighting){.option} with reveal.js (defaults to `monokai`). See the [highlight.js demo page](https://highlightjs.org/demo) for available themes.

All [reveal.js configuration options](https://revealjs.com/config/) are available as variables. To turn off boolean flags that default to true in reveal.js, use `0`.
:::

::: {#variables-for-beamer-slides .section .level3}
### [](#variables-for-beamer-slides){.anchor aria-hidden="true"}Variables for Beamer slides

These variables change the appearance of PDF slides using [`beamer`](https://ctan.org/pkg/beamer).

`aspectratio`
:   slide aspect ratio (`43` for 4:3 \[default\], `169` for 16:9, `1610` for 16:10, `149` for 14:9, `141` for 1.41:1, `54` for 5:4, `32` for 3:2)

`beameroption`
:   add extra beamer option with `\setbeameroption{}`

`institute`
:   author affiliations: can be a list when there are multiple authors

`logo`
:   logo image for slides

`logooptions`
:   options for logo image (e.g., `width`, `height`)

`navigation`
:   controls navigation symbols (default is `empty` for no navigation symbols; other valid values are `frame`, `vertical`, and `horizontal`)

`section-titles`
:   enables "title pages" for new sections (default is true)

`theme`, `colortheme`, `fonttheme`, `innertheme`, `outertheme`
:   beamer themes

`themeoptions`, `colorthemeoptions`, `fontthemeoptions`, `innerthemeoptions`, `outerthemeoptions`
:   options for LaTeX beamer themes (lists)

`titlegraphic`
:   image for title slide: can be a list

`titlegraphicoptions`
:   options for title slide image (e.g., `width`, `height`)

`shorttitle`, `shortsubtitle`, `shortauthor`, `shortinstitute`, `shortdate`
:   some beamer themes use short versions of the title, subtitle, author, institute, date
:::

::: {#variables-for-powerpoint .section .level3}
### [](#variables-for-powerpoint){.anchor aria-hidden="true"}Variables for PowerPoint

These variables control the visual aspects of a slide show that are not easily controlled via templates.

`monofont`
:   font to use for code.
:::

::::::::: {#variables-for-latex .section .level3}
### [](#variables-for-latex){.anchor aria-hidden="true"}Variables for LaTeX

Pandoc uses these variables when [creating a PDF](#creating-a-pdf) with a LaTeX engine.

::: {#layout .section .level4}
#### [](#layout){.anchor aria-hidden="true"}Layout

`block-headings`

:   make `\paragraph` and `\subparagraph` (fourth- and fifth-level headings, or fifth- and sixth-level with book classes) free-standing rather than run-in; requires further formatting to distinguish from `\subsubsection` (third- or fourth-level headings). Instead of using this option, [KOMA-Script](https://ctan.org/pkg/koma-script) can adjust headings more extensively:

        ---
        documentclass: scrartcl
        header-includes: |
          \RedeclareSectionCommand[
            beforeskip=-10pt plus -2pt minus -1pt,
            afterskip=1sp plus -1sp minus 1sp,
            font=\normalfont\itshape]{paragraph}
          \RedeclareSectionCommand[
            beforeskip=-10pt plus -2pt minus -1pt,
            afterskip=1sp plus -1sp minus 1sp,
            font=\normalfont\scshape,
            indent=0pt]{subparagraph}
        ...

`classoption`

:   option for document class, e.g. `oneside`; repeat for multiple options:

        ---
        classoption:
        - twocolumn
        - landscape
        ...

`documentclass`
:   document class: usually one of the standard classes, [`article`](https://ctan.org/pkg/article), [`book`](https://ctan.org/pkg/book), and [`report`](https://ctan.org/pkg/report); the [KOMA-Script](https://ctan.org/pkg/koma-script) equivalents, `scrartcl`, `scrbook`, and `scrreprt`, which default to smaller margins; or [`memoir`](https://ctan.org/pkg/memoir)

`geometry`

:   option for [`geometry`](https://ctan.org/pkg/geometry) package, e.g. `margin=1in`; repeat for multiple options:

        ---
        geometry:
        - top=30mm
        - left=20mm
        - heightrounded
        ...

`shorthands`
:   Enable language-specific shorthands when loading `babel`. (By default, pandoc includes `shorthands=off` when loading `babel`, disabling language-specific shorthands.)

`hyperrefoptions`

:   option for [`hyperref`](https://ctan.org/pkg/hyperref) package, e.g. `linktoc=all`; repeat for multiple options:

        ---
        hyperrefoptions:
        - linktoc=all
        - pdfwindowui
        - pdfpagemode=FullScreen
        ...

`indent`
:   if true, pandoc will use document class settings for indentation (the default LaTeX template otherwise removes indentation and adds space between paragraphs)

`linestretch`
:   adjusts line spacing using the [`setspace`](https://ctan.org/pkg/setspace) package, e.g. `1.25`, `1.5`

`margin-left`, `margin-right`, `margin-top`, `margin-bottom`
:   sets margins if `geometry` is not used (otherwise `geometry` overrides these)

`pagestyle`
:   control `\pagestyle{}`: the default article class supports `plain` (default), `empty` (no running heads or page numbers), and `headings` (section titles in running heads)

`papersize`
:   paper size, e.g. `letter`, `a4`

`secnumdepth`
:   numbering depth for sections (with [`--number-sections`](#option--number-sections){.option} option or `numbersections` variable)

`beamerarticle`
:   produce an article from Beamer slides. Note: if you set this variable, you must specify the beamer writer but use the default *LaTeX* template: for example, `pandoc -Vbeamerarticle -t beamer --template default.latex`.

`handout`
:   produce a handout version of Beamer slides (with overlays condensed into single slides)

`csquotes`
:   load `csquotes` package and use `\enquote` or `\enquote*` for quoted text.

`csquotesoptions`
:   options to use for `csquotes` package (repeat for multiple options).

`babeloptions`
:   options to pass to the babel package (may be repeated for multiple options). This defaults to `provide=*` if the main language isn't a European language written with Latin or Cyrillic script or Vietnamese. Most users will not need to adjust the default setting.
:::

::: {#fonts .section .level4}
#### [](#fonts){.anchor aria-hidden="true"}Fonts

`fontenc`
:   allows font encoding to be specified through `fontenc` package (with `pdflatex`); default is `T1` (see [LaTeX font encodings guide](https://ctan.org/pkg/encguide))

`fontfamily`
:   font package for use with `pdflatex`: [TeX Live](https://www.tug.org/texlive/) includes many options, documented in the [LaTeX Font Catalogue](https://tug.org/FontCatalogue/). The default is [Latin Modern](https://ctan.org/pkg/lm).

`fontfamilyoptions`

:   options for package used as `fontfamily`; repeat for multiple options. For example, to use the Libertine font with proportional lowercase (old-style) figures through the [`libertinus`](https://ctan.org/pkg/libertinus) package:

        ---
        fontfamily: libertinus
        fontfamilyoptions:
        - osf
        - p
        ...

`fontsize`
:   font size for body text. The standard classes allow 10pt, 11pt, and 12pt. To use another size, set `documentclass` to one of the [KOMA-Script](https://ctan.org/pkg/koma-script) classes, such as `scrartcl` or `scrbook`.

`mainfont`, `sansfont`, `monofont`, `mathfont`, `CJKmainfont`, `CJKsansfont`, `CJKmonofont`
:   font families for use with `xelatex` or `lualatex`: take the name of any system font, using the [`fontspec`](https://ctan.org/pkg/fontspec) package. `CJKmainfont` uses the [`xecjk`](https://ctan.org/pkg/xecjk) package if `xelatex` is used, or the [`luatexja`](https://ctan.org/pkg/luatexja) package if `lualatex` is used.

`mainfontoptions`, `sansfontoptions`, `monofontoptions`, `mathfontoptions`, `CJKoptions`, `luatexjapresetoptions`

:   options to use with `mainfont`, `sansfont`, `monofont`, `mathfont`, `CJKmainfont` in `xelatex` and `lualatex`. Allow for any choices available through [`fontspec`](https://ctan.org/pkg/fontspec); repeat for multiple options. For example, to use the [TeX Gyre](http://www.gust.org.pl/projects/e-foundry/tex-gyre) version of Palatino with lowercase figures:

        ---
        mainfont: TeX Gyre Pagella
        mainfontoptions:
        - Numbers=Lowercase
        - Numbers=Proportional
        ...

`mainfontfallback`, `sansfontfallback`, `monofontfallback`

:   fonts to try if a glyph isn't found in `mainfont`, `sansfont`, or `monofont` respectively. These are lists. The font name must be followed by a colon and optionally a set of options, for example:

        ---
        mainfontfallback:
          - "FreeSans:"
          - "NotoColorEmoji:mode=harf"
        ...

    Font fallbacks currently only work with `lualatex`.

`babelfonts`

:   a map of Babel language names (e.g. `chinese`) to the font to be used with the language:

        ---
        babelfonts:
          chinese-hant: "Noto Serif CJK TC"
          russian: "Noto Serif"
        ...

`microtypeoptions`
:   options to pass to the microtype package
:::

::: {#links .section .level4}
#### [](#links){.anchor aria-hidden="true"}Links

`colorlinks`
:   add color to link text; automatically enabled if any of `linkcolor`, `filecolor`, `citecolor`, `urlcolor`, or `toccolor` are set

`boxlinks`
:   add visible box around links (has no effect if `colorlinks` is set)

`linkcolor`, `filecolor`, `citecolor`, `urlcolor`, `toccolor`
:   color for internal links, external links, citation links, linked URLs, and links in table of contents, respectively: uses options allowed by [`xcolor`](https://ctan.org/pkg/xcolor), including the `dvipsnames`, `svgnames`, and `x11names` lists

`links-as-notes`
:   causes links to be printed as footnotes

`urlstyle`
:   style for URLs (e.g., `tt`, `rm`, `sf`, and, the default, `same`)
:::

::: {#front-matter .section .level4}
#### [](#front-matter){.anchor aria-hidden="true"}Front matter

`lof`, `lot`
:   include list of figures, list of tables (can also be set using [`--lof/--list-of-figures`](#option--lof%5B){.option}, [`--lot/--list-of-tables`](#option--lot%5B){.option})

`thanks`
:   contents of acknowledgments footnote after document title

`toc`
:   include table of contents (can also be set using [`--toc/--table-of-contents`](#option--toc%5B){.option})

`toc-depth`
:   level of section to include in table of contents
:::

::: {#biblatex-bibliographies .section .level4}
#### [](#biblatex-bibliographies){.anchor aria-hidden="true"}BibLaTeX Bibliographies

These variables function when using BibLaTeX for [citation rendering](#citation-rendering).

`biblatexoptions`
:   list of options for biblatex

`biblio-style`
:   bibliography style, when used with [`--natbib`](#option--natbib){.option} and [`--biblatex`](#option--biblatex){.option}

`biblio-title`
:   bibliography title, when used with [`--natbib`](#option--natbib){.option} and [`--biblatex`](#option--biblatex){.option}

`bibliography`
:   bibliography to use for resolving references

`natbiboptions`
:   list of options for natbib
:::

::: {#other .section .level4}
#### [](#other){.anchor aria-hidden="true"}Other

`pdf-trailer-id`
:   the PDF trailer ID; must be two PDF byte strings if set, conventionally with 16 bytes each. E.g., `<00112233445566778899aabbccddeeff> <00112233445566778899aabbccddeeff>`. See the section on [reproducible builds](#reproducible-builds).

`pdfstandard`

:   PDF standard(s) for the document, e.g. `ua-2`, `a-4f`. Supports PDF/A, PDF/X, and PDF/UA variants. Requires LuaLaTeX and LaTeX 2023+. Repeat for multiple standards:

        ---
        pdfstandard:
        - ua-2
        - a-4f
        ...
:::
:::::::::

::: {#variables-for-context .section .level3}
### [](#variables-for-context){.anchor aria-hidden="true"}Variables for ConTeXt

Pandoc uses these variables when [creating a PDF](#creating-a-pdf) with ConTeXt.

`fontsize`
:   font size for body text (e.g. `10pt`, `12pt`)

`headertext`, `footertext`
:   text to be placed in running header or footer (see [ConTeXt Headers and Footers](https://wiki.contextgarden.net/Document_layout_and_layers/Headers_and_footers)); repeat up to four times for different placement

`indenting`
:   controls indentation of paragraphs, e.g. `yes,small,next` (see [ConTeXt Indentation](https://wiki.contextgarden.net/Text_blocks/Typography/Indentation)); repeat for multiple options

`interlinespace`
:   adjusts line spacing, e.g. `4ex` (using [`setupinterlinespace`](https://wiki.contextgarden.net/Command/setupinterlinespace)); repeat for multiple options

`layout`
:   options for page margins and text arrangement (see [ConTeXt Layout](https://wiki.contextgarden.net/Document_layout_and_layers/Tutorials)); repeat for multiple options

`linkcolor`, `contrastcolor`
:   color for links outside and inside a page, e.g. `red`, `blue` (see [ConTeXt Color](https://wiki.contextgarden.net/Color))

`linkstyle`
:   typeface style for links, e.g. `normal`, `bold`, `slanted`, `boldslanted`, `type`, `cap`, `small`

`lof`, `lot`
:   include list of figures, list of tables

`mainfont`, `sansfont`, `monofont`, `mathfont`
:   font families: take the name of any system font (see [ConTeXt Font Switching](https://wiki.contextgarden.net/Characters_words_and_fonts/Tutorials))

`mainfontfallback`, `sansfontfallback`, `monofontfallback`
:   list of fonts to try, in order, if a glyph is not found in the main font. Use `\definefallbackfamily`-compatible font name syntax. Emoji fonts are unsupported.

`margin-left`, `margin-right`, `margin-top`, `margin-bottom`
:   sets margins, if `layout` is not used (otherwise `layout` overrides these)

`pagenumbering`
:   page number style and location (using [`setuppagenumbering`](https://wiki.contextgarden.net/Command/setuppagenumbering)); repeat for multiple options

`papersize`
:   paper size, e.g. `letter`, `A4`, `landscape` (see [ConTeXt Paper Setup](https://wiki.contextgarden.net/Document_layout_and_layers/Paper_setup)); repeat for multiple options

`pdfa`
:   adds to the preamble the setup necessary to generate PDF/A of the type specified, e.g. `1a:2005`, `2a`. If no type is specified (i.e. the value is set to True, by e.g. [`--metadata=pdfa`](#option--metadata){.option} or `pdfa: true` in a YAML metadata block), `1b:2005` will be used as default, for reasons of backwards compatibility. Using [`--variable=pdfa`](#option--variable){.option} without specified value is not supported. To successfully generate PDF/A the required ICC color profiles have to be available and the content and all included files (such as images) have to be standard-conforming. The ICC profiles and output intent may be specified using the variables `pdfaiccprofile` and `pdfaintent`. See also [ConTeXt PDFA](https://wiki.contextgarden.net/Input_and_compilation/PDF/PDFA) for more details.

`pdfaiccprofile`
:   when used in conjunction with `pdfa`, specifies the ICC profile to use in the PDF, e.g. `default.cmyk`. If left unspecified, `sRGB.icc` is used as default. May be repeated to include multiple profiles. Note that the profiles have to be available on the system. They can be obtained from [ConTeXt ICC Profiles](https://wiki.contextgarden.net/Input_and_compilation/PDF/PDFX#ICC_profiles).

`pdfaintent`
:   when used in conjunction with `pdfa`, specifies the output intent for the colors, e.g. `ISO coated v2 300\letterpercent\space (ECI)` If left unspecified, `sRGB IEC61966-2.1` is used as default.

`toc`
:   include table of contents (can also be set using [`--toc/--table-of-contents`](#option--toc%5B){.option})

`urlstyle`
:   typeface style for links without link text, e.g. `normal`, `bold`, `slanted`, `boldslanted`, `type`, `cap`, `small`

`whitespace`
:   spacing between paragraphs, e.g. `none`, `small` (using [`setupwhitespace`](https://wiki.contextgarden.net/Command/setupwhitespace))

`includesource`
:   include all source documents as file attachments in the PDF file
:::

::: {#variables-for-wkhtmltopdf .section .level3}
### [](#variables-for-wkhtmltopdf){.anchor aria-hidden="true"}Variables for `wkhtmltopdf`

Pandoc uses these variables when [creating a PDF](#creating-a-pdf) with [`wkhtmltopdf`](https://wkhtmltopdf.org). The [`--css`](#option--css){.option} option also affects the output.

`footer-html`, `header-html`
:   add information to the header and footer

`margin-left`, `margin-right`, `margin-top`, `margin-bottom`
:   set the page margins

`papersize`
:   sets the PDF paper size
:::

::: {#variables-for-man-pages .section .level3}
### [](#variables-for-man-pages){.anchor aria-hidden="true"}Variables for man pages

`adjusting`
:   adjusts text to left (`l`), right (`r`), center (`c`), or both (`b`) margins

`footer`
:   footer in man pages

`header`
:   header in man pages

`section`
:   section number in man pages
:::

::: {#variables-for-texinfo .section .level3}
### [](#variables-for-texinfo){.anchor aria-hidden="true"}Variables for Texinfo

`version`
:   version of software (used in title and title page)

`filename`
:   name of info file to be generated (defaults to a name based on the texi filename)
:::

::: {#variables-for-typst .section .level3}
### [](#variables-for-typst){.anchor aria-hidden="true"}Variables for Typst

`template`
:   Typst template to use (relative path only).

`margin`
:   A dictionary with the fields defined in the Typst documentation: `x`, `y`, `top`, `bottom`, `left`, `right`.

`papersize`
:   Paper size: `a4`, `us-letter`, etc.

`mainfont`
:   Name of system font to use for the main font.

`fontsize`
:   Font size (e.g., `12pt`).

`section-numbering`
:   Schema to use for numbering sections, e.g. `1.A.1`.

`page-numbering`
:   Schema to use for numbering pages, e.g. `1` or `i`, or an empty string to omit page numbering.

`columns`
:   Number of columns for body text.

`thanks`
:   contents of acknowledgments footnote after document title

`mathfont`, `codefont`
:   Name of system font to use for math and code, respectively.

`linestretch`
:   adjusts line spacing, e.g. `1.25`, `1.5`

`linkcolor`, `filecolor`, `citecolor`
:   color for external links, internal links, and citation links, respectively: expects a hexadecimal color code
:::

::: {#variables-for-ms .section .level3}
### [](#variables-for-ms){.anchor aria-hidden="true"}Variables for ms

`fontfamily`
:   `A` (Avant Garde), `B` (Bookman), `C` (Helvetica), `HN` (Helvetica Narrow), `P` (Palatino), or `T` (Times New Roman). This setting does not affect source code, which is always displayed using monospace Courier. These built-in fonts are limited in their coverage of characters. Additional fonts may be installed using the script [`install-font.sh`](https://www.schaffter.ca/mom/bin/install-font.sh) provided by Peter Schaffter and documented in detail on [his web site](https://www.schaffter.ca/mom/momdoc/appendices.html#steps).

`indent`
:   paragraph indent (e.g. `2m`)

`lineheight`
:   line height (e.g. `12p`)

`pointsize`
:   point size (e.g. `10p`)
:::

::: {#variables-set-automatically .section .level3}
### [](#variables-set-automatically){.anchor aria-hidden="true"}Variables set automatically

Pandoc sets these variables automatically in response to [options](#options) or document contents; users can also modify them. These vary depending on the output format, and include the following:

`body`
:   body of document

`date-meta`
:   the `date` variable converted to ISO 8601 YYYY-MM-DD, included in all HTML based formats (dzslides, epub, html, html4, html5, revealjs, s5, slideous, slidy). The recognized formats for `date` are: `mm/dd/yyyy`, `mm/dd/yy`, `yyyy-mm-dd` (ISO 8601), `dd MM yyyy` (e.g. either `02 Apr 2018` or `02 April 2018`), `MM dd, yyyy` (e.g. `Apr. 02, 2018` or `April 02, 2018),`yyyy\[mm\[dd\]\]`(e.g.`20180402, `201804` or `2018`).

`header-includes`
:   contents specified by [`-H/--include-in-header`](#option--include-in-header){.option} (may have multiple values)

`include-before`
:   contents specified by [`-B/--include-before-body`](#option--include-before-body){.option} (may have multiple values)

`include-after`
:   contents specified by [`-A/--include-after-body`](#option--include-after-body){.option} (may have multiple values)

`meta-json`
:   JSON representation of all of the document's metadata. Field values are transformed to the selected output format.

`numbersections`
:   non-null value if [`-N/--number-sections`](#option--number-sections){.option} was specified

`sourcefile`, `outputfile`

:   source and destination filenames, as given on the command line. `sourcefile` can also be a list if input comes from multiple files, or empty if input is from stdin. You can use the following snippet in your template to distinguish them:

        $if(sourcefile)$
        $for(sourcefile)$
        $sourcefile$
        $endfor$
        $else$
        (stdin)
        $endif$

    Similarly, `outputfile` can be `-` if output goes to the terminal. If you need absolute paths, use e.g. `$curdir$/$sourcefile$`.

`pdf-engine`
:   name of PDF engine if provided using [`--pdf-engine`](#option--pdf-engine){.option}, or the default engine for the format if PDF output is requested.

`curdir`
:   working directory from which pandoc is run.

`pandoc-version`
:   pandoc version.

`toc`
:   non-null value if [`--toc/--table-of-contents`](#option--toc%5B){.option} was specified

`toc-title`
:   title of table of contents (works only with EPUB, HTML, revealjs, opendocument, odt, docx, pptx, beamer, LaTeX). Note that in docx and pptx a custom `toc-title` will be picked up from metadata, but cannot be set as a variable.
:::
::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::
