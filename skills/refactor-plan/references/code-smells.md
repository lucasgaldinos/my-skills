# Code Smells — Detection & Routing

<context>

Code smells are surface symptoms of deeper design problems. They are not bugs — code with
smells works correctly today but resists change tomorrow. The categories below follow
Fowler's *Refactoring* taxonomy, organized by the **structural problem they signal**, not
by syntactic appearance. Each entry lists how to detect it and which pattern or
refactoring family typically fixes it.

This file is the diagnostic catalog. It is consumed in Steps 2–3 of the workflow.
</context>

<rules>

- A single smell rarely points to a single fix. List candidates, not commandments.
- Smells are evidence, not verdicts. Always cite the file:line that triggered the
  detection in any output.
- Some smells are tolerable in isolation but compound when co-located. A long method
  *and* a god class *and* primitive obsession in one file is a stronger signal than
  any of them alone.
</rules>

## Bloaters

<rules>

- **Long Method** — a method longer than ~20 lines, doing more than one logical step.
  * Detect: line count, multiple comment-separated sections, nested control flow > 2.
  * Fix: Extract Method (Fowler), then if a coherent group of extracted methods emerges,
    Extract Class. Rarely a GoF pattern.

- **Large Class / God Class** — a class with too many responsibilities; often >500 lines
  or >20 public methods.
  * Detect: file size, method count, low cohesion (methods don't share fields).
  * Fix: Extract Class, Extract Subclass, Extract Interface. If the class drives a
    finite state machine, **State** pattern. If it dispatches by type, **Strategy** or
    **Visitor**.

- **Primitive Obsession** — using strings/ints/maps for concepts that deserve a class
  (money, phone, address, state codes).
  * Detect: stringly-typed parameters, magic numbers, repeated validation.
  * Fix: Replace Data Value with Object, Replace Type Code with Class/Subclass/State.

- **Long Parameter List** — more than ~3–4 parameters, especially when several change
  together.
  * Detect: parameter count, parameters that are always passed together.
  * Fix: Introduce Parameter Object, **Builder** pattern (when assembly is complex).

- **Data Clumps** — the same set of variables appearing together in multiple places.
  * Detect: same parameter list across N functions, same field group across N classes.
  * Fix: Extract Class, Introduce Parameter Object.
</rules>

## Object-Orientation Abusers

<rules>

- **Switch Statements / Long Type-Code Conditionals** — `switch (type)` or chained
  `if (x.kind == "A") ... else if (x.kind == "B")`.
  * Detect: regex `\b(switch|case)\b` or repeated `instanceof` / `isinstance` /
    `typeof` chains.
  * Fix: Replace Conditional with Polymorphism, then **Strategy**, **State**, or
    **Visitor** depending on what varies (algorithm, behavior-by-state, or operations
    over a stable hierarchy).

- **Temporary Field** — a field used only in some scenarios; null/empty otherwise.
  * Detect: field guarded by null checks; comments like "only set when X".
  * Fix: Extract Class for the temporary state. Sometimes **State** pattern.

- **Refused Bequest** — subclass that doesn't use most of what it inherits, or
  overrides parent methods to no-op.
  * Detect: empty overrides, methods that throw `NotSupportedException`.
  * Fix: Replace Inheritance with Delegation; reconsider hierarchy. Often signals
    **Bridge** is the right shape.

- **Alternative Classes with Different Interfaces** — classes that do similar things
  but expose mismatched APIs.
  * Detect: parallel method names with different signatures across two classes.
  * Fix: Rename Method, Move Method, Extract Superclass. If one is legacy/external,
    **Adapter** pattern.
</rules>

## Change Preventers

<rules>

- **Divergent Change** — one class changes in many different ways for many different
  reasons.
  * Detect: a class touched by many unrelated PRs/commits; many unrelated change axes
    in the same file.
  * Fix: Extract Class along the change axes. This is a **Single Responsibility
    Principle** violation.

- **Shotgun Surgery** — one change forces edits across many classes.
  * Detect: a feature delta that touches >5 files for what feels like one logical
    change.
  * Fix: Move Method/Field to consolidate. Often signals **Mediator**, **Facade**, or
    **Observer** is missing.

- **Parallel Inheritance Hierarchies** — every time you add a subclass to A you must
  add a subclass to B.
  * Detect: matching N×N class names like `XController` ↔ `XView`.
  * Fix: Move responsibilities so one hierarchy uses instances of the other. Often
    **Bridge** or **Visitor**.
</rules>

## Dispensables

<rules>

- **Comments (as deodorant)** — long explanatory comments compensating for unclear code.
  * Fix: Extract Method with a name that makes the comment redundant.

- **Duplicate Code** — same expression in two places (literal duplication or
  structural duplication where only types differ).
  * Fix: Extract Method/Class for literal duplication; **Template Method** for
    structural duplication where steps vary; **Strategy** when full algorithms vary.

- **Lazy Class** — a class that doesn't earn its keep.
  * Fix: Inline Class.

- **Speculative Generality** — abstractions, hooks, or parameters added for use cases
  that never materialized.
  * Fix: Collapse Hierarchy, Inline Class, Remove Parameter. **Resist the urge to add
    a pattern for a change axis that has not actually arrived.**

- **Dead Code** — unreachable or unused code paths.
  * Fix: Delete. No pattern needed.

- **Data Class** — a class with only fields and getters/setters, no behavior.
  * Detect: zero non-accessor methods.
  * Fix: Move behavior toward the data (Move Method). Sometimes legitimate (DTOs at
    boundaries).
</rules>

## Couplers

<rules>

- **Feature Envy** — a method more interested in another class's data than its own.
  * Detect: method that accesses another object's fields/methods more than its own.
  * Fix: Move Method to the envied class.

- **Inappropriate Intimacy** — two classes that know too much about each other's
  internals.
  * Detect: bidirectional field access, mutual private-state knowledge.
  * Fix: Move Method/Field, Extract Class, **Mediator** if many such relationships
    exist.

- **Message Chains** — `a.getB().getC().getD().doThing()`.
  * Detect: chained accessor calls > 2 levels.
  * Fix: Hide Delegate. Sometimes **Facade**.

- **Middle Man** — a class that delegates almost everything.
  * Detect: methods that are one-line passthroughs.
  * Fix: Remove Middle Man. (Distinct from intentional **Proxy** / **Decorator**, which
    add behavior around delegation.)
</rules>

## Smell → first-look pattern routing

<rules>

| Dominant smell | First-look pattern or refactoring |
| --- | --- |
| Long method, no other smells | Extract Method (no GoF needed) |
| Large class with one change axis | Extract Class |
| Large class with state-driven branches | **State** |
| Large class with algorithm choice | **Strategy** |
| Switch on type / instanceof chains | Replace Conditional with Polymorphism, then **Strategy** / **Visitor** |
| Telescoping constructor / long param list | Introduce Parameter Object → **Builder** if complex |
| Duplicate code, varying steps | **Template Method** |
| Duplicate code, varying full algorithms | **Strategy** |
| Shotgun surgery for one logical change | **Mediator** / **Facade** / **Observer** |
| Divergent change | Extract Class along change axis (SRP) |
| Refused bequest | Replace Inheritance with Delegation; consider **Bridge** |
| Alternative classes with mismatched API | Rename/Move; **Adapter** if external/legacy |
| Inappropriate intimacy across many classes | **Mediator** |
| Message chains | Hide Delegate; **Facade** |
| Heavy object instantiated eagerly | **Proxy** (virtual) |
| Many similar objects exhausting memory | **Flyweight** |
| Tree of nested objects, uniform ops | **Composite** |
| Behavior must layer dynamically | **Decorator** |
| Sequential validation/processing handlers | **Chain of Responsibility** |
| Need undo/queue/log of actions | **Command** |
| One-to-many notification | **Observer** |
| Need state snapshot/restore | **Memento** |
| New ops over stable hierarchy | **Visitor** |

</rules>

<gotchas>

- Detection signals are hints, not proofs. Always confirm with a read of the actual
  code before recommending.
- A class >500 lines is not automatically a god class — generated code, exhaustive
  enums, and protocol definitions can legitimately be large.
- `switch` is not always wrong. State machines implemented via `switch` can be clearer
  than a State-pattern hierarchy when the number of states is small (~3) and stable.
- Speculative-generality smells become "tech debt" if a pattern was applied for a
  change axis that never arrived. Recommending the **removal** of an unused pattern
  is a valid output of this skill.
</gotchas>
