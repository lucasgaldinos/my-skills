# Mermaid Diagram Skill Audit TODO

Audit date: 2026-05-18

## Implementation Progress

- [x] Recorded audit findings and improvement rationale.
- [x] Added a small-model decision gate to `SKILL.md`.
- [x] Added compact config routing to `SKILL.md`.
- [x] Created `docs/layout-configuration-guide.md` with practical layout recipes.
- [x] Updated `docs/diagram-routing.md` with renderer constraints, quantitative-data-first routing, and layout-versus-semantics guidance.
- [x] Added warnings for renderer-sensitive advanced layouts and undocumented tidy-tree knobs.
- [x] Ran diagnostics for edited Markdown files; no errors remain.
- [ ] Optional next step: render the example diagrams in the exact target Mermaid renderer before publishing them as guaranteed-working examples.

## Styling And Template Work

- [x] Confirmed no migration guide for legacy `%%{ init }%%`; add only a warning and prefer YAML frontmatter.
- [x] Added dark/light readability guidance for themeVariables and flowchart readability config.
- [x] Added `docs/styling-and-readability-guide.md`.
- [x] Routed styling docs and templates from `SKILL.md`.
- [x] Added approved `templates/` folder with individual Markdown templates and a gallery index.
- [x] Added core templates: flowchart light/dark, state, sequence, ER, and class.
- [x] Added theme templates: GitHub light, GitHub dark, dark slide, and print-friendly.
- [x] Smoke-rendered all individual templates with Mermaid CLI (`mmdc`).
- [ ] Optional next step: validate templates in the exact target renderer (GitHub, VS Code, Obsidian, or site build) and adjust unsupported theme variables if needed.

## Follow-Up Decisions

- [x] Adopted styling hierarchy: semantic diagram type → readability/fit config → theme palette → semantic `classDef` node classes.
- [x] Removed CSS as a normal styling path for the skill.
- [x] Updated SKILL guidance to prefer fully supported/stable diagrams by default.
- [x] Updated SKILL/layout guidance to ask before using beta/experimental diagram types or non-default layouts when multiple layouts may fit.
- [x] Added practical math support guidance with renderer caveats and fallbacks.
- [x] Added dedicated layout templates for dagre, ELK, and tidy-tree.
- [x] Deleted the cose-bilkent template after local Mermaid CLI failed to render it.
- [x] Rewrote math guidance around Mermaid-native KaTeX support instead of generic external Markdown math.
- [x] Documented Mermaid math support scope: v10.9.0+, `$$...$$`, flowcharts, and sequence diagrams.
- [x] Added renderer support matrix and known Mermaid math issues from GitHub search.
- [x] Added flowchart and sequence KaTeX math templates.
- [x] Smoke-rendered both KaTeX math templates with Mermaid CLI (`mmdc`).
- [x] Researched Mermaid issues `#5482` and `#7046`: GitHub math rendering remains unreliable, and Markdown formatting should not be mixed with Mermaid math.
- [x] Generated `tmp/math-rendering-comparison.md` and rendered five comparison diagrams with Mermaid CLI.
- [x] Confirmed readable sequence math pattern: unquoted messages/notes, single LaTeX backslashes, short expressions, and spacing config.
- [x] Confirmed flowchart guidance: short edge labels are acceptable, but long formulas should use dedicated formula nodes with spacing config.
- [x] Added arrow semantics guidance and updated templates to distinguish primary flow, fallback/dependency/feedback, rejected paths, async sequence notifications, UML class operators, and ER identifying/non-identifying cardinality.
- [x] Removed active cose-bilkent routing after the template was removed for weak documentation/renderer support.
- [x] Routed config decisions to `docs/mermaid-config-variables.md` for exact schema-backed variable names, defaults, and config placement.
- [ ] Optional next step: validate the layout templates in the exact target renderer.

<!--
## Summary Findings

- The skill is correctly implemented at the top level: it routes by intent, tells the agent to read syntax references before generating, names common Mermaid gotchas, and produces a clear output contract.
- The routing table is useful, but it relies on the model already understanding the difference between behavior, structure, time, concept maps, and quantitative charts. Smaller LLMs may still overuse `flowchart` because the current guidance does not force an explicit decision checklist.

  >[!note] What options to fix this?
  > provide some possible fixes.

  Possible fixes:
  + Add the small-model decision gate now present in `SKILL.md`.
  + Add examples and anti-examples for common confusions: flowchart vs state, flowchart vs sequence, class vs ER, C4 vs deployment topology.
  + Add acceptance tests/prompts where the expected answer is not `flowchart`.
  + Require one clarifying question when node semantics or renderer target changes the answer.
  + Keep detailed config in a separate guide so smaller models see a short routing path first.
