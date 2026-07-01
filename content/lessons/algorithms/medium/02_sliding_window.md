---
title: Sliding Window
track: algorithms
difficulty: medium
tags: sliding-window
exercise: content/problems/algorithms/medium/03_longest_substring_without_repeating.py
---

# Sliding Window

## Overview

A sliding window tracks a contiguous range `[left, right]` in a string or array. You expand the window by advancing `right`, and shrink from `left` when a constraint breaks. Many substring/subarray problems become O(n) instead of O(n²).

**Why not check every substring?** A string of length n has O(n²) substrings. Brute force rechecks overlapping regions repeatedly. A sliding window reuses work from the previous step — each element enters and leaves the window at most once.

Imagine a fixed-size frame sliding along a timeline. Instead of recomputing the whole sum inside the frame from scratch each step, you add the new entry and drop the one that left.

## When to use it

- "Longest/shortest substring/subarray where …"
- Fixed-size window of length k (moving average, max in window)
- Running sum or frequency counts over a range
- Contiguous subarray with a sum/count constraint

## Fixed vs variable window

**Fixed size k**: maintain a sum or deque of the last k elements; slide one step at a time.

**Variable size**: grow `right` until invalid, then shrink `left` until valid again.

**Why two flavors?** Fixed-k problems always know the window width. Variable problems hunt for the best length that still satisfies a rule.

## Template: longest substring without repeats

```python
def length_of_longest_substring(s):
    left = 0
    best = 0
    seen = set()
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best
```

**Why `while` not `if`?** A single shrink step may not be enough. If `left` skips duplicate characters, you may need multiple removals before `ch` is safe to add.

**Why `right - left + 1`?** Both endpoints are inclusive. A window from index 2 to 4 has length `4 - 2 + 1 = 3`.

Frequency-map variant (allows at most k duplicates):

```python
def longest_with_k_distinct(s, k):
    left = 0
    counts = {}
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > k:
            left_ch = s[left]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            left += 1
        best = max(best, right - left + 1)
    return best
```

## Worked example: longest unique substring

**Input:** `s = "abcabcbb"`

| right | ch | seen after add | action on duplicate | left | window  | best |
|-------|----|----------------|---------------------|------|---------|------|
| 0     | a  | {a}            | —                   | 0    | "a"     | 1    |
| 1     | b  | {a,b}          | —                   | 0    | "ab"    | 2    |
| 2     | c  | {a,b,c}        | —                   | 0    | "abc"   | 3    |
| 3     | a  | —              | shrink until a gone | 1    | "bca"   | 3    |
| 4     | b  | —              | shrink until b gone | 2    | "cab"   | 3    |
| 5     | c  | —              | shrink until c gone | 3    | "abc"   | 3    |
| 6     | b  | —              | shrink              | 4    | "cb"    | 3    |
| 7     | b  | —              | shrink              | 5    | "b"     | 3    |

**Output:** `3` (windows like `"abc"`, `"bca"`, `"cab"` all have length 3).

**Input:** `s = "bbbbb"` → best window `"bbb"` but unique chars force length `1` at any time → **Output:** `1`.

## Worked example: max sum subarray of size k

**Input:** `arr = [2, 1, 5, 1, 3, 2]`, `k = 3`

```python
def max_sum_fixed_window(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)
    return best
```

**Step-by-step:**

- Initial window `[2, 1, 5]` → sum = 8, best = 8
- Slide right: add `arr[3]=1`, subtract `arr[0]=2` → sum = 7
- Slide: add `arr[4]=3`, subtract `arr[1]=1` → sum = 9, best = 9
- Slide: add `arr[5]=2`, subtract `arr[2]=5` → sum = 6

**Output:** `9` from window `[5, 1, 3]`.

**Why subtract `arr[right - k]`?** When the window slides one step right, the leftmost element leaves. Adding the new right element and removing the old left element updates the sum in O(1).

Moving average with the same pattern:

```python
def moving_average(arr, k):
    window_sum = sum(arr[:k])
    averages = [window_sum / k]
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        averages.append(window_sum / k)
    return averages
```

**Input:** `arr = [1, 2, 3, 4]`, `k = 2` → **Output:** `[1.5, 2.5, 3.5]`

## Variable window: sum at most target

```python
def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    best = float('inf')
    for right, num in enumerate(nums):
        window_sum += num
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if best == float('inf') else best
```

**Input:** `target = 7`, `nums = [2, 3, 1, 2, 4, 3]`

| right | num | window_sum | left | window      | best len |
|-------|-----|------------|------|-------------|----------|
| 0     | 2   | 2          | 0    | [2]         | inf      |
| 1     | 3   | 5          | 0    | [2,3]       | inf      |
| 2     | 1   | 6          | 0    | [2,3,1]     | inf      |
| 3     | 2   | 8          | 0→1  | shrink/grow | 4        |
| ...   |     |            |      |             |          |
| 5     | 3   | 7          | 4    | [4,3]       | 2        |

**Output:** `2` (subarray `[4, 3]`).

**Why shrink while `window_sum >= target`?** We want the **shortest** valid window. Once valid, tightening from the left might still leave a valid window with smaller length.

## Maintaining the invariant

Write down what must always be true inside the window:

- All characters unique
- Sum ≥ target (or ≤ target for maximum-length problems)
- At most k distinct characters
- No zeros in the window (for product problems)

The inner `while` restores the invariant after each expansion.

**Why write the invariant first?** It tells you whether to use `if` or `while`, when to update `best`, and what data structure (set, dict, running sum) to maintain.

Count subarrays with exactly k odd numbers (advanced pattern):

```python
# Idea: at_most(k) - at_most(k-1)
# Build at_most by sliding window on odd count
```

## Common pitfalls

- Shrinking with `if` instead of `while` when multiple steps are needed
- Updating the answer before the window is valid again
- Using O(n) work inside each shrink (use a frequency map or running sum)
- Off-by-one in window length: `right - left + 1` includes both endpoints
- Forgetting to handle empty input or `k > len(arr)` in fixed windows

```python
# Bug: missing closing paren (always verify your max/min line)
best = max(best, right - left + 1)  # correct
```

## Complexity

Each index enters and leaves the window at most once → O(n) time, O(k) space for auxiliary structures (set, dict, or deque of size at most k).

## Practice

Implement longest substring without repeating characters using the template above.

```python
length_of_longest_substring('abcabcbb')  # 3
length_of_longest_substring('pwwkew')    # 3 ('wke')
```

## Related patterns

- **Prefix sums** when the window rule involves arbitrary range sums
- **Monotonic deque** for "max in sliding window of size k" in O(n)
