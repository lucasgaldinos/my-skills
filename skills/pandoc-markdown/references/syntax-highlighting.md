::: {#syntax-highlighting .section .level1}
# [](#syntax-highlighting){.anchor aria-hidden="true"}Syntax highlighting

Pandoc will automatically highlight syntax in [fenced code blocks](#fenced-code-blocks) that are marked with a language name. The Haskell library [skylighting](https://github.com/jgm/skylighting) is used for highlighting. Currently highlighting is supported only for HTML, EPUB, Docx, Ms, Man, Typst, and LaTeX/PDF output. To see a list of language names that pandoc will recognize, type `pandoc --list-highlight-languages`.

The color scheme can be selected using the [`--syntax-highlighting`](#option--syntax-highlighting){.option} option. The default color scheme is `pygments`, which imitates the default color scheme used by the Python library pygments (though pygments is not actually used to do the highlighting). To see a list of highlight styles, type `pandoc --list-highlight-styles`.

If you are not satisfied with the predefined styles, you can use [`--print-highlight-style`](#option--print-highlight-style){.option} to generate a JSON `.theme` file which can be modified and used as the argument to [`--syntax-highlighting`](#option--syntax-highlighting){.option}. To get a JSON version of the `pygments` style, for example:

    pandoc -o my.theme --print-highlight-style pygments

Then edit `my.theme` and use it like this:

    pandoc --syntax-highlighting my.theme

If you are not satisfied with the built-in highlighting, or you want to highlight a language that isn't supported, you can use the [`--syntax-definition`](#option--syntax-definition){.option} option to load a [KDE-style XML syntax definition file](https://docs.kde.org/stable5/en/kate/katepart/highlight.html). Before writing your own, have a look at KDE's [repository of syntax definitions](https://github.com/KDE/syntax-highlighting/tree/master/data/syntax).

If you receive an error that pandoc "Could not read highlighting theme", check that the JSON file is encoded with UTF-8 and has no Byte-Order Mark (BOM).

To disable highlighting, use [`--syntax-highlighting=none`](#option--syntax-highlighting){.option}.

To use a format's idiomatic syntax highlighting instead of pandoc's built-in highlighting, use [`--syntax-highlighting=idiomatic`](#option--syntax-highlighting){.option}. Currently, `idiomatic` only affects the following formats:

-   In reveal.js, it causes reveal.js's highlighting plugin to be used for source code highlighting. The style may be customized by setting the `highlightjs-theme` variable.

-   In Typst, it causes Typst's built-in highlighting to be used. (This is also the default for Typst.)

-   In LaTeX, it causes the [`listings`](https://ctan.org/pkg/listings) package to be used. Note that `listings` does not support multi-byte encoding for source code. To handle UTF-8 you would need to use a custom template. This issue is fully documented here: [Encoding issue with the listings package](https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings#Encoding_issue).

-   In other formats, `idiomatic` will have the same result as `default`.
:::
