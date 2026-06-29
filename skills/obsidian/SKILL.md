---
name: obsidian
description: >
  Use when working with Obsidian — Obsidian vault notes, Obsidian-flavored Markdown, Obsidian
  Canvas (.canvas files), Obsidian Bases (.base files), Obsidian Web Clipper templates, Obsidian
  MCP vault operations, Obsidian CLI vault management, or extracting web content to clip into
  Obsidian. Triggers on "Obsidian", "Obsidian vault", "Obsidian note", "Obsidian canvas",
  "Obsidian base", "wikilink", "callout", "Obsidian Web Clipper", "clip into Obsidian",
  "defuddle", or "obsidian-cli". Routes to the correct sub-skill before acting.
argument-hint: "Whenever obsidian is cited, ask the user what they want to do if not specified and load the correct sub-skill before proceeding"
user-invocable: true

---

# Obsidian Skill Router

<context>

This is the **entry point** for all Obsidian-related tasks. It does not perform actions itself —
it identifies the correct sub-skill and loads it before proceeding. Each sub-skill carries
specialized tool patterns, schemas, and safety rules; skipping this routing step and improvising
will produce incorrect output or silent failures.

**Exception:** Conceptual or informational questions about Obsidian (not a file, vault, or tool
operation) can be answered directly without loading any sub-skill.
</context>

## Routing

<instructions>

Follow these two steps in order before taking any action.

<step n="1" name="check-if-sub-skill-is-needed">

If the user is asking a **conceptual or informational question** about Obsidian with no file,
vault, or tool operation involved — **respond directly. Do not load any sub-skill.**

Examples that need no sub-skill: *"What is Obsidian?"*, *"How do callouts work?"*,
*"What is the difference between Bases and Canvas?"*

For all other requests, proceed to Step 2.
</step>

<step n="2" name="identify-and-load-sub-skill">

Match the user's intent to exactly one route in the table below. Load the linked SKILL.md
**before** taking any other action or generating any output.

<routing>

<route name="mcpvault">

### mcp-vault

<when>

User wants vault CRUD, search, tags, frontmatter, or git sync **AND the Obsidian MCP server is
active**.
</when>
<keywords>

read note, write note, patch note, move note, delete note, search vault, update tags,
update frontmatter, daily note headless, sync vault, git backup, vault backup</keywords>
<load>

[mcpvault/SKILL.md](mcpvault/SKILL.md)</load>
<note>

For app-context actions (open in editor, backlinks, plugin debugging), use `obsidian-cli` even
when MCP is active — these require the running Obsidian app.
</note>
</route>

<route name="obsidian-cli">

### obisdian-cli

<when>

User wants to interact with a **running Obsidian app instance**, OR the MCP server is not active.
</when>
<keywords>

open note in Obsidian, obsidian CLI, backlinks, unresolved links, reload plugin, debug
plugin, debug theme, screenshot Obsidian, eval javascript in Obsidian, daily note app,
obsidian command</keywords>
<load>

[obsidian-cli/SKILL.md](obsidian-cli/SKILL.md)</load>
<note>

Requires Obsidian desktop app to be running. Use as fallback for vault read/write when MCP is
unavailable.
</note>
</route>

<route name="obsidian-bases">

### obsidian-bases

<when>

User wants to create or edit a `.base` file — YAML-configured database-like views over notes.
</when>
<keywords>

base file, .base, table view, card view, list view, filter notes, formula, summary,
database view, Obsidian Bases, group notes</keywords>
<load>

[obsidian-bases/SKILL.md](obsidian-bases/SKILL.md)</load>
<note>

`.base` files are YAML query views. Completely different from `.canvas` JSON graphs. If the user
says "canvas" instead of "base", route to `json-canvas`.
</note>
</route>

<route name="json-canvas">

### json-canvas

<when>

User wants to create or edit a `.canvas` file — visual mind maps, flowcharts, or node/edge graphs.
</when>
<keywords>

canvas file, .canvas, mind map, flowchart, visual canvas, knowledge graph,
project board, JSON canvas, Obsidian canvas, node, edge, connect notes visually</keywords>
<load>

[json-canvas/SKILL.md](json-canvas/SKILL.md)</load>
<note>

`.canvas` files are JSON node/edge graphs. Completely different from `.base` YAML views. If the
user says "base" instead of "canvas", route to `obsidian-bases`.
</note>
</route>

