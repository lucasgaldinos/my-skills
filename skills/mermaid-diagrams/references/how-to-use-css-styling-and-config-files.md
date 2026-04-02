---
title: using mermaid configuration in markdown files
description:
  - "How to use Mermaid configuration in markdown files. This includes setting themes, looks, and various margin configurations to customize the appearance of the diagrams."
---

# Using Mermaid configuration in markdown files

<diagrams>

<sequence-diagram>

On how to build a sequence diagram, see the [sequence diagram syntax reference](./sequenceDiagram.md).

## Sequence Diagram Configuration and Styling

<configuration>

### How configuration works (3 layers)

Mermaid reads configuration from three sources, applied in this order (last wins):

1. **Built-in defaults** — hardcoded in the library.
2. **Site-level `initialize()` call** — set once in JavaScript for all diagrams on a page/app. Only relevant when you control the HTML.
3. **Per-diagram frontmatter** (v10.5.0+) — a `---` YAML block at the top of the diagram code block. This is the recommended approach for markdown files.

### Frontmatter config (use this in markdown)

The entire config object (except security settings) can be overridden per diagram via YAML frontmatter placed *inside* the ` ```mermaid ` code block:

````markdown
```mermaid
---
config:
  theme: redux-dark
  look: neo
  sequence:
    diagramMarginX: 30
    diagramMarginY: 10
    boxTextMargin: 8
    noteMargin: 12
    messageMargin: 40
    mirrorActors: true
    actorFontSize: 13
    noteFontSize: 13
    messageFontSize: 14
    noteAlign: left
---
sequenceDiagram
    ...
```
````

**Important**: sequence-specific parameters must be nested under the `sequence:` key, not directly under `config:`. This mirrors the `mermaid.sequenceConfig` JS object structure.

### All sequence-specific config parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `diagramMarginX` | 50 | Horizontal outer margin (left + right) |
| `diagramMarginY` | 10 | Vertical outer margin (top + bottom) |
| `leftMargin` | 150 | Margin between actors |
| `width` | 150 | Actor box width |
| `height` | 65 | Actor box height |
| `boxMargin` | 10 | Margin around loop/alt/critical boxes |
| `boxTextMargin` | 5 | Margin around text inside loop/alt/critical boxes |
| `noteMargin` | 10 | Margin around note boxes |
| `messageMargin` | 35 | Space between messages |
| `messageAlign` | `"center"` | Message label alignment: `"left"`, `"center"`, `"right"` |
| `mirrorActors` | false | Whether to repeat actor boxes at the bottom |
| `bottomMarginAdj` | 1 | Extra space at the bottom (useful when CSS clips the diagram) |
| `actorFontSize` | 14 | Font size for actor labels |
| `actorFontFamily` | `"Open Sans", sans-serif` | Font family for actor labels |
| `actorFontWeight` | `"Open Sans", sans-serif` | Font weight for actor labels |
| `noteFontSize` | 14 | Font size inside notes |
| `noteFontFamily` | `"trebuchet ms", verdana, arial` | Font family inside notes |
| `noteFontWeight` | (same as family default) | Font weight inside notes |
| `noteAlign` | `"center"` | Note text alignment: `"left"`, `"center"`, `"right"` |
| `messageFontSize` | 16 | Font size for message labels |
| `messageFontFamily` | `"trebuchet ms", verdana, arial` | Font family for message labels |
| `messageFontWeight` | (same as family default) | Font weight for message labels |

### What `mermaid.sequenceConfig` is and where it belongs

`mermaid.sequenceConfig` is a **JavaScript property** — it belongs in an HTML `<script>` tag on a page that embeds mermaid directly:

```html
<script>
  mermaid.sequenceConfig = {
    diagramMarginX: 50,
    noteMargin: 10,
    messageMargin: 35,
    mirrorActors: true,
  };
