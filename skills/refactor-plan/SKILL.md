---
name: refactor-plan
description: >
  Use when the user wants to refactor code, identify or apply design patterns,
  diagnose code smells, fix SOLID violations, clean up architecture, or pay down
  technical debt. Triggers on phrases like "refactor this", "what design pattern
  fits here", "identify patterns in this codebase", "this code smells",
  "suggest a pattern", "fix this god class", "decouple these modules",
  "apply SOLID", "clean up this architecture". Routes a structured workflow:
  understand intent → detect smells/existing patterns → match to GoF patterns
  and Fowler refactorings → produce one of three outputs (analysis report,
  implementation plan, or applied refactor) the user picks per invocation.
argument-hint: "<target file/folder/module> <optional: analyze | plan | apply>"
---

# Refactor Plan

<context>

This is a **workflow skill** that combines three responsibilities — **identify** existing
design patterns, **diagnose** code smells and SOLID violations, and **suggest** the right
GoF pattern or Fowler refactoring to fix them. The sequence matters: a pattern suggestion
made before understanding the user's intent and the actual problem class is, at best, a
cargo-cult recommendation; at worst, it locks the codebase into the wrong abstraction.

The key insight: design patterns are answers to **specific problem categories**, not generic
"better code." Every recommendation must trace back to a concrete smell, a stated change
axis, or a SOLID violation observed in the code — never to "this looks like it could use a
Factory."

This skill is **language-agnostic**. Patterns are described in prose and structural terms,
not in code-specific syntax. Future template assets per language will live under
`assets/templates/<language>/` but are out of scope here.
</context>

<prerequisites>

Before running the workflow, confirm:

- [ ] The user has identified a target — a file, module, folder, or whole codebase scope.
- [ ] The user has stated an output mode (or you will ask in Step 1): `analyze`, `plan`, or `apply`.
- [ ] You have read access to the target code via 'read_file' / 'grep_search' / 'semantic_search'.
</prerequisites>

## Step 1: Capture intent (structured interview)

<instructions>

Use 'vscode_askQuestions' (or equivalent) to ask the user the following. **Do not skip this
step** even if the user gave a one-line request — pattern recommendations made without
intent are the most common failure mode of this skill.

Ask in a single batched question call:

1. **Output mode** — `analyze` (report only), `plan` (structured refactor proposal under
   `/spec/` or `/plans/`), or `apply` (modify files after plan approval).
2. **Primary motivation** — what's painful today? (e.g., "adding a new device type touches
   12 files", "this class is 2000 lines", "tests are impossible to write", "two teams
   keep stepping on each other in this module").
3. **Change axes** — what is most likely to change in the next 6–12 months? (new product
   types, new platforms/protocols, new algorithms, new output formats, new UI surfaces,
   none stated).
4. **Constraints** — language, framework, performance ceiling, public API stability,
   backward-compatibility requirements, team size touching this code.
