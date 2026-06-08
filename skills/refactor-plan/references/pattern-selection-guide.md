# Pattern Selection Guide — Routing Table with Trade-offs

<context>

This is the master routing table consumed in Step 4 of the workflow. For each candidate
pattern it lists: the discriminating question, the cost, the runner-up alternative, and
the failure mode if the pattern is misapplied.

Use this file to *justify* a pattern recommendation, not just to pick one. Every entry
in the final analysis/plan must cite both the chosen pattern and the runner-up that was
considered and rejected, with the reason.
</context>

<rules>

- A recommendation without a runner-up is suspect. The discriminator between two
  similar patterns is what proves the choice was made deliberately.
- Cost includes new files, new indirection, and new test surface — not just code lines.
- "Failure mode" describes what goes wrong when the pattern is applied to the wrong
  problem. This is the most useful debugging information for a reviewer.
</rules>

## Creational

<rules>

| Pattern | Use when | Don't use when | Runner-up | Cost | Failure mode if misapplied |
| --- | --- | --- | --- | --- | --- |
| **Factory Method** | One product family, varying concrete types selected at runtime by subclass | The product type is stable; or full families vary together | Plain function returning a subtype | One parallel hierarchy of creators | Class explosion when product variants are tiny |
| **Abstract Factory** | Multiple related products must vary together as a family (ecosystem switch) | Only one product type varies | Factory Method per type | Abstract interface + N concrete factories | Adding a new product type requires editing every factory |
| **Builder** | Object has many optional parts and assembly order matters | Constructor is short and parameters are mandatory | Named/keyword arguments; Parameter Object | Builder class + director (optional) | Premature builder for trivially-constructed objects adds noise |
| **Prototype** | Cloning is cheaper than constructing; or you must duplicate without knowing concrete type | Objects are immutable and cheap to construct | Copy constructor / serialization | Clone interface + deep-copy logic | Shared mutable state across "clones" if shallow copy is wrong |
| **Singleton** | Hardware/resource constraint literally permits one instance, AND no testability cost is acceptable | You "want global access" — that is a global variable smell | Dependency injection of a single instance | Static state, lazy init, thread-safety code | Global state breaks tests, hides dependencies, race conditions |

</rules>

## Structural

<rules>

| Pattern | Use when | Don't use when | Runner-up | Cost | Failure mode if misapplied |
| --- | --- | --- | --- | --- | --- |
| **Adapter** | An external/legacy/sealed class must satisfy a domain interface | Both classes are yours and refactorable | Move Method / Rename | One wrapper class per adaptation | Adapter chains hide root-cause API mismatch |
| **Bridge** | Two orthogonal axes vary (abstraction × implementation) | Only one axis varies | Plain inheritance / Strategy | Two parallel hierarchies | Bridge for a single-axis problem doubles class count for nothing |
| **Composite** | Domain is part-whole tree; client treats leaf and composite uniformly | Structure is flat or fixed-depth | Iterator over a list | Component interface + composite container | Composite over a non-recursive structure adds dead code |
| **Decorator** | Behavior must layer dynamically; many combinations needed | Only a handful of fixed combinations exist | Subclass per combination; Strategy | Decorator chain + decorator-aware client | Deep decorator stacks become unreadable; ordering becomes implicit contract |
| **Facade** | Subsystem is unwieldy; common usage is a stereotyped sequence | Subsystem is already small and well-named | Helper module / utility functions | One Facade class | Facade that grows past ~5 methods is itself a god class |
| **Flyweight** | Memory exhaustion from many similar objects with shareable intrinsic state | Object count is moderate; or state isn't separable | Caching / object pool | Intrinsic/extrinsic split + pool registry | Wrong intrinsic/extrinsic split causes shared-state bugs |
| **Proxy** (virtual) | Heavyweight resource should be lazy-loaded transparently | Eager construction is fine and predictable | Direct lazy field initialization | Proxy class implementing target interface | Proxy that always loads is worse than no proxy |
| **Proxy** (protection) | Access control must be enforced uniformly at the boundary | Access control belongs at a different layer | Decorator with auth check | Proxy + permission model | Auth scattered across proxies and elsewhere is worst-of-both |
| **Proxy** (caching) | Computation is repeated and pure | Inputs change frequently; cache invalidation is hard | Memoization decorator | Cache keying + invalidation policy | Stale cache bugs are the canonical proxy failure mode |