- `docs/diagram-routing.md` is mostly properly categorized. The family map is coherent, and the interchangeability traps are the strongest part of the skill. It should add more first-pass tests for quantitative data, renderer/platform support, and whether the diagram is meant to show an algorithm, a static system, a lifecycle, or measured values.
- The config guidance in `SKILL.md` is too thin. It only mentions `theme`, `look`, and `layout`, while the selected chapter 4 examples use advanced layout-engine parameters for `elk`, `cose-bilkent`, and `tidy-tree`.
- Existing reference coverage is scattered. `references/config-layouts.md` lists `elk`, `tidy-tree`, `cose-bilkent`, and `dagre`, but does not explain when to choose each or which knobs are safe. `references/config-tidy-tree.md` says tidy-tree is mainly supported for mindmaps and does not document the `direction`, `levelSpacing`, or `nodeSpacing` keys shown in the local notes.
  >[!note]
  >yes, but as you've searched, there's information on the web for us to use.

  Applied:
  + Used official Mermaid layout/schema findings for the new practical guide.
  + Documented ELK keys that are schema-backed.
  + Documented flowchart spacing keys that are schema-backed.
  + Kept `cose-bilkent` parameter examples but marked them renderer-sensitive.
  + Kept tidy-tree custom knobs out of the stable guidance unless the renderer is tested.
- Several files under `references/` are autogenerated Mermaid docs and say not to edit them directly. New skill-specific guidance should go in a custom docs file such as `docs/layout-configuration-guide.md` or `references/config-layout-recipes.md`, then `SKILL.md` can link to it.
  >[!note] Asking questions
  >One option is to explicitly ask some questions from a checklist to better understand what the user wants. Using vscode_askQuestions/a similar tool or explicitly asking in chat if none is available but only for questions that cannot be inferred.

  Applied:
  + `SKILL.md` now tells the agent to prefer a structured question tool for decisions that change diagram type, renderer compatibility, or config strategy.
  + `docs/diagram-routing.md` now includes a fallback question set for ambiguous requests.

## Smaller LLM Risk Assessment

- Current skill will probably hold for larger models, but smaller models may fail in these cases:
  + User says "architecture diagram" and the model emits a generic `flowchart` instead of choosing between C4, `architecture-beta`, `block-beta`, or a plain flowchart fallback.
  + User provides table-like quantitative data and the model emits boxes instead of `xychart-beta`, `pie`, `sankey-beta`, `radar`, or `treemap`.
  + User asks for layout cleanup and the model changes the diagram type instead of using config.
  + User asks for a GitHub-compatible diagram and the model uses beta features or unsupported layout engines without warning.
  + User examples include undocumented/local config keys and the model presents them as stable Mermaid syntax.
- Add a short "small-model decision gate" near Step 1:
  + Are boxes actions? Use `flowchart`.
  + Are boxes states/conditions? Use `stateDiagram-v2`.
  + Are there two or more actors exchanging messages? Use `sequenceDiagram`.
  + Are there rows/columns, keys, and cardinality? Use `erDiagram`.
  + Are there classes with methods/inheritance? Use `classDiagram`.
  + Is value encoded by amount, proportion, or time series? Use a quantitative chart.
  + Is this mainly layout/styling? Keep the semantic diagram type and adjust config.

## `diagram-routing.md` Assessment

