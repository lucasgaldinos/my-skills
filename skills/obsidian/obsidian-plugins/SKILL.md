---
name: obsidian-plugins
description: >
  Use this skill when developing, debugging, or reviewing Obsidian plugins or themes —
  writing TypeScript plugin code, styling with CSS variables, registering views/commands/events,
  handling the Vault API, building settings tabs, releasing to the community directory,
  or checking submission requirements and developer policies. Triggers on "Obsidian plugin",
  "build a plugin for Obsidian", "Obsidian API", "Obsidian theme", "create an Obsidian extension",
  "register a view in Obsidian", "how do I access the vault in Obsidian",
  "Obsidian settings tab", "Obsidian CodeMirror extension", "Obsidian manifest",
  "submit my plugin to Obsidian", "Obsidian CSS variables", "Obsidian plugin guidelines",
  "Obsidian developer docs", "isDesktopOnly", "Obsidian ItemView", "registerMarkdownPostProcessor".
  Routes to the correct reference document before answering any implementation question.
argument-hint: "What are you building for Obsidian? A plugin? A theme? Which feature?"
user-invocable: true
---

<!-- markdownlint-disable MD044 -->

# Obsidian Plugin & Theme Development — Reference Router

<context>

This skill provides a **local clone of the official [obsidian-developer-docs](https://github.com/obsidianmd/obsidian-developer-docs)**
at `references/`. Every `.md` file under `references/` is a page from [docs.obsidian.md](https://docs.obsidian.md/).
The references include: **Plugins** (lifecycle, APIs, UI, guides, releasing), **Reference** (manifest schema,
CSS variables, full TypeScript API — 1195 docs across 172 classes), **Themes** (app themes, Publish themes),
and **Policies** (developer policies, submission requirements, self-critique checklists).

**This skill does NOT contain the reference content itself.** It tells you which file to read and how to
search the references efficiently. Always read the referenced file before answering an implementation
question — the TypeScript API surface is large and versioned.
</context>

---

## Reference Map

<context>

```text
references/
├── Home.md                         ← Landing page, community links
├── Developer policies.md           ← What plugins MUST / MUST NOT do
├── Obsidian October plugin self-critique checklist.md  ← Pre-submission quality checklist
├── Plugins/
│   ├── Events.md                   ← Event system, registerEvent()
│   ├── Vault.md                    ← Vault API: read, write, delete, process
│   ├── Editor/                     ← CodeMirror 6: extensions, decorations, state fields, view plugins, post-processing
│   ├── Getting started/            ← Anatomy, build tutorial, dev workflow, mobile, React/Svelte
│   ├── Guides/                     ← Bases views, defer views, declarative settings, load time, secrets, pop-out windows
│   ├── Releasing/                  ← Guidelines, submission requirements, submit workflow, GitHub Actions, beta testing
│   └── User interface/             ← Commands, context menus, HTML elements, icons, modals, ribbon, settings, status bar, views, workspace
├── Reference/
│   ├── Manifest.md                 ← manifest.json schema
│   ├── Versions.md                 ← API version history
│   ├── CSS variables/              ← Foundations, Components, Editor, Plugins, Window, Publish
│   └── TypeScript API/             ← 172+ class dirs, ~1195 docs (one .md per class, subdir per method)
└── Themes/
    ├── App themes/                 ← Build, guidelines, submit, release
    └── Obsidian Publish themes/    ← Build, best practices
```

For the full directory tree with individual file annotations, use:

```bash
find references -name "*.md" | sort
```

</context>

---

## Routing Table

<instructions>

When the user asks an Obsidian development question, match their intent below.
**Read the referenced file(s) before answering.** The table is ordered by development phase.

</instructions>

<routing>

<route name="new-plugin">

**I'm new — where do I start?**

<read>

`references/Plugins/Getting started/Anatomy of a plugin.md` →
`references/Plugins/Getting started/Build a plugin.md` →
`references/Reference/Manifest.md`
</read>
</route>

<route name="vault-operations">

Prompt
: **I need to read/write/delete files in the vault**

<read>

`references/Plugins/Vault.md` — getMarkdownFiles(), read(), cachedRead(), modify(), process(), delete(), trash()</read>
<note>

Prefer `Vault.process()` over read()+modify() to avoid race conditions. For async: `cachedRead()` then `process()`.</note>
</route>

<route name="command">

prompt
: **Add a command** → `references/Plugins/User interface/Commands.md`
</route>

<route name="settings">

prompt
: **Add a settings tab** → `references/Plugins/User interface/Settings.md` (declarative API, Obsidian 1.13+).
For older versions: `references/Plugins/Guides/Migrate to declarative settings.md`.
For secrets: `references/Plugins/Guides/Store secrets.md`.
</route>

<route name="custom-view">

prompt
: **Create a custom view** → `references/Plugins/User interface/Views.md` (ItemView, registerView) +
`references/Plugins/User interface/Workspace.md` (leaves, layout).
For heavy views: `references/Plugins/Guides/Defer views.md`.
</route>

<route name="modal">

prompt
: **Modal / dialog / pop-up** → `references/Plugins/User interface/Modals.md`
</route>

<route name="ribbon">

prompt
: **Ribbon icon** → `references/Plugins/User interface/Ribbon actions.md`
</route>

<route name="status-bar">

prompt
: **Status bar item** → `references/Plugins/User interface/Status bar.md`
</route>

<route name="context-menu">

prompt
: **Right-click context menu** → `references/Plugins/User interface/Context menus.md`
</route>

<route name="icons">

prompt
: **Use icons** → `references/Plugins/User interface/Icons.md`
</route>

<route name="markdown-post-processing">

prompt
: **Transform Markdown in reading mode** →
`references/Plugins/Editor/Markdown post processing.md` (registerMarkdownPostProcessor,
registerMarkdownCodeBlockProcessor) + `references/Plugins/Editor/Editor.md`
</route>

<route name="editor-extensions">

prompt
: **Extend the editor (CodeMirror 6)** — decorations, widgets, state fields:

<read>

`references/Plugins/Editor/Editor extensions.md` →
`references/Plugins/Editor/Decorations.md` →
`references/Plugins/Editor/State fields.md` →
`references/Plugins/Editor/State management.md` →
`references/Plugins/Editor/View plugins.md` →
`references/Plugins/Editor/Viewport.md` →
`references/Plugins/Editor/Communicating with editor extensions.md`
</read>
</route>

<route name="events">

prompt
: **Listen to events** → `references/Plugins/Events.md` (registerEvent, registerInterval, registerDomEvent)

+ `references/Plugins/Vault.md` (create, modify, delete, rename events)
</route>

<route name="bases-view">

prompt
: **Build a Bases view** → `references/Plugins/Guides/Build a Bases view.md`
</route>

<route name="mobile">

prompt
: **Support mobile** → `references/Plugins/Getting started/Mobile development.md`

<note>

Critical: no Node/Electron APIs at top level, gate with `Platform.isDesktopApp`, use `requestUrl`
not `fetch`, no regex lookbehinds on iOS &lt;16.4.
</note>
</route>

<route name="react-svelte">

prompt
: **Use React / Svelte** → `references/Plugins/Getting started/Use React in your plugin.md` or `references/Plugins/Getting started/Use Svelte in your plugin.md`
</route>

<route name="typescript-api">

prompt
: **Look up a specific TypeScript class or method** → Find the class `.md` under `references/Reference/TypeScript API/`. Methods are in subdirectories (e.g., `Plugin/onload.md`, `Vault/read.md`). If unsure of the class name, `<search>`grep_search the method/concept name scoped to `references/Reference/TypeScript API/`.
</search>
</route>

<route name="css-variables">

prompt
: **CSS variables for styling** → `references/Reference/CSS variables/About styling.md` +
`references/Reference/CSS variables/CSS variables.md` (index). Then the relevant subdirectory:
Foundations/ (colors, spacing), Components/ (buttons, modals), Editor/ (content styling).
</route>

<route name="theme">

prompt
: **Build a theme** → `references/Themes/App themes/Build a theme.md` +
`references/Themes/App themes/Theme guidelines.md` +
`references/Reference/CSS variables/`.
For Publish: `references/Themes/Obsidian Publish themes/Build a Publish theme.md`.
</route>

<route name="release">

prompt
: **Release / submit to community directory** →

<read>

`references/Developer policies.md` (MUST read first) →
`references/Plugins/Releasing/Submission requirements for plugins.md` →
`references/Plugins/Releasing/Plugin guidelines.md` →
`references/Plugins/Releasing/Submit your plugin.md` →
`references/Plugins/Releasing/Release your plugin with GitHub Actions.md`
</read>
</route>

<route name="pre-finish-plugin">

prompt
: **Before finishing a plugin** — run through `references/Obsidian October plugin self-critique checklist.md`. Covers releasing/naming, compatibility, mobile support, coding style, security, API usage, and performance. Every item is a common rejection reason.
</route>

<route name="pre-finish-theme">

prompt
: **Before finishing a theme** — run through `references/Obsidian October theme self-critique checklist.md`. Covers CSS variable usage, performance (`:has()` pitfalls), asset bundling, licensing, screenshots, and naming.
</route>

<route name="pre-finish-vault">

prompt
: **Before finishing a vault tool / organization workflow** — consult `references/Obsidian October vault self-critique checklist.md` for vault maintenance, orphan notes, broken links, properties cleanup, and backup verification.
</route>

<route name="load-time">

prompt
: **Optimize load time** → `references/Plugins/Guides/Optimize plugin load time.md`
</route>

<route name="manifest">

prompt
: **manifest.json schema** → `references/Reference/Manifest.md`
</route>

<route name="pop-out">

prompt
: **Pop-out windows** → `references/Plugins/Guides/Support pop-out windows.md`
</route>

<route name="dev-workflow">

prompt
: **Dev workflow / hot reload** → `references/Plugins/Getting started/Development workflow.md`
</route>

</routing>

---

## Search Strategies

<instructions>

The TypeScript API alone has 1195 docs across 172 class directories. Search before guessing.

Prefer **`ripgrep` (`rg`)** for text search and **`fd`** for file-name lookup — always prefix
with **`rtk`** to compress output. Fall back to `grep_search` tool for workspace-scoped search.

</instructions>

### Find files by name (`fd`)

```bash
rtk fd "Plugin.md" references/Reference/TypeScript\ API       # class doc by name
rtk fd "process.md" references/Reference/TypeScript\ API       # method doc by name
rtk fd "\.md$" references/Plugins/Editor                       # all .md under a section
```

### Full-text search (`rg`)

```bash
rtk rg "registerView" references/                              # concept anywhere
rtk rg -C 2 "Vault.process" references/                        # with 2 lines context
rtk rg --type md "onLayoutReady" references/Plugins/Guides/    # scope to section
rtk rg -i "ItemView" references/Reference/TypeScript\ API/     # case-insensitive API lookup
```

### grep_search patterns (fallback tool)

| You need | Query pattern |
| --- | --- |
| How to register something | `registerView\|registerCommand\|registerEvent` |
| Vault file operations | `vault\.(read\|modify\|process\|delete\|trash)` |
| Editor decorations | `Decoration\|WidgetType\|ViewPlugin` |
| Settings / configuration | `settings\|loadData\|saveData\|SettingTab` |
| CSS variable for a component | `--button\|--modal\|--dialog\|--checkbox` |

### Scoped search by section

Prefix `rg` with the path, or use `grep_search` `includePattern`:

| Section | Path / `includePattern` |
| --- | --- |
| Getting started | `references/Plugins/Getting started/**` |
| User interface | `references/Plugins/User interface/**` |
| Editor | `references/Plugins/Editor/**` |
| Guides | `references/Plugins/Guides/**` |
| Releasing | `references/Plugins/Releasing/**` |
| CSS variables | `references/Reference/CSS variables/**` |
| TypeScript API | `references/Reference/TypeScript API/**` |

### Deep research

For multi-document questions, use the **Explore** subagent set to `thorough`. Example:

> Explore `references/Plugins/User interface/Views.md`,
> `references/Plugins/User interface/Settings.md`, and
> `references/Plugins/Getting started/Mobile development.md`
> for building a mobile-compatible plugin with custom views and settings.

---

## Critical Rules & Gotchas

<rules>

These are the most common reasons plugins get rejected or break at runtime.
Summarized from the reference docs — always read the full docs before submission.

### Security & Policy

+ **Never use `innerHTML`, `outerHTML`, or `insertAdjacentHTML`** with user input. Use `createEl()`, `createDiv()`, `createSpan()` (`references/Plugins/User interface/HTML elements.md`).
+ **Never use `app` or `window.app`** — use `this.app` from your Plugin instance. The global is for debugging only.
+ **No client-side telemetry.** Server-side telemetry requires a privacy policy in the README.
+ **Don't set default hotkeys** for commands.
+ **Disclose network access in your README** — explain why and which services are contacted.
+ **Code cannot be obfuscated.**

### Code Quality

+ **Use Sentence case for all UI text** — "Template folder location", not "Template Folder Location".
+ **Don't assign styles via JavaScript or inline HTML** — use scoped CSS classes.
+ **Prefer `async`/`await` over raw `Promise` chains.**
+ **Never use `var`** — use `const` (preferred) or `let`.
+ **Check with `instanceof` before casting** to `TFile`, `TFolder`, or `FileSystemAdapter`.
+ **Release all resources in `onunload()`.** Use `registerEvent()`, `registerInterval()`, `registerDomEvent()` — they auto-cleanup on unload.
+ **Don't include plugin name/ID in command names** — Obsidian prefixes automatically.

### Mobile Compatibility

<small>

From `references/Plugins/Getting started/Mobile development.md`</small>

+ **Don't import `fs`, `path`, `electron` at top level.** Gate behind `Platform.isDesktopApp`.
+ **Don't cast `Vault.adapter` to `FileSystemAdapter`** without `instanceof` — on mobile it's `CapacitorAdapter`.
+ **Use `requestUrl()` not `fetch` or `axios`** — handles mobile CORS quirks.
+ **Use `Platform` API, not `process.platform`.**

</rules>

<gotchas>

+ **`Vault.process()` vs read()+modify():** Always prefer `process()` — it guarantees the file hasn't changed between read and write. For async: `cachedRead()` then `process()`, verifying data hasn't changed in the callback. See `references/Plugins/Vault.md`.
+ **View lifecycle:** Never store references to your view instances. Obsidian may call the view factory multiple times. Use `workspace.getLeavesOfType()` to find views. See `references/Plugins/User interface/Views.md`.
+ **Vault `create` event at startup:** Obsidian fires `vault.on('create')` for every file during init. Gate behind `workspace.onLayoutReady()` or check `workspace.layoutReady`. See `references/Plugins/Guides/Optimize plugin load time.md`.
+ **manifest.json `id` must match plugin folder name** for local dev — otherwise `onExternalSettingsChange` won't fire. See `references/Reference/Manifest.md`.
+ **Declarative settings need Obsidian ≥ 1.13.0** (`getSettingDefinitions()`). For older versions, use the legacy `display()` or dual-support pattern. See `references/Plugins/Guides/Migrate to declarative settings.md`.

</gotchas>

---

## Development Workflows

<context>

Common end-to-end paths through the reference docs.

</context>

<workflow name="new-plugin">

prompt
: **Build a plugin from scratch:**
`references/Plugins/Getting started/Anatomy of a plugin.md` →
`references/Reference/Manifest.md` →
`references/Plugins/Getting started/Build a plugin.md` →
`references/Plugins/Getting started/Development workflow.md` →
add features via routing table →
`references/Developer policies.md` + `references/Plugins/Releasing/Plugin guidelines.md` →
`references/Plugins/Releasing/Submit your plugin.md`
</workflow>

<workflow name="custom-view">

prompt
: **Add a custom view:**
`references/Plugins/User interface/Views.md` →
`references/Plugins/User interface/Workspace.md` →
`references/Plugins/User interface/HTML elements.md` →
(optional) `references/Plugins/Guides/Defer views.md`
</workflow>

<workflow name="editor-enhancements">

prompt
: **Add CodeMirror 6 editor enhancements:** `references/Plugins/Editor/Editor extensions.md` → `references/Plugins/Editor/Decorations.md` → `references/Plugins/Editor/State fields.md` → `references/Plugins/Editor/View plugins.md` → (if multi-extension) `references/Plugins/Editor/Communicating with editor extensions.md`
</workflow>

<workflow name="release">

prompt
: **Prepare for release:** `references/Developer policies.md` → `references/Plugins/Releasing/Submission requirements for plugins.md` → `references/Plugins/Releasing/Plugin guidelines.md` → `references/Obsidian October plugin self-critique checklist.md` → `references/Plugins/Releasing/Submit your plugin.md` → `references/Plugins/Releasing/Release your plugin with GitHub Actions.md`
</workflow>

<workflow name="pre-finish-plugin">

prompt
: **Before finishing a plugin** — read `references/Obsidian October plugin self-critique checklist.md` and verify every item. Covers: releasing/naming, compatibility, mobile, coding style, security, API usage, performance, UI text. Do this before considering the plugin done.
</workflow>

<workflow name="pre-finish-theme">

prompt
: **Before finishing a theme** — read `references/Obsidian October theme self-critique checklist.md` and verify every item. Covers: CSS variables, performance (`:has()` pitfalls), local assets, screenshots, licensing, naming.
</workflow>

<workflow name="pre-finish-vault">

prompt
: **Before finishing a vault organization tool or workflow** — consult `references/Obsidian October vault self-critique checklist.md` for vault maintenance, orphan notes, broken links, properties, backup verification, and rediscovery ideas.
</workflow>

---

## API Version Awareness

<context>

The TypeScript API docs include version annotations (e.g., "0.9.7", "1.13.0") showing when each
method was introduced. See `references/Reference/Versions.md` for version history.

+ Set `minAppVersion` in manifest.json to the highest API version your plugin uses.
+ If a method requires "1.13.0", your plugin requires Obsidian ≥ 1.13.0.
</context>
