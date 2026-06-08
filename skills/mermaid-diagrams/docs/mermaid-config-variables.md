---
title: "Mermaid"
source: "https://mermaid.js.org/config/schema-docs/config.html"
author:
published:
created: 2026-05-19
description: "A comprehensive reference for the Mermaid.js configuration schema, detailing global settings and specific parameters for various diagram types including Flowcharts, Sequence Diagrams, and Gantt charts."
tags:
  - "mermaid-js"
  - "configuration-schema"
  - "json-schema"
  - "documentation"
  - "diagramming-tools"
  - "web-development"
  - "visualization-settings"
  - "technical-reference"
image: "https://mermaid.js.org/mermaid-logo-horizontal.svg"
---
# Mermaid Config Schema

```url
https://mermaid.js.org/schemas/config.schema.json
```

| Abstract | Extensible | Status | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Can be instantiated | No | Unknown status | No | Forbidden | Forbidden | none | [config.schema.json](https://mermaid.js.org/schemas/config.schema.json "open original schema") |

## Mermaid Config Type

`object` ([Mermaid Config](https://mermaid.js.org/config/schema-docs/config.html))

## Mermaid Config Properties

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [theme](#theme) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-theme.html "https://mermaid.js.org/schemas/config.schema.json#/properties/theme") |
| [themeVariables](#themevariables) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-themevariables.html "https://mermaid.js.org/schemas/config.schema.json#/properties/themeVariables") |
| [themeCSS](#themecss) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-themecss.html "https://mermaid.js.org/schemas/config.schema.json#/properties/themeCSS") |
| [look](#look) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-look.html "https://mermaid.js.org/schemas/config.schema.json#/properties/look") |
| [handDrawnSeed](#handdrawnseed) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-handdrawnseed.html "https://mermaid.js.org/schemas/config.schema.json#/properties/handDrawnSeed") |
| [layout](#layout) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-layout.html "https://mermaid.js.org/schemas/config.schema.json#/properties/layout") |
| [maxTextSize](#maxtextsize) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-maxtextsize.html "https://mermaid.js.org/schemas/config.schema.json#/properties/maxTextSize") |
| [maxEdges](#maxedges) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-maxedges.html "https://mermaid.js.org/schemas/config.schema.json#/properties/maxEdges") |
| [elk](#elk) | `object` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-elk.html "https://mermaid.js.org/schemas/config.schema.json#/properties/elk") |
| [darkMode](#darkmode) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-darkmode.html "https://mermaid.js.org/schemas/config.schema.json#/properties/darkMode") |
| [htmlLabels](#htmllabels) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/properties/htmlLabels") |
| [fontFamily](#fontfamily) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-fontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/properties/fontFamily") |
| [altFontFamily](#altfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-altfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/properties/altFontFamily") |
| [logLevel](#loglevel) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-loglevel.html "https://mermaid.js.org/schemas/config.schema.json#/properties/logLevel") |
| [securityLevel](#securitylevel) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-securitylevel.html "https://mermaid.js.org/schemas/config.schema.json#/properties/securityLevel") |
| [startOnLoad](#startonload) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-startonload.html "https://mermaid.js.org/schemas/config.schema.json#/properties/startOnLoad") |
| [arrowMarkerAbsolute](#arrowmarkerabsolute) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute") |
| [secure](#secure) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-secure.html "https://mermaid.js.org/schemas/config.schema.json#/properties/secure") |
| [legacyMathML](#legacymathml) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-legacymathml.html "https://mermaid.js.org/schemas/config.schema.json#/properties/legacyMathML") |
| [forceLegacyMathML](#forcelegacymathml) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-forcelegacymathml.html "https://mermaid.js.org/schemas/config.schema.json#/properties/forceLegacyMathML") |
| [deterministicIds](#deterministicids) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-deterministicids.html "https://mermaid.js.org/schemas/config.schema.json#/properties/deterministicIds") |
| [deterministicIDSeed](#deterministicidseed) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-deterministicidseed.html "https://mermaid.js.org/schemas/config.schema.json#/properties/deterministicIDSeed") |
| [flowchart](#flowchart) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/flowchart") |
| [sequence](#sequence) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/sequence") |
| [gantt](#gantt) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/gantt") |
| [journey](#journey) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/journey") |
| [timeline](#timeline) | Merged | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/timeline") |
| [class](#class) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/class") |
| [state](#state) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/state") |
| [er](#er) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/er") |
| [pie](#pie) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/pie") |
| [quadrantChart](#quadrantchart) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/quadrantChart") |
| [xyChart](#xychart) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/xyChart") |
| [requirement](#requirement) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/requirement") |
| [architecture](#architecture) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/architecture") |
| [mindmap](#mindmap) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/mindmap") |
| [ishikawa](#ishikawa) | Merged | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/ishikawa") |
| [kanban](#kanban) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/kanban") |
| [gitGraph](#gitgraph) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/gitGraph") |
| [c4](#c4) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/c4") |
| [sankey](#sankey) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/sankey") |
| [packet](#packet) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/packet") |
| [block](#block) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/block") |
| [eventmodeling](#eventmodeling) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/eventmodeling") |
| [treeView](#treeview) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/treeView") |
| [radar](#radar) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/radar") |
| [venn](#venn) | Merged | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/venn") |
| [wardley-beta](#wardley-beta) | Merged | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/wardley-beta") |
| [dompurifyConfig](#dompurifyconfig) | `object` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-dom-purify-configuration.html "https://mermaid.js.org/schemas/config.schema.json#/properties/dompurifyConfig") |
| [wrap](#wrap) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/properties/wrap") |
| [fontSize](#fontsize) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/properties/fontSize") |
| [markdownAutoWrap](#markdownautowrap) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-markdownautowrap.html "https://mermaid.js.org/schemas/config.schema.json#/properties/markdownAutoWrap") |
| [suppressErrorRendering](#suppresserrorrendering) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-suppresserrorrendering.html "https://mermaid.js.org/schemas/config.schema.json#/properties/suppressErrorRendering") |

## theme

Theme, the CSS style sheet. You may also use `themeCSS` to override this value.

`theme`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-theme.html "https://mermaid.js.org/schemas/config.schema.json#/properties/theme")

### theme Type

`string`

### theme Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"default"` |  |
| `"base"` |  |
| `"dark"` |  |
| `"forest"` |  |
| `"neutral"` |  |
| `"neo"` |  |
| `"neo-dark"` |  |
| `"redux"` |  |
| `"redux-dark"` |  |
| `"redux-color"` |  |
| `"redux-dark-color"` |  |
| `"null"` | Can be set to disable any pre-defined mermaid theme |

### theme Default Value

The default value is:

```json
"default"
```

## themeVariables

`themeVariables`

- is optional
- Type: unknown
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-themevariables.html "https://mermaid.js.org/schemas/config.schema.json#/properties/themeVariables")
- tsType: `any`

### themeVariables Type

unknown

## themeCSS

`themeCSS`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-themecss.html "https://mermaid.js.org/schemas/config.schema.json#/properties/themeCSS")

### themeCSS Type

`string`

## look

Defines which main look to use for the diagram.

`look`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-look.html "https://mermaid.js.org/schemas/config.schema.json#/properties/look")

### look Type

`string`

### look Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"classic"` |  |
| `"handDrawn"` |  |
| `"neo"` |  |

### look Default Value

The default value is:

```json
"classic"
```

## handDrawnSeed

Defines the seed to be used when using handDrawn look. This is important for the automated tests as they will always find differences without the seed. The default value is 0 which gives a random seed.

`handDrawnSeed`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-handdrawnseed.html "https://mermaid.js.org/schemas/config.schema.json#/properties/handDrawnSeed")

### handDrawnSeed Type

`number`

### handDrawnSeed Default Value

The default value is:

```json
0
```

## layout

Defines which layout algorithm to use for rendering the diagram.

`layout`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-layout.html "https://mermaid.js.org/schemas/config.schema.json#/properties/layout")

### layout Type

`string`

### layout Default Value

The default value is:

```json
"dagre"
```

## maxTextSize

The maximum allowed size of the users text diagram

`maxTextSize`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-maxtextsize.html "https://mermaid.js.org/schemas/config.schema.json#/properties/maxTextSize")

### maxTextSize Type

`number`

### maxTextSize Default Value

The default value is:

```json
50000
```

## maxEdges

Defines the maximum number of edges that can be drawn in a graph.

`maxEdges`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-maxedges.html "https://mermaid.js.org/schemas/config.schema.json#/properties/maxEdges")

### maxEdges Type

`integer`

### maxEdges Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### maxEdges Default Value

The default value is:

```json
500
```

## elk

`elk`

- is optional
- Type: `object` ([Details](https://mermaid.js.org/config/schema-docs/config-properties-elk.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-elk.html "https://mermaid.js.org/schemas/config.schema.json#/properties/elk")

### elk Type

`object` ([Details](https://mermaid.js.org/config/schema-docs/config-properties-elk.html))

## darkMode

`darkMode`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-darkmode.html "https://mermaid.js.org/schemas/config.schema.json#/properties/darkMode")

### darkMode Type

`boolean`

### darkMode Default Value

The default value is:

```json
false
```

## htmlLabels

Flag for setting whether or not a html tag should be used for rendering labels on nodes and edges. **Note:** Diagram-specific `htmlLabels` settings (e.g., `flowchart.htmlLabels`) are deprecated. Use this root-level `htmlLabels` setting instead. The root-level `htmlLabels` takes precedence over any diagram-specific settings.

`htmlLabels`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/properties/htmlLabels")

### htmlLabels Type

`boolean`

## fontFamily

Specifies the font to be used in the rendered diagrams. Can be any possible CSS `font-family`. See <https://developer.mozilla.org/en-US/docs/Web/CSS/font-family>

`fontFamily`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-fontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/properties/fontFamily")

### fontFamily Type

`string`

### fontFamily Default Value

The default value is:

```json
"\"trebuchet ms\", verdana, arial, sans-serif;"
```

## altFontFamily

`altFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-altfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/properties/altFontFamily")

### altFontFamily Type

`string`

## logLevel

This option decides the amount of logging to be used by mermaid.

`logLevel`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-properties-loglevel.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-loglevel.html "https://mermaid.js.org/schemas/config.schema.json#/properties/logLevel")

### logLevel Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-properties-loglevel.html))

### logLevel Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"trace"` | Equivalent to 0 |
| `0` |  |
| `"debug"` | Equivalent to 1 |
| `1` |  |
| `"info"` | Equivalent to 2 |
| `2` |  |
| `"warn"` | Equivalent to 3 |
| `3` |  |
| `"error"` | Equivalent to 4 |
| `4` |  |
| `"fatal"` | Equivalent to 5 (default) |
| `5` |  |

### logLevel Default Value

The default value is:

```json
5
```

## securityLevel

Level of trust for parsed diagram

`securityLevel`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-securitylevel.html "https://mermaid.js.org/schemas/config.schema.json#/properties/securityLevel")

### securityLevel Type

`string`

### securityLevel Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"strict"` | (\*\*default\*\*) HTML tags in the text are encoded and click functionality is disabled. |
| `"loose"` | HTML tags in text are allowed and click functionality is enabled. |
| `"antiscript"` | HTML tags in text are allowed (only script elements are removed), and click functionality is enabled. |
| `"sandbox"` | With this security level, all rendering takes place in a sandboxed iframe. This prevent any javascript from running in the context. This may hinder interactive functionality of the diagram, like scripts, popups in the sequence diagram, or links to other tabs or targets, etc. |

### securityLevel Default Value

The default value is:

```json
"strict"
```

## startOnLoad

Dictates whether mermaid starts on Page load

`startOnLoad`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-startonload.html "https://mermaid.js.org/schemas/config.schema.json#/properties/startOnLoad")

### startOnLoad Type

`boolean`

### startOnLoad Default Value

The default value is:

```json
true
```

## arrowMarkerAbsolute

Controls whether or arrow markers in html code are absolute paths or anchors. This matters if you are using base tag settings.

`arrowMarkerAbsolute`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute")

### arrowMarkerAbsolute Type

`boolean`

### arrowMarkerAbsolute Default Value

The default value is:

```json
false
```

## secure

This option controls which `currentConfig` keys are considered secure and can only be changed via call to `mermaid.initialize`. This prevents malicious graph directives from overriding a site's default security.

`secure`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-secure.html "https://mermaid.js.org/schemas/config.schema.json#/properties/secure")

### secure Type

`string[]`

### secure Default Value

The default value is:

```json
["secure", "securityLevel", "startOnLoad", "maxTextSize", "suppressErrorRendering", "maxEdges"]
```

## legacyMathML

This option specifies if Mermaid can expect the dependent to include KaTeX stylesheets for browsers without their own MathML implementation. If this option is disabled and MathML is not supported, the math equations are replaced with a warning. If this option is enabled and MathML is not supported, Mermaid will fall back to legacy rendering for KaTeX.

`legacyMathML`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-legacymathml.html "https://mermaid.js.org/schemas/config.schema.json#/properties/legacyMathML")

### legacyMathML Type

`boolean`

### legacyMathML Default Value

The default value is:

```json
false
```

## forceLegacyMathML

This option forces Mermaid to rely on KaTeX's own stylesheet for rendering MathML. Due to differences between OS fonts and browser's MathML implementation, this option is recommended if consistent rendering is important. If set to true, ignores legacyMathML.

`forceLegacyMathML`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-forcelegacymathml.html "https://mermaid.js.org/schemas/config.schema.json#/properties/forceLegacyMathML")

### forceLegacyMathML Type

`boolean`

### forceLegacyMathML Default Value

The default value is:

```json
false
```

## deterministicIds

This option controls if the generated ids of nodes in the SVG are generated randomly or based on a seed. If set to `false`, the IDs are generated based on the current date and thus are not deterministic. This is the default behavior.

This matters if your files are checked into source control e.g. git and should not change unless content is changed.

`deterministicIds`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-deterministicids.html "https://mermaid.js.org/schemas/config.schema.json#/properties/deterministicIds")

### deterministicIds Type

`boolean`

### deterministicIds Default Value

The default value is:

```json
false
```

## deterministicIDSeed

This option is the optional seed for deterministic ids. If set to `undefined` but deterministicIds is `true`, a simple number iterator is used. You can set this attribute to base the seed on a static string.

`deterministicIDSeed`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-deterministicidseed.html "https://mermaid.js.org/schemas/config.schema.json#/properties/deterministicIDSeed")

### deterministicIDSeed Type

`string`

## flowchart

The object containing configurations specific for flowcharts

`flowchart`

- is required
- Type: `object` ([Flowchart Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/flowchart")

### flowchart Type

`object` ([Flowchart Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## sequence

The object containing configurations specific for sequence diagrams

`sequence`

- is required
- Type: `object` ([Sequence Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/sequence")

### sequence Type

`object` ([Sequence Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## gantt

The object containing configurations specific for gantt diagrams

`gantt`

- is required
- Type: `object` ([Gantt Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/gantt")

### gantt Type

`object` ([Gantt Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## journey

The object containing configurations specific for journey diagrams

`journey`

- is required
- Type: `object` ([Journey Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/journey")

### journey Type

`object` ([Journey Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## timeline

`timeline`

- is optional
- Type: `object` ([Timeline Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/timeline")

### timeline Type

`object` ([Timeline Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## class

`class`

- is required
- Type: `object` ([Class Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/class")

### class Type

`object` ([Class Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## state

The object containing configurations specific for entity relationship diagrams

`state`

- is required
- Type: `object` ([State Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/state")

### state Type

`object` ([State Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## er

The object containing configurations specific for entity relationship diagrams

`er`

- is required
- Type: `object` ([Er Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/er")

### er Type

`object` ([Er Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## pie

`pie`

- is required
- Type: `object` ([Pie Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/pie")

### pie Type

`object` ([Pie Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## quadrantChart

`quadrantChart`

- is required
- Type: `object` ([Quadrant Chart Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/quadrantChart")

### quadrantChart Type

`object` ([Quadrant Chart Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## xyChart

This object contains configuration specific to XYCharts

`xyChart`

- is required
- Type: `object` ([XYChart Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/xyChart")

### xyChart Type

`object` ([XYChart Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## requirement

The object containing configurations specific for req diagrams

`requirement`

- is required
- Type: `object` ([Requirement Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/requirement")

### requirement Type

`object` ([Requirement Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## architecture

The object containing configurations specific for architecture diagrams

`architecture`

- is required
- Type: `object` ([Architecture Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/architecture")

### architecture Type

`object` ([Architecture Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## mindmap

The object containing configurations specific for mindmap diagrams

`mindmap`

- is required
- Type: `object` ([Mindmap Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/mindmap")

### mindmap Type

`object` ([Mindmap Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## ishikawa

The object containing configurations specific for ishikawa diagrams

`ishikawa`

- is optional
- Type: `object` ([Ishikawa Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/ishikawa")

### ishikawa Type

`object` ([Ishikawa Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## kanban

The object containing configurations specific for kanban diagrams

`kanban`

- is required
- Type: `object` ([Kanban Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/kanban")

### kanban Type

`object` ([Kanban Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## gitGraph

`gitGraph`

- is required
- Type: `object` ([Git Graph Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/gitGraph")

### gitGraph Type

`object` ([Git Graph Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## c4

The object containing configurations specific for c4 diagrams

`c4`

- is required
- Type: `object` ([C4 Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/c4")

### c4 Type

`object` ([C4 Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## sankey

The object containing configurations specific for sankey diagrams.

`sankey`

- is required
- Type: `object` ([Sankey Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/sankey")

### sankey Type

`object` ([Sankey Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## packet

The object containing configurations specific for packet diagrams.

`packet`

- is required
- Type: `object` ([Packet Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/packet")

### packet Type

`object` ([Packet Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## block

The object containing configurations specific for block diagrams.

`block`

- is required
- Type: `object` ([Block Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/block")

### block Type

`object` ([Block Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## eventmodeling

The object containing configurations specific for Event Modeling diagrams.

`eventmodeling`

- is required
- Type: `object` ([Event Modeling Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/eventmodeling")

### eventmodeling Type

`object` ([Event Modeling Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## treeView

The object containing configurations specific for treeView diagrams.

`treeView`

- is required
- Type: `object` ([TreeView Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/treeView")

### treeView Type

`object` ([TreeView Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## radar

The object containing configurations specific for radar diagrams.

`radar`

- is required
- Type: `object` ([Radar Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/radar")

### radar Type

`object` ([Radar Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## venn

The object containing configurations specific for Venn diagrams.

`venn`

- is required
- Type: `object` ([Venn Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/venn")

### venn Type

`object` ([Venn Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## wardley-beta

The object containing configurations specific for Wardley Maps diagrams.

`wardley-beta`

- is optional
- Type: `object` ([Wardley Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config.html "https://mermaid.js.org/schemas/config.schema.json#/properties/wardley-beta")

### wardley-beta Type

`object` ([Wardley Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config.html))

all of

- [Base Diagram Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html "check type definition")

## dompurifyConfig

Configuration options to pass to the `dompurify` library.

`dompurifyConfig`

- is optional
- Type: `object` ([DOM Purify Configuration](https://mermaid.js.org/config/schema-docs/config-properties-dom-purify-configuration.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-dom-purify-configuration.html "https://mermaid.js.org/schemas/config.schema.json#/properties/dompurifyConfig")
- tsType: `import('dompurify').Config`

### dompurifyConfig Type

`object` ([DOM Purify Configuration](https://mermaid.js.org/config/schema-docs/config-properties-dom-purify-configuration.html))

## wrap

`wrap`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/properties/wrap")

### wrap Type

`boolean`

## fontSize

`fontSize`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/properties/fontSize")

### fontSize Type

`number`

### fontSize Default Value

The default value is:

```json
16
```

## markdownAutoWrap

`markdownAutoWrap`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-markdownautowrap.html "https://mermaid.js.org/schemas/config.schema.json#/properties/markdownAutoWrap")

### markdownAutoWrap Type

`boolean`

### markdownAutoWrap Default Value

The default value is:

```json
true
```

## suppressErrorRendering

Suppresses inserting 'Syntax error' diagram in the DOM. This is useful when you want to control how to handle syntax errors in your application.

`suppressErrorRendering`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-suppresserrorrendering.html "https://mermaid.js.org/schemas/config.schema.json#/properties/suppressErrorRendering")

### suppressErrorRendering Type

`boolean`

### suppressErrorRendering Default Value

The default value is:

```json
false
```

## Mermaid Config Definitions

## Definitions group BaseDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/BaseDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [useWidth](#usewidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config-properties-usewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BaseDiagramConfig/properties/useWidth") |
| [useMaxWidth](#usemaxwidth) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BaseDiagramConfig/properties/useMaxWidth") |

### useWidth

`useWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config-properties-usewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BaseDiagramConfig/properties/useWidth")

#### useWidth Type

`number`

### useMaxWidth

When this flag is set to `true`, the height and width is set to 100% and is then scaled with the available space. If set to `false`, the absolute space required is used.

`useMaxWidth`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BaseDiagramConfig/properties/useMaxWidth")

#### useMaxWidth Type

`boolean`

#### useMaxWidth Default Value

The default value is:

```json
true
```

## Definitions group C4DiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [diagramMarginX](#diagrammarginx) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/diagramMarginX") |
| [diagramMarginY](#diagrammarginy) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/diagramMarginY") |
| [c4ShapeMargin](#c4shapemargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapeMargin") |
| [c4ShapePadding](#c4shapepadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapePadding") |
| [width](#width) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/width") |
| [height](#height) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/height") |
| [boxMargin](#boxmargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boxMargin") |
| [c4ShapeInRow](#c4shapeinrow) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapeinrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapeInRow") |
| [nextLinePaddingX](#nextlinepaddingx) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-nextlinepaddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/nextLinePaddingX") |
| [c4BoundaryInRow](#c4boundaryinrow) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4boundaryinrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4BoundaryInRow") |
| [personFontSize](#personfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontSize") |
| [personFontFamily](#personfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontFamily") |
| [personFontWeight](#personfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontWeight") |
| [external\_personFontSize](#external_personfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontSize") |
| [external\_personFontFamily](#external_personfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontFamily") |
| [external\_personFontWeight](#external_personfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontWeight") |
| [systemFontSize](#systemfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontSize") |
| [systemFontFamily](#systemfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontFamily") |
| [systemFontWeight](#systemfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontWeight") |
| [external\_systemFontSize](#external_systemfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontSize") |
| [external\_systemFontFamily](#external_systemfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontFamily") |
| [external\_systemFontWeight](#external_systemfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontWeight") |
| [system\_dbFontSize](#system_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontSize") |
| [system\_dbFontFamily](#system_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontFamily") |
| [system\_dbFontWeight](#system_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontWeight") |
| [external\_system\_dbFontSize](#external_system_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontSize") |
| [external\_system\_dbFontFamily](#external_system_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontFamily") |
| [external\_system\_dbFontWeight](#external_system_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontWeight") |
| [system\_queueFontSize](#system_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontSize") |
| [system\_queueFontFamily](#system_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontFamily") |
| [system\_queueFontWeight](#system_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontWeight") |
| [external\_system\_queueFontSize](#external_system_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontSize") |
| [external\_system\_queueFontFamily](#external_system_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontFamily") |
| [external\_system\_queueFontWeight](#external_system_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontWeight") |
| [boundaryFontSize](#boundaryfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontSize") |
| [boundaryFontFamily](#boundaryfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontFamily") |
| [boundaryFontWeight](#boundaryfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontWeight") |
| [messageFontSize](#messagefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontSize") |
| [messageFontFamily](#messagefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontFamily") |
| [messageFontWeight](#messagefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontWeight") |
| [containerFontSize](#containerfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontSize") |
| [containerFontFamily](#containerfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontFamily") |
| [containerFontWeight](#containerfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontWeight") |
| [external\_containerFontSize](#external_containerfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontSize") |
| [external\_containerFontFamily](#external_containerfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontFamily") |
| [external\_containerFontWeight](#external_containerfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontWeight") |
| [container\_dbFontSize](#container_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontSize") |
| [container\_dbFontFamily](#container_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontFamily") |
| [container\_dbFontWeight](#container_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontWeight") |
| [external\_container\_dbFontSize](#external_container_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontSize") |
| [external\_container\_dbFontFamily](#external_container_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontFamily") |
| [external\_container\_dbFontWeight](#external_container_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontWeight") |
| [container\_queueFontSize](#container_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontSize") |
| [container\_queueFontFamily](#container_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontFamily") |
| [container\_queueFontWeight](#container_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontWeight") |
| [external\_container\_queueFontSize](#external_container_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontSize") |
| [external\_container\_queueFontFamily](#external_container_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontFamily") |
| [external\_container\_queueFontWeight](#external_container_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontWeight") |
| [componentFontSize](#componentfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontSize") |
| [componentFontFamily](#componentfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontFamily") |
| [componentFontWeight](#componentfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontWeight") |
| [external\_componentFontSize](#external_componentfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontSize") |
| [external\_componentFontFamily](#external_componentfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontFamily") |
| [external\_componentFontWeight](#external_componentfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontWeight") |
| [component\_dbFontSize](#component_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontSize") |
| [component\_dbFontFamily](#component_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontFamily") |
| [component\_dbFontWeight](#component_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontWeight") |
| [external\_component\_dbFontSize](#external_component_dbfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontSize") |
| [external\_component\_dbFontFamily](#external_component_dbfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontFamily") |
| [external\_component\_dbFontWeight](#external_component_dbfontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontWeight") |
| [component\_queueFontSize](#component_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontSize") |
| [component\_queueFontFamily](#component_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontFamily") |
| [component\_queueFontWeight](#component_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontWeight") |
| [external\_component\_queueFontSize](#external_component_queuefontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontSize") |
| [external\_component\_queueFontFamily](#external_component_queuefontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontFamily") |
| [external\_component\_queueFontWeight](#external_component_queuefontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontWeight") |
| [wrap](#wrap-1) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/wrap") |
| [wrapPadding](#wrappadding) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrappadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/wrapPadding") |
| [person\_bg\_color](#person_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-person_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/person_bg_color") |
| [person\_border\_color](#person_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-person_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/person_border_color") |
| [external\_person\_bg\_color](#external_person_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_person_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_person_bg_color") |
| [external\_person\_border\_color](#external_person_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_person_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_person_border_color") |
| [system\_bg\_color](#system_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_bg_color") |
| [system\_border\_color](#system_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_border_color") |
| [system\_db\_bg\_color](#system_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_db_bg_color") |
| [system\_db\_border\_color](#system_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_db_border_color") |
| [system\_queue\_bg\_color](#system_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queue_bg_color") |
| [system\_queue\_border\_color](#system_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queue_border_color") |
| [external\_system\_bg\_color](#external_system_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_bg_color") |
| [external\_system\_border\_color](#external_system_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_border_color") |
| [external\_system\_db\_bg\_color](#external_system_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_db_bg_color") |
| [external\_system\_db\_border\_color](#external_system_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_db_border_color") |
| [external\_system\_queue\_bg\_color](#external_system_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queue_bg_color") |
| [external\_system\_queue\_border\_color](#external_system_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queue_border_color") |
| [container\_bg\_color](#container_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_bg_color") |
| [container\_border\_color](#container_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_border_color") |
| [container\_db\_bg\_color](#container_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_db_bg_color") |
| [container\_db\_border\_color](#container_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_db_border_color") |
| [container\_queue\_bg\_color](#container_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queue_bg_color") |
| [container\_queue\_border\_color](#container_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queue_border_color") |
| [external\_container\_bg\_color](#external_container_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_bg_color") |
| [external\_container\_border\_color](#external_container_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_border_color") |
| [external\_container\_db\_bg\_color](#external_container_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_db_bg_color") |
| [external\_container\_db\_border\_color](#external_container_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_db_border_color") |
| [external\_container\_queue\_bg\_color](#external_container_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queue_bg_color") |
| [external\_container\_queue\_border\_color](#external_container_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queue_border_color") |
| [component\_bg\_color](#component_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_bg_color") |
| [component\_border\_color](#component_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_border_color") |
| [component\_db\_bg\_color](#component_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_db_bg_color") |
| [component\_db\_border\_color](#component_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_db_border_color") |
| [component\_queue\_bg\_color](#component_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queue_bg_color") |
| [component\_queue\_border\_color](#component_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queue_border_color") |
| [external\_component\_bg\_color](#external_component_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_bg_color") |
| [external\_component\_border\_color](#external_component_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_border_color") |
| [external\_component\_db\_bg\_color](#external_component_db_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_db_bg_color") |
| [external\_component\_db\_border\_color](#external_component_db_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_db_border_color") |
| [external\_component\_queue\_bg\_color](#external_component_queue_bg_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queue_bg_color") |
| [external\_component\_queue\_border\_color](#external_component_queue_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queue_border_color") |
| [personFont](#personfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFont") |
| [external\_personFont](#external_personfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-1.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFont") |
| [systemFont](#systemfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-2.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFont") |
| [external\_systemFont](#external_systemfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-3.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFont") |
| [system\_dbFont](#system_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-4.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFont") |
| [external\_system\_dbFont](#external_system_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-5.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFont") |
| [system\_queueFont](#system_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-6.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFont") |
| [external\_system\_queueFont](#external_system_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-7.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFont") |
| [containerFont](#containerfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-8.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFont") |
| [external\_containerFont](#external_containerfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-9.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFont") |
| [container\_dbFont](#container_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-10.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFont") |
| [external\_container\_dbFont](#external_container_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-11.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFont") |
| [container\_queueFont](#container_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-12.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFont") |
| [external\_container\_queueFont](#external_container_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-13.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFont") |
| [componentFont](#componentfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-14.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFont") |
| [external\_componentFont](#external_componentfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-15.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFont") |
| [component\_dbFont](#component_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-16.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFont") |
| [external\_component\_dbFont](#external_component_dbfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-17.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFont") |
| [component\_queueFont](#component_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-18.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFont") |
| [external\_component\_queueFont](#external_component_queuefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-19.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFont") |
| [boundaryFont](#boundaryfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-20.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFont") |
| [messageFont](#messagefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-21.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFont") |

### diagramMarginX

Margin to the right and left of the c4 diagram, must be a positive value.

`diagramMarginX`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/diagramMarginX")

#### diagramMarginX Type

`integer`

#### diagramMarginX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginX Default Value

The default value is:

```json
50
```

### diagramMarginY

Margin to the over and under the c4 diagram, must be a positive value.

`diagramMarginY`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/diagramMarginY")

#### diagramMarginY Type

`integer`

#### diagramMarginY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginY Default Value

The default value is:

```json
10
```

### c4ShapeMargin

Margin between shapes

`c4ShapeMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapeMargin")

#### c4ShapeMargin Type

`integer`

#### c4ShapeMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### c4ShapeMargin Default Value

The default value is:

```json
50
```

### c4ShapePadding

Padding between shapes

`c4ShapePadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapePadding")

#### c4ShapePadding Type

`integer`

#### c4ShapePadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### c4ShapePadding Default Value

The default value is:

```json
20
```

### width

Width of person boxes

`width`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/width")

#### width Type

`integer`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### width Default Value

The default value is:

```json
216
```

### height

Height of person boxes

`height`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/height")

#### height Type

`integer`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### height Default Value

The default value is:

```json
60
```

### boxMargin

Margin around boxes

`boxMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boxMargin")

#### boxMargin Type

`integer`

#### boxMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxMargin Default Value

The default value is:

```json
10
```

### c4ShapeInRow

How many shapes to place in each row.

`c4ShapeInRow`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4shapeinrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4ShapeInRow")

#### c4ShapeInRow Type

`integer`

#### c4ShapeInRow Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### c4ShapeInRow Default Value

The default value is:

```json
4
```

### nextLinePaddingX

`nextLinePaddingX`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-nextlinepaddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/nextLinePaddingX")

#### nextLinePaddingX Type

`number`

#### nextLinePaddingX Default Value

The default value is:

```json
0
```

### c4BoundaryInRow

How many boundaries to place in each row.

`c4BoundaryInRow`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-c4boundaryinrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/c4BoundaryInRow")

#### c4BoundaryInRow Type

`integer`

#### c4BoundaryInRow Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### c4BoundaryInRow Default Value

The default value is:

```json
2
```

### personFontSize

This sets the font size of Person shape for the diagram

`personFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontSize")

#### personFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontsize.html))

#### personFontSize Default Value

The default value is:

```json
14
```

### personFontFamily

This sets the font weight of Person shape for the diagram

`personFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontFamily")

#### personFontFamily Type

`string`

#### personFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### personFontWeight

This sets the font weight of Person shape for the diagram

`personFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFontWeight")

#### personFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-personfontweight.html))

#### personFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_personFontSize

This sets the font size of External Person shape for the diagram

`external_personFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontSize")

#### external\_personFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontsize.html))

#### external\_personFontSize Default Value

The default value is:

```json
14
```

### external\_personFontFamily

This sets the font family of External Person shape for the diagram

`external_personFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontFamily")

#### external\_personFontFamily Type

`string`

#### external\_personFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_personFontWeight

This sets the font weight of External Person shape for the diagram

`external_personFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFontWeight")

#### external\_personFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_personfontweight.html))

#### external\_personFontWeight Default Value

The default value is:

```json
"normal"
```

### systemFontSize

This sets the font size of System shape for the diagram

`systemFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontSize")

#### systemFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontsize.html))

#### systemFontSize Default Value

The default value is:

```json
14
```

### systemFontFamily

This sets the font family of System shape for the diagram

`systemFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontFamily")

#### systemFontFamily Type

`string`

#### systemFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### systemFontWeight

This sets the font weight of System shape for the diagram

`systemFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFontWeight")

#### systemFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-systemfontweight.html))

#### systemFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_systemFontSize

This sets the font size of External System shape for the diagram

`external_systemFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontSize")

#### external\_systemFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontsize.html))

#### external\_systemFontSize Default Value

The default value is:

```json
14
```

### external\_systemFontFamily

This sets the font family of External System shape for the diagram

`external_systemFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontFamily")

#### external\_systemFontFamily Type

`string`

#### external\_systemFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_systemFontWeight

This sets the font weight of External System shape for the diagram

`external_systemFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFontWeight")

#### external\_systemFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_systemfontweight.html))

#### external\_systemFontWeight Default Value

The default value is:

```json
"normal"
```

### system\_dbFontSize

This sets the font size of System DB shape for the diagram

`system_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontSize")

#### system\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontsize.html))

#### system\_dbFontSize Default Value

The default value is:

```json
14
```

### system\_dbFontFamily

This sets the font family of System DB shape for the diagram

`system_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontFamily")

#### system\_dbFontFamily Type

`string`

#### system\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### system\_dbFontWeight

This sets the font weight of System DB shape for the diagram

`system_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFontWeight")

#### system\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_dbfontweight.html))

#### system\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_system\_dbFontSize

This sets the font size of External System DB shape for the diagram

`external_system_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontSize")

#### external\_system\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontsize.html))

#### external\_system\_dbFontSize Default Value

The default value is:

```json
14
```

### external\_system\_dbFontFamily

This sets the font family of External System DB shape for the diagram

`external_system_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontFamily")

#### external\_system\_dbFontFamily Type

`string`

#### external\_system\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_system\_dbFontWeight

This sets the font weight of External System DB shape for the diagram

`external_system_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFontWeight")

#### external\_system\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_dbfontweight.html))

#### external\_system\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### system\_queueFontSize

This sets the font size of System Queue shape for the diagram

`system_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontSize")

#### system\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontsize.html))

#### system\_queueFontSize Default Value

The default value is:

```json
14
```

### system\_queueFontFamily

This sets the font family of System Queue shape for the diagram

`system_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontFamily")

#### system\_queueFontFamily Type

`string`

#### system\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### system\_queueFontWeight

This sets the font weight of System Queue shape for the diagram

`system_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFontWeight")

#### system\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queuefontweight.html))

#### system\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_system\_queueFontSize

This sets the font size of External System Queue shape for the diagram

`external_system_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontSize")

#### external\_system\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontsize.html))

#### external\_system\_queueFontSize Default Value

The default value is:

```json
14
```

### external\_system\_queueFontFamily

This sets the font family of External System Queue shape for the diagram

`external_system_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontFamily")

#### external\_system\_queueFontFamily Type

`string`

#### external\_system\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_system\_queueFontWeight

This sets the font weight of External System Queue shape for the diagram

`external_system_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFontWeight")

#### external\_system\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queuefontweight.html))

#### external\_system\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### boundaryFontSize

This sets the font size of Boundary shape for the diagram

`boundaryFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontSize")

#### boundaryFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontsize.html))

#### boundaryFontSize Default Value

The default value is:

```json
14
```

### boundaryFontFamily

This sets the font family of Boundary shape for the diagram

`boundaryFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontFamily")

#### boundaryFontFamily Type

`string`

#### boundaryFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### boundaryFontWeight

This sets the font weight of Boundary shape for the diagram

`boundaryFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFontWeight")

#### boundaryFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-boundaryfontweight.html))

#### boundaryFontWeight Default Value

The default value is:

```json
"normal"
```

### messageFontSize

This sets the font size of Message shape for the diagram

`messageFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontSize")

#### messageFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontsize.html))

#### messageFontSize Default Value

The default value is:

```json
12
```

### messageFontFamily

This sets the font family of Message shape for the diagram

`messageFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontFamily")

#### messageFontFamily Type

`string`

#### messageFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### messageFontWeight

This sets the font weight of Message shape for the diagram

`messageFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFontWeight")

#### messageFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-messagefontweight.html))

#### messageFontWeight Default Value

The default value is:

```json
"normal"
```

### containerFontSize

This sets the font size of Container shape for the diagram

`containerFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontSize")

#### containerFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontsize.html))

#### containerFontSize Default Value

The default value is:

```json
14
```

### containerFontFamily

This sets the font family of Container shape for the diagram

`containerFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontFamily")

#### containerFontFamily Type

`string`

#### containerFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### containerFontWeight

This sets the font weight of Container shape for the diagram

`containerFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFontWeight")

#### containerFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-containerfontweight.html))

#### containerFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_containerFontSize

This sets the font size of External Container shape for the diagram

`external_containerFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontSize")

#### external\_containerFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontsize.html))

#### external\_containerFontSize Default Value

The default value is:

```json
14
```

### external\_containerFontFamily

This sets the font family of External Container shape for the diagram

`external_containerFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontFamily")

#### external\_containerFontFamily Type

`string`

#### external\_containerFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_containerFontWeight

This sets the font weight of External Container shape for the diagram

`external_containerFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFontWeight")

#### external\_containerFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_containerfontweight.html))

#### external\_containerFontWeight Default Value

The default value is:

```json
"normal"
```

### container\_dbFontSize

This sets the font size of Container DB shape for the diagram

`container_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontSize")

#### container\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontsize.html))

#### container\_dbFontSize Default Value

The default value is:

```json
14
```

### container\_dbFontFamily

This sets the font family of Container DB shape for the diagram

`container_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontFamily")

#### container\_dbFontFamily Type

`string`

#### container\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### container\_dbFontWeight

This sets the font weight of Container DB shape for the diagram

`container_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFontWeight")

#### container\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_dbfontweight.html))

#### container\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_container\_dbFontSize

This sets the font size of External Container DB shape for the diagram

`external_container_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontSize")

#### external\_container\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontsize.html))

#### external\_container\_dbFontSize Default Value

The default value is:

```json
14
```

### external\_container\_dbFontFamily

This sets the font family of External Container DB shape for the diagram

`external_container_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontFamily")

#### external\_container\_dbFontFamily Type

`string`

#### external\_container\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_container\_dbFontWeight

This sets the font weight of External Container DB shape for the diagram

`external_container_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFontWeight")

#### external\_container\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_dbfontweight.html))

#### external\_container\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### container\_queueFontSize

This sets the font size of Container Queue shape for the diagram

`container_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontSize")

#### container\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontsize.html))

#### container\_queueFontSize Default Value

The default value is:

```json
14
```

### container\_queueFontFamily

This sets the font family of Container Queue shape for the diagram

`container_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontFamily")

#### container\_queueFontFamily Type

`string`

#### container\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### container\_queueFontWeight

This sets the font weight of Container Queue shape for the diagram

`container_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFontWeight")

#### container\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queuefontweight.html))

#### container\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_container\_queueFontSize

This sets the font size of External Container Queue shape for the diagram

`external_container_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontSize")

#### external\_container\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontsize.html))

#### external\_container\_queueFontSize Default Value

The default value is:

```json
14
```

### external\_container\_queueFontFamily

This sets the font family of External Container Queue shape for the diagram

`external_container_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontFamily")

#### external\_container\_queueFontFamily Type

`string`

#### external\_container\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_container\_queueFontWeight

This sets the font weight of External Container Queue shape for the diagram

`external_container_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFontWeight")

#### external\_container\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queuefontweight.html))

#### external\_container\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### componentFontSize

This sets the font size of Component shape for the diagram

`componentFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontSize")

#### componentFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontsize.html))

#### componentFontSize Default Value

The default value is:

```json
14
```

### componentFontFamily

This sets the font family of Component shape for the diagram

`componentFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontFamily")

#### componentFontFamily Type

`string`

#### componentFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### componentFontWeight

This sets the font weight of Component shape for the diagram

`componentFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFontWeight")

#### componentFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-componentfontweight.html))

#### componentFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_componentFontSize

This sets the font size of External Component shape for the diagram

`external_componentFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontSize")

#### external\_componentFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontsize.html))

#### external\_componentFontSize Default Value

The default value is:

```json
14
```

### external\_componentFontFamily

This sets the font family of External Component shape for the diagram

`external_componentFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontFamily")

#### external\_componentFontFamily Type

`string`

#### external\_componentFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_componentFontWeight

This sets the font weight of External Component shape for the diagram

`external_componentFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFontWeight")

#### external\_componentFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_componentfontweight.html))

#### external\_componentFontWeight Default Value

The default value is:

```json
"normal"
```

### component\_dbFontSize

This sets the font size of Component DB shape for the diagram

`component_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontSize")

#### component\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontsize.html))

#### component\_dbFontSize Default Value

The default value is:

```json
14
```

### component\_dbFontFamily

This sets the font family of Component DB shape for the diagram

`component_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontFamily")

#### component\_dbFontFamily Type

`string`

#### component\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### component\_dbFontWeight

This sets the font weight of Component DB shape for the diagram

`component_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFontWeight")

#### component\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_dbfontweight.html))

#### component\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_component\_dbFontSize

This sets the font size of External Component DB shape for the diagram

`external_component_dbFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontSize")

#### external\_component\_dbFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontsize.html))

#### external\_component\_dbFontSize Default Value

The default value is:

```json
14
```

### external\_component\_dbFontFamily

This sets the font family of External Component DB shape for the diagram

`external_component_dbFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontFamily")

#### external\_component\_dbFontFamily Type

`string`

#### external\_component\_dbFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_component\_dbFontWeight

This sets the font weight of External Component DB shape for the diagram

`external_component_dbFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFontWeight")

#### external\_component\_dbFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_dbfontweight.html))

#### external\_component\_dbFontWeight Default Value

The default value is:

```json
"normal"
```

### component\_queueFontSize

This sets the font size of Component Queue shape for the diagram

`component_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontSize")

#### component\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontsize.html))

#### component\_queueFontSize Default Value

The default value is:

```json
14
```

### component\_queueFontFamily

This sets the font family of Component Queue shape for the diagram

`component_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontFamily")

#### component\_queueFontFamily Type

`string`

#### component\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### component\_queueFontWeight

This sets the font weight of Component Queue shape for the diagram

`component_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFontWeight")

#### component\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queuefontweight.html))

#### component\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### external\_component\_queueFontSize

This sets the font size of External Component Queue shape for the diagram

`external_component_queueFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontSize")

#### external\_component\_queueFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontsize.html))

#### external\_component\_queueFontSize Default Value

The default value is:

```json
14
```

### external\_component\_queueFontFamily

This sets the font family of External Component Queue shape for the diagram

`external_component_queueFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontFamily")

#### external\_component\_queueFontFamily Type

`string`

#### external\_component\_queueFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### external\_component\_queueFontWeight

This sets the font weight of External Component Queue shape for the diagram

`external_component_queueFontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFontWeight")

#### external\_component\_queueFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queuefontweight.html))

#### external\_component\_queueFontWeight Default Value

The default value is:

```json
"normal"
```

### wrap

This sets the auto-wrap state for the diagram

`wrap`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/wrap")

#### wrap Type

`boolean`

#### wrap Default Value

The default value is:

```json
true
```

### wrapPadding

This sets the auto-wrap padding for the diagram (sides only)

`wrapPadding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrappadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/wrapPadding")

#### wrapPadding Type

`number`

#### wrapPadding Default Value

The default value is:

```json
10
```

### person\_bg\_color

`person_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-person_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/person_bg_color")

#### person\_bg\_color Type

`string`

#### person\_bg\_color Default Value

The default value is:

```json
"#08427B"
```

### person\_border\_color

`person_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-person_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/person_border_color")

#### person\_border\_color Type

`string`

#### person\_border\_color Default Value

The default value is:

```json
"#073B6F"
```

### external\_person\_bg\_color

`external_person_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_person_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_person_bg_color")

#### external\_person\_bg\_color Type

`string`

#### external\_person\_bg\_color Default Value

The default value is:

```json
"#686868"
```

### external\_person\_border\_color

`external_person_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_person_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_person_border_color")

#### external\_person\_border\_color Type

`string`

#### external\_person\_border\_color Default Value

The default value is:

```json
"#8A8A8A"
```

### system\_bg\_color

`system_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_bg_color")

#### system\_bg\_color Type

`string`

#### system\_bg\_color Default Value

The default value is:

```json
"#1168BD"
```

### system\_border\_color

`system_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_border_color")

#### system\_border\_color Type

`string`

#### system\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### system\_db\_bg\_color

`system_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_db_bg_color")

#### system\_db\_bg\_color Type

`string`

#### system\_db\_bg\_color Default Value

The default value is:

```json
"#1168BD"
```

### system\_db\_border\_color

`system_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_db_border_color")

#### system\_db\_border\_color Type

`string`

#### system\_db\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### system\_queue\_bg\_color

`system_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queue_bg_color")

#### system\_queue\_bg\_color Type

`string`

#### system\_queue\_bg\_color Default Value

The default value is:

```json
"#1168BD"
```

### system\_queue\_border\_color

`system_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-system_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queue_border_color")

#### system\_queue\_border\_color Type

`string`

#### system\_queue\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### external\_system\_bg\_color

`external_system_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_bg_color")

#### external\_system\_bg\_color Type

`string`

#### external\_system\_bg\_color Default Value

The default value is:

```json
"#999999"
```

### external\_system\_border\_color

`external_system_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_border_color")

#### external\_system\_border\_color Type

`string`

#### external\_system\_border\_color Default Value

The default value is:

```json
"#8A8A8A"
```

### external\_system\_db\_bg\_color

`external_system_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_db_bg_color")

#### external\_system\_db\_bg\_color Type

`string`

#### external\_system\_db\_bg\_color Default Value

The default value is:

```json
"#999999"
```

### external\_system\_db\_border\_color

`external_system_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_db_border_color")

#### external\_system\_db\_border\_color Type

`string`

#### external\_system\_db\_border\_color Default Value

The default value is:

```json
"#8A8A8A"
```

### external\_system\_queue\_bg\_color

`external_system_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queue_bg_color")

#### external\_system\_queue\_bg\_color Type

`string`

#### external\_system\_queue\_bg\_color Default Value

The default value is:

```json
"#999999"
```

### external\_system\_queue\_border\_color

`external_system_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_system_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queue_border_color")

#### external\_system\_queue\_border\_color Type

`string`

#### external\_system\_queue\_border\_color Default Value

The default value is:

```json
"#8A8A8A"
```

### container\_bg\_color

`container_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_bg_color")

#### container\_bg\_color Type

`string`

#### container\_bg\_color Default Value

The default value is:

```json
"#438DD5"
```

### container\_border\_color

`container_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_border_color")

#### container\_border\_color Type

`string`

#### container\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### container\_db\_bg\_color

`container_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_db_bg_color")

#### container\_db\_bg\_color Type

`string`

#### container\_db\_bg\_color Default Value

The default value is:

```json
"#438DD5"
```

### container\_db\_border\_color

`container_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_db_border_color")

#### container\_db\_border\_color Type

`string`

#### container\_db\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### container\_queue\_bg\_color

`container_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queue_bg_color")

#### container\_queue\_bg\_color Type

`string`

#### container\_queue\_bg\_color Default Value

The default value is:

```json
"#438DD5"
```

### container\_queue\_border\_color

`container_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-container_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queue_border_color")

#### container\_queue\_border\_color Type

`string`

#### container\_queue\_border\_color Default Value

The default value is:

```json
"#3C7FC0"
```

### external\_container\_bg\_color

`external_container_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_bg_color")

#### external\_container\_bg\_color Type

`string`

#### external\_container\_bg\_color Default Value

The default value is:

```json
"#B3B3B3"
```

### external\_container\_border\_color

`external_container_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_border_color")

#### external\_container\_border\_color Type

`string`

#### external\_container\_border\_color Default Value

The default value is:

```json
"#A6A6A6"
```

### external\_container\_db\_bg\_color

`external_container_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_db_bg_color")

#### external\_container\_db\_bg\_color Type

`string`

#### external\_container\_db\_bg\_color Default Value

The default value is:

```json
"#B3B3B3"
```

### external\_container\_db\_border\_color

`external_container_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_db_border_color")

#### external\_container\_db\_border\_color Type

`string`

#### external\_container\_db\_border\_color Default Value

The default value is:

```json
"#A6A6A6"
```

### external\_container\_queue\_bg\_color

`external_container_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queue_bg_color")

#### external\_container\_queue\_bg\_color Type

`string`

#### external\_container\_queue\_bg\_color Default Value

The default value is:

```json
"#B3B3B3"
```

### external\_container\_queue\_border\_color

`external_container_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_container_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queue_border_color")

#### external\_container\_queue\_border\_color Type

`string`

#### external\_container\_queue\_border\_color Default Value

The default value is:

```json
"#A6A6A6"
```

### component\_bg\_color

`component_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_bg_color")

#### component\_bg\_color Type

`string`

#### component\_bg\_color Default Value

The default value is:

```json
"#85BBF0"
```

### component\_border\_color

`component_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_border_color")

#### component\_border\_color Type

`string`

#### component\_border\_color Default Value

The default value is:

```json
"#78A8D8"
```

### component\_db\_bg\_color

`component_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_db_bg_color")

#### component\_db\_bg\_color Type

`string`

#### component\_db\_bg\_color Default Value

The default value is:

```json
"#85BBF0"
```

### component\_db\_border\_color

`component_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_db_border_color")

#### component\_db\_border\_color Type

`string`

#### component\_db\_border\_color Default Value

The default value is:

```json
"#78A8D8"
```

### component\_queue\_bg\_color

`component_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queue_bg_color")

#### component\_queue\_bg\_color Type

`string`

#### component\_queue\_bg\_color Default Value

The default value is:

```json
"#85BBF0"
```

### component\_queue\_border\_color

`component_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-component_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queue_border_color")

#### component\_queue\_border\_color Type

`string`

#### component\_queue\_border\_color Default Value

The default value is:

```json
"#78A8D8"
```

### external\_component\_bg\_color

`external_component_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_bg_color")

#### external\_component\_bg\_color Type

`string`

#### external\_component\_bg\_color Default Value

The default value is:

```json
"#CCCCCC"
```

### external\_component\_border\_color

`external_component_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_border_color")

#### external\_component\_border\_color Type

`string`

#### external\_component\_border\_color Default Value

The default value is:

```json
"#BFBFBF"
```

### external\_component\_db\_bg\_color

`external_component_db_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_db_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_db_bg_color")

#### external\_component\_db\_bg\_color Type

`string`

#### external\_component\_db\_bg\_color Default Value

The default value is:

```json
"#CCCCCC"
```

### external\_component\_db\_border\_color

`external_component_db_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_db_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_db_border_color")

#### external\_component\_db\_border\_color Type

`string`

#### external\_component\_db\_border\_color Default Value

The default value is:

```json
"#BFBFBF"
```

### external\_component\_queue\_bg\_color

`external_component_queue_bg_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queue_bg_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queue_bg_color")

#### external\_component\_queue\_bg\_color Type

`string`

#### external\_component\_queue\_bg\_color Default Value

The default value is:

```json
"#CCCCCC"
```

### external\_component\_queue\_border\_color

`external_component_queue_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-external_component_queue_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queue_border_color")

#### external\_component\_queue\_border\_color Type

`string`

#### external\_component\_queue\_border\_color Default Value

The default value is:

```json
"#BFBFBF"
```

### personFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`personFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/personFont")
- tsType: `() => Partial<FontConfig>`

#### personFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator.html))

### external\_personFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_personFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-1.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-1.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_personFont")
- tsType: `() => Partial<FontConfig>`

#### external\_personFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-1.html))

### systemFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`systemFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-2.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-2.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/systemFont")
- tsType: `() => Partial<FontConfig>`

#### systemFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-2.html))

### external\_systemFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_systemFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-3.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-3.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_systemFont")
- tsType: `() => Partial<FontConfig>`

#### external\_systemFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-3.html))

### system\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`system_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-4.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-4.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_dbFont")
- tsType: `() => Partial<FontConfig>`

#### system\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-4.html))

### external\_system\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_system_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-5.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-5.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_dbFont")
- tsType: `() => Partial<FontConfig>`

#### external\_system\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-5.html))

### system\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`system_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-6.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-6.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/system_queueFont")
- tsType: `() => Partial<FontConfig>`

#### system\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-6.html))

### external\_system\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_system_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-7.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-7.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_system_queueFont")
- tsType: `() => Partial<FontConfig>`

#### external\_system\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-7.html))

### containerFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`containerFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-8.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-8.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/containerFont")
- tsType: `() => Partial<FontConfig>`

#### containerFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-8.html))

### external\_containerFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_containerFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-9.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-9.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_containerFont")
- tsType: `() => Partial<FontConfig>`

#### external\_containerFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-9.html))

### container\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`container_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-10.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-10.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_dbFont")
- tsType: `() => Partial<FontConfig>`

#### container\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-10.html))

### external\_container\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_container_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-11.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-11.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_dbFont")
- tsType: `() => Partial<FontConfig>`

#### external\_container\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-11.html))

### container\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`container_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-12.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-12.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/container_queueFont")
- tsType: `() => Partial<FontConfig>`

#### container\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-12.html))

### external\_container\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_container_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-13.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-13.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_container_queueFont")
- tsType: `() => Partial<FontConfig>`

#### external\_container\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-13.html))

### componentFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`componentFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-14.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-14.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/componentFont")
- tsType: `() => Partial<FontConfig>`

#### componentFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-14.html))

### external\_componentFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_componentFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-15.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-15.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_componentFont")
- tsType: `() => Partial<FontConfig>`

#### external\_componentFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-15.html))

### component\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`component_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-16.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-16.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_dbFont")
- tsType: `() => Partial<FontConfig>`

#### component\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-16.html))

### external\_component\_dbFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_component_dbFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-17.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-17.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_dbFont")
- tsType: `() => Partial<FontConfig>`

#### external\_component\_dbFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-17.html))

### component\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`component_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-18.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-18.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/component_queueFont")
- tsType: `() => Partial<FontConfig>`

#### component\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-18.html))

### external\_component\_queueFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`external_component_queueFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-19.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-19.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/external_component_queueFont")
- tsType: `() => Partial<FontConfig>`

#### external\_component\_queueFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-19.html))

### boundaryFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`boundaryFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-20.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-20.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/boundaryFont")
- tsType: `() => Partial<FontConfig>`

#### boundaryFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-20.html))

### messageFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`messageFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-21.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-21.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/C4DiagramConfig/properties/messageFont")
- tsType: `() => Partial<FontConfig>`

#### messageFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-font-calculator-21.html))

## Definitions group GitGraphDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/titleTopMargin") |
| [diagramPadding](#diagrampadding) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/diagramPadding") |
| [nodeLabel](#nodelabel) | Merged | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-nodelabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/nodeLabel") |
|  | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-mainbranchname.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/mainBranchName") |
|  | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-mainbranchorder.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/mainBranchOrder") |
| [showCommitLabel](#showcommitlabel) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-showcommitlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/showCommitLabel") |
| [showBranches](#showbranches) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-showbranches.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/showBranches") |
| [rotateCommitLabel](#rotatecommitlabel) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-rotatecommitlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/rotateCommitLabel") |
| [parallelCommits](#parallelcommits) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-parallelcommits.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/parallelCommits") |
| [arrowMarkerAbsolute](#arrowmarkerabsolute-1) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### diagramPadding

`diagramPadding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/diagramPadding")

#### diagramPadding Type

`number`

#### diagramPadding Default Value

The default value is:

```json
8
```

### nodeLabel

`nodeLabel`

- is optional
- Type: `object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-nodelabel.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-nodelabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/nodeLabel")

#### nodeLabel Type

`object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-nodelabel.html))

all of

- [Node Label](https://mermaid.js.org/config/schema-docs/config-defs-node-label.html "check type definition")

#### nodeLabel Default Value

The default value is:

```json
{
  "width": 75,
  "height": 100,
  "x": -25,
  "y": 0
}
```

### mainBranchName

`mainBranchName`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-mainbranchname.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/mainBranchName")

#### mainBranchName Type

`string`

#### mainBranchName Default Value

The default value is:

```json
"main"
```

### mainBranchOrder

`mainBranchOrder`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-mainbranchorder.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/mainBranchOrder")

#### mainBranchOrder Type

`number`

#### mainBranchOrder Default Value

The default value is:

```json
0
```

### showCommitLabel

`showCommitLabel`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-showcommitlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/showCommitLabel")

#### showCommitLabel Type

`boolean`

#### showCommitLabel Default Value

The default value is:

```json
true
```

### showBranches

`showBranches`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-showbranches.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/showBranches")

#### showBranches Type

`boolean`

#### showBranches Default Value

The default value is:

```json
true
```

### rotateCommitLabel

`rotateCommitLabel`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-rotatecommitlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/rotateCommitLabel")

#### rotateCommitLabel Type

`boolean`

#### rotateCommitLabel Default Value

The default value is:

```json
true
```

### parallelCommits

`parallelCommits`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-parallelcommits.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GitGraphDiagramConfig/properties/parallelCommits")

#### parallelCommits Type

`boolean`

#### parallelCommits Default Value

The default value is:

```json
false
```

### arrowMarkerAbsolute

Controls whether or arrow markers in html code are absolute paths or anchors. This matters if you are using base tag settings.

`arrowMarkerAbsolute`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute")

#### arrowMarkerAbsolute Type

`boolean`

#### arrowMarkerAbsolute Default Value

The default value is:

```json
false
```

## Definitions group NodeLabel

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/width") |
| [height](#height-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/height") |
| [x](#x) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-x.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/x") |
| [y](#y) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-y.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/y") |

### width

`width`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/width")

#### width Type

`number`

### height

`height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/height")

#### height Type

`number`

### x

`x`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-x.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/x")

#### x Type

`number`

### y

`y`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-node-label-properties-y.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/NodeLabel/properties/y")

#### y Type

`number`

## Definitions group RequirementDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [rect\_fill](#rect_fill) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_fill.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_fill") |
| [text\_color](#text_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-text_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/text_color") |
| [rect\_border\_size](#rect_border_size) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_border_size.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_border_size") |
| [rect\_border\_color](#rect_border_color) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_border_color") |
| [rect\_min\_width](#rect_min_width) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_min_width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_min_width") |
| [rect\_min\_height](#rect_min_height) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_min_height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_min_height") |
| [fontSize](#fontsize-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/fontSize") |
| [rect\_padding](#rect_padding) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_padding") |
| [line\_height](#line_height) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-line_height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/line_height") |

### rect\_fill

`rect_fill`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_fill.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_fill")

#### rect\_fill Type

`string`

#### rect\_fill Default Value

The default value is:

```json
"#f9f9f9"
```

### text\_color

`text_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-text_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/text_color")

#### text\_color Type

`string`

#### text\_color Default Value

The default value is:

```json
"#333"
```

### rect\_border\_size

`rect_border_size`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_border_size.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_border_size")

#### rect\_border\_size Type

`string`

#### rect\_border\_size Default Value

The default value is:

```json
"0.5px"
```

### rect\_border\_color

`rect_border_color`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_border_color.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_border_color")

#### rect\_border\_color Type

`string`

#### rect\_border\_color Default Value

The default value is:

```json
"#bbb"
```

### rect\_min\_width

`rect_min_width`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_min_width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_min_width")

#### rect\_min\_width Type

`number`

#### rect\_min\_width Default Value

The default value is:

```json
200
```

### rect\_min\_height

`rect_min_height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_min_height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_min_height")

#### rect\_min\_height Type

`number`

#### rect\_min\_height Default Value

The default value is:

```json
200
```

### fontSize

`fontSize`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/fontSize")

#### fontSize Type

`number`

#### fontSize Default Value

The default value is:

```json
14
```

### rect\_padding

`rect_padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-rect_padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/rect_padding")

#### rect\_padding Type

`number`

#### rect\_padding Default Value

The default value is:

```json
10
```

### line\_height

`line_height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-requirement-diagram-config-properties-line_height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RequirementDiagramConfig/properties/line_height")

#### line\_height Type

`number`

#### line\_height Default Value

The default value is:

```json
20
```

## Definitions group ArchitectureDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [padding](#padding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/padding") |
| [iconSize](#iconsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-iconsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/iconSize") |
| [fontSize](#fontsize-2) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/fontSize") |
| [randomize](#randomize) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-randomize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/randomize") |
| [nodeSeparation](#nodeseparation) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-nodeseparation.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/nodeSeparation") |
| [idealEdgeLengthMultiplier](#idealedgelengthmultiplier) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-idealedgelengthmultiplier.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/idealEdgeLengthMultiplier") |
| [edgeElasticity](#edgeelasticity) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-edgeelasticity.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/edgeElasticity") |
| [numIter](#numiter) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-numiter.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/numIter") |

### padding

`padding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
40
```

### iconSize

`iconSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-iconsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/iconSize")

#### iconSize Type

`number`

#### iconSize Default Value

The default value is:

```json
80
```

### fontSize

`fontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/fontSize")

#### fontSize Type

`number`

#### fontSize Default Value

The default value is:

```json
16
```

### randomize

Whether to randomize initial node positions before running the layout algorithm. When false (default), the layout is deterministic and produces identical results on every render. When true, nodes start at random positions, which may produce varied but potentially better-spaced layouts.

`randomize`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-randomize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/randomize")

#### randomize Type

`boolean`

#### randomize Default Value

The default value is:

```json
false
```

### nodeSeparation

Minimum separation (in pixels) between sibling nodes in the same group, passed through to the underlying fcose layout. Increase to spread overlapping siblings apart when many edges share the same port direction.

`nodeSeparation`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-nodeseparation.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/nodeSeparation")

#### nodeSeparation Type

`number`

#### nodeSeparation Default Value

The default value is:

```json
75
```

### idealEdgeLengthMultiplier

Multiplier applied to `iconSize` to compute the ideal length of edges between nodes within the same group. Increase to add breathing room; decrease to pack the diagram tighter. Edges crossing group boundaries are unaffected and use a fixed shorter length.

`idealEdgeLengthMultiplier`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-idealedgelengthmultiplier.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/idealEdgeLengthMultiplier")

#### idealEdgeLengthMultiplier Type

`number`

#### idealEdgeLengthMultiplier Default Value

The default value is:

```json
1.5
```

### edgeElasticity

Spring elasticity (0–1) applied to edges between nodes within the same group, passed through to fcose. Higher values pull connected nodes closer together; lower values let the layout spread them out. Edges crossing group boundaries are unaffected.

`edgeElasticity`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-edgeelasticity.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/edgeElasticity")

#### edgeElasticity Type

`number`

#### edgeElasticity Default Value

The default value is:

```json
0.45
```

### numIter

Maximum number of iterations the fcose layout algorithm runs before stopping. Increase for higher quality on large or densely-connected diagrams at the cost of render time.

`numIter`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-architecture-diagram-config-properties-numiter.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ArchitectureDiagramConfig/properties/numIter")

#### numIter Type

`number`

#### numIter Default Value

The default value is:

```json
2500
```

## Definitions group MindmapDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [padding](#padding-1) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/padding") |
| [maxNodeWidth](#maxnodewidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-maxnodewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/maxNodeWidth") |
| [layoutAlgorithm](#layoutalgorithm) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-layoutalgorithm.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/layoutAlgorithm") |

### padding

`padding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
10
```

### maxNodeWidth

`maxNodeWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-maxnodewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/maxNodeWidth")

#### maxNodeWidth Type

`number`

#### maxNodeWidth Default Value

The default value is:

```json
200
```

### layoutAlgorithm

Layout algorithm to use for positioning mindmap nodes

`layoutAlgorithm`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-mindmap-diagram-config-properties-layoutalgorithm.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/MindmapDiagramConfig/properties/layoutAlgorithm")

#### layoutAlgorithm Type

`string`

#### layoutAlgorithm Default Value

The default value is:

```json
"cose-bilkent"
```

## Definitions group IshikawaDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/IshikawaDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [diagramPadding](#diagrampadding-1) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/IshikawaDiagramConfig/properties/diagramPadding") |
| [useMaxWidth](#usemaxwidth-1) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/IshikawaDiagramConfig/properties/useMaxWidth") |

### diagramPadding

The amount of padding around the diagram as a whole so that embedded diagrams have margins, expressed in pixels.

`diagramPadding`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/IshikawaDiagramConfig/properties/diagramPadding")

#### diagramPadding Type

`integer`

#### diagramPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramPadding Default Value

The default value is:

```json
20
```

### useMaxWidth

`useMaxWidth`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-ishikawa-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/IshikawaDiagramConfig/properties/useMaxWidth")

#### useMaxWidth Type

`boolean`

#### useMaxWidth Default Value

The default value is:

```json
false
```

## Definitions group KanbanDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [padding](#padding-2) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/padding") |
| [sectionWidth](#sectionwidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-sectionwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/sectionWidth") |
| [ticketBaseUrl](#ticketbaseurl) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-ticketbaseurl.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/ticketBaseUrl") |

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
8
```

### sectionWidth

`sectionWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-sectionwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/sectionWidth")

#### sectionWidth Type

`number`

#### sectionWidth Default Value

The default value is:

```json
200
```

### ticketBaseUrl

`ticketBaseUrl`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-kanban-diagram-config-properties-ticketbaseurl.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/KanbanDiagramConfig/properties/ticketBaseUrl")

#### ticketBaseUrl Type

`string`

#### ticketBaseUrl Default Value

The default value is:

```json
""
```

## Definitions group PieDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/PieDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [textPosition](#textposition) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config-properties-textposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PieDiagramConfig/properties/textPosition") |

### textPosition

Axial position of slice's label from zero at the center to 1 at the outside edges.

`textPosition`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-pie-diagram-config-properties-textposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PieDiagramConfig/properties/textPosition")

#### textPosition Type

`number`

#### textPosition Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

#### textPosition Default Value

The default value is:

```json
0.75
```

## Definitions group QuadrantChartConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [chartWidth](#chartwidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-chartwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/chartWidth") |
| [chartHeight](#chartheight) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-chartheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/chartHeight") |
| [titleFontSize](#titlefontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/titleFontSize") |
| [titlePadding](#titlepadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/titlePadding") |
| [quadrantPadding](#quadrantpadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantPadding") |
| [xAxisLabelPadding](#xaxislabelpadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxislabelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisLabelPadding") |
| [yAxisLabelPadding](#yaxislabelpadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxislabelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisLabelPadding") |
| [xAxisLabelFontSize](#xaxislabelfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxislabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisLabelFontSize") |
| [yAxisLabelFontSize](#yaxislabelfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxislabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisLabelFontSize") |
| [quadrantLabelFontSize](#quadrantlabelfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantlabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantLabelFontSize") |
| [quadrantTextTopPadding](#quadranttexttoppadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadranttexttoppadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantTextTopPadding") |
| [pointTextPadding](#pointtextpadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointtextpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointTextPadding") |
| [pointLabelFontSize](#pointlabelfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointlabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointLabelFontSize") |
| [pointRadius](#pointradius) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointradius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointRadius") |
| [xAxisPosition](#xaxisposition) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxisposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisPosition") |
| [yAxisPosition](#yaxisposition) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxisposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisPosition") |
| [quadrantInternalBorderStrokeWidth](#quadrantinternalborderstrokewidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantinternalborderstrokewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantInternalBorderStrokeWidth") |
| [quadrantExternalBorderStrokeWidth](#quadrantexternalborderstrokewidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantexternalborderstrokewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantExternalBorderStrokeWidth") |

### chartWidth

Width of the chart

`chartWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-chartwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/chartWidth")

#### chartWidth Type

`number`

#### chartWidth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### chartWidth Default Value

The default value is:

```json
500
```

### chartHeight

Height of the chart

`chartHeight`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-chartheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/chartHeight")

#### chartHeight Type

`number`

#### chartHeight Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### chartHeight Default Value

The default value is:

```json
500
```

### titleFontSize

Chart title top and bottom padding

`titleFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/titleFontSize")

#### titleFontSize Type

`number`

#### titleFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleFontSize Default Value

The default value is:

```json
20
```

### titlePadding

Padding around the quadrant square

`titlePadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/titlePadding")

#### titlePadding Type

`number`

#### titlePadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titlePadding Default Value

The default value is:

```json
10
```

### quadrantPadding

quadrant title padding from top if the quadrant is rendered on top

`quadrantPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantPadding")

#### quadrantPadding Type

`number`

#### quadrantPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### quadrantPadding Default Value

The default value is:

```json
5
```

### xAxisLabelPadding

Padding around x-axis labels

`xAxisLabelPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxislabelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisLabelPadding")

#### xAxisLabelPadding Type

`number`

#### xAxisLabelPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### xAxisLabelPadding Default Value

The default value is:

```json
5
```

### yAxisLabelPadding

Padding around y-axis labels

`yAxisLabelPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxislabelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisLabelPadding")

#### yAxisLabelPadding Type

`number`

#### yAxisLabelPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### yAxisLabelPadding Default Value

The default value is:

```json
5
```

### xAxisLabelFontSize

x-axis label font size

`xAxisLabelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxislabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisLabelFontSize")

#### xAxisLabelFontSize Type

`number`

#### xAxisLabelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### xAxisLabelFontSize Default Value

The default value is:

```json
16
```

### yAxisLabelFontSize

y-axis label font size

`yAxisLabelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxislabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisLabelFontSize")

#### yAxisLabelFontSize Type

`number`

#### yAxisLabelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### yAxisLabelFontSize Default Value

The default value is:

```json
16
```

### quadrantLabelFontSize

quadrant title font size

`quadrantLabelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantlabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantLabelFontSize")

#### quadrantLabelFontSize Type

`number`

#### quadrantLabelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### quadrantLabelFontSize Default Value

The default value is:

```json
16
```

### quadrantTextTopPadding

quadrant title padding from top if the quadrant is rendered on top

`quadrantTextTopPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadranttexttoppadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantTextTopPadding")

#### quadrantTextTopPadding Type

`number`

#### quadrantTextTopPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### quadrantTextTopPadding Default Value

The default value is:

```json
5
```

### pointTextPadding

padding between point and point label

`pointTextPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointtextpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointTextPadding")

#### pointTextPadding Type

`number`

#### pointTextPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### pointTextPadding Default Value

The default value is:

```json
5
```

### pointLabelFontSize

point title font size

`pointLabelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointlabelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointLabelFontSize")

#### pointLabelFontSize Type

`number`

#### pointLabelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### pointLabelFontSize Default Value

The default value is:

```json
12
```

### pointRadius

radius of the point to be drawn

`pointRadius`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-pointradius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/pointRadius")

#### pointRadius Type

`number`

#### pointRadius Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### pointRadius Default Value

The default value is:

```json
5
```

### xAxisPosition

position of x-axis labels

`xAxisPosition`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-xaxisposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/xAxisPosition")

#### xAxisPosition Type

`string`

#### xAxisPosition Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"top"` |  |
| `"bottom"` |  |

#### xAxisPosition Default Value

The default value is:

```json
"top"
```

### yAxisPosition

position of y-axis labels

`yAxisPosition`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-yaxisposition.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/yAxisPosition")

#### yAxisPosition Type

`string`

#### yAxisPosition Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` |  |
| `"right"` |  |

#### yAxisPosition Default Value

The default value is:

```json
"left"
```

### quadrantInternalBorderStrokeWidth

stroke width of edges of the box that are inside the quadrant

`quadrantInternalBorderStrokeWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantinternalborderstrokewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantInternalBorderStrokeWidth")

#### quadrantInternalBorderStrokeWidth Type

`number`

#### quadrantInternalBorderStrokeWidth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### quadrantInternalBorderStrokeWidth Default Value

The default value is:

```json
1
```

### quadrantExternalBorderStrokeWidth

stroke width of edges of the box that are outside the quadrant

`quadrantExternalBorderStrokeWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-quadrant-chart-config-properties-quadrantexternalborderstrokewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/QuadrantChartConfig/properties/quadrantExternalBorderStrokeWidth")

#### quadrantExternalBorderStrokeWidth Type

`number`

#### quadrantExternalBorderStrokeWidth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### quadrantExternalBorderStrokeWidth Default Value

The default value is:

```json
2
```

## Definitions group XYChartAxisConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [showLabel](#showlabel) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showLabel") |
| [labelFontSize](#labelfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-labelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/labelFontSize") |
| [labelPadding](#labelpadding) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-labelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/labelPadding") |
| [showTitle](#showtitle) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showtitle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showTitle") |
| [titleFontSize](#titlefontsize-1) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/titleFontSize") |
| [titlePadding](#titlepadding-1) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/titlePadding") |
| [showTick](#showtick) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showtick.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showTick") |
| [tickLength](#ticklength) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-ticklength.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/tickLength") |
| [tickWidth](#tickwidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-tickwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/tickWidth") |
| [showAxisLine](#showaxisline) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showaxisline.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showAxisLine") |
| [axisLineWidth](#axislinewidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-axislinewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/axisLineWidth") |

### showLabel

Should show the axis labels (tick text)

`showLabel`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showlabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showLabel")

#### showLabel Type

`boolean`

#### showLabel Default Value

The default value is:

```json
true
```

### labelFontSize

font size of the axis labels (tick text)

`labelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-labelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/labelFontSize")

#### labelFontSize Type

`number`

#### labelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### labelFontSize Default Value

The default value is:

```json
14
```

### labelPadding

top and bottom space from axis label (tick text)

`labelPadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-labelpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/labelPadding")

#### labelPadding Type

`number`

#### labelPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### labelPadding Default Value

The default value is:

```json
5
```

### showTitle

Should show the axis title

`showTitle`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showtitle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showTitle")

#### showTitle Type

`boolean`

#### showTitle Default Value

The default value is:

```json
true
```

### titleFontSize

font size of the axis title

`titleFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/titleFontSize")

#### titleFontSize Type

`number`

#### titleFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### titleFontSize Default Value

The default value is:

```json
16
```

### titlePadding

top and bottom space from axis title

`titlePadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/titlePadding")

#### titlePadding Type

`number`

#### titlePadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titlePadding Default Value

The default value is:

```json
5
```

### showTick

Should show the axis tick lines

`showTick`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showtick.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showTick")

#### showTick Type

`boolean`

#### showTick Default Value

The default value is:

```json
true
```

### tickLength

length of the axis tick lines

`tickLength`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-ticklength.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/tickLength")

#### tickLength Type

`number`

#### tickLength Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### tickLength Default Value

The default value is:

```json
5
```

### tickWidth

width of the axis tick lines

`tickWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-tickwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/tickWidth")

#### tickWidth Type

`number`

#### tickWidth Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### tickWidth Default Value

The default value is:

```json
2
```

### showAxisLine

Show line across the axis

`showAxisLine`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-showaxisline.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/showAxisLine")

#### showAxisLine Type

`boolean`

#### showAxisLine Default Value

The default value is:

```json
true
```

### axisLineWidth

Width of the axis line

`axisLineWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config-properties-axislinewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartAxisConfig/properties/axisLineWidth")

#### axisLineWidth Type

`number`

#### axisLineWidth Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### axisLineWidth Default Value

The default value is:

```json
2
```

## Definitions group XYChartConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-2) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/width") |
| [height](#height-2) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/height") |
| [titleFontSize](#titlefontsize-2) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/titleFontSize") |
| [titlePadding](#titlepadding-2) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/titlePadding") |
| [showDataLabel](#showdatalabel) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showdatalabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showDataLabel") |
| [showDataLabelOutsideBar](#showdatalabeloutsidebar) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showdatalabeloutsidebar.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showDataLabelOutsideBar") |
| [showTitle](#showtitle-1) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showtitle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showTitle") |
| [xAxis](#xaxis) | `object` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/xAxis") |
| [yAxis](#yaxis) | `object` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/yAxis") |
| [chartOrientation](#chartorientation) | Not specified | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-chartorientation.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/chartOrientation") |
| [plotReservedSpacePercent](#plotreservedspacepercent) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-plotreservedspacepercent.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/plotReservedSpacePercent") |

### width

width of the chart

`width`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/width")

#### width Type

`number`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### width Default Value

The default value is:

```json
700
```

### height

height of the chart

`height`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/height")

#### height Type

`number`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### height Default Value

The default value is:

```json
500
```

### titleFontSize

Font size of the chart title

`titleFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/titleFontSize")

#### titleFontSize Type

`number`

#### titleFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### titleFontSize Default Value

The default value is:

```json
20
```

### titlePadding

Top and bottom space from the chart title

`titlePadding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-titlepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/titlePadding")

#### titlePadding Type

`number`

#### titlePadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titlePadding Default Value

The default value is:

```json
10
```

### showDataLabel

Should show the value corresponding to the bar within the bar

`showDataLabel`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showdatalabel.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showDataLabel")

#### showDataLabel Type

`boolean`

#### showDataLabel Default Value

The default value is:

```json
false
```

### showDataLabelOutsideBar

If showing data label then show it outside the bar

`showDataLabelOutsideBar`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showdatalabeloutsidebar.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showDataLabelOutsideBar")

#### showDataLabelOutsideBar Type

`boolean`

#### showDataLabelOutsideBar Default Value

The default value is:

```json
false
```

### showTitle

Should show the chart title

`showTitle`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-showtitle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/showTitle")

#### showTitle Type

`boolean`

#### showTitle Default Value

The default value is:

```json
true
```

### xAxis

This object contains configuration for XYChart axis config

`xAxis`

- is required
- Type: `object` ([XYChart axis config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/xAxis")

#### xAxis Type

`object` ([XYChart axis config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html))

#### xAxis Default Value

The default value is:

```json
{
  "$ref": "#/$defs/XYChartAxisConfig",
  "title": "XYChart axis config",
  "description": "This object contains configuration for XYChart axis config",
  "type": "object",
  "unevaluatedProperties": true,
  "required": [
    "showLabel",
    "labelFontSize",
    "labelPadding",
    "showTitle",
    "titleFontSize",
    "titlePadding",
    "showTick",
    "tickLength",
    "tickWidth",
    "showAxisLine",
    "axisLineWidth"
  ],
  "properties": {
    "showLabel": {
      "description": "Should show the axis labels (tick text)",
      "type": "boolean",
      "default": true
    },
    "labelFontSize": {
      "description": "font size of the axis labels (tick text)",
      "type": "number",
      "default": 14,
      "minimum": 1
    },
    "labelPadding": {
      "description": "top and bottom space from axis label (tick text)",
      "type": "number",
      "default": 5,
      "minimum": 0
    },
    "showTitle": {
      "description": "Should show the axis title",
      "type": "boolean",
      "default": true
    },
    "titleFontSize": {
      "description": "font size of the axis title",
      "type": "number",
      "default": 16,
      "minimum": 1
    },
    "titlePadding": {
      "description": "top and bottom space from axis title",
      "type": "number",
      "default": 5,
      "minimum": 0
    },
    "showTick": {
      "description": "Should show the axis tick lines",
      "type": "boolean",
      "default": true
    },
    "tickLength": {
      "description": "length of the axis tick lines",
      "type": "number",
      "default": 5,
      "minimum": 1
    },
    "tickWidth": {
      "description": "width of the axis tick lines",
      "type": "number",
      "default": 2,
      "minimum": 1
    },
    "showAxisLine": {
      "description": "Show line across the axis",
      "type": "boolean",
      "default": true
    },
    "axisLineWidth": {
      "description": "Width of the axis line",
      "type": "number",
      "default": 2,
      "minimum": 1
    }
  }
}
```

### yAxis

This object contains configuration for XYChart axis config

`yAxis`

- is required
- Type: `object` ([XYChart axis config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/yAxis")

#### yAxis Type

`object` ([XYChart axis config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-axis-config.html))

#### yAxis Default Value

The default value is:

```json
{
  "$ref": "#/$defs/XYChartAxisConfig",
  "title": "XYChart axis config",
  "description": "This object contains configuration for XYChart axis config",
  "type": "object",
  "unevaluatedProperties": true,
  "required": [
    "showLabel",
    "labelFontSize",
    "labelPadding",
    "showTitle",
    "titleFontSize",
    "titlePadding",
    "showTick",
    "tickLength",
    "tickWidth",
    "showAxisLine",
    "axisLineWidth"
  ],
  "properties": {
    "showLabel": {
      "description": "Should show the axis labels (tick text)",
      "type": "boolean",
      "default": true
    },
    "labelFontSize": {
      "description": "font size of the axis labels (tick text)",
      "type": "number",
      "default": 14,
      "minimum": 1
    },
    "labelPadding": {
      "description": "top and bottom space from axis label (tick text)",
      "type": "number",
      "default": 5,
      "minimum": 0
    },
    "showTitle": {
      "description": "Should show the axis title",
      "type": "boolean",
      "default": true
    },
    "titleFontSize": {
      "description": "font size of the axis title",
      "type": "number",
      "default": 16,
      "minimum": 1
    },
    "titlePadding": {
      "description": "top and bottom space from axis title",
      "type": "number",
      "default": 5,
      "minimum": 0
    },
    "showTick": {
      "description": "Should show the axis tick lines",
      "type": "boolean",
      "default": true
    },
    "tickLength": {
      "description": "length of the axis tick lines",
      "type": "number",
      "default": 5,
      "minimum": 1
    },
    "tickWidth": {
      "description": "width of the axis tick lines",
      "type": "number",
      "default": 2,
      "minimum": 1
    },
    "showAxisLine": {
      "description": "Show line across the axis",
      "type": "boolean",
      "default": true
    },
    "axisLineWidth": {
      "description": "Width of the axis line",
      "type": "number",
      "default": 2,
      "minimum": 1
    }
  }
}
```

### chartOrientation

How to plot will be drawn horizontal or vertical

`chartOrientation`

- is required
- Type: unknown
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-chartorientation.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/chartOrientation")
- tsType: `"vertical" | "horizontal"`

#### chartOrientation Type

unknown

#### chartOrientation Default Value

The default value is:

```json
"vertical"
```

### plotReservedSpacePercent

Minimum percent of space plots of the chart will take

`plotReservedSpacePercent`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-xychart-config-properties-plotreservedspacepercent.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/XYChartConfig/properties/plotReservedSpacePercent")

#### plotReservedSpacePercent Type

`number`

#### plotReservedSpacePercent Constraints

**minimum**: the value of this number must greater than or equal to: `30`

#### plotReservedSpacePercent Default Value

The default value is:

```json
50
```

## Definitions group ErDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/titleTopMargin") |
| [diagramPadding](#diagrampadding-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/diagramPadding") |
| [layoutDirection](#layoutdirection) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-layoutdirection.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/layoutDirection") |
| [minEntityWidth](#minentitywidth) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-minentitywidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/minEntityWidth") |
| [minEntityHeight](#minentityheight) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-minentityheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/minEntityHeight") |
| [entityPadding](#entitypadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-entitypadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/entityPadding") |
| [nodeSpacing](#nodespacing) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/nodeSpacing") |
| [rankSpacing](#rankspacing) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/rankSpacing") |
| [stroke](#stroke) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-stroke.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/stroke") |
| [fill](#fill) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-fill.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/fill") |
| [fontSize](#fontsize-3) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/fontSize") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### diagramPadding

The amount of padding around the diagram as a whole so that embedded diagrams have margins, expressed in pixels.

`diagramPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/diagramPadding")

#### diagramPadding Type

`integer`

#### diagramPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramPadding Default Value

The default value is:

```json
20
```

### layoutDirection

Directional bias for layout of entities

`layoutDirection`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-layoutdirection.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/layoutDirection")

#### layoutDirection Type

`string`

#### layoutDirection Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"TB"` | Top-Bottom |
| `"BT"` | Bottom-Top |
| `"LR"` | Left-Right |
| `"RL"` | Right to Left |

#### layoutDirection Default Value

The default value is:

```json
"TB"
```

### minEntityWidth

The minimum width of an entity box. Expressed in pixels.

`minEntityWidth`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-minentitywidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/minEntityWidth")

#### minEntityWidth Type

`integer`

#### minEntityWidth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### minEntityWidth Default Value

The default value is:

```json
100
```

### minEntityHeight

The minimum height of an entity box. Expressed in pixels.

`minEntityHeight`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-minentityheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/minEntityHeight")

#### minEntityHeight Type

`integer`

#### minEntityHeight Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### minEntityHeight Default Value

The default value is:

```json
75
```

### entityPadding

The minimum internal padding between text in an entity box and the enclosing box borders. Expressed in pixels.

`entityPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-entitypadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/entityPadding")

#### entityPadding Type

`integer`

#### entityPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### entityPadding Default Value

The default value is:

```json
15
```

### nodeSpacing

`nodeSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/nodeSpacing")

#### nodeSpacing Type

`integer`

#### nodeSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### nodeSpacing Default Value

The default value is:

```json
140
```

### rankSpacing

`rankSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/rankSpacing")

#### rankSpacing Type

`integer`

#### rankSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### rankSpacing Default Value

The default value is:

```json
80
```

### stroke

Stroke color of box edges and lines.

`stroke`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-stroke.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/stroke")

#### stroke Type

`string`

#### stroke Default Value

The default value is:

```json
"gray"
```

### fill

Fill color of entity boxes

`fill`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-fill.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/fill")

#### fill Type

`string`

#### fill Default Value

The default value is:

```json
"honeydew"
```

### fontSize

Font size (expressed as an integer representing a number of pixels)

`fontSize`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ErDiagramConfig/properties/fontSize")

#### fontSize Type

`integer`

#### fontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### fontSize Default Value

The default value is:

```json
12
```

## Definitions group StateDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/titleTopMargin") |
| [arrowMarkerAbsolute](#arrowmarkerabsolute-2) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/arrowMarkerAbsolute") |
| [dividerMargin](#dividermargin) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-dividermargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/dividerMargin") |
| [sizeUnit](#sizeunit) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-sizeunit.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/sizeUnit") |
| [padding](#padding-3) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/padding") |
| [textHeight](#textheight) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-textheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/textHeight") |
| [titleShift](#titleshift) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-titleshift.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/titleShift") |
| [noteMargin](#notemargin) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/noteMargin") |
| [nodeSpacing](#nodespacing-1) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/nodeSpacing") |
| [rankSpacing](#rankspacing-1) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/rankSpacing") |
| [forkWidth](#forkwidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-forkwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/forkWidth") |
| [forkHeight](#forkheight) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-forkheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/forkHeight") |
| [miniPadding](#minipadding) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-minipadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/miniPadding") |
| [fontSizeFactor](#fontsizefactor) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-fontsizefactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/fontSizeFactor") |
| [fontSize](#fontsize-4) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/fontSize") |
| [labelHeight](#labelheight) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-labelheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/labelHeight") |
| [edgeLengthFactor](#edgelengthfactor) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-edgelengthfactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/edgeLengthFactor") |
| [compositTitleSize](#composittitlesize) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-composittitlesize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/compositTitleSize") |
| [radius](#radius) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-radius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/radius") |
| [defaultRenderer](#defaultrenderer) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/defaultRenderer") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### arrowMarkerAbsolute

`arrowMarkerAbsolute`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/arrowMarkerAbsolute")

#### arrowMarkerAbsolute Type

`boolean`

### dividerMargin

`dividerMargin`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-dividermargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/dividerMargin")

#### dividerMargin Type

`number`

#### dividerMargin Default Value

The default value is:

```json
10
```

### sizeUnit

`sizeUnit`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-sizeunit.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/sizeUnit")

#### sizeUnit Type

`number`

#### sizeUnit Default Value

The default value is:

```json
5
```

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
8
```

### textHeight

`textHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-textheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/textHeight")

#### textHeight Type

`number`

#### textHeight Default Value

The default value is:

```json
10
```

### titleShift

`titleShift`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-titleshift.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/titleShift")

#### titleShift Type

`number`

#### titleShift Default Value

The default value is:

```json
-15
```

### noteMargin

`noteMargin`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/noteMargin")

#### noteMargin Type

`number`

#### noteMargin Default Value

The default value is:

```json
10
```

### nodeSpacing

`nodeSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/nodeSpacing")

#### nodeSpacing Type

`integer`

#### nodeSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### rankSpacing

`rankSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/rankSpacing")

#### rankSpacing Type

`integer`

#### rankSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### forkWidth

`forkWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-forkwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/forkWidth")

#### forkWidth Type

`number`

#### forkWidth Default Value

The default value is:

```json
70
```

### forkHeight

`forkHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-forkheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/forkHeight")

#### forkHeight Type

`number`

#### forkHeight Default Value

The default value is:

```json
7
```

### miniPadding

`miniPadding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-minipadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/miniPadding")

#### miniPadding Type

`number`

#### miniPadding Default Value

The default value is:

```json
2
```

### fontSizeFactor

Font size factor, this is used to guess the width of the edges labels before rendering by dagre layout. This might need updating if/when switching font

`fontSizeFactor`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-fontsizefactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/fontSizeFactor")

#### fontSizeFactor Type

`number`

#### fontSizeFactor Default Value

The default value is:

```json
5.02
```

### fontSize

`fontSize`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/fontSize")

#### fontSize Type

`number`

#### fontSize Default Value

The default value is:

```json
24
```

### labelHeight

`labelHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-labelheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/labelHeight")

#### labelHeight Type

`number`

#### labelHeight Default Value

The default value is:

```json
16
```

### edgeLengthFactor

`edgeLengthFactor`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-edgelengthfactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/edgeLengthFactor")

#### edgeLengthFactor Type

`string`

#### edgeLengthFactor Default Value

The default value is:

```json
"20"
```

### compositTitleSize

`compositTitleSize`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-composittitlesize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/compositTitleSize")

#### compositTitleSize Type

`number`

#### compositTitleSize Default Value

The default value is:

```json
35
```

### radius

`radius`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-radius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/radius")

#### radius Type

`number`

#### radius Default Value

The default value is:

```json
5
```

### defaultRenderer

Decides which rendering engine that is to be used for the rendering.

`defaultRenderer`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/StateDiagramConfig/properties/defaultRenderer")

#### defaultRenderer Type

`string`

#### defaultRenderer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"dagre-d3"` | The \[dagre-d3-es\](<https://www.npmjs.com/package/dagre-d3-es>) library. |
| `"dagre-wrapper"` | wrapper for dagre implemented in mermaid |
| `"elk"` | Layout using \[elkjs\](<https://github.com/kieler/elkjs>) |

#### defaultRenderer Default Value

The default value is:

```json
"dagre-wrapper"
```

## Definitions group ClassDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/titleTopMargin") |
| [arrowMarkerAbsolute](#arrowmarkerabsolute-3) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute") |
| [dividerMargin](#dividermargin-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-dividermargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/dividerMargin") |
| [padding](#padding-4) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/padding") |
| [textHeight](#textheight-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-textheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/textHeight") |
| [defaultRenderer](#defaultrenderer-1) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/defaultRenderer") |
| [nodeSpacing](#nodespacing-2) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/nodeSpacing") |
| [rankSpacing](#rankspacing-2) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/rankSpacing") |
| [diagramPadding](#diagrampadding-3) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/diagramPadding") |
| [htmlLabels](#htmllabels-1) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/htmlLabels") |
| [hideEmptyMembersBox](#hideemptymembersbox) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-hideemptymembersbox.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/hideEmptyMembersBox") |
| [hierarchicalNamespaces](#hierarchicalnamespaces) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-hierarchicalnamespaces.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/hierarchicalNamespaces") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### arrowMarkerAbsolute

Controls whether or arrow markers in html code are absolute paths or anchors. This matters if you are using base tag settings.

`arrowMarkerAbsolute`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/properties/arrowMarkerAbsolute")

#### arrowMarkerAbsolute Type

`boolean`

#### arrowMarkerAbsolute Default Value

The default value is:

```json
false
```

### dividerMargin

`dividerMargin`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-dividermargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/dividerMargin")

#### dividerMargin Type

`number`

#### dividerMargin Default Value

The default value is:

```json
10
```

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
5
```

### textHeight

`textHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-textheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/textHeight")

#### textHeight Type

`number`

#### textHeight Default Value

The default value is:

```json
10
```

### defaultRenderer

Decides which rendering engine that is to be used for the rendering.

`defaultRenderer`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/defaultRenderer")

#### defaultRenderer Type

`string`

#### defaultRenderer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"dagre-d3"` | The \[dagre-d3-es\](<https://www.npmjs.com/package/dagre-d3-es>) library. |
| `"dagre-wrapper"` | wrapper for dagre implemented in mermaid |
| `"elk"` | Layout using \[elkjs\](<https://github.com/kieler/elkjs>) |

#### defaultRenderer Default Value

The default value is:

```json
"dagre-wrapper"
```

### nodeSpacing

`nodeSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/nodeSpacing")

#### nodeSpacing Type

`integer`

#### nodeSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### rankSpacing

`rankSpacing`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/rankSpacing")

#### rankSpacing Type

`integer`

#### rankSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### diagramPadding

The amount of padding around the diagram as a whole so that embedded diagrams have margins, expressed in pixels.

`diagramPadding`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/diagramPadding")

#### diagramPadding Type

`integer`

#### diagramPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramPadding Default Value

The default value is:

```json
20
```

### htmlLabels

`htmlLabels`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/htmlLabels")

#### htmlLabels Type

`boolean`

#### htmlLabels Default Value

The default value is:

```json
false
```

### hideEmptyMembersBox

`hideEmptyMembersBox`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-hideemptymembersbox.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/hideEmptyMembersBox")

#### hideEmptyMembersBox Type

`boolean`

#### hideEmptyMembersBox Default Value

The default value is:

```json
false
```

### hierarchicalNamespaces

When true (default), nested namespaces render as hierarchical clusters, with each segment of a dotted name (e.g. `A.B.C`) becoming its own nested box. When false, namespaces render in compact mode: only explicitly declared namespaces are emitted and their full qualified name is used as a single flat label.

`hierarchicalNamespaces`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-class-diagram-config-properties-hierarchicalnamespaces.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/ClassDiagramConfig/properties/hierarchicalNamespaces")

#### hierarchicalNamespaces Type

`boolean`

#### hierarchicalNamespaces Default Value

The default value is:

```json
true
```

## Definitions group JourneyDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [diagramMarginX](#diagrammarginx-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/diagramMarginX") |
| [diagramMarginY](#diagrammarginy-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/diagramMarginY") |
| [leftMargin](#leftmargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-leftmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/leftMargin") |
| [maxLabelWidth](#maxlabelwidth) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-maxlabelwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/maxLabelWidth") |
| [width](#width-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/width") |
| [height](#height-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/height") |
| [boxMargin](#boxmargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/boxMargin") |
| [boxTextMargin](#boxtextmargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/boxTextMargin") |
| [noteMargin](#notemargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/noteMargin") |
| [messageMargin](#messagemargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/messageMargin") |
| [messageAlign](#messagealign) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/messageAlign") |
| [bottomMarginAdj](#bottommarginadj) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/bottomMarginAdj") |
| [rightAngles](#rightangles) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/rightAngles") |
| [taskFontSize](#taskfontsize) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskFontSize") |
| [taskFontFamily](#taskfontfamily) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskFontFamily") |
| [taskMargin](#taskmargin) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskMargin") |
| [activationWidth](#activationwidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/activationWidth") |
| [textPlacement](#textplacement) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-textplacement.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/textPlacement") |
| [actorColours](#actorcolours) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-actorcolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/actorColours") |
| [sectionFills](#sectionfills) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-sectionfills.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/sectionFills") |
| [sectionColours](#sectioncolours) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-sectioncolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/sectionColours") |
| [titleColor](#titlecolor) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlecolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleColor") |
| [titleFontFamily](#titlefontfamily) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleFontFamily") |
| [titleFontSize](#titlefontsize-3) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleFontSize") |

### diagramMarginX

Margin to the right and left of the c4 diagram, must be a positive value.

`diagramMarginX`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/diagramMarginX")

#### diagramMarginX Type

`integer`

#### diagramMarginX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginX Default Value

The default value is:

```json
50
```

### diagramMarginY

Margin to the over and under the c4 diagram, must be a positive value.

`diagramMarginY`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/diagramMarginY")

#### diagramMarginY Type

`integer`

#### diagramMarginY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginY Default Value

The default value is:

```json
10
```

### leftMargin

Margin between actors

`leftMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-leftmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/leftMargin")

#### leftMargin Type

`integer`

#### leftMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### leftMargin Default Value

The default value is:

```json
150
```

### maxLabelWidth

Maximum width of actor labels

`maxLabelWidth`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-maxlabelwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/maxLabelWidth")

#### maxLabelWidth Type

`integer`

#### maxLabelWidth Default Value

The default value is:

```json
360
```

### width

Width of actor boxes

`width`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/width")

#### width Type

`integer`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### width Default Value

The default value is:

```json
150
```

### height

Height of actor boxes

`height`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/height")

#### height Type

`integer`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### height Default Value

The default value is:

```json
50
```

### boxMargin

Margin around loop boxes

`boxMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/boxMargin")

#### boxMargin Type

`integer`

#### boxMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxMargin Default Value

The default value is:

```json
10
```

### boxTextMargin

Margin around the text in loop/alt/opt boxes

`boxTextMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/boxTextMargin")

#### boxTextMargin Type

`integer`

#### boxTextMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxTextMargin Default Value

The default value is:

```json
5
```

### noteMargin

Margin around notes

`noteMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/noteMargin")

#### noteMargin Type

`integer`

#### noteMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### noteMargin Default Value

The default value is:

```json
10
```

### messageMargin

Space between messages.

`messageMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/messageMargin")

#### messageMargin Type

`integer`

#### messageMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### messageMargin Default Value

The default value is:

```json
35
```

### messageAlign

Multiline message alignment

`messageAlign`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/messageAlign")

#### messageAlign Type

`string`

#### messageAlign Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` |  |
| `"center"` |  |
| `"right"` |  |

#### messageAlign Default Value

The default value is:

```json
"center"
```

### bottomMarginAdj

Prolongs the edge of the diagram downwards.

Depending on css styling this might need adjustment.

`bottomMarginAdj`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/bottomMarginAdj")

#### bottomMarginAdj Type

`integer`

#### bottomMarginAdj Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### bottomMarginAdj Default Value

The default value is:

```json
1
```

### rightAngles

Curved Arrows become Right Angles

This will display arrows that start and begin at the same node as right angles, rather than as curves.

`rightAngles`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/rightAngles")

#### rightAngles Type

`boolean`

#### rightAngles Default Value

The default value is:

```json
false
```

### taskFontSize

`taskFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskFontSize")

#### taskFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontsize.html))

#### taskFontSize Default Value

The default value is:

```json
14
```

### taskFontFamily

`taskFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskFontFamily")

#### taskFontFamily Type

`string`

#### taskFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### taskMargin

`taskMargin`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-taskmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/taskMargin")

#### taskMargin Type

`number`

#### taskMargin Default Value

The default value is:

```json
50
```

### activationWidth

Width of activation box

`activationWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/activationWidth")

#### activationWidth Type

`number`

#### activationWidth Default Value

The default value is:

```json
10
```

### textPlacement

text placement as: tspan | fo | old only text as before

`textPlacement`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-textplacement.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/textPlacement")

#### textPlacement Type

`string`

#### textPlacement Default Value

The default value is:

```json
"fo"
```

### actorColours

`actorColours`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-actorcolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/actorColours")

#### actorColours Type

`string[]`

#### actorColours Default Value

The default value is:

```json
["#8FBC8F", "#7CFC00", "#00FFFF", "#20B2AA", "#B0E0E6", "#FFFFE0"]
```

### sectionFills

`sectionFills`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-sectionfills.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/sectionFills")

#### sectionFills Type

`string[]`

#### sectionFills Default Value

The default value is:

```json
["#191970", "#8B008B", "#4B0082", "#2F4F4F", "#800000", "#8B4513", "#00008B"]
```

### sectionColours

`sectionColours`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-sectioncolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/sectionColours")

#### sectionColours Type

`string[]`

#### sectionColours Default Value

The default value is:

```json
["#fff"]
```

### titleColor

Color of the title text in Journey Diagrams

`titleColor`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlecolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleColor")

#### titleColor Type

`string`

#### titleColor Default Value

The default value is:

```json
""
```

### titleFontFamily

Font family to be used for the title text in Journey Diagrams

`titleFontFamily`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleFontFamily")

#### titleFontFamily Type

`string`

#### titleFontFamily Default Value

The default value is:

```json
"\"trebuchet ms\", verdana, arial, sans-serif"
```

### titleFontSize

Font size to be used for the title text in Journey Diagrams

`titleFontSize`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-titlefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/JourneyDiagramConfig/properties/titleFontSize")

#### titleFontSize Type

`string`

#### titleFontSize Default Value

The default value is:

```json
"4ex"
```

## Definitions group TimelineDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [diagramMarginX](#diagrammarginx-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/diagramMarginX") |
| [diagramMarginY](#diagrammarginy-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/diagramMarginY") |
| [leftMargin](#leftmargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-leftmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/leftMargin") |
| [width](#width-4) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/width") |
| [height](#height-4) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/height") |
| [padding](#padding-5) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/padding") |
| [boxMargin](#boxmargin-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/boxMargin") |
| [boxTextMargin](#boxtextmargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/boxTextMargin") |
| [noteMargin](#notemargin-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/noteMargin") |
| [messageMargin](#messagemargin-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/messageMargin") |
| [messageAlign](#messagealign-1) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/messageAlign") |
| [bottomMarginAdj](#bottommarginadj-1) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/bottomMarginAdj") |
| [rightAngles](#rightangles-1) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/rightAngles") |
| [taskFontSize](#taskfontsize-1) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskFontSize") |
| [taskFontFamily](#taskfontfamily-1) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskFontFamily") |
| [taskMargin](#taskmargin-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskMargin") |
| [activationWidth](#activationwidth-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/activationWidth") |
| [textPlacement](#textplacement-1) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-textplacement.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/textPlacement") |
| [actorColours](#actorcolours-1) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-actorcolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/actorColours") |
| [sectionFills](#sectionfills-1) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-sectionfills.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/sectionFills") |
| [sectionColours](#sectioncolours-1) | `array` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-sectioncolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/sectionColours") |
| [disableMulticolor](#disablemulticolor) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-disablemulticolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/disableMulticolor") |

### diagramMarginX

Margin to the right and left of the c4 diagram, must be a positive value.

`diagramMarginX`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/diagramMarginX")

#### diagramMarginX Type

`integer`

#### diagramMarginX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginX Default Value

The default value is:

```json
50
```

### diagramMarginY

Margin to the over and under the c4 diagram, must be a positive value.

`diagramMarginY`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/diagramMarginY")

#### diagramMarginY Type

`integer`

#### diagramMarginY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginY Default Value

The default value is:

```json
10
```

### leftMargin

Margin between actors

`leftMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-leftmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/leftMargin")

#### leftMargin Type

`integer`

#### leftMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### leftMargin Default Value

The default value is:

```json
150
```

### width

Width of actor boxes

`width`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/width")

#### width Type

`integer`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### width Default Value

The default value is:

```json
150
```

### height

Height of actor boxes

`height`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/height")

#### height Type

`integer`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### height Default Value

The default value is:

```json
50
```

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/padding")

#### padding Type

`number`

### boxMargin

Margin around loop boxes

`boxMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/boxMargin")

#### boxMargin Type

`integer`

#### boxMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxMargin Default Value

The default value is:

```json
10
```

### boxTextMargin

Margin around the text in loop/alt/opt boxes

`boxTextMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/boxTextMargin")

#### boxTextMargin Type

`integer`

#### boxTextMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxTextMargin Default Value

The default value is:

```json
5
```

### noteMargin

Margin around notes

`noteMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/noteMargin")

#### noteMargin Type

`integer`

#### noteMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### noteMargin Default Value

The default value is:

```json
10
```

### messageMargin

Space between messages.

`messageMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/messageMargin")

#### messageMargin Type

`integer`

#### messageMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### messageMargin Default Value

The default value is:

```json
35
```

### messageAlign

Multiline message alignment

`messageAlign`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/messageAlign")

#### messageAlign Type

`string`

#### messageAlign Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` |  |
| `"center"` |  |
| `"right"` |  |

#### messageAlign Default Value

The default value is:

```json
"center"
```

### bottomMarginAdj

Prolongs the edge of the diagram downwards.

Depending on css styling this might need adjustment.

`bottomMarginAdj`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/bottomMarginAdj")

#### bottomMarginAdj Type

`integer`

#### bottomMarginAdj Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### bottomMarginAdj Default Value

The default value is:

```json
1
```

### rightAngles

Curved Arrows become Right Angles

This will display arrows that start and begin at the same node as right angles, rather than as curves.

`rightAngles`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/rightAngles")

#### rightAngles Type

`boolean`

#### rightAngles Default Value

The default value is:

```json
false
```

### taskFontSize

`taskFontSize`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskFontSize")

#### taskFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontsize.html))

#### taskFontSize Default Value

The default value is:

```json
14
```

### taskFontFamily

`taskFontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskFontFamily")

#### taskFontFamily Type

`string`

#### taskFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### taskMargin

`taskMargin`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-taskmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/taskMargin")

#### taskMargin Type

`number`

#### taskMargin Default Value

The default value is:

```json
50
```

### activationWidth

Width of activation box

`activationWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/activationWidth")

#### activationWidth Type

`number`

#### activationWidth Default Value

The default value is:

```json
10
```

### textPlacement

text placement as: tspan | fo | old only text as before

`textPlacement`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-textplacement.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/textPlacement")

#### textPlacement Type

`string`

#### textPlacement Default Value

The default value is:

```json
"fo"
```

### actorColours

`actorColours`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-actorcolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/actorColours")

#### actorColours Type

`string[]`

#### actorColours Default Value

The default value is:

```json
["#8FBC8F", "#7CFC00", "#00FFFF", "#20B2AA", "#B0E0E6", "#FFFFE0"]
```

### sectionFills

`sectionFills`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-sectionfills.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/sectionFills")

#### sectionFills Type

`string[]`

#### sectionFills Default Value

The default value is:

```json
["#191970", "#8B008B", "#4B0082", "#2F4F4F", "#800000", "#8B4513", "#00008B"]
```

### sectionColours

`sectionColours`

- is optional
- Type: `string[]`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-sectioncolours.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/sectionColours")

#### sectionColours Type

`string[]`

#### sectionColours Default Value

The default value is:

```json
["#fff"]
```

### disableMulticolor

`disableMulticolor`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-timeline-diagram-config-properties-disablemulticolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TimelineDiagramConfig/properties/disableMulticolor")

#### disableMulticolor Type

`boolean`

#### disableMulticolor Default Value

The default value is:

```json
false
```

## Definitions group GanttDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin-4) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/titleTopMargin") |
| [barHeight](#barheight) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-barheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/barHeight") |
| [barGap](#bargap) | `integer` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-bargap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/barGap") |
| [topPadding](#toppadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-toppadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/topPadding") |
| [rightPadding](#rightpadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-rightpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/rightPadding") |
| [leftPadding](#leftpadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-leftpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/leftPadding") |
| [gridLineStartPadding](#gridlinestartpadding) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-gridlinestartpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/gridLineStartPadding") |
| [fontSize](#fontsize-5) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/fontSize") |
| [sectionFontSize](#sectionfontsize) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-sectionfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/sectionFontSize") |
| [numberSectionStyles](#numbersectionstyles) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-numbersectionstyles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/numberSectionStyles") |
| [axisFormat](#axisformat) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-axisformat.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/axisFormat") |
| [tickInterval](#tickinterval) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-tickinterval.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/tickInterval") |
| [topAxis](#topaxis) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-topaxis.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/topAxis") |
| [displayMode](#displaymode) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-displaymode.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/displayMode") |
| [weekday](#weekday) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-weekday.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/weekday") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### barHeight

The height of the bars in the graph

`barHeight`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-barheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/barHeight")

#### barHeight Type

`integer`

#### barHeight Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### barHeight Default Value

The default value is:

```json
20
```

### barGap

The margin between the different activities in the gantt diagram

`barGap`

- is optional
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-bargap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/barGap")

#### barGap Type

`integer`

#### barGap Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### barGap Default Value

The default value is:

```json
4
```

### topPadding

Margin between title and gantt diagram and between axis and gantt diagram.

`topPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-toppadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/topPadding")

#### topPadding Type

`integer`

#### topPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### topPadding Default Value

The default value is:

```json
50
```

### rightPadding

The space allocated for the section name to the right of the activities

`rightPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-rightpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/rightPadding")

#### rightPadding Type

`integer`

#### rightPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### rightPadding Default Value

The default value is:

```json
75
```

### leftPadding

The space allocated for the section name to the left of the activities

`leftPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-leftpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/leftPadding")

#### leftPadding Type

`integer`

#### leftPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### leftPadding Default Value

The default value is:

```json
75
```

### gridLineStartPadding

Vertical starting position of the grid lines

`gridLineStartPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-gridlinestartpadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/gridLineStartPadding")

#### gridLineStartPadding Type

`integer`

#### gridLineStartPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### gridLineStartPadding Default Value

The default value is:

```json
35
```

### fontSize

Font size

`fontSize`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-fontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/fontSize")

#### fontSize Type

`integer`

#### fontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### fontSize Default Value

The default value is:

```json
11
```

### sectionFontSize

Font size for sections

`sectionFontSize`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-sectionfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/sectionFontSize")
- tsType: `string | number`

#### sectionFontSize Type

`integer`

#### sectionFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### sectionFontSize Default Value

The default value is:

```json
11
```

### numberSectionStyles

The number of alternating section styles

`numberSectionStyles`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-numbersectionstyles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/numberSectionStyles")

#### numberSectionStyles Type

`integer`

#### numberSectionStyles Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### numberSectionStyles Default Value

The default value is:

```json
4
```

### axisFormat

Date/time format of the axis

This might need adjustment to match your locale and preferences.

`axisFormat`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-axisformat.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/axisFormat")

#### axisFormat Type

`string`

#### axisFormat Default Value

The default value is:

```json
"%Y-%m-%d"
```

### tickInterval

axis ticks

Pattern is:

```javascript
/^([1-9][0-9]*)(millisecond|second|minute|hour|day|week|month)$/;
```

`tickInterval`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-tickinterval.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/tickInterval")

#### tickInterval Type

`string`

#### tickInterval Constraints

**pattern**: the string must match the following regular expression:

```javascript
/^([1-9][0-9]*)(millisecond|second|minute|hour|day|week|month)$/
```

[try pattern](https://regexr.com/?expression=%5E\(%5B1-9%5D%5B0-9%5D*\)\(millisecond%7Csecond%7Cminute%7Chour%7Cday%7Cweek%7Cmonth\)%24 "try regular expression with regexr.com")

### topAxis

When this flag is set, date labels will be added to the top of the chart

`topAxis`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-topaxis.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/topAxis")

#### topAxis Type

`boolean`

#### topAxis Default Value

The default value is:

```json
false
```

### displayMode

Controls the display mode.

`displayMode`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-displaymode.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/displayMode")

#### displayMode Type

`string`

#### displayMode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `""` |  |
| `"compact"` | Enables displaying multiple tasks on the same row. |

#### displayMode Default Value

The default value is:

```json
""
```

### weekday

On which day a week-based interval should start

`weekday`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config-properties-weekday.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/GanttDiagramConfig/properties/weekday")

#### weekday Type

`string`

#### weekday Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"monday"` |  |
| `"tuesday"` |  |
| `"wednesday"` |  |
| `"thursday"` |  |
| `"friday"` |  |
| `"saturday"` |  |
| `"sunday"` |  |

#### weekday Default Value

The default value is:

```json
"sunday"
```

## Definitions group SequenceDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [arrowMarkerAbsolute](#arrowmarkerabsolute-4) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/arrowMarkerAbsolute") |
| [hideUnusedParticipants](#hideunusedparticipants) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-hideunusedparticipants.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/hideUnusedParticipants") |
| [activationWidth](#activationwidth-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/activationWidth") |
| [diagramMarginX](#diagrammarginx-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/diagramMarginX") |
| [diagramMarginY](#diagrammarginy-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/diagramMarginY") |
| [actorMargin](#actormargin) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actormargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorMargin") |
| [width](#width-5) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/width") |
| [height](#height-5) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/height") |
| [boxMargin](#boxmargin-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/boxMargin") |
| [boxTextMargin](#boxtextmargin-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/boxTextMargin") |
| [noteMargin](#notemargin-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteMargin") |
| [messageMargin](#messagemargin-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageMargin") |
| [messageAlign](#messagealign-2) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageAlign") |
| [mirrorActors](#mirroractors) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-mirroractors.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/mirrorActors") |
| [forceMenus](#forcemenus) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-forcemenus.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/forceMenus") |
| [bottomMarginAdj](#bottommarginadj-2) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/bottomMarginAdj") |
| [rightAngles](#rightangles-2) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/rightAngles") |
| [showSequenceNumbers](#showsequencenumbers) | `boolean` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-showsequencenumbers.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/showSequenceNumbers") |
| [actorFontSize](#actorfontsize) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontSize") |
| [actorFontFamily](#actorfontfamily) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontFamily") |
| [actorFontWeight](#actorfontweight) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontWeight") |
| [noteFontSize](#notefontsize) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontSize") |
| [noteFontFamily](#notefontfamily) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontFamily") |
| [noteFontWeight](#notefontweight) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontWeight") |
| [noteAlign](#notealign) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteAlign") |
| [messageFontSize](#messagefontsize-1) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontSize") |
| [messageFontFamily](#messagefontfamily-1) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontFamily") |
| [messageFontWeight](#messagefontweight-1) | Multiple | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontWeight") |
| [wrap](#wrap-2) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/wrap") |
| [wrapPadding](#wrappadding-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrappadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/wrapPadding") |
| [labelBoxWidth](#labelboxwidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-labelboxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/labelBoxWidth") |
| [labelBoxHeight](#labelboxheight) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-labelboxheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/labelBoxHeight") |
| [messageFont](#messagefont-1) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFont") |
| [noteFont](#notefont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-1.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFont") |
| [actorFont](#actorfont) | Not specified | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-2.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFont") |

### arrowMarkerAbsolute

`arrowMarkerAbsolute`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/arrowMarkerAbsolute")

#### arrowMarkerAbsolute Type

`boolean`

### hideUnusedParticipants

`hideUnusedParticipants`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-hideunusedparticipants.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/hideUnusedParticipants")

#### hideUnusedParticipants Type

`boolean`

#### hideUnusedParticipants Default Value

The default value is:

```json
false
```

### activationWidth

Width of the activation rect

`activationWidth`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-activationwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/activationWidth")

#### activationWidth Type

`integer`

#### activationWidth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### activationWidth Default Value

The default value is:

```json
10
```

### diagramMarginX

Margin to the right and left of the sequence diagram

`diagramMarginX`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-diagrammarginx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/diagramMarginX")

#### diagramMarginX Type

`integer`

#### diagramMarginX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginX Default Value

The default value is:

```json
50
```

### diagramMarginY

Margin to the over and under the sequence diagram

`diagramMarginY`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-diagrammarginy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/diagramMarginY")

#### diagramMarginY Type

`integer`

#### diagramMarginY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramMarginY Default Value

The default value is:

```json
10
```

### actorMargin

Margin between actors

`actorMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actormargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorMargin")

#### actorMargin Type

`integer`

#### actorMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### actorMargin Default Value

The default value is:

```json
50
```

### width

Width of actor boxes

`width`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/width")

#### width Type

`integer`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### width Default Value

The default value is:

```json
150
```

### height

Height of actor boxes

`height`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/height")

#### height Type

`integer`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### height Default Value

The default value is:

```json
50
```

### boxMargin

Margin around loop boxes

`boxMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/boxMargin")

#### boxMargin Type

`integer`

#### boxMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxMargin Default Value

The default value is:

```json
10
```

### boxTextMargin

Margin around the text in loop/alt/opt boxes

`boxTextMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-boxtextmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/boxTextMargin")

#### boxTextMargin Type

`integer`

#### boxTextMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### boxTextMargin Default Value

The default value is:

```json
5
```

### noteMargin

Margin around notes

`noteMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-notemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteMargin")

#### noteMargin Type

`integer`

#### noteMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### noteMargin Default Value

The default value is:

```json
10
```

### messageMargin

Space between messages.

`messageMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageMargin")

#### messageMargin Type

`integer`

#### messageMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### messageMargin Default Value

The default value is:

```json
35
```

### messageAlign

Multiline message alignment

`messageAlign`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-messagealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageAlign")

#### messageAlign Type

`string`

#### messageAlign Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` |  |
| `"center"` |  |
| `"right"` |  |

#### messageAlign Default Value

The default value is:

```json
"center"
```

### mirrorActors

Mirror actors under diagram

`mirrorActors`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-mirroractors.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/mirrorActors")

#### mirrorActors Type

`boolean`

#### mirrorActors Default Value

The default value is:

```json
true
```

### forceMenus

forces actor popup menus to always be visible (to support E2E testing).

`forceMenus`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-forcemenus.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/forceMenus")

#### forceMenus Type

`boolean`

#### forceMenus Default Value

The default value is:

```json
false
```

### bottomMarginAdj

Prolongs the edge of the diagram downwards.

Depending on css styling this might need adjustment.

`bottomMarginAdj`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-bottommarginadj.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/bottomMarginAdj")

#### bottomMarginAdj Type

`integer`

#### bottomMarginAdj Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### bottomMarginAdj Default Value

The default value is:

```json
1
```

### rightAngles

Curved Arrows become Right Angles

This will display arrows that start and begin at the same node as right angles, rather than as curves.

`rightAngles`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-journey-diagram-config-properties-rightangles.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/rightAngles")

#### rightAngles Type

`boolean`

#### rightAngles Default Value

The default value is:

```json
false
```

### showSequenceNumbers

This will show the node numbers

`showSequenceNumbers`

- is required
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-showsequencenumbers.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/showSequenceNumbers")

#### showSequenceNumbers Type

`boolean`

#### showSequenceNumbers Default Value

The default value is:

```json
false
```

### actorFontSize

This sets the font size of the actor's description

`actorFontSize`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontSize")

#### actorFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontsize.html))

#### actorFontSize Default Value

The default value is:

```json
14
```

### actorFontFamily

This sets the font family of the actor's description

`actorFontFamily`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontFamily")

#### actorFontFamily Type

`string`

#### actorFontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### actorFontWeight

This sets the font weight of the actor's description

`actorFontWeight`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFontWeight")

#### actorFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-actorfontweight.html))

#### actorFontWeight Default Value

The default value is:

```json
400
```

### noteFontSize

This sets the font size of actor-attached notes

`noteFontSize`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontSize")

#### noteFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontsize.html))

#### noteFontSize Default Value

The default value is:

```json
14
```

### noteFontFamily

This sets the font family of actor-attached notes

`noteFontFamily`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontFamily")

#### noteFontFamily Type

`string`

#### noteFontFamily Default Value

The default value is:

```json
"\"trebuchet ms\", verdana, arial, sans-serif"
```

### noteFontWeight

This sets the font weight of actor-attached notes

`noteFontWeight`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFontWeight")

#### noteFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notefontweight.html))

#### noteFontWeight Default Value

The default value is:

```json
400
```

### noteAlign

This sets the text alignment of actor-attached notes

`noteAlign`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-notealign.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteAlign")

#### noteAlign Type

`string`

#### noteAlign Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` |  |
| `"center"` |  |
| `"right"` |  |

#### noteAlign Default Value

The default value is:

```json
"center"
```

### messageFontSize

This sets the font size of actor messages

`messageFontSize`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontsize.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontSize")

#### messageFontSize Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontsize.html))

#### messageFontSize Default Value

The default value is:

```json
16
```

### messageFontFamily

This sets the font family of actor messages

`messageFontFamily`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontFamily")

#### messageFontFamily Type

`string`

#### messageFontFamily Default Value

The default value is:

```json
"\"trebuchet ms\", verdana, arial, sans-serif"
```

### messageFontWeight

This sets the font weight of actor messages

`messageFontWeight`

- is required
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFontWeight")

#### messageFontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-messagefontweight.html))

#### messageFontWeight Default Value

The default value is:

```json
400
```

### wrap

This sets the auto-wrap state for the diagram

`wrap`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-wrap.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/wrap")

#### wrap Type

`boolean`

#### wrap Default Value

The default value is:

```json
false
```

### wrapPadding

This sets the auto-wrap padding for the diagram (sides only)

`wrapPadding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-c4-diagram-config-properties-wrappadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/wrapPadding")

#### wrapPadding Type

`number`

#### wrapPadding Default Value

The default value is:

```json
10
```

### labelBoxWidth

This sets the width of the loop-box (loop, alt, opt, par)

`labelBoxWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-labelboxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/labelBoxWidth")

#### labelBoxWidth Type

`number`

#### labelBoxWidth Default Value

The default value is:

```json
50
```

### labelBoxHeight

This sets the height of the loop-box (loop, alt, opt, par)

`labelBoxHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-labelboxheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/labelBoxHeight")

#### labelBoxHeight Type

`number`

#### labelBoxHeight Default Value

The default value is:

```json
20
```

### messageFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`messageFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/messageFont")
- tsType: `() => Partial<FontConfig>`

#### messageFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator.html))

### noteFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`noteFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-1.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-1.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/noteFont")
- tsType: `() => Partial<FontConfig>`

#### noteFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-1.html))

### actorFont

javascript function that returns a `FontConfig`.

By default, these return the appropriate `*FontSize`, `*FontFamily`, `*FontWeight` values.

For example, the font calculator called `boundaryFont` might be defined as:

```javascript
boundaryFont: function () {
  return {
    fontFamily: this.boundaryFontFamily,
    fontSize: this.boundaryFontSize,
    fontWeight: this.boundaryFontWeight,
  };
}
```

`actorFont`

- is optional
- Type: unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-2.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-2.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SequenceDiagramConfig/properties/actorFont")
- tsType: `() => Partial<FontConfig>`

#### actorFont Type

unknown ([Font Calculator](https://mermaid.js.org/config/schema-docs/config-defs-sequence-diagram-config-properties-font-calculator-2.html))

## Definitions group FlowchartDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [titleTopMargin](#titletopmargin-5) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/titleTopMargin") |
| [subGraphTitleMargin](#subgraphtitlemargin) | `object` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-subgraphtitlemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/subGraphTitleMargin") |
| [arrowMarkerAbsolute](#arrowmarkerabsolute-5) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/arrowMarkerAbsolute") |
| [diagramPadding](#diagrampadding-4) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/diagramPadding") |
| [htmlLabels](#htmllabels-2) | `boolean` | Optional | can be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/htmlLabels") |
| [nodeSpacing](#nodespacing-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/nodeSpacing") |
| [rankSpacing](#rankspacing-3) | `integer` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/rankSpacing") |
| [curve](#curve) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-curve.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/curve") |
| [padding](#padding-6) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/padding") |
| [defaultRenderer](#defaultrenderer-2) | `string` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/defaultRenderer") |
| [wrappingWidth](#wrappingwidth) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-wrappingwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/wrappingWidth") |
| [inheritDir](#inheritdir) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-inheritdir.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/inheritDir") |

### titleTopMargin

Margin top for the text over the diagram

`titleTopMargin`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-git-graph-diagram-config-properties-titletopmargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/titleTopMargin")

#### titleTopMargin Type

`integer`

#### titleTopMargin Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### titleTopMargin Default Value

The default value is:

```json
25
```

### subGraphTitleMargin

Defines a top/bottom margin for subgraph titles

`subGraphTitleMargin`

- is required
- Type: `object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-subgraphtitlemargin.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-subgraphtitlemargin.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/subGraphTitleMargin")

#### subGraphTitleMargin Type

`object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-subgraphtitlemargin.html))

#### subGraphTitleMargin Default Value

The default value is:

```json
{
  "top": 0,
  "bottom": 0
}
```

### arrowMarkerAbsolute

`arrowMarkerAbsolute`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-arrowmarkerabsolute.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/arrowMarkerAbsolute")

#### arrowMarkerAbsolute Type

`boolean`

### diagramPadding

The amount of padding around the diagram as a whole so that embedded diagrams have margins, expressed in pixels.

`diagramPadding`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-er-diagram-config-properties-diagrampadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/diagramPadding")

#### diagramPadding Type

`integer`

#### diagramPadding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### diagramPadding Default Value

The default value is:

```json
20
```

### htmlLabels

**DEPRECATED: Use global `htmlLabels` instead.**

Flag for setting whether or not a html tag should be used for rendering labels on nodes and edges. This property is deprecated. Please use the global `htmlLabels` configuration instead.

`htmlLabels`

- is optional
- Type: `boolean`
- can be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-htmllabels.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/htmlLabels")

#### htmlLabels Type

`boolean`

#### htmlLabels Default Value

The default value is:

```json
null
```

### nodeSpacing

Defines the spacing between nodes on the same level

Pertains to horizontal spacing for TB (top to bottom) or BT (bottom to top) graphs, and the vertical spacing for LR as well as RL graphs.

`nodeSpacing`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-nodespacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/nodeSpacing")

#### nodeSpacing Type

`integer`

#### nodeSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### nodeSpacing Default Value

The default value is:

```json
50
```

### rankSpacing

Defines the spacing between nodes on different levels

Pertains to horizontal spacing for TB (top to bottom) or BT (bottom to top) graphs, and the vertical spacing for LR as well as RL graphs.

`rankSpacing`

- is required
- Type: `integer`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-rankspacing.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/rankSpacing")

#### rankSpacing Type

`integer`

#### rankSpacing Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### rankSpacing Default Value

The default value is:

```json
50
```

### curve

Defines how mermaid renders curves for flowcharts.

`curve`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-curve.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/curve")

#### curve Type

`string`

#### curve Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"basis"` |  |
| `"bumpX"` |  |
| `"bumpY"` |  |
| `"cardinal"` |  |
| `"catmullRom"` |  |
| `"linear"` |  |
| `"monotoneX"` |  |
| `"monotoneY"` |  |
| `"natural"` |  |
| `"step"` |  |
| `"stepAfter"` |  |
| `"stepBefore"` |  |
| `"rounded"` |  |

#### curve Default Value

The default value is:

```json
"basis"
```

### padding

Represents the padding between the labels and the shape

**Only used in new experimental rendering.**

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
15
```

### defaultRenderer

Decides which rendering engine that is to be used for the rendering.

`defaultRenderer`

- is required
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-state-diagram-config-properties-defaultrenderer.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/defaultRenderer")

#### defaultRenderer Type

`string`

#### defaultRenderer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"dagre-d3"` | The \[dagre-d3-es\](<https://www.npmjs.com/package/dagre-d3-es>) library. |
| `"dagre-wrapper"` | wrapper for dagre implemented in mermaid |
| `"elk"` | Layout using \[elkjs\](<https://github.com/kieler/elkjs>) |

#### defaultRenderer Default Value

The default value is:

```json
"dagre-wrapper"
```

### wrappingWidth

Width of nodes where text is wrapped.

When using markdown strings the text is wrapped automatically, this value sets the max width of a text before it continues on a new line.

`wrappingWidth`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-wrappingwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/wrappingWidth")

#### wrappingWidth Type

`number`

#### wrappingWidth Default Value

The default value is:

```json
200
```

### inheritDir

If true, subgraphs without explicit direction will inherit the global graph direction (e.g., LR, TB, RL, BT). Defaults to false to preserve legacy layout behavior.

`inheritDir`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config-properties-inheritdir.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FlowchartDiagramConfig/properties/inheritDir")

#### inheritDir Type

`boolean`

#### inheritDir Default Value

The default value is:

```json
false
```

## Definitions group SankeyLinkColor

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyLinkColor" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |

## Definitions group SankeyLabelStyle

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyLabelStyle" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |

## Definitions group SankeyNodeAlignment

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyNodeAlignment" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |

## Definitions group SankeyDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-6) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/width") |
| [height](#height-6) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/height") |
| [linkColor](#linkcolor) | Merged | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/linkColor") |
| [nodeAlignment](#nodealignment) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodealignment.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeAlignment") |
| [useMaxWidth](#usemaxwidth-2) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/useMaxWidth") |
| [showValues](#showvalues) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-showvalues.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/showValues") |
| [prefix](#prefix) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-prefix.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/prefix") |
| [suffix](#suffix) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-suffix.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/suffix") |
| [nodeWidth](#nodewidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeWidth") |
| [nodePadding](#nodepadding) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodePadding") |
| [labelStyle](#labelstyle) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-labelstyle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/labelStyle") |
| [nodeColors](#nodecolors) | `object` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodecolors.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeColors") |

### width

`width`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/width")

#### width Type

`number`

#### width Default Value

The default value is:

```json
600
```

### height

`height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/height")

#### height Type

`number`

#### height Default Value

The default value is:

```json
400
```

### linkColor

The color of the links in the sankey diagram.

`linkColor`

- is optional
- Type: merged type ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/linkColor")

#### linkColor Type

merged type ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor.html))

any of

- [Untitled string in Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor-anyof-0.html "check type definition")
- [Untitled string in Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-linkcolor-anyof-1.html "check type definition")

#### linkColor Default Value

The default value is:

```json
"gradient"
```

### nodeAlignment

Controls the alignment of the Sankey diagrams.

See <https://github.com/d3/d3-sankey#alignments>.

`nodeAlignment`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodealignment.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeAlignment")

#### nodeAlignment Type

`string`

#### nodeAlignment Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"left"` | Align all inputs to the left. |
| `"right"` | Align all outputs to the right. |
| `"center"` | Like \`left\`, except that nodes without any incoming links are moved as right as possible. |
| `"justify"` | Like \`left\`, except that nodes without any outgoing links are moved to the far right. |

#### nodeAlignment Default Value

The default value is:

```json
"justify"
```

### useMaxWidth

`useMaxWidth`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-usemaxwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/useMaxWidth")

#### useMaxWidth Type

`boolean`

#### useMaxWidth Default Value

The default value is:

```json
false
```

### showValues

Toggle to display or hide values along with title.

`showValues`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-showvalues.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/showValues")

#### showValues Type

`boolean`

#### showValues Default Value

The default value is:

```json
true
```

### prefix

The prefix to use for values

`prefix`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-prefix.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/prefix")

#### prefix Type

`string`

#### prefix Default Value

The default value is:

```json
""
```

### suffix

The suffix to use for values

`suffix`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-suffix.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/suffix")

#### suffix Type

`string`

#### suffix Default Value

The default value is:

```json
""
```

### nodeWidth

The width of the nodes in the sankey diagram.

`nodeWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodewidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeWidth")

#### nodeWidth Type

`number`

#### nodeWidth Default Value

The default value is:

```json
10
```

### nodePadding

The padding between nodes in the sankey diagram.

`nodePadding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodepadding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodePadding")

#### nodePadding Type

`number`

#### nodePadding Default Value

The default value is:

```json
12
```

### labelStyle

The style of labels in the sankey diagram.

`labelStyle`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-labelstyle.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/labelStyle")

#### labelStyle Type

`string`

#### labelStyle Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| --- | --- |
| `"legacy"` | Plain text labels (original style). |
| `"outlined"` | Labels with a white outline for better readability against colored backgrounds. |

#### labelStyle Default Value

The default value is:

```json
"legacy"
```

### nodeColors

A mapping of node IDs to their colors. Nodes not specified will use the default color scheme.

`nodeColors`

- is optional
- Type: `object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodecolors.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodecolors.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/SankeyDiagramConfig/properties/nodeColors")

#### nodeColors Type

`object` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-sankey-diagram-config-properties-nodecolors.html))

## Definitions group PacketDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [rowHeight](#rowheight) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-rowheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/rowHeight") |
| [bitWidth](#bitwidth) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-bitwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/bitWidth") |
| [bitsPerRow](#bitsperrow) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-bitsperrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/bitsPerRow") |
| [showBits](#showbits) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-showbits.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/showBits") |
| [paddingX](#paddingx) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-paddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/paddingX") |
| [paddingY](#paddingy) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-paddingy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/paddingY") |

### rowHeight

The height of each row in the packet diagram.

`rowHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-rowheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/rowHeight")

#### rowHeight Type

`number`

#### rowHeight Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### rowHeight Default Value

The default value is:

```json
32
```

### bitWidth

The width of each bit in the packet diagram.

`bitWidth`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-bitwidth.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/bitWidth")

#### bitWidth Type

`number`

#### bitWidth Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### bitWidth Default Value

The default value is:

```json
32
```

### bitsPerRow

The number of bits to display per row.

`bitsPerRow`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-bitsperrow.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/bitsPerRow")

#### bitsPerRow Type

`number`

#### bitsPerRow Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### bitsPerRow Default Value

The default value is:

```json
32
```

### showBits

Toggle to display or hide bit numbers.

`showBits`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-showbits.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/showBits")

#### showBits Type

`boolean`

#### showBits Default Value

The default value is:

```json
true
```

### paddingX

The horizontal padding between the blocks in a row.

`paddingX`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-paddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/paddingX")

#### paddingX Type

`number`

#### paddingX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### paddingX Default Value

The default value is:

```json
5
```

### paddingY

The vertical padding between the rows.

`paddingY`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-packet-diagram-config-properties-paddingy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/PacketDiagramConfig/properties/paddingY")

#### paddingY Type

`number`

#### paddingY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### paddingY Default Value

The default value is:

```json
5
```

## Definitions group BlockDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/BlockDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [padding](#padding-7) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BlockDiagramConfig/properties/padding") |

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-block-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/BlockDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### padding Default Value

The default value is:

```json
8
```

## Definitions group EventModelingDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/EventModelingDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [padding](#padding-8) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/EventModelingDiagramConfig/properties/padding") |
| [rowHeight](#rowheight-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config-properties-rowheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/EventModelingDiagramConfig/properties/rowHeight") |

### padding

The padding around the Event Modeling diagram.

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/EventModelingDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Default Value

The default value is:

```json
30
```

### rowHeight

The height of each row in the Event Modeling diagram.

`rowHeight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-event-modeling-diagram-config-properties-rowheight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/EventModelingDiagramConfig/properties/rowHeight")

#### rowHeight Type

`number`

#### rowHeight Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### rowHeight Default Value

The default value is:

```json
32
```

## Definitions group TreeViewDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [rowIndent](#rowindent) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-rowindent.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/rowIndent") |
| [paddingX](#paddingx-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-paddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/paddingX") |
| [paddingY](#paddingy-1) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-paddingy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/paddingY") |
| [lineThickness](#linethickness) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-linethickness.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/lineThickness") |

### rowIndent

Horizontal distance between rows differing by one level

`rowIndent`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-rowindent.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/rowIndent")

#### rowIndent Type

`number`

#### rowIndent Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### rowIndent Default Value

The default value is:

```json
10
```

### paddingX

Horizontal padding of label

`paddingX`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-paddingx.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/paddingX")

#### paddingX Type

`number`

#### paddingX Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### paddingX Default Value

The default value is:

```json
5
```

### paddingY

Vertical padding of label

`paddingY`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-paddingy.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/paddingY")

#### paddingY Type

`number`

#### paddingY Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### paddingY Default Value

The default value is:

```json
5
```

### lineThickness

Thickness of the line

`lineThickness`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-treeview-diagram-config-properties-linethickness.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/TreeViewDiagramConfig/properties/lineThickness")

#### lineThickness Type

`number`

#### lineThickness Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### lineThickness Default Value

The default value is:

```json
1
```

## Definitions group RadarDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-7) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/width") |
| [height](#height-7) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/height") |
| [marginTop](#margintop) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-margintop.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginTop") |
| [marginRight](#marginright) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginright.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginRight") |
| [marginBottom](#marginbottom) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginbottom.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginBottom") |
| [marginLeft](#marginleft) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginleft.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginLeft") |
| [axisScaleFactor](#axisscalefactor) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-axisscalefactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/axisScaleFactor") |
| [axisLabelFactor](#axislabelfactor) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-axislabelfactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/axisLabelFactor") |
| [curveTension](#curvetension) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-curvetension.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/curveTension") |

### width

The size of the radar diagram.

`width`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/width")

#### width Type

`number`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### width Default Value

The default value is:

```json
600
```

### height

The size of the radar diagram.

`height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/height")

#### height Type

`number`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### height Default Value

The default value is:

```json
600
```

### marginTop

The margin from the top of the radar diagram.

`marginTop`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-margintop.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginTop")

#### marginTop Type

`number`

#### marginTop Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### marginTop Default Value

The default value is:

```json
50
```

### marginRight

The margin from the right of the radar diagram.

`marginRight`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginright.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginRight")

#### marginRight Type

`number`

#### marginRight Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### marginRight Default Value

The default value is:

```json
50
```

### marginBottom

The margin from the bottom of the radar diagram.

`marginBottom`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginbottom.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginBottom")

#### marginBottom Type

`number`

#### marginBottom Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### marginBottom Default Value

The default value is:

```json
50
```

### marginLeft

The margin from the left of the radar diagram.

`marginLeft`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-marginleft.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/marginLeft")

#### marginLeft Type

`number`

#### marginLeft Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### marginLeft Default Value

The default value is:

```json
50
```

### axisScaleFactor

The scale factor of the axis.

`axisScaleFactor`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-axisscalefactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/axisScaleFactor")

#### axisScaleFactor Type

`number`

#### axisScaleFactor Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### axisScaleFactor Default Value

The default value is:

```json
1
```

### axisLabelFactor

The scale factor of the axis label.

`axisLabelFactor`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-axislabelfactor.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/axisLabelFactor")

#### axisLabelFactor Type

`number`

#### axisLabelFactor Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### axisLabelFactor Default Value

The default value is:

```json
1.05
```

### curveTension

The tension factor for the Catmull-Rom spline conversion to cubic Bézier curves.

`curveTension`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-radar-diagram-config-properties-curvetension.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/RadarDiagramConfig/properties/curveTension")

#### curveTension Type

`number`

#### curveTension Constraints

**maximum**: the value of this number must smaller than or equal to: `1`

**minimum**: the value of this number must greater than or equal to: `0`

#### curveTension Default Value

The default value is:

```json
0.17
```

## Definitions group VennDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-8) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/width") |
| [height](#height-8) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/height") |
| [padding](#padding-9) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/padding") |
| [useDebugLayout](#usedebuglayout) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-usedebuglayout.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/useDebugLayout") |

### width

The width of the Venn diagram.

`width`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/width")

#### width Type

`number`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### width Default Value

The default value is:

```json
800
```

### height

The height of the Venn diagram.

`height`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/height")

#### height Type

`number`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### height Default Value

The default value is:

```json
450
```

### padding

`padding`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### padding Default Value

The default value is:

```json
8
```

### useDebugLayout

`useDebugLayout`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-venn-diagram-config-properties-usedebuglayout.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/VennDiagramConfig/properties/useDebugLayout")

#### useDebugLayout Type

`boolean`

#### useDebugLayout Default Value

The default value is:

```json
false
```

## Definitions group WardleyDiagramConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [width](#width-9) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/width") |
| [height](#height-9) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/height") |
| [padding](#padding-10) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/padding") |
| [nodeRadius](#noderadius) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-noderadius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/nodeRadius") |
| [nodeLabelOffset](#nodelabeloffset) | `number` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-nodelabeloffset.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/nodeLabelOffset") |
| [axisFontSize](#axisfontsize) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-axisfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/axisFontSize") |
| [labelFontSize](#labelfontsize-1) | `number` | Required | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-labelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/labelFontSize") |
| [showGrid](#showgrid) | `boolean` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-showgrid.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/showGrid") |

### width

The width of the Wardley diagram canvas.

`width`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-width.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/width")

#### width Type

`number`

#### width Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### width Default Value

The default value is:

```json
900
```

### height

The height of the Wardley diagram canvas.

`height`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-height.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/height")

#### height Type

`number`

#### height Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### height Default Value

The default value is:

```json
600
```

### padding

The padding around the Wardley diagram.

`padding`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-padding.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/padding")

#### padding Type

`number`

#### padding Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### padding Default Value

The default value is:

```json
48
```

### nodeRadius

The radius of component nodes.

`nodeRadius`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-noderadius.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/nodeRadius")

#### nodeRadius Type

`number`

#### nodeRadius Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### nodeRadius Default Value

The default value is:

```json
6
```

### nodeLabelOffset

The offset distance for node labels.

`nodeLabelOffset`

- is optional
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-nodelabeloffset.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/nodeLabelOffset")

#### nodeLabelOffset Type

`number`

#### nodeLabelOffset Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### nodeLabelOffset Default Value

The default value is:

```json
8
```

### axisFontSize

The font size for axis labels.

`axisFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-axisfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/axisFontSize")

#### axisFontSize Type

`number`

#### axisFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### axisFontSize Default Value

The default value is:

```json
12
```

### labelFontSize

The font size for component labels.

`labelFontSize`

- is required
- Type: `number`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-labelfontsize.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/labelFontSize")

#### labelFontSize Type

`number`

#### labelFontSize Constraints

**minimum**: the value of this number must greater than or equal to: `0`

#### labelFontSize Default Value

The default value is:

```json
10
```

### showGrid

Whether to display a background grid.

`showGrid`

- is optional
- Type: `boolean`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-wardley-diagram-config-properties-showgrid.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/WardleyDiagramConfig/properties/showGrid")

#### showGrid Type

`boolean`

#### showGrid Default Value

The default value is:

```json
false
```

## Definitions group FontCalculator

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontCalculator" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |

## Definitions group FontConfig

Reference this group by using

```json
{ "$ref": "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig" }
```

| Property | Type | Required | Nullable | Defined by |
| --- | --- | --- | --- | --- |
| [fontSize](#fontsize-6) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-css-font-size.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontSize") |
| [fontFamily](#fontfamily-1) | `string` | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontFamily") |
| [fontWeight](#fontweight) | Multiple | Optional | cannot be null | [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontWeight") |

### fontSize

The font size to use

`fontSize`

- is optional
- Type: any of the following: `string` or `number` ([CSS Font Size](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-css-font-size.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-css-font-size.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontSize")

#### fontSize Type

any of the following: `string` or `number` ([CSS Font Size](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-css-font-size.html))

#### fontSize Default Value

The default value is:

```json
14
```

### fontFamily

The CSS [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) to use.

`fontFamily`

- is optional
- Type: `string`
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontfamily.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontFamily")

#### fontFamily Type

`string`

#### fontFamily Default Value

The default value is:

```json
"\"Open Sans\", sans-serif"
```

### fontWeight

The font weight to use.

`fontWeight`

- is optional
- Type: any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontweight.html))
- cannot be null
- defined in: [Mermaid Config](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontweight.html "https://mermaid.js.org/schemas/config.schema.json#/$defs/FontConfig/properties/fontWeight")

#### fontWeight Type

any of the following: `string` or `number` ([Details](https://mermaid.js.org/config/schema-docs/config-defs-font-config-properties-fontweight.html))

#### fontWeight Default Value

The default value is:

```json
"normal"
```