</script>
```

This is **not** how you configure diagrams in markdown files. It is a legacy site-level override. **Use frontmatter instead** for any markdown context.

### mermaidCLI

The CLI (`mmdc`) accepts a JSON config file via `--configFile`:

```bash
mmdc -i input.md -o output.svg --configFile config.json
```

The JSON mirrors the YAML frontmatter structure:

```json
{
  "sequence": {
    "diagramMarginX": 30,
    "noteMargin": 12,
    "mirrorActors": true
  }
}
```

This is only needed in build pipelines that render mermaid to static SVG/PNG — not needed for live markdown preview.

### Platform support for frontmatter config

| Context | Frontmatter config supported? | Notes |
|---------|-------------------------------|-------|
| **GitHub** (`.md` files, READMEs, wikis) | ✅ Yes | GitHub uses Mermaid v10.9+; frontmatter fully supported since v10.5.0 |
| **VSCode** (`bierner.markdown-mermaid` extension) | ✅ Yes | Extension bundles Mermaid v11.x; frontmatter is respected |
| **VSCode** (built-in markdown preview, no extension) | ❌ No | No mermaid support at all without the extension |
| **Obsidian** | ⚠️ Partial | Depends on plugin version; `theme` works, some params may be ignored |
| **Static site generators** (Hugo, Jekyll, Docusaurus) | ✅ Yes (usually) | Depends on the mermaid version bundled by the theme/plugin |
| **mermaid.live** | ✅ Yes | Full support |

</configuration>

<styling>

### What CSS styling controls

CSS targets the rendered SVG elements that mermaid injects into the DOM. The classes are defined in `src/themes/sequence.scss` inside the mermaid source. Key classes:

| CSS class | Controls |
|-----------|----------|
| `.actor` | Actor box fill and stroke |
| `text.actor` | Actor label text |
| `.actor-line` | The vertical lifeline |
| `.messageLine0` | Solid message arrows |
| `.messageLine1` | Dotted message arrows |
| `.messageText` | Message label text |
| `.labelBox` | Background of loop/alt/critical labels |
| `.loopText` | Text inside loop/alt/critical boxes |
| `.loopLine` | Border of loop/alt/critical boxes |
| `.note` | Note box fill and stroke |
| `.noteText` | Note box text |

### Where to put the CSS — by context

**VSCode markdown preview**

Add a path to a CSS file in `.vscode/settings.json`:

```json
{
  "markdown.styles": ["./styles/mermaid-overrides.css"]
}
```

The path is relative to the workspace root. The CSS file is injected into the preview's HTML `<head>`. You can target mermaid classes directly:

```css
/* styles/mermaid-overrides.css */
.note {
  fill: #1e2a3a;
  stroke: #4a90d9;
}
.noteText {
  fill: #cce4f7;
  font-size: 12px;
}
.actor {
  fill: #0d1b2a;
  stroke: #4a90d9;
}
```

This works **only in VSCode's local preview** — the CSS is not embedded in the markdown file and won't affect rendering anywhere else.

**HTML pages embedding mermaid**

Include the CSS in the `<head>` of the page:

```html
<head>
  <link rel="stylesheet" href="mermaid-overrides.css" />
</head>
```

Or inline via `<style>`. The CSS path is relative to the HTML file.

**GitHub / GitLab / remote markdown renderers**

❌ **Not possible.** Remote markdown renderers sanitize HTML and strip `<style>` tags and `<link>` elements. There is no way to inject a custom stylesheet into a mermaid diagram rendered on GitHub. Your only styling options are:

- Frontmatter `theme` and `themeVariables` (see below)
- `rect rgba(...)` background blocks inside the diagram code

### Styling via `themeVariables` (works everywhere frontmatter works)

The `base` theme exposes variables that control colors and fonts without needing CSS:

````markdown
```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#0d1b2a"
    primaryTextColor: "#cce4f7"
    primaryBorderColor: "#4a90d9"
    lineColor: "#4a90d9"
    noteBkgColor: "#1e2a3a"
    noteTextColor: "#cce4f7"
    actorBkg: "#0d1b2a"
    actorBorder: "#4a90d9"
    actorTextColor: "#cce4f7"
    signalColor: "#cce4f7"
    signalTextColor: "#cce4f7"
---
sequenceDiagram
    ...
```
````

> Note: `themeVariables` only takes full effect with `theme: base`. Other themes compute most variables internally and may ignore overrides.

</styling>

<nuances>

### Known limitations and gotchas

- **`theme: redux-dark` and `look: neo`** are supported in Mermaid v11+ only. Older renderers (e.g., older VSCode extension versions or some CI tools) will fall back to the default theme silently.
- **`noteAlign: left`** improves readability for multi-line notes but is ignored by some renderers that bundle older mermaid versions.
- **Frontmatter does not affect** the VSCode extension's `markdown-mermaid.darkModeTheme` / `lightModeTheme` settings — those are the fallback when no frontmatter is present.
- **`mirrorActors: true`** repeats actor boxes at the bottom of long diagrams. Useful for diagrams that scroll, distracting for short ones.
- **`bottomMarginAdj`** is a workaround for clipping caused by certain CSS resets that add a bottom margin to SVGs — set to `10`–`20` if the bottom actor row is cut off.
- **Color values in `themeVariables`** must be hex strings (`#rrggbb`) — named colors like `red` or `blue` are not recognized by the theming engine.
- **`mermaid.sequenceConfig` is legacy** — it predates frontmatter (which was added in v10.5.0). If you see it in documentation or examples, translate it to frontmatter `sequence:` YAML instead.

</nuances>

</sequence-diagram>

<flowchart>

on how to build a flowchart, see the [flowchart syntax reference](./flowchart.md)

## Flowchart Configuration and Styling

<configuration>

</configuration>

<styling>

</styling>

<nuances>

</nuances>

</flowchart>

</diagrams>
