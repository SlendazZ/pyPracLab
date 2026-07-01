---
title: Exceptions and Context Managers
track: syntax
difficulty: easy
tags: exceptions, with
exercise: content/problems/syntax/medium/22_context_manager_timer.py
---

# Exceptions and Context Managers

## Overview

Python uses exceptions for error flow. `try/except` handles expected failures; `with` guarantees cleanup via context managers (files, locks, timers).

**Why exceptions instead of error codes?** Error codes force every caller to check return values. Exceptions separate happy-path logic from error handling and automatically propagate up the call stack until something catches them.

Well-written Python rarely checks "did this fail?" after every line. Instead, you handle predictable failures at boundaries (user input, files, network) and let unexpected bugs surface with a clear traceback.

## try / except / else / finally

Parse JSON safely:

```python
import json

text = '{"name": "ada"}'
try:
    data = json.loads(text)
except json.JSONDecodeError as exc:
    print(f'invalid json: {exc}')
    data = None
else:
    print(f'parsed: {data}')   # runs only if no exception
finally:
    print('done parsing')      # always runs
```

**Output with valid JSON:**

```
parsed: {'name': 'ada'}
done parsing
```

**Output with invalid JSON `'not json'`:**

```
invalid json: Expecting value: line 1 column 1 (char 0)
done parsing
```

**Why four blocks?** Each has a distinct role:

- `try` — code that might fail
- `except` — handle a specific failure
- `else` — runs only on success (keeps `try` block small)
- `finally` — cleanup that must run regardless

Convert user input to int:

```python
raw = '42'
try:
    value = int(raw)
except ValueError:
    print('not a number')
    value = None
```

**Input `'42'` →** `value == 42`. **Input `'abc'` →** prints message, `value is None`.

## Raising exceptions

Validate input and fail fast:

```python
def set_age(age):
    if age < 0:
        raise ValueError('age must be non-negative')
    return age
```

```python
set_age(25)   # 25
set_age(-1)   # ValueError: age must be non-negative
```

Re-raise after logging:

```python
try:
    risky_operation()
except IOError as exc:
    log.error('disk error: %s', exc)
    raise   # propagate to caller after recording
```

**Why specific types like `ValueError`?** Callers can catch exactly what they expect. A bare `except:` catches everything — including `KeyboardInterrupt` and bugs you did not intend to hide.

Chain exceptions with context:

```python
try:
    parse(data)
except ParseError as exc:
    raise ValueError('bad user payload') from exc
```

**Why `from exc`?** The traceback shows both the original cause and your higher-level message — invaluable when debugging layered systems.

## EAFP vs LBYL

**EAFP** (Easier to Ask Forgiveness than Permission) — try, then handle:

```python
try:
    value = config['timeout']
except KeyError:
    value = 30  # default
```

**LBYL** (Look Before You Leap) — check first:

```python
if 'timeout' in config:
    value = config['timeout']
else:
    value = 30
```

Convert with EAFP when failure is rare:

```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
```

**Why EAFP is Pythonic?** It avoids race conditions in concurrent code and keeps the happy path unindented. Use LBYL when the check is cheap and the exception path is common.

## Context managers

Files must be closed even when reads fail:

```python
with open('data.txt') as f:
    content = f.read()
# file closed automatically, even if read() raised an error
```

**Why `with`?** Without it you need `try/finally` around every `open()`:

```python
f = open('data.txt')
try:
    content = f.read()
finally:
    f.close()
```

The context manager protocol (`__enter__` / `__exit__`) handles that boilerplate.

Multiple resources in one statement:

```python
with open('in.txt') as src, open('out.txt', 'w') as dst:
    dst.write(src.read())
# both files closed when block ends
```

## Worked example: timer context manager

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()
    yield                    # body of `with` block runs here
    elapsed = time.perf_counter() - start
    print(f'{label}: {elapsed:.4f}s')
```

**Usage:**

```python
with timer('sort'):
    sorted(range(100000, 0, -1))
# prints something like: sort: 0.0234s
```

**How it works:**

1. Code before `yield` runs on entry (`__enter__`)
2. Your `with` block body executes at `yield`
3. Code after `yield` runs on exit (`__exit__`), even if the block raised

If the block raises, the exception propagates after the cleanup code unless you suppress it in `__exit__`.

## Class-based context manager

```python
class Timer:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f'{self.label}: {elapsed:.4f}s')
        return False  # do not suppress exceptions
```

**Usage:**

```python
with Timer('work') as t:
    do_something()
# work: 0.0012s
```

**Why two styles?** `@contextmanager` is concise for simple setup/teardown. A class is clearer when you need state, multiple methods, or reusable instances.

## Worked example: suppressing known errors

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('temp.cache')
# no crash if file already gone
```

**Why `suppress`?** Cleaner than an empty `except` block when you genuinely expect and ignore a specific failure.

## Common pitfalls

- Swallowing exceptions with `pass` — at least log what went wrong
- Catching `Exception` too broadly and hiding bugs
- `return` in `finally` overrides other returns (avoid returning from `finally`)
- Catching the wrong type — `except KeyError` will not catch `ValueError`
- Opening files without `with` and forgetting `close()` on error paths

```python
# Too broad — hides bugs
try:
    process()
except Exception:
    pass

# Better — catch what you expect
try:
    process()
except (ValueError, KeyError) as exc:
    log.warning('expected issue: %s', exc)
```

## Practice

Build a timer context manager that prints elapsed seconds.

```python
with timer('work'):
    do_something()
# work: 0.0012s
```

## Summary

Handle errors at boundaries with specific exception types; use `with` for resource lifecycle (files, locks, connections, timers); let unexpected bugs propagate with clear stack traces rather than silencing them.
