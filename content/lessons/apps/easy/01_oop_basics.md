---
title: Classes and Application State
track: apps
difficulty: easy
tags: oop
exercise: content/problems/apps/easy/02_todo_list.py
---

# Classes and Application State

## Overview

A class bundles data (attributes) and behavior (methods) for one concept: a todo list, shopping cart, game board. Application logic becomes easier to test when state lives in well-named objects.

Without classes, a growing script accumulates loose variables and functions that pass the same dict everywhere. A class says: this data and these operations belong together. Callers interact through a small public API instead of reaching into raw lists and indexes.

If you can describe something as a noun with verbs — a cart that adds items, a list that completes tasks — it is probably a class candidate.

## Minimal class

Every instance method takes `self` as the first parameter — the object being operated on. `__init__` runs when you construct a new instance:

```python
class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task: str) -> None:
        self.items.append(task)

    def done(self, index: int) -> str:
        return self.items.pop(index)
```

Usage:

```python
todos = TodoList()
todos.add('buy milk')
todos.add('write tests')
finished = todos.done(0)   # removes and returns 'buy milk'
```

`self.items` is per-instance state. Two `TodoList` objects do not share the same list unless you deliberately wire them that way:

```python
work = TodoList()
home = TodoList()
work.add('deploy')
len(home.items)   # 0 — separate lists
```

## Worked example: a complete TodoList

A more realistic version validates input and exposes read-only views:

```python
class TodoList:
    def __init__(self):
        self._items: list[str] = []

    def add(self, task: str) -> None:
        task = task.strip()
        if not task:
            raise ValueError('task cannot be empty')
        self._items.append(task)

    def list(self) -> list[str]:
        return list(self._items)

    def complete(self, index: int) -> str:
        if index < 0 or index >= len(self._items):
            raise IndexError('no task at that index')
        return self._items.pop(index)

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f'TodoList({self._items!r})'
```

Step by step:
1. `_items` with a leading underscore signals internal storage (convention, not enforcement).
2. `add` strips whitespace and rejects empty strings.
3. `list` returns a copy so callers cannot mutate internal state directly.
4. `complete` bounds-checks before `pop`.
5. `__len__` enables `len(todos)`; `__repr__` helps debugging.

Quick test in the REPL:

```python
t = TodoList()
t.add('read chapter 3')
assert len(t) == 1
assert t.list() == ['read chapter 3']
t.complete(0)
assert len(t) == 0
```

Why return a copy from `list()`?

```python
t = TodoList()
t.add('task')
view = t.list()
view.clear()        # does NOT empty the TodoList
len(t)              # still 1
```

## Encapsulation convention

Python trusts the programmer — conventions over strict privacy:

- Public API: no leading underscore (`add`, `complete`)
- Internal helper or storage: `_validate()`, `_items`
- Name mangling: `__secret` (rare; avoid unless subclass interference is a real problem)

Callers should use public methods. If you need to change how tasks are stored (list → database), you change `_items` internals without breaking `add`/`complete`.

## When to use a class vs functions

| Use a class when…              | Use functions when…     |
|--------------------------------|-------------------------|
| State persists across calls    | One-off transform       |
| Multiple related operations    | Single pure computation |
| You need several instances     | No shared state         |

Example: `normalize_email(s)` is a function; `ShoppingCart` is a class because it accumulates items across many `add` calls.

Worked example: shopping cart sketch:

```python
class ShoppingCart:
    def __init__(self):
        self._lines: list[tuple[str, int]] = []

    def add(self, name: str, price_cents: int) -> None:
        self._lines.append((name, price_cents))

    def total_cents(self) -> int:
        return sum(price for _, price in self._lines)

cart = ShoppingCart()
cart.add('notebook', 499)
cart.add('pen', 199)
cart.total_cents()   # 698
```

## Dataclasses for data-heavy objects

When a class is mostly fields with little behavior, `@dataclass` removes boilerplate:

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    done: bool = False

task = Task('deploy')
task.done = True
```

Dataclasses auto-generate `__init__`, `__repr__`, and equality. Use a regular class when behavior dominates; use dataclass for structured records.

Combine dataclass records with a class that owns a collection:

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    done: bool = False

class TaskBoard:
    def __init__(self):
        self._tasks: list[Task] = []

    def add(self, title: str) -> None:
        self._tasks.append(Task(title))

    def pending(self) -> list[Task]:
        return [t for t in self._tasks if not t.done]
```

## Common pitfalls

- Mutable default args in `__init__` — use `None` and assign in body:

```python
def __init__(self, items=None):
    self.items = [] if items is None else list(items)
```

Wrong version `def __init__(self, items=[])` shares one list across all instances.

- God objects that know everything — split responsibilities (storage vs UI)
- Forgetting `self.` when assigning instance attributes
- Returning the internal list directly — callers can `.clear()` your state
- Putting I/O (print, input) inside domain classes — keep them testable

## Practice

Implement a TodoList with add, list, and complete operations.

## Summary

Classes model things your app manipulates over time. Keep them small; test methods in isolation. Use `__init__` for setup, underscore conventions for internals, and return copies when exposing mutable state.
