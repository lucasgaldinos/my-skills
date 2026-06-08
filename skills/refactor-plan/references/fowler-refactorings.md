# Fowler Refactorings — When *Not* to Reach for a GoF Pattern

<context>

Many real-world code-quality problems are solved by basic mechanical refactorings, not
by adopting a design pattern. Reaching for a GoF pattern when an Extract Method would
have sufficed is over-engineering — it adds indirection, classes, and cognitive load
without addressing the actual smell.

Use this file in Step 4 of the workflow as a **filter before pattern recommendation**.
If a Fowler refactoring fully resolves the smell, prefer it. Patterns are warranted
when the *change axis* (not just the local mess) justifies the structural cost.
</context>

<rules>

- A Fowler refactoring changes structure without changing observable behavior.
- A GoF pattern introduces a *new abstraction* — it changes how future code is
  written, not just how current code reads.
- The two are composable: most pattern adoptions are sequences of Fowler refactorings
  (Extract Method → Extract Class → Extract Interface → Strategy).
</rules>

## Composing methods

<rules>

- **Extract Method** — pull a fragment of code into a new method whose name explains
  intent. The single highest-leverage refactoring; resolves Long Method, kills
  comment-as-deodorant, prepares the code for further moves.
- **Inline Method** — when the method body is as clear as its name, fold it back. Use
  to reverse over-extraction.
- **Extract Variable** — name a sub-expression. Eliminates magic and makes diffs
  reviewable.
- **Inline Variable** — reverse of above; useful when the variable adds noise.
- **Replace Temp with Query** — turn a local computed-once temp into a method call.
  Enables further extraction.
- **Split Temp** — assign each computed value to its own variable when one temp is
  reused for multiple meanings.
- **Remove Assignments to Parameters** — never reassign a parameter; assign to a local.
- **Replace Method with Method Object** — when a method is too tangled for Extract
  Method to disentangle, promote it to a class. Often a precursor to **Command**.
</rules>

## Moving features between objects

<rules>

- **Move Method** — when a method is more interested in another class's data than its
  own, move it. Resolves Feature Envy.
- **Move Field** — relocate a field to the class that uses it most.
- **Extract Class** — split one class into two when responsibilities have diverged.
  Most direct fix for SRP violations.
- **Inline Class** — collapse a class that no longer earns its keep. Counter to
  Speculative Generality.
- **Hide Delegate** — replace `a.getB().getC()` with `a.getC()`. Resolves Message
  Chains without introducing a Facade unless the delegation is broad.
- **Remove Middle Man** — when too much was hidden, expose the delegate directly.
- **Introduce Foreign Method / Local Extension** — add behavior to a class you don't
  own. The local extension form is essentially **Adapter** or **Decorator** for
  external types.
</rules>

## Organizing data

<rules>

- **Replace Data Value with Object** — promote a primitive (string, int) to a class
  when it acquires behavior. Resolves Primitive Obsession.
- **Replace Type Code with Class / Subclass / State** — three-step ladder for stringly-
  typed enums. The "with State" terminus is the **State** GoF pattern.
- **Encapsulate Field** — replace public field with accessors when behavior must
  attach.
- **Introduce Parameter Object** — bundle a recurring parameter clump into a class.
  Resolves Data Clumps and Long Parameter List.
- **Replace Array with Object** — when array positions encode meaning (`row[0]` is
  always name), make it a class.
</rules>

## Simplifying conditional expressions

<rules>

- **Decompose Conditional** — extract the condition, the then-branch, and the
  else-branch into named methods.
- **Consolidate Conditional Expression** — collapse multiple checks with the same
  result into one.
- **Replace Nested Conditional with Guard Clauses** — early return on edge cases;
  flattens cyclomatic complexity.
- **Replace Conditional with Polymorphism** — the bridge from Fowler-land to GoF-land.
  When you reach this refactoring, the next step is usually **Strategy**, **State**,
  or **Visitor**, depending on whether the variation is in algorithm, behavior-by-
  state, or operation-over-hierarchy.
- **Introduce Null Object** — replace null checks with a no-op implementation. A
  light structural pattern in its own right.
</rules>

## Making method calls simpler

<rules>

- **Rename Method / Variable / Parameter** — names that lie are technical debt.
- **Add / Remove Parameter** — adjust signatures when callers' needs change.
- **Separate Query from Modifier** — methods either return a value OR mutate state,
  not both. Critical for testability.
- **Replace Parameter with Method Call** — when the caller can compute the parameter,
  let the callee compute it instead.
- **Preserve Whole Object** — pass the object, not five of its fields.
- **Replace Constructor with Factory Method** — the doorway to **Factory Method**
  pattern. Use when construction depends on conditions or returns subtypes.
</rules>

## Dealing with generalization

<rules>

- **Pull Up / Push Down Method or Field** — move members up/down the inheritance
  hierarchy as needed.
- **Extract Superclass / Subclass / Interface** — pull commonality up into a new
  abstraction. Extract Interface is the Fowler equivalent of programming-to-an-
  interface; it precedes most pattern adoptions.
- **Form Template Method** — when two methods share a sequence with varying steps,
  pull the sequence up. This *is* the **Template Method** pattern.
- **Replace Inheritance with Delegation** — when subclass relationships violate LSP
  or constrain composition. The doorway to **Strategy**, **Bridge**, **Composite**,
  or **Decorator**.
- **Replace Delegation with Inheritance** — reverse, used rarely; valid when a
  delegating wrapper exists solely to expose the delegate's full interface.
</rules>

## Decision rule — refactoring vs. pattern

<rules>

| If the smell is... | Try Fowler first | Reach for pattern when |
| --- | --- | --- |
| Method too long | Extract Method | Method represents a reified action with undo/queue (→ Command) |
| Class too large, single change axis | Extract Class | Multiple change axes ↔ Strategy/State/Observer |
| Switch-on-type, single occurrence | Replace Conditional with Polymorphism | Multiple sites switch on the same axis (→ Strategy/State/Visitor) |
| Long parameter list | Introduce Parameter Object | Construction is multi-step / conditional (→ Builder) |
| Primitive value with behavior | Replace Data Value with Object | Type code drives behavior across the system (→ State) |
| Two classes with mismatched API, both yours | Move Method, Rename | One is external/legacy/sealed (→ Adapter) |
| Subclass refuses parent contract | Replace Inheritance with Delegation | Two orthogonal change axes (→ Bridge) |

</rules>

<gotchas>

- A pattern adopted prematurely is harder to reverse than a Fowler refactoring. Prefer
  the smaller move whenever it fully resolves the smell.
- "Form Template Method" and the **Template Method** pattern are the same thing
  expressed at different abstraction levels — the Fowler refactoring is the mechanic,
  the pattern is the catalog entry.
- "Replace Constructor with Factory Method" is similarly the mechanic for the
  **Factory Method** pattern.
- When a refactoring sequence ends at a pattern, document the *whole sequence* in the
  plan output, not just the final pattern — the intermediate states are independently
  shippable and reduce risk.
</gotchas>
