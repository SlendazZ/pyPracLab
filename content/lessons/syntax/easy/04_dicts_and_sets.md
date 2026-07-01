---
title: Dicts, Sets, and defaultdict
track: syntax
difficulty: easy
tags: dict, set, collections
exercise: content/problems/syntax/easy/07_defaultdict_groupby.py
---

# Dicts, Sets, and defaultdict

## Overview

Dictionaries map keys to values in O(1) average time. Sets store unique elements for O(1) membership tests. Together they power counting, grouping, and deduplication — three of the most common patterns in Python programs.

**Why not just use lists?** Searching a list is O(n); dict and set lookups are O(1) on average. For "have I seen this before?" or "how many times did this appear?", dicts and sets are the right tool.

Interview problems and real apps alike lean on these structures. Mastering them means fewer nested loops and clearer code.

## Dict essentials

Count word frequencies with `.get()`:

```python
words = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# counts == {'cat': 3, 'dog': 2, 'bird': 1}
```

**Why `.get(word, 0)`?** Accessing a missing key with `counts[word]` raises `KeyError`. `.get` returns 0 for new words so you can increment safely.

Iterate key-value pairs:

```python
for word, count in counts.items():
    print(f'{word}: {count}')
# cat: 3
# dog: 2
# bird: 1
```

Safe lookup with a default:

```python
scores = {'ada': 95, 'bob': 87}
scores.get('charlie', 0)  # 0 (key missing, no error)
```

Build a dict from two parallel lists:

```python
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
mapping = dict(zip(keys, vals))
# {'a': 1, 'b': 2, 'c': 3}
```

Check membership before expensive work:

```python
allowed = {'admin', 'editor', 'viewer'}
role = 'guest'
if role in allowed:
    grant_access()
```

## Worked example: two-sum lookup

**Problem:** find two indices whose values sum to `target`.

```python
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    need = target - num
    if need in seen:
        print(seen[need], i)  # 0 1
        break
    seen[num] = i
```

**Walkthrough step by step:**

| i | num | need | seen before | action        |
|---|-----|------|-------------|---------------|
| 0 | 2   | 7    | {}          | store 2→0     |
| 1 | 7   | 2    | {2:0}       | 2 found! → 0,1|

**Output:** indices `0` and `1` because `2 + 7 = 9`.

**Why a dict?** You need instant lookup of "have we seen the complement?" while scanning left to right. A list would require scanning `seen` each time.

## Sets for uniqueness

Track visited nodes:

```python
visited = set()
for node in graph_neighbors:
    if node not in visited:
        visited.add(node)
        process(node)
```

**Why `if node not in visited`?** Set membership is O(1). A list would be O(n) per check and grow expensive on large graphs.

Deduplicate while preserving order:

```python
items = ['b', 'a', 'b', 'c', 'a']
unique = list(dict.fromkeys(items))
# unique == ['b', 'a', 'c']
```

Set operations for overlap:

```python
a = {1, 2, 3}
b = {2, 3, 4}
a & b   # {2, 3}  intersection — in both
a | b   # {1, 2, 3, 4}  union — in either
a - b   # {1}  difference — in a but not b
```

Find users in both groups:

```python
group_a = {'ada', 'bob', 'cleo'}
group_b = {'bob', 'dana', 'ada'}
both = group_a & group_b
# {'ada', 'bob'}
```

**Why `dict.fromkeys` instead of `set`?** Sets discard order. Dict keys preserve insertion order (Python 3.7+), giving you uniqueness and order.

## defaultdict — group without boilerplate

```python
from collections import defaultdict

employees = [('Ada', 'eng'), ('Bob', 'sales'), ('Cleo', 'eng')]
groups = defaultdict(list)
for name, dept in employees:
    groups[dept].append(name)
# dict(groups) == {'eng': ['Ada', 'Cleo'], 'sales': ['Bob']}
```

**Why defaultdict?** Without it you write:

```python
groups = {}
for name, dept in employees:
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(name)
```

Every grouping problem repeats that `if` check. `defaultdict(list)` creates an empty list on first access automatically.

Group words by first letter:

```python
words = ['apple', 'banana', 'apricot', 'blueberry']
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
```

Count with `defaultdict(int)` — zero default:

```python
votes = defaultdict(int)
for choice in ['a', 'b', 'a', 'a', 'c']:
    votes[choice] += 1
# dict(votes) == {'a': 3, 'b': 1, 'c': 1}
```

**Why `int` as factory?** Calling `int()` returns `0`, so missing keys start at zero and `+= 1` works without `.get`.

## Counter for frequencies

```python
from collections import Counter

words = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
counts = Counter(words)
# Counter({'cat': 3, 'dog': 2, 'bird': 1})

top = counts.most_common(2)
# [('cat', 3), ('dog', 2)]
```

Compare two strings for anagrams:

```python
from collections import Counter

def is_anagram(a, b):
    return Counter(a) == Counter(b)

is_anagram('listen', 'silent')  # True
is_anagram('hello', 'world')    # False
```

**Why Counter over manual counting?** It is shorter, supports arithmetic (`counts1 + counts2`), subtraction, and `most_common(k)` is built in.

## Worked example: first duplicate

**Input:** `nums = [1, 3, 4, 3, 2, 1]` — find the first value that appears twice.

```python
def first_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    return None

first_duplicate([1, 3, 4, 3, 2, 1])  # 3
```

**Trace:**

- See 1 → add to seen `{1}`
- See 3 → add `{1, 3}`
- See 4 → add `{1, 3, 4}`
- See 3 again → already in seen → return `3`

## Common patterns

- **Two-sum lookup**: store complements in a dict (see worked example above)
- **Group by key**: `defaultdict(list)` or `itertools.groupby` (requires sorted input)
- **Visited set** in graph/BFS traversal — O(1) "already seen?" checks
- **Frequency map** for anagrams: compare `Counter(s1)` vs `Counter(s2)`

## Common pitfalls

- Using mutable objects (lists) as dict keys — keys must be hashable
- Modifying a dict while iterating — iterate over `list(d)` copy instead
- `set()` loses order; use `dict.fromkeys` trick if order matters
- Assuming `defaultdict` creates nested dicts — use `defaultdict(lambda: defaultdict(int))` or nested factories for 2D grouping
- Using `is` to compare small integers/strings when you mean value equality in dict keys

```python
# Dangerous while iterating
for k in d:
    if bad(k):
        del d[k]  # RuntimeError

# Safe: iterate a snapshot
for k in list(d):
    if bad(k):
        del d[k]
```

## Practice

Group words by their first letter using defaultdict.

```python
from collections import defaultdict

words = ['apple', 'apricot', 'banana']
by_letter = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
# {'a': ['apple', 'apricot'], 'b': ['banana']}
```

## Summary

| Need            | Tool          |
|-----------------|---------------|
| Count           | dict / Counter|
| Unique items    | set           |
| Group lists     | defaultdict   |
| Fast lookup     | dict / set    |
