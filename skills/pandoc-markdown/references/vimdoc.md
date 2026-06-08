::::: {#vimdoc .section .level1}
# [](#vimdoc){.anchor aria-hidden="true"}Vimdoc

Vimdoc writer generates Vim help files and makes use of the following metadata variables:

::: {#cb459 .sourceCode}
``` {.sourceCode .yaml}
abstract: "A short description"
author: Author
title: Title

# Vimdoc-specific
filename: "definition-lists.txt"
vimdoc-prefix: pandoc
```
:::

Complete header requires `abstract`, `author`, `title` and `filename` to be set. Compiling file with such metadata produces the following file (assumes [`--standalone`](#option--standalone){.option}, see [Templates](#templates)):

``` vimdoc
*definition-lists.txt*  A short description

                            Title by Author


                                 Type |gO| to see the table of contents.

[...]

 vim:tw=72:sw=4:ts=4:ft=help:norl:et:
```

If `vimdoc-prefix` is set, all non-command tags are prefixed with its value, it is used to prevent tag collision: all headers have a tag (either inferred or explicit) and multiple help pages can have the same header names, therefore collision is to be expected. Let our input be the following markdown file:

::: {#cb461 .sourceCode}
``` {.sourceCode .markdown}
## Header

`:[range]Fnl {expr}`{#:Fnl}
:   Evaluates {expr} or range

`vim.b`{#vim.b}
:   Buffer-scoped (`:h b:`) variables for the current buffer. Invalid or unset
    key returns `nil`. Can be indexed with an integer to access variables for a
    specific buffer.

[Span]{#span}
:   generic inline container for phrasing content, which does not inherently
    represent anything.
```
:::

Convert it to vimdoc:

``` vimdoc
------------------------------------------------------------------------
Header                                                            *header*

:[range]Fnl {expr}                                                  *:Fnl*
    Evaluates {expr} or range
`vim.b`                                                            *vim.b*
    Buffer-scoped (|b:|) variables for the current buffer. Invalid or
    unset key returns `nil`. Can be indexed with an integer to access
    variables for a specific buffer.
Span                                                                *span*
    generic inline container for phrasing content, which does not
    inherently represent anything.
```

Convert it to vimdoc with metadata variable set (e.g. with [`-M vimdoc-prefix=pandoc`](#option--metadata){.option})

``` vimdoc
------------------------------------------------------------------------
Header                                                     *pandoc-header*

:[range]Fnl {expr}                                                  *:Fnl*
    Evaluates {expr} or range
`vim.b`                                                     *pandoc-vim.b*
    Buffer-scoped (|b:|) variables for the current buffer. Invalid or
    unset key returns `nil`. Can be indexed with an integer to access
    variables for a specific buffer.
Span                                                         *pandoc-span*
    generic inline container for phrasing content, which does not
    inherently represent anything.
```

`vim.b` and `Span` got their prefixes but not `:Fnl` because ex-commands (those starting with `:`) don't get a prefix, since they are considered unique across help pages.

In both cases `:help b:` became reference `|b:|` (also works with `:h b:`). Links pointing to either <https://vimhelp.org/> or <https://neovim.io/doc/user> become references too.

Vim traditionally wraps at 78, but Pandoc defaults to 72. Use [`--columns 78`](#option--columns){.option} to match Vim.
:::::
