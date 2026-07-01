---
title: List Comprehensions
track: syntax
difficulty: easy
tags: comprehension, list
exercise: content/problems/syntax/easy/01_list_comprehension_evens.py
---

# List Comprehensions

## Overview

A list comprehension builds a new list in one expression. It is the idiomatic Python replacement for simple loops that append to a list.

**Why use them?** Comprehensions are faster to read and often faster to run than equivalent `for` loops because Python can optimize the whole expression. They also make the intent obvious: "build a list of X from Y where Z."

Think of a comprehension as a **recipe in one line**: you say what goes into the new list, where it comes from, and (optionally) which items to skip.

## Syntax

```python
[expression for item in iterable if condition]
```

Read left to right: **what to collect**, **from where**, **optional filter**.

Fill in this sentence for any comprehension:

- "Give me `[expression]` for each `item` in `iterable` (only if `condition`)."

Example sentence: "Give me `x * x` for each `x` in `range(10)`" → ten squares.

## Basic examples

Build a list of squares from 0 through 9:

```python
squares = [x * x for x in range(10)]
# squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

The loop version does the same thing but spreads the logic across four lines:

```python
squares = []
for x in range(10):
    squares.append(x * x)
```

Keep only even numbers from a list:

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
# evens == [2, 4, 6]
```

**Why `x % 2 == 0`?** The `%` operator gives the remainder after division. Even numbers leave remainder 0 when divided by 2. The `if` clause filters before the expression runs — only passing items get collected.

Transform and filter strings in one pass:

```python
names = ['ada', '', 'bob', 'charlie']
labels = [name.upper() for name in names if name]
# labels == ['ADA', 'BOB', 'CHARLIE']  (empty string skipped)
```

Convert temperatures from Fahrenheit to Celsius:

```python
fahrenheit = [32, 50, 68, 86]
celsius = [(f - 32) * 5 / 9 for f in fahrenheit]
# celsius == [0.0, 10.0, 20.0, 30.0]
```

**Why the `if name` check?** Empty strings are falsy in Python. Filtering them out avoids calling `.upper()` on junk data and keeps your output clean.

## Worked example: from loop to comprehension

**Goal:** square every even number in `[3, 8, 5, 12, 7, 4]`.

**Step 1 — write the loop first** (always a safe starting point):

```python
numbers = [3, 8, 5, 12, 7, 4]
result = []
for x in numbers:
    if x % 2 == 0:
        result.append(x * x)
# result == [64, 144, 16]
```

**Step 2 — identify the three parts:**

- Expression: `x * x` (what you append)
- Iterable: `numbers` (what you loop over)
- Filter: `x % 2 == 0` (the `if` inside the loop)

**Step 3 — compress into one line:**

```python
result = [x * x for x in numbers if x % 2 == 0]
# same output: [64, 144, 16]
```

Nothing changed logically — only the shape. The expression is what you used to `append`. The `if` clause is the guard inside the loop.

## Worked example: cleaning user input

**Input:** `raw = ['  ada  ', '', 'BOB', '  ', 'charlie']`

**Goal:** strip whitespace and drop blanks.

```python
clean = [name.strip().lower() for name in raw if name.strip()]
# clean == ['ada', 'bob', 'charlie']
```

**Trace for `'  ada  '`:**

1. `name.strip()` → `'ada'` (truthy, passes filter)
2. Expression: `'ada'.lower()` → `'ada'`

**Trace for `'  '`:**

1. `name.strip()` → `''` (falsy, skipped)

**Why chain `.strip().lower()` in the expression?** You only transform values that survived the filter, so you never waste work on blanks.

## Filter + transform together

```python
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x * x for x in numbers if x % 2 == 0]
# even_squares == [4, 16, 36]
```

Equivalent loop:

```python
result = []
for x in numbers:
    if x % 2 == 0:
        result.append(x * x)
```

**Why not two steps?** A single comprehension avoids building a temporary intermediate list and keeps the data flow in one place.

Build index-value pairs from a list:

```python
colors = ['red', 'green', 'blue']
indexed = [(i, color) for i, color in enumerate(colors)]
# indexed == [(0, 'red'), (1, 'green'), (2, 'blue')]
```

Extract lengths of words longer than three characters:

```python
words = ['cat', 'elephant', 'dog', 'mouse']
long_lengths = [len(w) for w in words if len(w) > 3]
# long_lengths == [8, 5]
```

## Conditional expressions inside comprehensions

The `if` **after** `for` filters items. An `if/else` **inside** the expression transforms each item (ternary):

```python
nums = [1, 2, 3, 4, 5]
# Filter: keep only evens, then double
doubled_evens = [x * 2 for x in nums if x % 2 == 0]
# [4, 8]

# Ternary: double evens, keep odds unchanged
mixed = [x * 2 if x % 2 == 0 else x for x in nums]
# [1, 4, 3, 8, 5]
```