- Category placement is mostly correct:
  + `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `journey`, and `zenuml` under behavioral is reasonable.
  + `classDiagram`, `erDiagram`, C4, `architecture-beta`, `block-beta`, `packet-beta`, and `requirementDiagram` under structural is correct.
  + `gantt`, `timeline`, and `gitGraph` under temporal is correct.
  + `mindmap`, `quadrantChart`, and `kanban` under analytical/conceptual is acceptable.
  + `pie`, `xychart-beta`, `sankey-beta`, `radar`, and `treemap` under quantitative is correct.
- Improvements needed:
  + Add renderer support as an explicit routing constraint. Some diagram types are semantically correct but bad choices for GitHub, Obsidian, or basic VS Code previews.
  + Add a "data first" branch before defaulting to flowchart. Quantitative data should route to quantitative types before generic process diagrams.
  + Add guidance for "module dependency map" versus "formal architecture" versus "deployment topology". Current C4/architecture/flowchart distinction is good but could be more operational.
  + Add a fallback question set for ambiguous input: "Should nodes represent actions, states, actors, data entities, deployed systems, or measurements?"

  >[!important]
  >good additions. I liked them.

## Config Gaps From `chapter_4_insights.md`

- Lines 94-113 and 186-195 use `layout: cose-bilkent` with:
  + `nodeRepulsion`
  + `idealEdgeLength`
  + `edgeElasticity`
  + `nestingFactor`
  + `gravity`
- Add docs explaining `cose-bilkent` as a force-directed layout candidate for dense relationship graphs, tangled clusters, and exploratory maps. Mark parameter support as renderer/version-sensitive unless verified against the target Mermaid schema/runtime.
- Lines 123-136 and 155-168 use `layout: elk` with:
  + `nodePlacementStrategy: 'NETWORK_SIMPLEX'`
  + `mergeEdges: true`
- Add an ELK recipe because these options are documented in Mermaid config schema. Include other schema-listed keys: `cycleBreakingStrategy`, `forceNodeModelOrder`, and `considerModelOrder`.
- Add a caveat that `mergeEdges` may not behave consistently with subgraphs in every renderer/version, so the agent should include a rendering note when using it.
- Lines 213-226 use `layout: tidy-tree` with:
  + `direction`
  + `levelSpacing`
  + `nodeSpacing`
- Do not present those tidy-tree keys as official stable Mermaid options yet. Official docs mainly show `layout: tidy-tree` for mindmaps and do not clearly document those per-layout keys. Treat them as local/experimental examples unless tested in the target renderer.
- Add documented flowchart spacing alternatives:
  + `flowchart.nodeSpacing`
  + `flowchart.rankSpacing`
  + `flowchart.curve`

## Proposed Skill Features

- Add a "Config Routing" section to `SKILL.md` after Step 3:
  + Simple layered process: use default `dagre`.
  + Complex flowchart with fewer crossings: use `layout: elk` and read the ELK recipe.
  + Dense relationship graph: consider `layout: cose-bilkent`, but warn about renderer support.
  + Tree or hierarchy/mindmap: consider `layout: tidy-tree`; prefer documented mindmap usage.
  + Need more spacing in flowcharts: use `flowchart.nodeSpacing` and `flowchart.rankSpacing`, not undocumented layout keys.
  + Need visual style only: use `theme`, `themeVariables`, and `look`; do not change diagram type.
- Add a "Renderer Compatibility" checklist:
  + Target platform: GitHub, GitLab, Obsidian, VS Code extension, Mermaid Live, static site, or `mmdc`.
  + Mermaid version known or unknown.
  + Beta diagram types allowed or not.
  + Frontmatter config supported or not.
  + ELK/cose/tidy-tree layout engines enabled or not.
- Add a "When To Ask One Question" section:
  + Ask when action/state/system/data semantics are unclear.
  + Ask when user needs GitHub-safe output but requests beta/advanced layout features.
  + Ask when a requested config key is not in official docs/schema.
- Add "Do Not" rules:
  + Do not use `flowchart` as the default for structured data when `erDiagram`, `classDiagram`, or C4 fits.
  + Do not change diagram type to solve layout problems.
  + Do not claim undocumented layout knobs are portable.
  + Do not use autogenerated reference files as editable project guidance.

>[!important]
>these are the types of question that sometimes, only the user can answer.

Applied:

- These questions are now represented in `SKILL.md` as explicit structured-clarification guidance.
- `docs/diagram-routing.md` includes the concrete fallback question set.

## Proposed New Or Updated Docs

- Create `docs/layout-configuration-guide.md` or `references/config-layout-recipes.md` with:
  + Layout choice matrix: `dagre`, `elk`, `cose-bilkent`, `tidy-tree`.
  + YAML frontmatter examples for each layout.
  + ELK options table with documented schema keys.
  + Flowchart spacing recipe using `flowchart.nodeSpacing`, `flowchart.rankSpacing`, and `flowchart.curve`.
  + Cose-bilkent recipe marked renderer-sensitive until verified.
  + Tidy-tree recipe marked mindmap-first and experimental beyond documented usage.
- Update `SKILL.md`:
  + Add a small-model decision gate.
  + Link to the new layout config guide from Step 4.
  + Replace the current tiny layout table with a decision table plus platform warnings.
  + Add `config-tidy-tree.md` to the config reference list if tidy-tree remains mentioned.
- Update `docs/diagram-routing.md`:
  + Add platform compatibility as a final routing constraint.
  + Add quantitative-data-first routing examples.
  + Add a module-map decision rule: informal dependencies use `flowchart` or `block-beta`; formal architecture uses C4; deployed cloud topology uses `architecture-beta`.
- Optionally update `references/examples.md` with a compact gallery of correct examples and anti-examples for smaller models.

## Suggested Acceptance Criteria

- Given a process with decisions, the skill chooses `flowchart` and avoids C4/sequence syntax.
- Given actors exchanging messages, the skill chooses `sequenceDiagram`.
- Given a lifecycle with named statuses, the skill chooses `stateDiagram-v2`.
- Given database tables with PK/FK/cardinality, the skill chooses `erDiagram`.
- Given OOP classes with methods/inheritance, the skill chooses `classDiagram`.
- Given architecture intended for GitHub markdown, the skill avoids unsupported `architecture-beta` unless it gives a clear rendering warning.
- Given a dense flowchart with crossing edges, the skill keeps `flowchart` and considers `layout: elk` instead of changing semantics.
- Given the chapter 4 config examples, the skill can explain which options are documented, which are renderer-sensitive, and which need verification.

## Priority Order

1. Add small-model decision gate to `SKILL.md`.
2. Add layout/config decision table to `SKILL.md`.
3. Create custom layout configuration guide instead of editing autogenerated references.
4. Update `docs/diagram-routing.md` with renderer/platform and quantitative-data routing constraints.
5. Add examples and anti-examples for the most common confusions. -->
