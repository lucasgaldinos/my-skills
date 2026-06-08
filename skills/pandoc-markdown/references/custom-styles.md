::::: {#custom-styles .section .level1}
# [](#custom-styles){.anchor aria-hidden="true"}Custom Styles

Custom styles can be used in the docx, odt and ICML formats.

::: {#output .section .level2}
## [](#output){.anchor aria-hidden="true"}Output

By default, pandoc's odt, docx and ICML output applies a predefined set of styles for blocks such as paragraphs and block quotes, and uses largely default formatting (italics, bold) for inlines. This will work for most purposes, especially alongside a [reference doc](#option--reference-doc) file. However, if you need to apply your own styles to blocks, or match a preexisting set of styles, pandoc allows you to define custom styles for blocks and text using `div`s and `span`s, respectively.

If you define a Div, Span, or Table with the attribute `custom-style`, pandoc will apply your specified style to the contained elements (with the exception of elements whose function depends on a style, like headings, code blocks, block quotes, or links). So, for example, using the `bracketed_spans` syntax,

    [Get out]{custom-style="Emphatically"}, he said.

would produce a file with "Get out" styled with character style `Emphatically`. Similarly, using the `fenced_divs` syntax,

    Dickinson starts the poem simply:

    ::: {custom-style="Poetry"}
    | A Bird came down the Walk---
    | He did not know I saw---
    :::

would style the two contained lines with the `Poetry` paragraph style.

Styles will be defined in the output file as inheriting from normal text (docx) or Default Paragraph Style (odt), if the styles are not yet in your [reference doc](#option--reference-doc). If they are already defined, pandoc will not alter the definition.

This feature allows for greatest customization in conjunction with [pandoc filters](https://pandoc.org/filters.html). If you want all paragraphs after block quotes to be indented, you can write a filter to apply the styles necessary. If you want all italics to be transformed to the `Emphasis` character style (perhaps to change their color), you can write a filter which will transform all italicized inlines to inlines within an `Emphasis` custom-style `span`.

For docx or odt output, you don't need to enable any extensions for custom styles to work.

For icml output, you can also set an `object-style` in images:

    ![Image with object style](myImage.jpg){object-style="fixedSizeImage"}

In InDesign you'll see that object style given to the image, and you'll be able to customize it, or load its definition from a template of yours.
:::

::: {#input .section .level2}
## [](#input){.anchor aria-hidden="true"}Input

The docx reader, by default, only reads those styles that it can convert into pandoc elements, either by direct conversion or interpreting the derivation of the input document's styles.

By enabling the [`styles` extension](#ext-styles) in the docx reader ([`-f docx+styles`](#option--from){.option}), you can produce output that maintains the styles of the input document, using the `custom-style` class. A `custom-style` attribute will be added for each style. Divs will be created to hold the paragraph styles, and Spans to hold the character styles. Table styles will be applied directly to the Table.

For example, using the `custom-style-reference.docx` file in the test directory, we have the following different outputs:

Without the `+styles` extension:

    $ pandoc test/docx/custom-style-reference.docx -f docx -t markdown
    This is some text.

    This is text with an *emphasized* text style. And this is text with a
    **strengthened** text style.

    > Here is a styled paragraph that inherits from Block Text.

And with the extension:

    $ pandoc test/docx/custom-style-reference.docx -f docx+styles -t markdown

    ::: {custom-style="First Paragraph"}
    This is some text.
    :::

    ::: {custom-style="Body Text"}
    This is text with an [emphasized]{custom-style="Emphatic"} text style.
    And this is text with a [strengthened]{custom-style="Strengthened"}
    text style.
    :::

    ::: {custom-style="My Block Style"}
    > Here is a styled paragraph that inherits from Block Text.
    :::

With these custom styles, you can use your input document as a reference-doc while creating docx output (see below), and maintain the same styles in your input and output files.
:::
:::::