</rules>

## Behavioral

<rules>

| Pattern | Use when | Don't use when | Runner-up | Cost | Failure mode if misapplied |
| --- | --- | --- | --- | --- | --- |
| **Chain of Responsibility** | Sequential handlers, each may handle or forward; chain reconfigurable | Single handler always processes | Single function with branching | Handler interface + chain assembly | Hidden contract on handler order causes silent misroutes |
| **Command** | Need undo/redo, queueing, logging, or async dispatch of actions | Action is one-shot and disposable | Plain function call | Command class per action + invoker + receiver | Command for trivial actions inflates code without enabling undo |
| **Iterator** | Collection traversal must hide structure or support multiple concurrent traversals | Language already provides idiomatic iteration | Built-in iterator / generator | Iterator class | Custom iterator over a list reinvents `for` |
| **Mediator** | N×N coupling between components; coordination logic is complex | Components are loosely coupled already | Direct method calls; Observer | Mediator class as coordination hub | Mediator becomes god class if coordination logic grows unchecked |
| **Memento** | Need to snapshot/restore state without breaking encapsulation | State can be exposed safely; or snapshot is trivial | Serialization | Memento value class + caretaker | Memento that exposes internals defeats its purpose |
| **Observer** | Many subscribers, set varies at runtime, no return value needed | Few fixed listeners; or you need return values from listeners | Direct callbacks; pub/sub library | Subject + observer interface + registration | Observer with hidden ordering or re-entrancy is hard to debug |
| **State** | Object behavior depends on internal state; large `switch (state)` blocks exist | Few stable states with simple branching | `switch` / enum dispatch | State class per state + context delegation | State explosion if states aren't actually distinct |
| **Strategy** | Algorithm choice varies independently of context; runtime swap needed | One algorithm and no roadmap to add more | First-class function / lambda | Strategy interface + concrete strategies | Strategy with one impl is over-engineering |
| **Template Method** | Skeleton is fixed; specific steps vary by subclass | Variation is composable rather than step-wise | Strategy via composition | Abstract base + hook methods | Template Method with too many hooks blurs the skeleton |
| **Visitor** | Stable element hierarchy; many independent operations to add | Element types change often | Polymorphic methods on elements | Visitor interface + accept methods | Visitor over a churning hierarchy multiplies edits |

</rules>

## Confusion-pair discriminators

<rules>

| If torn between... | Ask | Choose left if... | Choose right if... |
| --- | --- | --- | --- |
| Strategy vs. Template Method | Where is variation expressed? | Composition / runtime swap | Inheritance / compile-time fixed |
| Strategy vs. State | What drives the swap? | External choice (config, request) | Internal state transition |
| Decorator vs. Strategy | Stacking or swapping? | Stacking layers around behavior | Replacing the algorithm |
| Decorator vs. Chain of Responsibility | Does each layer always run? | Yes — every wrapper executes | No — chain stops when handled |
| Adapter vs. Facade | One class or many? | Single mismatched interface | Whole subsystem to simplify |
| Adapter vs. Decorator | Same interface? | No — translates between interfaces | Yes — augments same interface |
| Factory Method vs. Abstract Factory | One product or family? | One product, varying concrete | Family of related products |
| Bridge vs. Strategy | Pre-existing hierarchy with two change axes? | Yes — split orthogonal axes | No — one axis with algorithm choice |
| Mediator vs. Observer | Centralized coordinator or decentralized broadcast? | Centralized with logic | Decentralized notifications |
| Memento vs. Command | Snapshot state or replay action? | Restore prior state | Undo by inverse action |
| Proxy vs. Decorator | Same interface, what's added? | Access/lifecycle control | Behavioral augmentation |
| Composite vs. Decorator | Tree structure or wrapping? | Recursive part-whole hierarchy | Single object with layers |

</rules>

<gotchas>

- The discriminator questions are the most frequent reviewer pushback. State the
  discriminator explicitly in any plan output.
- Many "wrong pattern" code reviews are not wrong-pattern at all — they are
  *premature pattern* (no real change axis yet) or *missing-Fowler-step* (a Fowler
  refactoring would have sufficed). Always check those two failure modes first.
- The trade-off matrix must be honest about cost. Recommendations that hide cost get
  rejected at implementation time and waste the planning effort.
</gotchas>
