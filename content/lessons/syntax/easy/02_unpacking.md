---
title: Iterable Unpacking
track: syntax
difficulty: easy
tags: unpacking
exercise: content/problems/syntax/easy/05_unpacking_head_tail.py
---

# Iterable Unpacking

## Overview

Python can assign multiple names from any iterable in one statement. The `*` operator collects "the rest" into a list. This shows up in function calls, loops, and data splitting constantly.

**Why learn unpacking?** It replaces index gymnastics (`items[0]`, `items[1:]`) with readable names (`first`, `rest`). Code that splits boundaries — first/last, head/tail, config merges — becomes shorter and less error-prone.

Unpacking is one of Python's most practical everyday features. Once you see `head, *tail = data`, slicing with `[0]` and `[1:]` starts to feel clumsy.

## Basic unpacking

Assign three values from a list:

```python
first, second, third = [1, 2, 3]
# first == 1, second == 2, third == 3
```

Unpack a tuple returned from a function:

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])
# lo == 1, hi == 5
```

**Why tuples and unpacking go together?** Functions often return multiple values as a tuple. Unpacking gives each value a meaningful name in one line.

Swap two variables without a temporary:

```python
a, b = 10, 20
a, b = b, a
# a == 20, b == 10
```

**Why does swap work?** Python evaluates the right-hand side into a tuple first `(b, a)`, then unpacks it into `(a, b)`. No temp variable needed.

Unpack any iterable, not just lists:

```python
x, y, z = range(3)
# x == 0, y == 1, z == 2
```

Ignore values you do not need with `_`:

```python
name, _, city = ('Ada', 36, 'London')
# name == 'Ada', city == 'London' (age discarded)
```

**Why `_`?** It signals "I must accept this position but I do not care about the value." Readers know the middle slot is intentionally unused.

## Star unpacking

Grab the first element and collect everything else:

```python
head, *tail = [1, 2, 3, 4]
# head == 1, tail == [2, 3, 4]
```

Split into first, middle, and last:

```python
seq = [10, 20, 30, 40, 50]
first, *middle, last = seq
# first == 10, middle == [20, 30, 40], last == 50
```

Collect everything except the final element:

```python
items = ['a', 'b', 'c']
*start, end = items
# start == ['a', 'b'], end == 'c'
```

Exactly one `*` is allowed on the left side of assignment.

**Why is `*rest` always a list?** Even when it captures a single element, Python uses a list so you can always iterate or slice `rest` predictably.

Take the first two and bundle the rest:

```python
first, second, *others = [1, 2, 3, 4, 5]
# first == 1, second == 2, others == [3, 4, 5]
```

## Worked example: head and tail

**Input:** `data = [42, 7, 13, 99]`

**Step 1:** unpack with star

```python
head, *tail = data
```

**Output:** `head == 42`, `tail == [7, 13, 99]`

**Use case:** recursive algorithms often process the first element, then recurse on the tail:

```python
def sum_list(nums):
    if not nums:
        return 0
    head, *tail = nums
    return head + sum_list(tail)

sum_list([1, 2, 3])  # 6
```

**Edge case — single element:**

```python
head, *tail = [99]
# head == 99, tail == []  (empty list, not an error)
```

**Edge case — empty list:** raises `ValueError` because there is no value for `head`.

## Worked example: splitting a CSV row

**Input:** `row = ['2024-01-15', 'ada', 'admin', 'eng']`

**Goal:** date, username, and everything else as roles.

```python
date, user, *roles = row
# date == '2024-01-15'
# user == 'ada'
# roles == ['admin', 'eng']
```

**Why better than indexing?** If more role columns appear later, `roles` grows automatically. You do not need to change `row[3:]` magic numbers.

## In function calls

Splat a list into positional arguments:

```python
def greet(first, last):
    return f'Hello, {first} {last}'

parts = ['Ada', 'Lovelace']
greet(*parts)  # same as greet('Ada', 'Lovelace')
# returns 'Hello, Ada Lovelace'
```

Pass extra values from one list into another call:

```python
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
add(*values)  # 6
```

Collect extra positional and keyword arguments:

```python
def log(msg, *args, **kwargs):
    print(msg, args, kwargs)

log('done', 1, 2, key='value')
# prints: done (1, 2) {'key': 'value'}
```

Forward arguments to another function:

```python
def wrapper(*args, **kwargs):
    return real_function(*args, **kwargs)
```

**Why `*args` and `**kwargs`?** They let one function accept any signature and pass it through — essential for decorators and wrappers.

Unpack a dict into keyword arguments:

```python
def connect(host, port, timeout=30):
    return f'{host}:{port} timeout={timeout}'

opts = {'host': 'localhost', 'port': 8080, 'timeout': 5}
connect(**opts)
# 'localhost:8080 timeout=5'
```

## In loops

Unpack each row as a key plus remaining values:

```python
records = [('user', 'ada', 'admin'), ('user', 'bob', 'guest')]
for kind, *fields in records:
    print(kind, fields)
# user ['ada', 'admin']
# user ['bob', 'guest']
```

Iterate with index and value using `enumerate`:

```python
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(i, color)
# 0 red
# 1 green
# 2 blue
```

Zip two lists into pairs:

```python
names = ['ada', 'bob']
scores = [95, 87]
for name, score in zip(names, scores):
    print(name, score)
# ada 95
# bob 87
```

**Why unpack in the loop header?** It keeps the loop body focused on logic instead of indexing `row[0]`, `row[1]`.

## Extended iterable unpacking (Python 3.5+)

Merge lists without mutating originals:

```python
a = [1, 2]
b = [3, 4]
merged = [0, *a, *b, 5]
# merged == [0, 1, 2, 3, 4, 5]
```

Prepend and append in one expression:

```python
defaults = ['http', 'localhost']
path = [*defaults, 'api', 'v1']
# ['http', 'localhost', 'api', 'v1']
```

Merge dictionaries (later keys win):

```python
defaults = {'host': 'localhost', 'port': 8080, 'debug': False}
overrides = {'port': 3000, 'debug': True}
combined = {**defaults, **overrides}
# combined == {'host': 'localhost', 'port': 3000, 'debug': True}
```

Add one extra key without copying the whole dict manually:

```python
base = {'a': 1, 'b': 2}
extended = {**base, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3}
```

**Why `{**a, **b}`?** It creates a new dict without modifying either input — safer than manual `.update()` when you need to keep defaults intact.

## Common pitfalls

- Too many or too few values without `*` → `ValueError`
- Using `*` on both sides of assignment (invalid syntax)
- Forgetting that `*rest` is always a list, even for one element
- Confusing `*args` (tuple in function defs) with `*rest` (list in assignments)
- Unpacking `None` — always ensure the iterable exists before unpacking

```python
# ValueError: not enough values to unpack
a, b = [1]

# Fix: use star or provide defaults elsewhere
a, *rest = [1]  # a == 1, rest == []
```

## Practice

Split a list into head (first element) and tail (everything else).

```python
data = [10, 20, 30]
head, *tail = data
# head == 10, tail == [20, 30]
```

Bonus: split into first, last, and middle:

```python
data = [10, 20, 30, 40]
first, *middle, last = data
# first == 10, middle == [20, 30], last == 40
```

## Summary

Unpacking makes boundary code readable: first/last, head/tail, merge configs, and splat arguments. Reach for `*` whenever you find yourself slicing with `[0]` and `[1:]` repeatedly.