<route name="obsidian-markdown">

### obsidian-markdown

<when>

User wants to **author or format content** inside an Obsidian note — not vault operations.
</when>
<keywords>

wikilink, callout, embed, frontmatter, properties, Obsidian markdown, OFM,
write note content, format note, tags in note, Mermaid in Obsidian, block reference</keywords>
<load>

[obsidian-markdown/SKILL.md](obsidian-markdown/SKILL.md)</load>
<note>

Use for content authoring only. Use `mcpvault` or `obsidian-cli` to save, move, or search
notes in the vault.
</note>
</route>

<route name="obsidian-clipper-template-creator">

### obsidian-clipper-template-creator

<when>

User wants to create a **Web Clipper JSON template** to clip a specific website into Obsidian.
</when>
<keywords>

clipper template, web clipper, clip website, clip article, clip YouTube, recipe
clipper, clipping template, Obsidian Web Clipper JSON, create template for site</keywords>
<load>

[obsidian-clipper-template-creator/SKILL.md](obsidian-clipper-template-creator/SKILL.md)</load>
<note>

This creates the template JSON only. The actual clipping is done by the browser extension.
Use `defuddle` first if you need to analyze the target page structure.
</note>
</route>

<route name="defuddle">

### defuddle

<when>

User wants to extract or read content from a web URL (not a `.md` file).
</when>
<keywords>

extract page, parse URL, get web content, read article from web, defuddle,
clean up web page, strip clutter from URL, get readable content from link</keywords>
<load>

[defuddle/SKILL.md](defuddle/SKILL.md)</load>
<note>

Do NOT use for `.md` URLs — those are already Markdown; use WebFetch directly. Often the first
step before creating a clipper template or saving a clipped note to vault.
</note>
</route>

<route name="obsidian-plugins">

### obsidian-plugins

<when>

user wants to create a new extension for obsidian,
</when>

<keywords>

extension, extension setup, features, extending obsidian.
</keywords>

<load>

[obsidian-plugins](./obsidian-plugins/SKILL.md)</load>

<note>

Use when the user is developing some type of extension for obsidian.

</routing>

</step>

</instructions>

## Disambiguation rules

<rules>

<rule name="mcp-vs-cli">

**MCP vs CLI — which to use:**
Use `mcpvault` for headless vault data operations (read, write, search, patch, move, tag,
frontmatter, git sync) when the MCP server is active. Use `obsidian-cli` for app-context actions
MCP cannot perform: opening a note in the editor, backlinks, unresolved links, plugin/theme
debugging, daily note template expansion with app variables, screenshots.
**Never mix tool patterns from both sub-skills in the same operation.**
</rule>

<rule name="authoring-vs-operations">

**Authoring content vs vault operations:**
Use `obsidian-markdown` when the task is *authoring or formatting note content* (syntax,
wikilinks, callouts, embeds, frontmatter structure). Use `mcpvault` or `obsidian-cli` when the
task is a *vault operation* (create file, move, search, tag, or sync files in the vault).
These two are often chained: author with `obsidian-markdown`, then save with `mcpvault`.
</rule>

<rule name="bases-vs-canvas">

**Bases vs Canvas — completely different formats:**
`.base` files are YAML-configured database views over existing notes (filters, formulas, view
types). `.canvas` files are visual JSON node/edge graph files (mind maps, flowcharts). Their
schemas are incompatible — never confuse them or apply one sub-skill's patterns to the other.
</rule>

<rule name="chained-workflows">

**Chained workflows:** A full web-to-vault workflow may span multiple sub-skills in sequence:
`defuddle` (extract page) → `obsidian-clipper-template-creator` (design template) →
`mcpvault` or `obsidian-cli` (save note to vault).
Load each sub-skill only when you reach that step — not all at once upfront.
</rule>

</rules>

<gotchas>

<gotcha>

Always load the sub-skill **before** taking any action. Sub-skills contain tool invocation
patterns, YAML schemas, and safety constraints not duplicated here — acting without them risks
incorrect or destructive output.
</gotcha>

<gotcha>

When a task spans multiple sub-skills, load them **sequentially as you reach each step** rather
than improvising the combined behavior.
</gotcha>

<gotcha>

When the user's intent is ambiguous, use `vscode_askQuestions` to clarify before routing.
A wrong sub-skill produces worse results than a one-question delay.
</gotcha>

</gotchas>
