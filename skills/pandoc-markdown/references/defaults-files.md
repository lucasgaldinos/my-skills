:::::::::::::: {#defaults-files .section .level1}
# [](#defaults-files){.anchor aria-hidden="true"}Defaults files

The [`--defaults`](#option--defaults){.option} option may be used to specify a package of options, in the form of a YAML or JSON file. Examples in this section will be given in YAML, but the equivalent forms in JSON will also work.

Fields that are omitted will just have their regular default values. So a defaults file can be as simple as one line:

::: {#cb18 .sourceCode}
``` {.sourceCode .yaml}
verbosity: INFO
```
:::

or in JSON:

::: {#cb19 .sourceCode}
``` {.sourceCode .json}
{ "verbosity": "INFO" }
```
:::

In fields that expect a file path (or list of file paths), the following syntax may be used to interpolate environment variables:

::: {#cb20 .sourceCode}
``` {.sourceCode .yaml}
csl:  ${HOME}/mycsldir/special.csl
```
:::

`${USERDATA}` may also be used; this will always resolve to the user data directory that is current when the defaults file is parsed, regardless of the setting of the environment variable `USERDATA`.

`${.}` will resolve to the directory containing the defaults file itself. This allows you to refer to resources contained in that directory:

::: {#cb21 .sourceCode}
``` {.sourceCode .yaml}
epub-cover-image: ${.}/cover.jpg
epub-metadata: ${.}/meta.xml
resource-path:
- .             # the working directory from which pandoc is run
- ${.}/images   # the images subdirectory of the directory
                # containing this defaults file
```
:::

This environment variable interpolation syntax *only* works in fields that expect file paths.

Defaults files can be placed in the `defaults` subdirectory of the user data directory and used from any directory. For example, one could create a file specifying defaults for writing letters, save it as `letter.yaml` in the `defaults` subdirectory of the user data directory, and then invoke these defaults from any directory using `pandoc --defaults letter` or `pandoc -dletter`.

When multiple defaults are used, their contents will be combined.

Note that, where command-line arguments may be repeated ([`--metadata-file`](#option--metadata-file){.option}, [`--css`](#option--css){.option}, [`--include-in-header`](#option--include-in-header){.option}, [`--include-before-body`](#option--include-before-body){.option}, [`--include-after-body`](#option--include-after-body){.option}, [`--variable`](#option--variable){.option}, [`--metadata`](#option--metadata){.option}, [`--syntax-definition`](#option--syntax-definition){.option}), the values specified on the command line will combine with values specified in the defaults file, rather than replacing them.

The following tables show the mapping between the command line and defaults file entries.

+---------------------------------+-----------------------------------+
| command line                    | defaults file                     |
+:================================+:==================================+
|     foo.md                      | ::: {#cb23 .sourceCode}           |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | input-file: foo.md                |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     foo.md bar.md               | ::: {#cb25 .sourceCode}           |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | input-files:                      |
|                                 |   - foo.md                        |
|                                 |   - bar.md                        |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+

The value of `input-files` may be left empty to indicate input from stdin, and it can be an empty sequence `[]` for no input.

::: {#general-options-1 .section .level2}
## [](#general-options-1){.anchor aria-hidden="true"}General options

+------------------------------------+-----------------------------------+
| command line                       | defaults file                     |
+:===================================+:==================================+
|     --from markdown+emoji          | ::: {#cb27 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | from: markdown+emoji              |
|                                    | ```                               |
|                                    | :::                               |
|                                    |                                   |
|                                    | ::: {#cb28 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | reader: markdown+emoji            |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --to markdown+hard_line_breaks | ::: {#cb30 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | to: markdown+hard_line_breaks     |
|                                    | ```                               |
|                                    | :::                               |
|                                    |                                   |
|                                    | ::: {#cb31 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | writer: markdown+hard_line_breaks |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --output foo.pdf               | ::: {#cb33 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | output-file: foo.pdf              |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --output -                     | ::: {#cb35 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | output-file:                      |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --data-dir dir                 | ::: {#cb37 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | data-dir: dir                     |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --defaults file                | ::: {#cb39 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | defaults:                         |
|                                    | - file                            |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --verbose                      | ::: {#cb41 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | verbosity: INFO                   |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --quiet                        | ::: {#cb43 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | verbosity: ERROR                  |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --fail-if-warnings             | ::: {#cb45 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | fail-if-warnings: true            |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --sandbox                      | ::: {#cb47 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | sandbox: true                     |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --log=FILE                     | ::: {#cb49 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | log-file: FILE                    |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+

Options specified in a defaults file itself always have priority over those in another file included with a `defaults:` entry.

`verbosity` can have the values `ERROR`, `WARNING`, or `INFO`.
:::

::: {#reader-options-1 .section .level2}
## [](#reader-options-1){.anchor aria-hidden="true"}Reader options

+--------------------------------------+-----------------------------------+
| command line                         | defaults file                     |
+:=====================================+:==================================+
|     --shift-heading-level-by -1      | ::: {#cb51 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | shift-heading-level-by: -1        |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --indented-code-classes python   | ::: {#cb53 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | indented-code-classes:            |
|                                      |   - python                        |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --default-image-extension ".jpg" | ::: {#cb55 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | default-image-extension: '.jpg'   |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --file-scope                     | ::: {#cb57 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | file-scope: true                  |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --citeproc \                     | ::: {#cb59 .sourceCode}           |
|      --lua-filter count-words.lua \  | ``` {.sourceCode .yaml}           |
|      --filter special.lua            | filters:                          |
|                                      |   - citeproc                      |
|                                      |   - count-words.lua               |
|                                      |   - type: json                    |
|                                      |     path: special.lua             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --metadata key=value \           | ::: {#cb61 .sourceCode}           |
|      --metadata key2                 | ``` {.sourceCode .yaml}           |
|                                      | metadata:                         |
|                                      |   key: value                      |
|                                      |   key2: true                      |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --metadata-file meta.yaml        | ::: {#cb63 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | metadata-files:                   |
|                                      |   - meta.yaml                     |
|                                      | ```                               |
|                                      | :::                               |
|                                      |                                   |
|                                      | ::: {#cb64 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | metadata-file: meta.yaml          |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --preserve-tabs                  | ::: {#cb66 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | preserve-tabs: true               |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --tab-stop 8                     | ::: {#cb68 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | tab-stop: 8                       |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --track-changes accept           | ::: {#cb70 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | track-changes: accept             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --extract-media dir              | ::: {#cb72 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | extract-media: dir                |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --abbreviations abbrevs.txt      | ::: {#cb74 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | abbreviations: abbrevs.txt        |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --trace                          | ::: {#cb76 .sourceCode}           |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | trace: true                       |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+

Metadata values specified in a defaults file are parsed as literal string text, not Markdown.

Filters will be assumed to be Lua filters if they have the `.lua` extension, and JSON filters otherwise. But the filter type can also be specified explicitly, as shown. Filters are run in the order specified. To include the built-in citeproc filter, use either `citeproc` or `{type: citeproc}`.
:::

::: {#general-writer-options-1 .section .level2}
## [](#general-writer-options-1){.anchor aria-hidden="true"}General writer options

+------------------------------------+-----------------------------------+
| command line                       | defaults file                     |
+:===================================+:==================================+
|     --standalone                   | ::: {#cb78 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | standalone: true                  |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --template letter              | ::: {#cb80 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | template: letter                  |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --variable key=val \           | ::: {#cb82 .sourceCode}           |
|       --variable key2              | ``` {.sourceCode .yaml}           |
|                                    | variables:                        |
|                                    |   key: val                        |
|                                    |   key2: true                      |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --eol nl                       | ::: {#cb84 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | eol: nl                           |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --dpi 300                      | ::: {#cb86 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | dpi: 300                          |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --wrap preserve                | ::: {#cb88 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | wrap: "preserve"                  |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --columns 72                   | ::: {#cb90 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | columns: 72                       |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --table-of-contents            | ::: {#cb92 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | table-of-contents: true           |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --toc                          | ::: {#cb94 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | toc: true                         |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --toc-depth 3                  | ::: {#cb96 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | toc-depth: 3                      |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --strip-comments               | ::: {#cb98 .sourceCode}           |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | strip-comments: true              |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --no-highlight                 | ::: {#cb100 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | syntax-highlighting: 'none'       |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --syntax-highlighting kate     | ::: {#cb102 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | syntax-highlighting: kate         |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --syntax-definition mylang.xml | ::: {#cb104 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | syntax-definitions:               |
|                                    |   - mylang.xml                    |
|                                    | ```                               |
|                                    | :::                               |
|                                    |                                   |
|                                    | ::: {#cb105 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | syntax-definition: mylang.xml     |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --include-in-header inc.tex    | ::: {#cb107 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | include-in-header:                |
|                                    |   - inc.tex                       |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --include-before-body inc.tex  | ::: {#cb109 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | include-before-body:              |
|                                    |   - inc.tex                       |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --include-after-body inc.tex   | ::: {#cb111 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | include-after-body:               |
|                                    |   - inc.tex                       |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --resource-path .:foo          | ::: {#cb113 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | resource-path: ['.','foo']        |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --request-header foo:bar       | ::: {#cb115 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | request-headers:                  |
|                                    |   - ["User-Agent", "Mozilla/5.0"] |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
|     --no-check-certificate         | ::: {#cb117 .sourceCode}          |
|                                    | ``` {.sourceCode .yaml}           |
|                                    | no-check-certificate: true        |
|                                    | ```                               |
|                                    | :::                               |
+------------------------------------+-----------------------------------+
:::

::: {#options-affecting-specific-writers-1 .section .level2}
## [](#options-affecting-specific-writers-1){.anchor aria-hidden="true"}Options affecting specific writers

+--------------------------------------+-----------------------------------+
| command line                         | defaults file                     |
+:=====================================+:==================================+
|     --self-contained                 | ::: {#cb119 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | self-contained: true              |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --link-images                    | ::: {#cb121 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | link-images: true                 |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --html-q-tags                    | ::: {#cb123 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | html-q-tags: true                 |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --ascii                          | ::: {#cb125 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | ascii: true                       |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --reference-links                | ::: {#cb127 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | reference-links: true             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --reference-location block       | ::: {#cb129 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | reference-location: block         |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --figure-caption-position=above  | ::: {#cb131 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | figure-caption-position: above    |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --table-caption-position=below   | ::: {#cb133 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | table-caption-position: below     |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --markdown-headings atx          | ::: {#cb135 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | markdown-headings: atx            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --list-tables                    | ::: {#cb137 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | list-tables: true                 |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --top-level-division chapter     | ::: {#cb139 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | top-level-division: chapter       |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --number-sections                | ::: {#cb141 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | number-sections: true             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --number-offset=1,4              | ::: {#cb143 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | number-offset: \[1,4\]            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --listings                       | ::: {#cb145 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | listings: true                    |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --list-of-figures                | ::: {#cb147 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | list-of-figures: true             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --lof                            | ::: {#cb149 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | lof: true                         |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --list-of-tables                 | ::: {#cb151 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | list-of-tables: true              |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --lot                            | ::: {#cb153 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | lot: true                         |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --incremental                    | ::: {#cb155 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | incremental: true                 |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --slide-level 2                  | ::: {#cb157 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | slide-level: 2                    |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --section-divs                   | ::: {#cb159 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | section-divs: true                |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --email-obfuscation references   | ::: {#cb161 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | email-obfuscation: references     |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --id-prefix ch1                  | ::: {#cb163 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | identifier-prefix: ch1            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --title-prefix MySite            | ::: {#cb165 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | title-prefix: MySite              |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --css styles/screen.css  \       | ::: {#cb167 .sourceCode}          |
|       --css styles/special.css       | ``` {.sourceCode .yaml}           |
|                                      | css:                              |
|                                      |   - styles/screen.css             |
|                                      |   - styles/special.css            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --reference-doc my.docx          | ::: {#cb169 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | reference-doc: my.docx            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --epub-cover-image cover.jpg     | ::: {#cb171 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | epub-cover-image: cover.jpg       |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --epub-title-page=false          | ::: {#cb173 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | epub-title-page: false            |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --epub-metadata meta.xml         | ::: {#cb175 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | epub-metadata: meta.xml           |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --epub-embed-font special.otf \  | ::: {#cb177 .sourceCode}          |
|       --epub-embed-font headline.otf | ``` {.sourceCode .yaml}           |
|                                      | epub-fonts:                       |
|                                      |   - special.otf                   |
|                                      |   - headline.otf                  |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --split-level 2                  | ::: {#cb179 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | split-level: 2                    |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --chunk-template="%i.html"       | ::: {#cb181 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | chunk-template: "%i.html"         |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --epub-subdirectory=""           | ::: {#cb183 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | epub-subdirectory: ''             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --ipynb-output best              | ::: {#cb185 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | ipynb-output: best                |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --pdf-engine xelatex             | ::: {#cb187 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | pdf-engine: xelatex               |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --pdf-engine-opt=--shell-escape  | ::: {#cb189 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | pdf-engine-opts:                  |
|                                      |   - '-shell-escape'               |
|                                      | ```                               |
|                                      | :::                               |
|                                      |                                   |
|                                      | ::: {#cb190 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | pdf-engine-opt: '-shell-escape'   |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
:::

::: {#citation-rendering-1 .section .level2}
## [](#citation-rendering-1){.anchor aria-hidden="true"}Citation rendering

+--------------------------------------+-----------------------------------+
| command line                         | defaults file                     |
+:=====================================+:==================================+
|     --citeproc                       | ::: {#cb192 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | citeproc: true                    |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --bibliography logic.bib         | ::: {#cb194 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | bibliography: logic.bib           |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --csl ieee.csl                   | ::: {#cb196 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | csl: ieee.csl                     |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --citation-abbreviations ab.json | ::: {#cb198 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | citation-abbreviations: ab.json   |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --natbib                         | ::: {#cb200 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | cite-method: natbib               |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+
|     --biblatex                       | ::: {#cb202 .sourceCode}          |
|                                      | ``` {.sourceCode .yaml}           |
|                                      | cite-method: biblatex             |
|                                      | ```                               |
|                                      | :::                               |
+--------------------------------------+-----------------------------------+

`cite-method` can be `citeproc`, `natbib`, or `biblatex`. This only affects LaTeX output. If you want to use citeproc to format citations, you should also set 'citeproc: true'.

If you need control over when the citeproc processing is done relative to other filters, you should instead use `citeproc` in the list of `filters` (see [Reader options](#reader-options-1)).
:::

::: {#math-rendering-in-html-1 .section .level2}
## [](#math-rendering-in-html-1){.anchor aria-hidden="true"}Math rendering in HTML

+---------------------------------+-----------------------------------+
| command line                    | defaults file                     |
+:================================+:==================================+
|     --mathjax                   | ::: {#cb204 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | html-math-method:                 |
|                                 |   method: mathjax                 |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     --mathml                    | ::: {#cb206 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | html-math-method:                 |
|                                 |   method: mathml                  |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     --webtex                    | ::: {#cb208 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | html-math-method:                 |
|                                 |   method: webtex                  |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     --katex                     | ::: {#cb210 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | html-math-method:                 |
|                                 |   method: katex                   |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     --gladtex                   | ::: {#cb212 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | html-math-method:                 |
|                                 |   method: gladtex                 |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+

In addition to the values listed above, `method` can have the value `plain`.

If the command line option accepts a URL argument, an `url:` field can be added to `html-math-method:`.
:::

::: {#options-for-wrapper-scripts-1 .section .level2}
## [](#options-for-wrapper-scripts-1){.anchor aria-hidden="true"}Options for wrapper scripts

+---------------------------------+-----------------------------------+
| command line                    | defaults file                     |
+:================================+:==================================+
|     --dump-args                 | ::: {#cb214 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | dump-args: true                   |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
|     --ignore-args               | ::: {#cb216 .sourceCode}          |
|                                 | ``` {.sourceCode .yaml}           |
|                                 | ignore-args: true                 |
|                                 | ```                               |
|                                 | :::                               |
+---------------------------------+-----------------------------------+
:::
::::::::::::::
