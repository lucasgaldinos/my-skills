# desing problem categories

## intro

* **Creational Patterns**: These address problems concerning the process of object creation. They abstract the instantiation process, giving designers immense flexibility in determining what gets created, who creates it, how it gets created, and when. By abstracting object creation, these patterns solve the problem of hard-coding dependencies, ensuring that a system is written in terms of abstract interfaces rather than concrete implementations.
* **Structural Patterns**: These deal with problems related to the composition of classes or objects to form larger, more complex structures. They solve integration problems, such as adapting incompatible interfaces or making independently developed class libraries work together seamlessly without altering their existing code.
* **Behavioral Patterns**: These characterize the ways in which classes or objects interact and distribute responsibility. They address problems regarding algorithms and complex control flows, allowing designers to shift their focus away from flow of control and instead concentrate on the interconnections and communication between objects.

Within the larger context of the "Introduction," these categories are presented to help developers systematically solve a variety of day-to-day **core design problems**:

* **Finding Appropriate Objects**: Decomposing a system into objects is notoriously difficult because factors like encapsulation, dependency, and performance often conflict. Design patterns help identify less-obvious abstractions that do not naturally occur in the real world, such as representing a specific process, algorithm, or state as an independent object to increase flexibility.
* **Determining Object Granularity**: Designers face problems regarding the size and number of objects. Patterns provide solutions that range from representing massive, complete subsystems as single objects to efficiently supporting huge numbers of fine-grained objects.
* **Specifying Object Interfaces and Implementations**: Patterns help define exactly what data should be sent across an interface and specify the constraints or relationships between different interfaces. Crucially, they solve implementation dependencies by enforcing a core principle of reusable design: **program to an interface, not an implementation**.
* **Designing for Change**: Unanticipated changes invariably cause expensive redesigns. The Introduction outlines specific problem categories that force redesign—such as tight coupling, algorithmic dependencies, platform dependence, and the limitations of extending functionality via subclassing. Patterns provide targeted solutions, such as object composition and delegation, to ensure the system remains robust in the face of these changes.

By categorizing design problems and their proven solutions, the "Introduction" establishes a framework that helps designers evaluate **what they want to be able to change in a system without forcing a complete redesign**. This cataloging of experience ensures that developers do not have to solve every complex architectural problem from first principles.

## organizing by scope

In the larger context of organizing the design pattern catalog, classification is necessary because patterns vary widely in their granularity and level of abstraction. To make the catalog easier to navigate and learn, the authors organize patterns using two primary criteria: *purpose* (what a pattern does) and *scope*.

Organizing patterns **by scope** specifies whether a design pattern applies primarily to **classes** or to **objects**:

* **Class Patterns:** These patterns deal with the relationships between classes and their subclasses. Because these relationships are established through inheritance, they are **static and fixed at compile-time**. While almost all design patterns use inheritance to some degree, only those that explicitly focus on class relationships are categorized under the class scope.
* **Object Patterns:** These patterns deal with the relationships between objects. Because these relationships rely on object composition rather than strict inheritance, they are **more dynamic and can be changed at run-time**. The sources note that the vast majority of design patterns fall into the object scope.

To create a complete organizational matrix, the concept of scope intersects directly with a pattern's purpose:

* **Creational Patterns:** Class-scoped creational patterns defer part of the object creation process to subclasses, whereas object-scoped creational patterns defer it to another object entirely.
* **Structural Patterns:** Class-scoped structural patterns use inheritance to compose classes, while object-scoped structural patterns describe ways to assemble objects into larger structures.
* **Behavioral Patterns:** Class-scoped behavioral patterns use inheritance to describe algorithms and control flow, whereas object-scoped behavioral patterns describe how a group of objects cooperate to perform a task that no single object could carry out on its own.
