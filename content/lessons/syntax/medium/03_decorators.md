---
title: Decorators
track: syntax
difficulty: medium
tags: decorator
exercise: content/problems/syntax/medium/09_decorator_shout.py
---

# Decorators

## Overview

A decorator wraps a function (or class) to add behavior without editing its body. Syntax `@decorator` above `def` is sugar for `func = decorator(func)` at **definition time**.

**Why use decorators?** They separate cross-cutting concerns — logging, timing, validation, caching — from business logic. The wrapped function stays focused on what it does; the decorator handles the boilerplate around every call.

Real projects use decorators constantly: web frameworks use them for routes and auth; `functools.lru_cache` speeds up expensive functions; `@property` turns methods into attributes. Learning the pattern unlocks a lot of Python code.

## What happens at definition time

```python
@shout
def greet(name):
    return f'hello {name}'
```

Python executes this in order:

1. Define the function object `greet`
2. Pass it to `shout(greet)`
3. Bind the return value back to the name `greet`

After decoration, calling `greet('ada')` actually calls the inner `wrapper`.

**Critical insight:** Decoration runs **once** when Python reads the `def`, not each time you call the function. The wrapper is installed permanently (until you reassign `greet`).

## Minimal decorator

```python
import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@shout
def greet(name):
    return f'hello {name}'
```

**Concrete output:**

```python
greet('ada')   # returns 'HELLO ADA'
greet(42)      # returns 42 (not a string, left unchanged)
```

**Why `*args, **kwargs`?** The wrapper must accept any arguments the original function accepts, or decoration breaks for functions with different signatures.

**Why return `wrapper` from `shout`?** The decorator is a function that takes `func` and returns a **new callable** that replaces it. Forgetting `return wrapper` means `greet` becomes `None` and every call crashes.

## Why functools.wraps matters

Without `@functools.wraps(func)`:

```python
greet.__name__   # 'wrapper'  (misleading in stack traces)
greet.__doc__    # None       (docstring lost)
```

With `@functools.wraps(func)`:

```python
greet.__name__   # 'greet'
greet.__doc__    # original docstring preserved
```

**Why does this matter?** Debuggers, loggers, and `help(greet)` rely on `__name__` and `__doc__`. Losing them makes production issues harder to trace.

## Worked example: timing decorator

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'{func.__name__} took {elapsed:.4f}s')
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b
```

**Output when called:**

```python
slow_add(2, 3)  # prints 'slow_add took 0.1001s', returns 5
```

The original function's return value passes through unchanged — the decorator only adds side effects around the call.

**Why `time.perf_counter()`?** It is monotonic and high resolution — better for measuring short intervals than `time.time()`.

## Worked example: logging arguments

```python
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__} with {args=} {kwargs=}')
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, b=3)
# calling add with args=(2,) kwargs={'b': 3}
# returns 5
```

**Why log before `func(...)`?** You capture inputs even if the inner function raises an exception — useful when debugging failures.

## Decorators with arguments

When the decorator itself needs configuration, add a factory layer:

```python
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def ping():
    print('ping')
```

**What `@repeat(3)` expands to:**

1. `repeat(3)` returns the `decorator` function
2. `decorator(ping)` returns `wrapper`
3. `ping` now points to `wrapper`

Calling `ping()` prints `'ping'` three times.

Three levels: **factory** → **decorator** → **wrapper**.

**Why three levels?** `@repeat(3)` must call `repeat(3)` first to get the actual decorator. Without the factory, you could not pass `n` at decoration time.

Retry on failure (simplified):

```python
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
            raise last_exc
        return wrapper
    return decorator
```

## Common built-ins

- `@property` — expose a method as a read-only attribute
- `@staticmethod` / `@classmethod` — alternate binding for class methods
- `@lru_cache` — memoization (cache function results by arguments)
- `@dataclass` — auto-generate `__init__`, `__repr__`, etc.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)  # fast — intermediate results cached
```

`@property` example — computed attribute:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(2)
c.area  # 12.56636 — called like an attribute, not c.area()
```

**Why `@property`?** It keeps a clean public API (`obj.area`) while allowing validation or computation behind the scenes.

## Stacking decorators

```python
@a
@b
def f():
    pass
```

Equivalent to `f = a(b(f))` — **bottom decorator applied first**.

**Why order matters?** If `@timer` is outside `@cache`, you time cache hits too. If `@cache` is outside `@timer`, you only time the first uncached call.

Concrete stacking trace:

```python
@timer      # applied second: timer(wrapper_from_cache)
@lru_cache  # applied first: cache(f)
def work(n):
    return n * n
```

First call: cache miss → `work` runs → result cached → timer prints.
Second call with same `n`: cache hit → `work` body skipped → timer still runs.

## Common pitfalls

- Forgetting to `return wrapper` from the decorator (silently returns `None`)
- Expecting decoration at call time — it runs once at import/definition
- Stacking order: `@a @b def f` → `f = a(b(f))` (bottom decorator applied first)
- Forgetting `@functools.wraps` and losing metadata
- Decorating instance methods without understanding `self` is just the first arg

## Practice

Write a decorator that uppercases string return values.

```python
@shout
def greet(name):
    return f'hello {name}'

greet('world')  # 'HELLO WORLD'
```

## Summary

Decorators = higher-order functions for cross-cutting concerns: logging, timing, auth, caching, validation. They run at definition time, wrap the original callable, and should always use `@functools.wraps` to preserve introspection.