**Why the position matters:** `[x for x in nums if x > 0]` skips items. `[x if x > 0 else 0 for x in nums]` keeps every item but replaces negatives with 0. Same keyword, different job.

Label numbers as even or odd strings:

```python
labels = ['even' if n % 2 == 0 else 'odd' for n in range(4)]
# ['even', 'odd', 'even', 'odd']
```

## Nested comprehensions

Generate all coordinate pairs in a 3x3 grid:

```python
pairs = [(x, y) for x in range(3) for y in range(3)]
# pairs == [(0,0), (0,1), (0,2), (1,0), ..., (2,2)]
```

**Why two `for` clauses?** Same as nested loops: outer `x`, inner `y`. Read them left to right, outermost first.

Build a multiplication table as a list of lists:

```python
matrix = [[i * j for j in range(3)] for i in range(3)]
# matrix == [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

Flatten a 2D list into one row:

```python
grid = [[1, 2], [3, 4], [5, 6]]
flat = [cell for row in grid for cell in row]
# flat == [1, 2, 3, 4, 5, 6]
```

Collect all vowels from a list of words:

```python
words = ['hello', 'sky']
vowels = [ch for word in words for ch in word if ch in 'aeiou']
# vowels == ['e', 'o']
```

Keep nesting shallow — deeply nested comprehensions hurt readability. **Why?** Each extra `for` adds mental load. If you need three or more levels, a regular loop with clear variable names is often kinder to future readers.

## Dict and set comprehensions

Map each word to its length:

```python
words = ['cat', 'elephant', 'dog']
lengths = {word: len(word) for word in words}
# lengths == {'cat': 3, 'elephant': 8, 'dog': 3}
```

Collect unique positive values:

```python
items = [-1, 3, 3, 0, 7, -2, 7]
positives = {x for x in items if x > 0}
# positives == {3, 7}  (sets discard duplicates)
```

Invert a simple mapping (swap keys and values):

```python
scores = {'ada': 95, 'bob': 87}
by_score = {score: name for name, score in scores.items()}
# by_score == {95: 'ada', 87: 'bob'}
```

Build a set of file extensions:

```python
files = ['report.pdf', 'notes.txt', 'data.pdf']
extensions = {f.split('.')[-1] for f in files}
# extensions == {'pdf', 'txt'}
```

**Why dict/set comprehensions?** Same readability win as list comprehensions, but you choose the collection type with the outer braces: `{}` for dict (with `key: value`) or `{expr}` for set.

## Generator expressions (memory-friendly cousin)

Parentheses instead of brackets create a generator — lazy, one item at a time:

```python
# Good: sum without storing millions of values
total = sum(x * x for x in range(1_000_000))

# Wasteful: builds a list of 1 million ints first
total = sum([x * x for x in range(1_000_000)])
```

Check if any name is too long:

```python
names = ['ada', 'alexandria', 'bob']
has_long = any(len(n) > 10 for n in names)
# has_long == False
```

**Why generators?** They avoid allocating a full list when you only need to iterate once (sum, any, all, max, or a single for-loop).

## When NOT to use them

- Side effects (printing, file I/O, database calls) — comprehensions should be pure transforms
- Long multi-line logic — use a regular loop so you can add comments and breakpoints
- When a generator suffices: `(x for x in big)` saves memory
- When readability suffers — a verbose loop beats a cryptic one-liner

```python
# Bad: side effect inside comprehension
[print(x) for x in items]  # works but unclear; use a for-loop
```

## Common pitfalls

- Shadowing loop variables — in Python 3 the loop variable leaks to outer scope after the comprehension; avoid reusing names like `i` or `x` nearby
- Building huge lists when `sum(...)`, `any(...)`, or a generator would work
- Putting the `if` in the wrong position (filter vs ternary — see above)
- Nested comprehensions that are hard to read — switch to nested loops

```python
# Filter before transform (correct for evens only)
[x * 2 for x in nums if x % 2 == 0]

# Conditional expression (different meaning — every item kept)
[x * 2 if x % 2 == 0 else x for x in nums]
```

## Practice

Filter even numbers and square them in one comprehension.

Given `numbers = [1, 2, 3, 4, 5, 6]`, the answer is `[4, 16, 36]`.

```python
numbers = [1, 2, 3, 4, 5, 6]
answer = [x * x for x in numbers if x % 2 == 0]
# answer == [4, 16, 36]
```

## Summary

Comprehensions = concise map+filter. Prefer them for pure transforms; prefer loops for effects and complex control flow. When learning, write the loop first, then refactor — that builds intuition for what the comprehension is actually doing.
