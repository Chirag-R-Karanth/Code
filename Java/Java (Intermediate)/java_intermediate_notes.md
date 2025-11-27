# Java Intermediate Notes

This document contains notes for intermediate Java topics.

## Object-Oriented Programming (OOP) Deep Dive

### `final` Keyword
- **`final` class:** Cannot be subclassed (e.g., `String`).
- **`final` method:** Cannot be overridden by subclasses.
- **`final` variable:** Can only be assigned once. For reference types, the reference itself is final, not the object it points to.

### Interfaces vs. Abstract Classes
| Feature        | Interface                                    | Abstract Class                               |
|----------------|----------------------------------------------|----------------------------------------------|
| Members        | Methods (implicitly public abstract), default, static, private methods, final static fields | Methods (abstract or concrete), fields       |
| Inheritance    | `implements` multiple interfaces             | `extends` one abstract class                 |
| Constructor    | No constructor                               | Can have constructors                        |
| State          | No instance state                            | Can have instance state                      |

## Collections Framework

### `List` Implementations
- **`ArrayList`:** Resizable array. Good for random access, poor for insertions/deletions in the middle.
- **`LinkedList`:** Doubly linked list. Good for insertions/deletions, poor for random access.

### `Set` Implementations
- **`HashSet`:** Uses a hash table for storage. Offers constant-time performance for basic operations (add, remove, contains). Unordered.
- **`LinkedHashSet`:** Maintains insertion order. Slightly slower than `HashSet`.
- **`TreeSet`:** Stores elements in a sorted order using a Red-Black tree. Offers `log(n)` time for basic operations.

### `Map` Implementations
- **`HashMap`:** Uses a hash table. Provides constant-time performance. Unordered.
- **`LinkedHashMap`:** Maintains insertion order or access order.
- **`TreeMap`:** Stores entries in a sorted order by key. Offers `log(n)` time.

### `Comparable` vs. `Comparator`
- **`Comparable`:** `java.lang.Comparable`. Defines a "natural ordering" for objects of a class. Implemented by the class itself (e.g., `String`, wrapper classes). `compareTo(Object o)`.
- **`Comparator`:** `java.util.Comparator`. Defines an "external ordering". Useful for sorting objects in different ways or when you can't modify the class. `compare(Object o1, Object o2)`.

## Generics

### Wildcard Types
- **`? extends T` (Upper Bounded Wildcard):** Represents an unknown type that is `T` or a subtype of `T`. You can `get` elements of type `T` from it, but generally cannot `add` to it (Producer Extends).
- **`? super T` (Lower Bounded Wildcard):** Represents an unknown type that is `T` or a supertype of `T`. You can `add` elements of type `T` to it, but generally cannot `get` elements of type `T` reliably (Consumer Super).

### Type Erasure
- Generics information is erased at compile time. At runtime, generic types become raw types (e.g., `List<String>` becomes `List`).
- This ensures backward compatibility with older Java versions.

## Exception Handling

### `try-with-resources`
- Automatically closes resources that implement `java.lang.AutoCloseable`.
- Syntax: `try (Resource res = new Resource()) { ... } catch (...) { ... }`

## Multithreading and Concurrency

### Synchronization
- **`synchronized` keyword:** Used for methods or blocks to protect shared resources. Only one thread can execute a synchronized method/block on a given object at a time.
- **`java.util.concurrent.locks.Lock` interface:** More flexible than `synchronized` blocks. Provides `lock()`, `unlock()`, `tryLock()`, etc. `ReentrantLock` is a common implementation.

### Concurrency Utilities (`java.util.concurrent`)
- **`ExecutorService`:** Manages a pool of threads. Submits `Runnable` or `Callable` tasks.
- **`Callable` vs. `Runnable`:** `Callable` can return a result and throw checked exceptions, `Runnable` cannot.
- **`Future`:** Represents the result of an asynchronous computation.

## Lambda Expressions and Stream API

### Functional Interfaces
- An interface with a single abstract method. Can be implemented using lambda expressions.
- Examples: `Runnable`, `Callable`, `Consumer`, `Supplier`, `Function`, `Predicate`.

### `Stream` Operations
- **Intermediate Operations:** Return another stream. Chained together (e.g., `filter()`, `map()`, `sorted()`).
- **Terminal Operations:** Produce a result or a side effect. Consume the stream (e.g., `forEach()`, `collect()`, `reduce()`, `count()`).

### `Optional` Class
- `java.util.Optional<T>`. Used to represent the presence or absence of a value.
- Helps to avoid `NullPointerException`s.
- Methods: `isPresent()`, `isEmpty()`, `get()`, `orElse()`, `orElseGet()`, `orElseThrow()`, `map()`, `flatMap()`.

## JVM Internals

### Memory Areas
- **Heap:** Stores objects and arrays. Garbage collected.
- **Stack:** Stores local variables and method call frames. Each thread has its own stack.
- **Method Area (Metaspace in Java 8+):** Stores class structures, method data, static variables.
- **PC Registers:** Stores the address of the next instruction to be executed for each thread.
- **Native Method Stacks:** For native methods.

## Design Patterns (Summary)

- **Creational:** Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.
- **Structural:** Deal with object composition, forming larger structures from smaller ones.
- **Behavioral:** Deal with communication between objects and assignment of responsibilities.
