::::::: {#epubs .section .level1}
# [](#epubs){.anchor aria-hidden="true"}EPUBs

::: {#epub-metadata .section .level2}
## [](#epub-metadata){.anchor aria-hidden="true"}EPUB Metadata

There are two ways to specify metadata for an EPUB. The first is to use the [`--epub-metadata`](#option--epub-metadata){.option} option, which takes as its argument an XML file with [Dublin Core elements](https://www.dublincore.org/specifications/dublin-core/dces/).

The second way is to use YAML, either in a [YAML metadata block](#extension-yaml_metadata_block) in a Markdown document, or in a separate YAML file specified with [`--metadata-file`](#option--metadata-file){.option}. Here is an example of a YAML metadata block with EPUB metadata:

    ---
    title:
    - type: main
      text: My Book
    - type: subtitle
      text: An investigation of metadata
    creator:
    - role: author
      text: John Smith
    - role: editor
      text: Sarah Jones
    identifier:
    - scheme: DOI
      text: doi:10.234234.234/33
    publisher:  My Press
    rights: © 2007 John Smith, CC BY-NC
    ibooks:
      version: 1.3.4
    ...

The following fields are recognized:

`identifier`
:   Either a string value or an object with fields `text` and `scheme`. Valid values for `scheme` are `ISBN-10`, `GTIN-13`, `UPC`, `ISMN-10`, `DOI`, `LCCN`, `GTIN-14`, `ISBN-13`, `Legal deposit number`, `URN`, `OCLC number`, `Co-publisher’s ISBN-13`, `ISMN-13`, `ISBN-A`, `JP e-code`, `OLCC number`, `JP Magazine ID`, `UPC-12+5`, `BNF Control number`, `ISSN-13`, `ARK`, `Digital file internal version number`.

`title`
:   Either a string value, or an object with fields `file-as` and `type`, or a list of such objects. Valid values for `type` are `main`, `subtitle`, `short`, `collection`, `edition`, `extended`.

`creator`
:   Either a string value, or an object with fields `role`, `file-as`, and `text`, or a list of such objects. Valid values for `role` are [MARC relators](https://loc.gov/marc/relators/relaterm.html), but pandoc will attempt to translate the human-readable versions (like "author" and "editor") to the appropriate marc relators.

`contributor`
:   Same format as `creator`.

`date`
:   A string value in `YYYY-MM-DD` format. (Only the year is necessary.) Pandoc will attempt to convert other common date formats.

`lang` (or legacy: `language`)
:   A string value in [BCP 47](https://tools.ietf.org/html/bcp47) format. Pandoc will default to the local language if nothing is specified.

`subject`
:   Either a string value, or an object with fields `text`, `authority`, and `term`, or a list of such objects. Valid values for `authority` are either a [reserved authority value](https://idpf.github.io/epub-registries/authorities/) (currently `AAT`, `BIC`, `BISAC`, `CLC`, `DDC`, `CLIL`, `EuroVoc`, `MEDTOP`, `LCSH`, `NDC`, `Thema`, `UDC`, and `WGS`) or an absolute IRI identifying a custom scheme. Valid values for `term` are defined by the scheme.

`description`
:   A string value.

`type`
:   A string value.

`format`
:   A string value.

`relation`
:   A string value.

`coverage`
:   A string value.

`rights`
:   A string value.

`belongs-to-collection`
:   A string value. Identifies the name of a collection to which the EPUB Publication belongs.

`group-position`
:   The `group-position` field indicates the numeric position in which the EPUB Publication belongs relative to other works belonging to the same `belongs-to-collection` field.

`cover-image`
:   A string value (path to cover image).

`css` (or legacy: `stylesheet`)
:   A string value (path to CSS stylesheet).

`page-progression-direction`
:   Either `ltr` or `rtl`. Specifies the `page-progression-direction` attribute for the [`spine` element](http://idpf.org/epub/301/spec/epub-publications.html#sec-spine-elem).

`accessModes`
:   An array of strings ([schema](https://kb.daisy.org/publishing/docs/metadata/schema.org/index.html)). Defaults to `["textual"]`.

`accessModeSufficient`
:   An array of strings ([schema](https://kb.daisy.org/publishing/docs/metadata/schema.org/index.html)). Defaults to `["textual"]`.

`accessibilityHazards`
:   An array of strings ([schema](https://kb.daisy.org/publishing/docs/metadata/schema.org/index.html)). Defaults to `["none"]`.

`accessibilityFeatures`

:   An array of strings ([schema](https://kb.daisy.org/publishing/docs/metadata/schema.org/index.html)). Defaults to

        - "alternativeText"
        - "readingOrder"
        - "structuralNavigation"
        - "tableOfContents"

`accessibilitySummary`
:   A string value.

`ibooks`
:   iBooks-specific metadata, with the following fields:
    -   `version`: (string)
    -   `specified-fonts`: `true`\|`false` (default `false`)
    -   `ipad-orientation-lock`: `portrait-only`\|`landscape-only`
    -   `iphone-orientation-lock`: `portrait-only`\|`landscape-only`
    -   `binding`: `true`\|`false` (default `true`)
    -   `scroll-axis`: `vertical`\|`horizontal`\|`default`
:::

::: {#the-epubtype-attribute .section .level2}
## [](#the-epubtype-attribute){.anchor aria-hidden="true"}The `epub:type` attribute

For `epub3` output, you can mark up the heading that corresponds to an EPUB chapter using the [`epub:type` attribute](http://www.idpf.org/epub/31/spec/epub-contentdocs.html#sec-epub-type-attribute). For example, to set the attribute to the value `prologue`, use this Markdown:

    # My chapter {epub:type=prologue}

Which will result in:

    <body epub:type="frontmatter">
      <section epub:type="prologue">
        <h1>My chapter</h1>

Pandoc will output `<body epub:type="bodymatter">`, unless you use one of the following values, in which case either `frontmatter` or `backmatter` will be output.

  `epub:type` of first section   `epub:type` of body
  ------------------------------ ---------------------
  prologue                       frontmatter
  abstract                       frontmatter
  acknowledgments                frontmatter
  copyright-page                 frontmatter
  dedication                     frontmatter
  credits                        frontmatter
  keywords                       frontmatter
  imprint                        frontmatter
  contributors                   frontmatter
  other-credits                  frontmatter
  errata                         frontmatter
  revision-history               frontmatter
  titlepage                      frontmatter
  halftitlepage                  frontmatter
  seriespage                     frontmatter
  foreword                       frontmatter
  preface                        frontmatter
  frontispiece                   frontmatter
  appendix                       backmatter
  colophon                       backmatter
  bibliography                   backmatter
  index                          backmatter
:::

::: {#linked-media .section .level2}
## [](#linked-media){.anchor aria-hidden="true"}Linked media

By default, pandoc will download media referenced from any `<img>`, `<audio>`, `<video>` or `<source>` element present in the generated EPUB, and include it in the EPUB container, yielding a completely self-contained EPUB. If you want to link to external media resources instead, use raw HTML in your source and add `data-external="1"` to the tag with the `src` attribute. For example:

    <audio controls="1">
      <source src="https://example.com/music/toccata.mp3"
              data-external="1" type="audio/mpeg">
      </source>
    </audio>

If the input format already is HTML then `data-external="1"` will work as expected for `<img>` elements. Similarly, for Markdown, external images can be declared with `![img](url){external=1}`. Note that this only works for images; the other media elements have no native representation in pandoc's AST and require the use of raw HTML.
:::

::: {#epub-styling .section .level2}
## [](#epub-styling){.anchor aria-hidden="true"}EPUB styling

By default, pandoc will include some basic styling contained in its `epub.css` data file. (To see this, use `pandoc --print-default-data-file epub.css`.) To use a different CSS file, just use the [`--css`](#option--css){.option} command line option. A few inline styles are defined in addition; these are essential for correct formatting of pandoc's HTML output.

The `document-css` variable may be set if the more opinionated styling of pandoc's default HTML templates is desired (and in that case the variables defined in [Variables for HTML](#variables-for-html) may be used to fine-tune the style).
:::
:::::::
