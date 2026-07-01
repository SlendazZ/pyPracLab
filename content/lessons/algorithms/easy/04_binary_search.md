---
title: Binary Search
track: algorithms
difficulty: easy
tags: binary-search
exercise: content/problems/algorithms/easy/16_binary_search.py
---

# Binary Search

## Overview

Binary search halves the search space each step on **sorted** data. It finds a target in O(log n) comparisons instead of O(n) linear scan.

**Why O(log n)?** Each comparison eliminates half the remaining elements. For 1,000,000 items you need at most ~20 comparisons, not 1,000,000.

Binary search is not just for arrays — any time you can ask "is the answer too big or too small?" and get a monotonic yes/no, you can binary search the answer space.

## When to use it

- Sorted array lookup
- "Find minimum value that satisfies X" (answer space search)
- Rotated sorted array, first/last occurrence
- Any monotonic predicate: once `f(x)` flips from False to True, binary search applies

## Classic template

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Linear scan for comparison:

```python
def linear_search(nums, target):
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1
```

**Why binary wins on big sorted data:** 1M elements → ~20 steps vs up to 1M.

## Worked example: find target

**Input:** `nums = [1, 3, 5, 7, 9, 11]`, `target = 7`

| step | lo | hi | mid | nums[mid] | action      |
|------|----|----|-----|-----------|-------------|
| 1    | 0  | 5  | 2   | 5         | 5 < 7 → lo=3 |
| 2    | 3  | 5  | 4   | 11        | 11 > 7 → hi=3|
| 3    | 3  | 3  | 3   | 7         | found! return 3 |

**Output:** index `3`

**Input:** `target = 4` → no exact match → **Output:** `-1`

**Input:** `target = 1` → found at index `0` on first or second step.

## Invariants

Pick one template and stick to it:

- **Closed interval** `[lo, hi]`: loop while `lo <= hi`, move to `mid ± 1`
- **Half-open** `[lo, hi)`: loop while `lo < hi`, `hi = mid` or `lo = mid + 1`

Mixing templates causes infinite loops or missed answers.

**Why invariants matter?** They define what region still might contain the answer. If you shrink wrong, you can skip the target or loop forever.

Closed-interval mental model: "the target, if it exists, is always between `lo` and `hi` inclusive until the loop ends."

## Find first index >= target (lower bound)

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

**Input:** `nums = [1, 2, 4, 4, 5]`, `target = 4`

- Search narrows to first `4` at index 2
- **Output:** `2`

**Input:** `target = 6` → **Output:** `5` (insert position past end)

**Why `hi = mid` not `mid - 1`?** You want the first position where `nums[mid] >= target`. When `nums[mid] == target`, the answer could still be to the left.

Find last index <= target (upper bound style):

```python
def upper_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1
```

**Input:** `nums = [1, 2, 4, 4, 5]`, `target = 4` → **Output:** `3` (last 4)

## Beyond arrays: search the answer space

Binary search works on any monotonic predicate — not just sorted arrays:

```python
def min_capacity(weights, days):
    # find smallest ship capacity to ship all packages in `days` days
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(weights, days, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Why search capacities?** If capacity `C` works, any capacity `> C` also works (monotonic). Binary search finds the minimum feasible value in O(log S) where S is the search range.

Guess square root (integer):

```python
def int_sqrt(n):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2  # bias up to avoid infinite loop
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo
```

**Input:** `n = 8` → **Output:** `2` (since 2² ≤ 8 < 3²)

## Worked example: search insert position

```python
def search_insert(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
```

**Input:** `nums = [1, 3, 5, 6]`, `target = 2`

- `nums[1] = 3 > 2` → search left half
- Loop ends with `lo = 1`
- **Output:** `1` (insert between 1 and 3)

**Input:** `target = 7` → **Output:** `4` (append after 6)

## Using bisect in production code

```python
import bisect

nums = [1, 3, 5, 5, 7]
bisect.bisect_left(nums, 5)   # 2 — first 5
bisect.bisect_right(nums, 5)  # 4 — insert after existing 5s
```

**Why learn templates first?** Interviews and bug fixes require knowing what `bisect` is doing under the hood.

## Common pitfalls

- Integer overflow in other languages; Python `(lo + hi) // 2` is safe
- Off-by-one on `<=` vs `<` in the loop condition
- Searching unsorted data without sorting or re-framing the problem
- Using `mid - 1` when the template calls for `mid` (loses valid answers)
- Infinite loop when `lo = mid` without biasing `mid` upward in some templates

## Complexity

O(log n) time, O(1) extra space for the standard template.

## Practice

Implement standard binary search, then try "search insert position" variants.

```python
binary_search([1, 3, 5, 7, 9, 11], 7)  # 3
search_insert([1, 3, 5, 6], 2)         # 1
```

## Cheat sheet

| Goal              | Move when true     |
|-------------------|--------------------|
| Find exact target | compare at mid       |
| First >= target   | hi = mid, else lo  |
| Last <= target    | lo = mid, else hi  |