5. **Out-of-scope** — anything explicitly off-limits (e.g., "don't touch the persistence
   layer", "no new dependencies").
6. **Existing patterns** — does the user already believe a pattern is in use here? (If
   yes, the skill validates; if no, the skill discovers.)
7. **Acceptance criteria** — how will the user know the refactor succeeded? (tests pass,
   class size shrinks, new feature lands in one file, cyclomatic complexity drops, etc.)
</instructions>

<warning>

> [!warning]
> Skip this step and the recommendation will be plausible-sounding but wrong. The four
> most consequential answers are **#2 (motivation)**, **#3 (change axes)**, **#4
> (constraints)**, and **#7 (acceptance criteria)** — they determine whether the right
> answer is Strategy vs. Template Method, Factory Method vs. Abstract Factory, or "do
> nothing, the code is fine for the stated change profile."
</warning>

## Step 2: Survey the codebase

<instructions>

Map the target before recommending anything. Use parallel tool calls where possible.

1. Use 'list_dir' on the target to understand structure and module boundaries.
2. Use 'semantic_search' with a query derived from the user's motivation (Step 1.2) to
   locate the hot spots.
3. Use 'grep_search' for known structural signals:
   + Long conditional blocks: `\b(if|elif|else if|switch|case)\b` (regex) — candidates
     for Strategy, State, Chain of Responsibility, replace-conditional-with-polymorphism.
   + Type-checking branches: `instanceof|isinstance|typeof|type\(` — candidates for
     polymorphism, Visitor, double-dispatch.
   + Telescoping constructors / large parameter lists — Builder candidate.
   + Singleton / global accessors: `getInstance|get_instance|\.instance\b` — verify
     justification.
   + God-class indicators: classes/files exceeding ~500 lines, ~20 public methods.
4. Use 'read_file' on the 2–5 most relevant hot spots in full (not summarized).

Record findings in a working table (file, lines, smell, evidence). Do not skip evidence —
every later recommendation must cite a concrete location.
</instructions>

<validation>

Before moving to Step 3, confirm:

- [ ] At least 2 concrete smell instances with file:line evidence, OR a justified statement
  that no significant smells were found.
- [ ] Existing patterns (if any) explicitly identified by name with evidence.
- [ ] The user's stated change axis maps to specific code locations.
</validation>

<recovery>

If the codebase is too large to survey exhaustively, scope down: ask the user to pick the
single most painful module, and run the workflow on that scope only. Do not attempt to
"refactor the whole codebase" in one pass — that recommendation is itself a smell.
</recovery>

## Step 3: Classify the problem

<instructions>

For each smell or pain point found in Step 2, classify it into a **problem category**
before reaching for a pattern. Read [references/design-problem-categories.md](references/design-problem-categories.md)
to anchor the classification. The categories are:

- **Creational** — object instantiation is hardcoded, conditional on type, or coupled to
  concrete classes.
- **Structural** — interfaces don't compose, hierarchies explode combinatorially, legacy
  modules don't fit, or memory/access patterns need optimization.
- **Behavioral** — algorithms, control flow, state transitions, or inter-object
  communication are tangled.

Then sub-classify into one of these problem axes:

| Problem axis | Likely category | First-look patterns |
| --- | --- | --- |
| "Adding a new type means editing N files" | Creational | Factory Method, Abstract Factory |
| "Constructor takes 12 optional args" | Creational | Builder |
| "Object initialization is expensive and repeated" | Creational | Prototype, Flyweight |
| "Need exactly one instance of X" | Creational | Singleton (verify carefully) |
| "Two incompatible interfaces must collaborate" | Structural | Adapter |
| "Class hierarchy explodes across two axes" | Structural | Bridge |
| "Tree of nested objects, client treats them uniformly" | Structural | Composite |
| "Need to add behavior at runtime without inheritance" | Structural | Decorator |
| "Subsystem is overwhelming to use" | Structural | Facade |
| "Memory exhaustion from many similar objects" | Structural | Flyweight |
| "Need to control/defer/cache access to a heavy object" | Structural | Proxy |
| "Long sequential validation/processing pipeline" | Behavioral | Chain of Responsibility |
| "Need undo/redo, queueing, or logging of actions" | Behavioral | Command |
| "Traversal logic clutters business logic" | Behavioral | Iterator |
| "Many-to-many object communication is chaos" | Behavioral | Mediator |
| "Need to snapshot and restore state safely" | Behavioral | Memento |
| "One change must notify N unknown observers" | Behavioral | Observer |
| "Object behavior changes with state, big switch blocks" | Behavioral | State |
| "Need to swap algorithms at runtime" | Behavioral | Strategy |
| "Same skeleton, varying steps" | Behavioral | Template Method |
| "Need new ops over heterogeneous structure w/o changes" | Behavioral | Visitor |

For SOLID-flavored smells specifically (god class, primitive obsession, feature envy,
inappropriate intimacy, refused bequest), read [references/solid-violations.md](references/solid-violations.md)
and [references/code-smells.md](references/code-smells.md).
</instructions>

<rules>

- **One smell can map to multiple patterns.** Always present at least one alternative
  with the trade-off, never a single "the answer is X" recommendation.
- **Some smells should not be fixed with a pattern.** Long methods often need
  Extract Method (a Fowler refactoring), not a GoF pattern. Read
  [references/fowler-refactorings.md](references/fowler-refactorings.md) to
  recognize when a basic refactoring is sufficient.
- **A pattern is justified only when the change axis is real.** Recommending Strategy
  for an algorithm that has had one implementation for five years and no roadmap to
  add more is over-engineering. State this explicitly when applicable.
</rules>

## Step 4: Match patterns and Fowler refactorings

<instructions>

For each classified problem, consult [references/pattern-selection-guide.md](references/pattern-selection-guide.md)
to map smell → candidate pattern(s) → trade-offs. For deeper reasoning on a specific
pattern, read the relevant subsection of [references/design-patterns-intro.md](references/design-patterns-intro.md).

For each candidate pattern, produce:

- **Why this pattern** — the specific smell + change axis combination it addresses.
- **Why not the alternative** — the runner-up pattern and why it's a worse fit here.
- **Cost** — new classes/files introduced, indirection added, testing surface change.
- **Reversibility** — how hard it is to back out if the change axis turns out wrong.
</instructions>

<gotchas>

- **Singleton is rarely the right answer.** It is almost always a global variable in
  disguise. Recommend it only when there is a hardware/resource constraint that
  literally permits one instance.
- **Visitor pays off only with stable element hierarchies and many operations.** If the
  element classes change frequently, Visitor amplifies churn.
- **Decorator vs. Strategy vs. Chain of Responsibility look similar.** Decorator
  augments behavior, Strategy swaps algorithms, Chain of Responsibility passes a
  request along until handled. The discriminator is **what changes**: behavior layers,
  algorithm choice, or handler selection.
- **Abstract Factory locks the product family at the abstract interface.** Adding a new
  product type to the family forces edits to every concrete factory — confirm the user
  accepts this trade before recommending.
</gotchas>

## Step 5: Produce output (mode-specific)

<instructions>

Read [assets/output-templates.md](assets/output-templates.md) and use the template
matching the mode chosen in Step 1.1.

- **`analyze`** → produce an analysis report inline in chat. No files modified.
- **`plan`** → write a refactor plan document to `spec/refactor-<short-name>.md` (or
  `plans/` if the project convention differs). The plan must follow the spec template
  the user has in their environment if one exists; otherwise use the template in
  `assets/output-templates.md`.
- **`apply`** → produce the plan first, get explicit user confirmation
  ("apply" / "yes, proceed"), then make file edits using 'replace_string_in_file' or
  'multi_replace_string_in_file'. Never apply without confirmation. After applying,
  run available tests/linters and report results.
</instructions>

<checkpoint>

For `plan` and `apply` modes, pause and explicitly ask:

- "Here is the plan. Does this match the change axes you described?"
- "Are there constraints I missed?"
- "For `apply` mode: confirm to proceed with file edits."

Only proceed past this checkpoint when the user confirms.
</checkpoint>

## Step 6: Validate

<instructions>

After producing output:

- For `analyze` / `plan`: confirm with the user that the recommendation addresses the
  motivation from Step 1.2 and the acceptance criteria from Step 1.7.
- For `apply`: run available test/lint commands ('run_in_terminal', requesting
  permission) and report the diff summary plus any test failures. If tests fail,
  do not declare the refactor complete — diagnose and fix or roll back.
</instructions>

<rules>

The workflow is complete when:

- [ ] The user's stated motivation (Step 1.2) is addressed by at least one
  recommendation, with evidence cited.
- [ ] Each recommendation names a concrete pattern or Fowler refactoring, not a vague
  "improve modularity."
- [ ] Trade-offs are documented (alternative considered, cost, reversibility).
- [ ] For `apply` mode: tests/lint pass, or failures are explicitly attributed and
  the user has decided whether to proceed or revert.
</rules>

---

## Reference routing

Load on demand. Do not pre-load — these files are large.

| File | Load when |
| --- | --- |
| [references/design-problem-categories.md](references/design-problem-categories.md) | Step 3 — classifying a smell into Creational/Structural/Behavioral |
| [references/design-patterns-intro.md](references/design-patterns-intro.md) | Step 4 — need deep prose explanation of a specific GoF pattern's intent |
| [references/code-smells.md](references/code-smells.md) | Step 2/3 — recognizing Fowler-style smells (god class, feature envy, etc.) |
| [references/solid-violations.md](references/solid-violations.md) | Step 3 — diagnosing SRP/OCP/LSP/ISP/DIP violations and the patterns that fix them |
| [references/fowler-refactorings.md](references/fowler-refactorings.md) | Step 4 — when the right answer is Extract Method / Move Method / etc., not a GoF pattern |
| [references/pattern-selection-guide.md](references/pattern-selection-guide.md) | Step 4 — smell → candidate pattern routing table with trade-offs |
| [references/refactoring-guru-links.md](references/refactoring-guru-links.md) | When the user wants the canonical refactoring.guru URL for a pattern |
| [references/refactoring-guru/](references/refactoring-guru/) | When deep, per-pattern refactoring.guru content has been mirrored locally by the quick-research agent (future) |
| [assets/output-templates.md](assets/output-templates.md) | Step 5 — formatting the analysis report, refactor plan, or apply summary |
