---
title: Two Pointers
track: algorithms
difficulty: easy
tags: two-pointers, array
exercise: content/problems/algorithms/easy/01_two_sum_sorted.py
---

# Two Pointers Technique

## Overview

The two-pointer technique replaces nested loops with two indices that move through data in a single pass. On sorted arrays it often turns O(n²) brute force into O(n).

**Why does it work?** Each pointer move eliminates an entire class of impossible answers. Instead of checking every pair with nested loops, you use structure in the data (usually sorted order) to skip combinations you know will fail.

Picture two fingers walking inward on a sorted number line. When the sum is too small, you cannot fix it by moving the right finger left — you need a bigger left value. That single observation removes many pairs at once.

## When to use it

- Input is sorted (or sorting is allowed)
- You need a pair, triple, or contiguous range matching a rule
- You compare from both ends (converging) or scan together (fast/slow)
- Problem asks for "in place" modification with O(1) extra space

## Prerequisites

Comfort with loops, indexing, and basic big-O notation. You should be able to trace how `left` and `right` change step by step on paper.

## Converging pointers

Place one index at each end and move inward based on a comparison:

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

### Why it works

On a sorted array, if the sum is too small, every pair involving `nums[left]` with indices `< right` is also too small — so increment `left`. If the sum is too large, decrement `right` for the symmetric reason.

You never discard the correct answer because:

- If `nums[left] + nums[right] > target`, then `nums[left] + nums[right - 1]`, `nums[left] + nums[right - 2]`, etc. are all too large — safe to shrink `right`
- The mirror argument applies when the sum is too small

Check if a pair sums to at least a minimum:

```python
def has_pair_at_least(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] >= target:
            return True
        left += 1
    return False
```

## Worked example: two-sum on sorted array

`nums = [1, 3, 4, 6, 8]`, target `7`:

| Step | left | right | nums[left] | nums[right] | sum | Action        |
|------|------|-------|------------|-------------|-----|---------------|
| 1    | 0    | 4     | 1          | 8           | 9   | too big → right-- |
| 2    | 0    | 3     | 1          | 6           | 7   | found! return [0, 3] |

**Output:** `[0, 3]` because `nums[0] + nums[3] = 1 + 6 = 7`.

**Why not check all pairs?** Five elements → 10 pairs with brute force. Two pointers checked only 2 pairs because sorting let us eliminate candidates.

Another input: `nums = [2, 3, 5, 8]`, target `10`:

| Step | left | right | sum | Action |
|------|------|-------|-----|--------|
| 1    | 0    | 3     | 10  | found [0, 3] |

Target `100` on the same array → pointers cross with no match → `[-1, -1]`.

## Worked example: palindrome check

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Input:** `s = "racecar"`

- Compare `r` vs `r` → match, move inward
- Compare `a` vs `a` → match
- Continue until `left >= right`
- **Output:** `True`

**Input:** `s = "hello"` → compare `h` vs `o` → mismatch → **Output:** `False`

**Input:** `s = "abba"` → compare `a`/`a`, then `b`/`b` → **Output:** `True`

**Why converging pointers?** Palindrome symmetry means the outer characters must match first. If they fail, inner characters do not matter.

## Same-direction (fast/slow)

Both pointers start at the left and move forward:

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1  # new length
```

**Input:** `nums = [1, 1, 2, 2, 3]`

| fast | slow | nums (relevant prefix) |
|------|------|------------------------|
| 1    | 0    | [1, 1, ...]            |
| 2    | 1    | [1, 2, ...]            |
| 3    | 1    | [1, 2, 2, ...]         |
| 4    | 2    | [1, 2, 3, ...]         |

**Output:** length `3`, first three elements `[1, 2, 3]`.

**Why fast/slow?** `slow` marks the write position for the deduplicated prefix; `fast` scans ahead. Each element is visited once → O(n).

Move zeros to the end (stable relative order):

```python
def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

**Input:** `[0, 1, 0, 3, 12]` → **Output:** `[1, 3, 12, 0, 0]`

Other same-direction uses:

- **Container with most water**: converging pointers, move the shorter line
- **Merge sorted arrays**: compare heads, advance the smaller side
- **Partition arrays**: Dutch national flag (three pointers)

## Worked example: merge two sorted lists (concept)

```python
def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
```

**Input:** `a = [1, 3, 5]`, `b = [2, 4]` → **Output:** `[1, 2, 3, 4, 5]`

**Why two pointers instead of concatenating and sorting?** Merging sorted lists is O(n + m). Sorting the combined list would be O((n+m) log(n+m)).

## Common pitfalls

- Using converging two-sum on unsorted data without sorting first
- Off-by-one: `left < right` vs `left <= right` changes whether pairs repeat
- Forgetting empty or single-element inputs
- Moving the wrong pointer — always justify each move with the sorted-order argument
- Sorting when the problem forbids it (check constraints first)

## Complexity

- Time: O(n) per pass (each pointer moves at most n steps)
- Space: O(1) for the pointer variables
- If you sort first: O(n log n) time for sort + O(n) for two pointers

## Practice

Open the linked exercise and implement two-sum on a sorted array.

```python
two_sum_sorted([1, 3, 4, 6, 8], 7)  # [0, 3]
```

## Cheat sheet

| Pattern      | Move rule              | Example problems   |
|--------------|------------------------|--------------------|
| Converging   | shrink from wrong side | two-sum, palindrome|
| Fast/slow    | both forward           | dedupe, partition  |
