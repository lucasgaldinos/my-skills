::::::::::::::::::: {#slide-shows .section .level1}
# [](#slide-shows){.anchor aria-hidden="true"}Slide shows

You can use pandoc to produce an HTML + JavaScript slide presentation that can be viewed via a web browser. There are five ways to do this, using [S5](https://meyerweb.com/eric/tools/s5/), [DZSlides](https://paulrouget.com/dzslides/), [Slidy](https://www.w3.org/Talks/Tools/Slidy2/), [Slideous](https://goessner.net/articles/slideous/), or [reveal.js](https://revealjs.com/). You can also produce a PDF slide show using LaTeX [`beamer`](https://ctan.org/pkg/beamer), or slide shows in Microsoft [PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) format.

Here's the Markdown source for a simple slide show, `habits.txt`:

    % Habits
    % John Doe
    % March 22, 2005

    # In the morning

    ## Getting up

    - Turn off alarm
    - Get out of bed

    ## Breakfast

    - Eat eggs
    - Drink coffee

    # In the evening

    ## Dinner

    - Eat spaghetti
    - Drink wine

    ------------------

    ![picture of spaghetti](images/spaghetti.jpg)

    ## Going to sleep

    - Get in bed
    - Count sheep

To produce an HTML/JavaScript slide show, simply type

    pandoc -t FORMAT -s habits.txt -o habits.html

where `FORMAT` is either `s5`, `slidy`, `slideous`, `dzslides`, or `revealjs`.

For Slidy, Slideous, reveal.js, and S5, the file produced by pandoc with the [`-s/--standalone`](#option--standalone){.option} option embeds a link to JavaScript and CSS files, which are assumed to be available at the relative path `s5/default` (for S5), `slideous` (for Slideous), `reveal.js` (for reveal.js), or at the Slidy website at `w3.org` (for Slidy). (These paths can be changed by setting the `slidy-url`, `slideous-url`, `revealjs-url`, or `s5-url` variables; see [Variables for HTML slides](#variables-for-html-slides), above.) For DZSlides, the (relatively short) JavaScript and CSS are included in the file by default.

With all HTML slide formats, the [`--self-contained`](#option--self-contained%5B){.option} option can be used to produce a single file that contains all of the data necessary to display the slide show, including linked scripts, stylesheets, images, and videos.

To produce a PDF slide show using beamer, type

    pandoc -t beamer habits.txt -o habits.pdf

Note that a reveal.js slide show can also be converted to a PDF by printing it to a file from the browser.

To produce a PowerPoint slide show, type

    pandoc habits.txt -o habits.pptx

:::: {#structuring-the-slide-show .section .level2}
## [](#structuring-the-slide-show){.anchor aria-hidden="true"}Structuring the slide show

By default, the *slide level* is the highest heading level in the hierarchy that is followed immediately by content, and not another heading, somewhere in the document. In the example above, level-1 headings are always followed by level-2 headings, which are followed by content, so the slide level is 2. This default can be overridden using the [`--slide-level`](#option--slide-level){.option} option.

The document is carved up into slides according to the following rules:

-   A horizontal rule always starts a new slide.

-   A heading at the slide level always starts a new slide.

-   Headings *below* the slide level in the hierarchy create headings *within* a slide. (In beamer, a "block" will be created. If the heading has the class `example`, an `exampleblock` environment will be used; if it has the class `alert`, an `alertblock` will be used; otherwise a regular `block` will be used.)

-   Headings *above* the slide level in the hierarchy create "title slides," which just contain the section title and help to break the slide show into sections. Non-slide content under these headings will be included on the title slide (for HTML slide shows) or in a subsequent slide with the same title (for beamer).

-   A title page is constructed automatically from the document's title block, if present. (In the case of beamer, this can be disabled by commenting out some lines in the default template.)

These rules are designed to support many different styles of slide show. If you don't care about structuring your slides into sections and subsections, you can either just use level-1 headings for all slides (in that case, level 1 will be the slide level) or you can set [`--slide-level=0`](#option--slide-level){.option}.

Note: in reveal.js slide shows, if slide level is 2, a two-dimensional layout will be produced, with level-1 headings building horizontally and level-2 headings building vertically. It is not recommended that you use deeper nesting of section levels with reveal.js unless you set [`--slide-level=0`](#option--slide-level){.option} (which lets reveal.js produce a one-dimensional layout and only interprets horizontal rules as slide boundaries).

::: {#powerpoint-layout-choice .section .level3}
### [](#powerpoint-layout-choice){.anchor aria-hidden="true"}PowerPoint layout choice

When creating slides, the pptx writer chooses from a number of pre-defined layouts, based on the content of the slide:

Title Slide
:   This layout is used for the initial slide, which is generated and filled from the metadata fields `date`, `author`, and `title`, if they are present.

Section Header
:   This layout is used for what pandoc calls "title slides", i.e. slides which start with a header which is above the slide level in the hierarchy.

Two Content
:   This layout is used for two-column slides, i.e. slides containing a div with class `columns` which contains at least two divs with class `column`.

Comparison
:   This layout is used instead of "Two Content" for any two-column slides in which at least one column contains text followed by non-text (e.g. an image or a table).

Content with Caption
:   This layout is used for any non-two-column slides which contain text followed by non-text (e.g. an image or a table).

Blank
:   This layout is used for any slides which only contain blank content, e.g. a slide containing only speaker notes, or a slide containing only a non-breaking space.

Title and Content
:   This layout is used for all slides which do not match the criteria for another layout.

These layouts are chosen from the default pptx reference doc included with pandoc, unless an alternative reference doc is specified using `--reference-doc`.
:::
::::

::: {#incremental-lists .section .level2}
## [](#incremental-lists){.anchor aria-hidden="true"}Incremental lists

By default, these writers produce lists that display "all at once." If you want your lists to display incrementally (one item at a time), use the [`-i`](#option--incremental%5B){.option} option. If you want a particular list to depart from the default, put it in a `div` block with class `incremental` or `nonincremental`. So, for example, using the `fenced div` syntax, the following would be incremental regardless of the document default:

    ::: incremental

    - Eat spaghetti
    - Drink wine

    :::

or

    ::: nonincremental

    - Eat spaghetti
    - Drink wine

    :::

While using `incremental` and `nonincremental` divs is the recommended method of setting incremental lists on a per-case basis, an older method is also supported: putting lists inside a blockquote will depart from the document default (that is, it will display incrementally without the [`-i`](#option--incremental%5B){.option} option and all at once with the [`-i`](#option--incremental%5B){.option} option):

    > - Eat spaghetti
    > - Drink wine

Both methods allow incremental and nonincremental lists to be mixed in a single document.

If you want to include a block-quoted list, you can work around this behavior by putting the list inside a fenced div, so that it is not the direct child of the block quote:

    > ::: wrapper
    > - a
    > - list in a quote
    > :::
:::

::: {#inserting-pauses .section .level2}
## [](#inserting-pauses){.anchor aria-hidden="true"}Inserting pauses

You can add "pauses" within a slide by including a paragraph containing three dots, separated by spaces:

    # Slide with a pause

    content before the pause

    . . .

    content after the pause

Note: this feature is not yet implemented for PowerPoint output.
:::

::: {#styling-the-slides .section .level2}
## [](#styling-the-slides){.anchor aria-hidden="true"}Styling the slides

You can change the style of HTML slides by putting customized CSS files in `$DATADIR/s5/default` (for S5), `$DATADIR/slidy` (for Slidy), or `$DATADIR/slideous` (for Slideous), where `$DATADIR` is the user data directory (see [`--data-dir`](#option--data-dir){.option}, above). The originals may be found in pandoc's system data directory (generally `$CABALDIR/pandoc-VERSION/s5/default`). Pandoc will look there for any files it does not find in the user data directory.

For dzslides, the CSS is included in the HTML file itself, and may be modified there.

All [reveal.js configuration options](https://revealjs.com/config/) can be set through variables. For example, themes can be used by setting the `theme` variable:

    -V theme=moon

Or you can specify a custom stylesheet using the [`--css`](#option--css){.option} option.

To style beamer slides, you can specify a `theme`, `colortheme`, `fonttheme`, `innertheme`, and `outertheme`, using the [`-V`](#option--variable){.option} option:

    pandoc -t beamer habits.txt -V theme:Warsaw -o habits.pdf

Note that heading attributes will turn into slide attributes (on a `<div>` or `<section>`) in HTML slide formats, allowing you to style individual slides. In beamer, a number of heading classes and attributes are recognized as frame options and will be passed through as options to the frame: see [Frame attributes in beamer](#frame-attributes-in-beamer), below.
:::

:::: {#speaker-notes .section .level2}
## [](#speaker-notes){.anchor aria-hidden="true"}Speaker notes

Speaker notes are supported in reveal.js, PowerPoint (pptx), and beamer output. You can add notes to your Markdown document thus:

    ::: notes

    This is my note.

    - It can contain Markdown
    - like this list

    :::

To show the notes window in reveal.js, press `s` while viewing the presentation. Speaker notes in PowerPoint will be available, as usual, in handouts and presenter view.

Notes are not yet supported for other slide formats, but the notes will not appear on the slides themselves.

::: {#speaker-notes-on-the-title-slide-powerpoint .section .level3}
### [](#speaker-notes-on-the-title-slide-powerpoint){.anchor aria-hidden="true"}Speaker notes on the title slide (PowerPoint)

For PowerPoint output, the title slide is generated from the document's YAML metadata block. To add speaker notes to this slide, use a `notes` field in the metadata:

    ---
    title: My Presentation
    author: Jane Doe
    notes: |
      Welcome everyone to this presentation.

      Remember to introduce yourself and mention the key topics.
    ---

The `notes` field can contain multiple paragraphs and Markdown formatting.
:::
::::

:::: {#columns .section .level2}
## [](#columns){.anchor aria-hidden="true"}Columns

To put material in side by side columns, you can use a native div container with class `columns`, containing two or more div containers with class `column` and a `width` attribute:

    :::::::::::::: {.columns}
    ::: {.column width="40%"}
    contents...
    :::
    ::: {.column width="60%"}
    contents...
    :::
    ::::::::::::::

Note: Specifying column widths does not currently work for PowerPoint.

::: {#additional-columns-attributes-in-beamer .section .level3}
### [](#additional-columns-attributes-in-beamer){.anchor aria-hidden="true"}Additional columns attributes in beamer

The div containers with classes `columns` and `column` can optionally have an `align` attribute. The class `columns` can optionally have a `totalwidth` attribute or an `onlytextwidth` class.

    :::::::::::::: {.columns align=center totalwidth=8em}
    ::: {.column width="40%"}
    contents...
    :::
    ::: {.column width="60%" align=bottom}
    contents...
    :::
    ::::::::::::::

The `align` attributes on `columns` and `column` can be used with the values `top`, `top-baseline`, `center` and `bottom` to vertically align the columns. It defaults to `top` in `columns`.

The `totalwidth` attribute limits the width of the columns to the given value.

    :::::::::::::: {.columns align=top .onlytextwidth}
    ::: {.column width="40%" align=center}
    contents...
    :::
    ::: {.column width="60%"}
    contents...
    :::
    ::::::::::::::

The class `onlytextwidth` sets the `totalwidth` to `\textwidth`.

See Section 12.7 of the [Beamer User's Guide](http://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf) for more details.
:::
::::

::: {#frame-attributes-in-beamer .section .level2}
## [](#frame-attributes-in-beamer){.anchor aria-hidden="true"}Frame attributes in beamer

Sometimes it is necessary to add the LaTeX `[fragile]` option to a frame in beamer (for example, when using the `minted` environment). This can be forced by adding the `fragile` class to the heading introducing the slide:

    # Fragile slide {.fragile}

All of the other frame attributes described in Section 8.1 of the [Beamer User's Guide](http://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf) may also be used: `allowdisplaybreaks`, `allowframebreaks`, `b`, `c`, `s`, `t`, `environment`, `label`, `plain`, `shrink`, `standout`, `noframenumbering`, `squeeze`. `allowframebreaks` is recommended especially for bibliographies, as it allows multiple slides to be created if the content overfills the frame:

    # References {.allowframebreaks}

In addition, the `frameoptions` attribute may be used to pass arbitrary frame options to a beamer slide:

    # Heading {frameoptions="squeeze,shrink,customoption=foobar"}
:::

:::::::: {#background-in-reveal.js-beamer-and-pptx .section .level2}
## [](#background-in-reveal.js-beamer-and-pptx){.anchor aria-hidden="true"}Background in reveal.js, beamer, and pptx

Background images can be added to self-contained reveal.js slide shows, beamer slide shows, and pptx slide shows.

:::: {#on-all-slides-beamer-reveal.js-pptx .section .level3}
### [](#on-all-slides-beamer-reveal.js-pptx){.anchor aria-hidden="true"}On all slides (beamer, reveal.js, pptx)

With beamer and reveal.js, the configuration option `background-image` can be used either in the YAML metadata block or as a command-line variable to get the same image on every slide.

Note that for reveal.js, the `background-image` will be used as a `parallaxBackgroundImage` (see below).

For pptx, you can use a `--reference-doc` in which background images have been set on the [relevant layouts](#powerpoint-layout-choice).

::: {#parallaxbackgroundimage-reveal.js .section .level4}
#### [](#parallaxbackgroundimage-reveal.js){.anchor aria-hidden="true"}`parallaxBackgroundImage` (reveal.js)

For reveal.js, there is also the reveal.js-native option `parallaxBackgroundImage`, which produces a parallax scrolling background. You must also set `parallaxBackgroundSize`, and can optionally set `parallaxBackgroundHorizontal` and `parallaxBackgroundVertical` to configure the scrolling behaviour. See the [reveal.js documentation](https://revealjs.com/backgrounds/#parallax-background) for more details about the meaning of these options.

In reveal.js's overview mode, the parallaxBackgroundImage will show up only on the first slide.
:::
::::

::: {#on-individual-slides-reveal.js-pptx .section .level3}
### [](#on-individual-slides-reveal.js-pptx){.anchor aria-hidden="true"}On individual slides (reveal.js, pptx)

To set an image for a particular reveal.js or pptx slide, add `{background-image="/path/to/image"}` to the first slide-level heading on the slide (which may even be empty).

As the [HTML writers pass unknown attributes through](#extension-link_attributes), other reveal.js background settings also work on individual slides, including `background-size`, `background-repeat`, `background-color`, `transition`, and `transition-speed`. (The `data-` prefix will automatically be added.)

Note: `data-background-image` is also supported in pptx for consistency with reveal.js -- if `background-image` isn't found, `data-background-image` will be checked.
:::

::: {#on-the-title-slide-reveal.js-pptx .section .level3}
### [](#on-the-title-slide-reveal.js-pptx){.anchor aria-hidden="true"}On the title slide (reveal.js, pptx)

To add a background image to the automatically generated title slide for reveal.js, use the `title-slide-attributes` variable in the YAML metadata block. It must contain a map of attribute names and values. (Note that the `data-` prefix is required here, as it isn't added automatically.)

For pptx, pass a `--reference-doc` with the background image set on the "Title Slide" layout.
:::

::: {#example-reveal.js .section .level3}
### [](#example-reveal.js){.anchor aria-hidden="true"}Example (reveal.js)

    ---
    title: My Slide Show
    parallaxBackgroundImage: /path/to/my/background_image.png
    title-slide-attributes:
        data-background-image: /path/to/title_image.png
        data-background-size: contain
    ---

    ## Slide One

    Slide 1 has background_image.png as its background.

    ## {background-image="/path/to/special_image.jpg"}

    Slide 2 has a special image for its background, even though the heading has no content.
:::
::::::::
:::::::::::::::::::
