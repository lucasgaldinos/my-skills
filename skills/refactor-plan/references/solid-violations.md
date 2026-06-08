# SOLID Violations — Diagnosis & Pattern Routing

<context>

SOLID is the bridge between code smells (symptoms) and design patterns (treatments).
A SOLID violation is a structural diagnosis — it names *what is wrong with the design*,
which then constrains the set of patterns that can fix it. This file maps each
principle's violations to detection signals, the patterns that resolve them, and the
costs of those fixes.

Use this in Step 3 of the workflow when a smell from `code-smells.md` doesn't yet point
to a specific pattern.
</context>

## SRP — Single Responsibility Principle

<rules>

> A class should have one, and only one, reason to change.

- **Violation signal**: the same class is edited for unrelated reasons across commits
  (Divergent Change smell). Methods cluster into disjoint groups by which fields they
  touch (low cohesion).
- **Detection**: file change history shows multiple unrelated change axes; methods
  partition into groups with no overlapping field access.
- **Patterns/refactorings that fix it**:
  * **Extract Class** — pure refactoring, no GoF needed when responsibilities are
    fully separable.
  * **Strategy** — when one of the responsibilities is "select an algorithm".
  * **State** — when one of the responsibilities is "behavior dependent on internal
    mode/lifecycle".
  * **Observer** — when one of the responsibilities is "notify others of changes".
- **Cost**: more classes, more files. Justified only when change axes are real and
  observed, not speculative.
</rules>

## OCP — Open/Closed Principle

<rules>

> Software entities should be open for extension, but closed for modification.

- **Violation signal**: adding a new variant of something requires editing existing
  code (especially `switch` blocks or factory if-chains). Shotgun Surgery for what
  should be a localized addition.
- **Detection**: search for `switch`/`if isinstance`/`elif type ==` blocks where each
  arm handles a known type; count files touched per "add new type" PR.
- **Patterns that fix it**:
  * **Factory Method** / **Abstract Factory** — when the violation is in
    object creation.
  * **Strategy** — when the violation is in algorithm selection.
  * **State** — when the violation is in state-dependent behavior.
  * **Visitor** — when the violation is in adding new *operations* (rather than new
    types) over a stable hierarchy. Visitor inverts OCP: it is open for new operations
    but closed against new element types.
  * **Chain of Responsibility** — when adding a new variant means inserting a new
    handler in a sequence.
- **Cost**: indirection, more types. The trade-off is asymmetric — Visitor closes one
  axis to open another. Pick based on which axis actually changes.
</rules>

## LSP — Liskov Substitution Principle

<rules>

> Subtypes must be substitutable for their base types without altering correctness.

- **Violation signal**: subclasses override methods to throw "NotSupported" or no-op;
  preconditions strengthened in subclass; postconditions weakened in subclass; tests
  pass against base type but fail against subtype.
- **Detection**: empty overrides, exception-throwing overrides, callers that
  type-check before invoking ("if it's a Penguin, don't call fly()").
- **Patterns/refactorings that fix it**:
  * **Replace Inheritance with Delegation** — pure refactoring; the "subclass" was
    really a different concept.
  * **Bridge** — when the inheritance hierarchy was conflating two orthogonal axes.
  * **Composite** — when the "wrong subclass" was actually a container relationship.
- **Cost**: deeper indirection. The benefit is that callers no longer need to type-
  check, which removes a whole class of bugs.
</rules>

## ISP — Interface Segregation Principle

<rules>

> Clients should not be forced to depend on interfaces they do not use.

- **Violation signal**: an interface or abstract class with many methods, where each
  client only uses a subset; implementations stub out unused methods.
- **Detection**: count methods on an interface vs. methods actually called by each
  client; look for stub implementations.
- **Patterns/refactorings that fix it**:
  * **Extract Interface** — split fat interface into role-specific interfaces.
  * **Adapter** — when one big external interface must be exposed as several small
    role-specific interfaces.
  * **Facade** — when many small client-specific interfaces are needed but the
    underlying subsystem must remain unified.
- **Cost**: more interfaces. Mitigated by naming interfaces after the *role* the
  client plays, not after the implementation class.
</rules>

## DIP — Dependency Inversion Principle

<rules>

> Depend on abstractions, not concretions. High-level modules should not depend on
> low-level modules.

- **Violation signal**: high-level business logic imports concrete infrastructure
  (database driver, HTTP client, file system); tests are impossible without
  monkey-patching or heavy mocks.
- **Detection**: imports of concrete external libraries inside domain/business
  modules; difficulty writing unit tests without I/O.
- **Patterns/refactorings that fix it**:
  * **Strategy** — concrete dependencies become injected strategies.
  * **Adapter** — wrap external concretions behind domain-defined interfaces.
  * **Abstract Factory** — when the dependency is a *family* of related concretions.
  * **Bridge** — when the dependency is on a platform/protocol axis that varies
    independently of the abstraction.
- **Cost**: dependency-injection plumbing. Pays off whenever the concrete dependency
  is a candidate for replacement (test doubles, multi-cloud, multi-protocol).
</rules>

## Diagnostic table — violation → first-look pattern

<rules>

| Violation | First-look fix |
| ----------------------------------------- | ------------------------------------------- |
| SRP — multiple change axes in one class | Extract Class; **Strategy** / **State** if axes are algorithmic/stateful |
| OCP — `switch` on type for creation | **Factory Method** / **Abstract Factory** |
| OCP — `switch` on type for behavior | **Strategy** / **State** |
| OCP — adding new ops to stable hierarchy | **Visitor** |
| LSP — subclass throws or no-ops | Replace Inheritance with Delegation; **Bridge** |
| ISP — fat interface, partial implementers | Extract Interface; **Adapter** |
| DIP — domain imports infrastructure | Inject via interface; **Strategy** / **Adapter** / **Abstract Factory** |

</rules>

<gotchas>

- A single class can violate multiple principles simultaneously. Fix the dominant one
  first; secondary violations often dissolve.
- **Premature SOLID is over-engineering.** A class with one change axis today does not
  violate SRP just because it *could* have multiple tomorrow. Wait for the second
  reason to change before extracting.
- LSP is the most subtle violation — it often passes type-checking but fails behavior
  contracts. Property-based tests catch it better than example-based tests.
</gotchas>
