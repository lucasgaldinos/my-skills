::: {#authors .section .level1}
# [](#authors){.anchor aria-hidden="true"}Authors

Copyright 2006--2024 John MacFarlane ([\[email protected\]](/cdn-cgi/l/email-protection){.__cf_email__ cfemail="0f6568624f6d6a7d646a636a76216a6b7a"}). Released under the [GPL](https://www.gnu.org/copyleft/gpl.html "GNU General Public License"), version 2 or greater. This software carries no warranty of any kind. (See COPYRIGHT for full copyright and warranty notices.) For a full list of contributors, see the file AUTHORS.md in the pandoc source code.
:::

::: {#footnotes .section .footnotes .footnotes-end-of-document role="doc-endnotes"}

------------------------------------------------------------------------

1.  ::: {#fn1}
    The point of this rule is to ensure that normal paragraphs starting with people's initials, like

        B. Russell won a Nobel Prize (but not for "On Denoting").

    do not get treated as list items.

    This rule will not prevent

        (C) 2007 Joe Smith

    from being interpreted as a list item. In this case, a backslash escape can be used:

        (C\) 2007 Joe Smith

    [↩︎](#fnref1){.footnote-back role="doc-backlink"}
    :::

2.  ::: {#fn2}
    I have been influenced by the suggestions of [David Wheeler](https://justatheory.com/2009/02/modest-markdown-proposal/).[↩︎](#fnref2){.footnote-back role="doc-backlink"}
    :::

3.  ::: {#fn3}
    This scheme is due to Michel Fortin, who proposed it on the [Markdown discussion list](http://six.pairlist.net/pipermail/markdown-discuss/2005-March/001097.html).[↩︎](#fnref3){.footnote-back role="doc-backlink"}
    :::

4.  ::: {#fn4}
    Note that if [`--file-scope`](#option--file-scope%5B){.option} is used, a div written this way will be given an identifier of the form `FILE__refs`, to avoid duplicate identifiers (see [`--file-scope`](#option--file-scope%5B){.option}). In view of this possibility, pandoc will place the bibliography in any div whose identifier is `refs` *or* ends with `__refs`.[↩︎](#fnref4){.footnote-back role="doc-backlink"}
    :::
:::
