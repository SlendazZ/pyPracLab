---
title: Dynamic Programming Intro
track: algorithms
difficulty: medium
tags: dp, memoization
exercise: content/problems/algorithms/easy/07_climbing_stairs.py
---

# Introduction to Dynamic Programming

## Overview

Dynamic programming (DP) solves problems with **overlapping subproblems** and **optimal substructure**. Instead of recomputing the same states, you store results in a table or cache.

**Why DP?** Naive recursion on problems like Fibonacci or climbing stairs recomputes the same values exponentially many times. DP trades memory for speed by remembering answers to subproblems you've already solved.

DP is not a trick — it is careful bookkeeping. Once you spot repeated subquestions, caching or tabulating them collapses exponential work to polynomial time.

## When to recognize DP

- Counting ways (climbing stairs, coin change)
- Min/max cost paths
- "Can you partition / reach / form …?"
- Recursive solution explodes in branching (Fibonacci, knapsack)
- Problem has choices at each step with optimal substructure

**Key question:** If I solve a smaller version optimally, can I build the full answer from it? If yes, and subproblems repeat, DP likely applies.

## Naive vs memoized: Fibonacci

Naive recursion — exponential time:

```python
def fib_naive(n):
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
# fib_naive(35) already feels slow — branches recompute fib(5) many times
```

Top-down with memo — linear time:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Concrete outputs:**

```python
fib(1)  # 1
fib(2)  # 1
fib(5)  # 5
fib(10) # 55
fib(100)  # fast with cache; naive would hang
```

**Why top-down first?** It mirrors the natural recursive definition. You can write the brute-force recursion, add `@lru_cache`, and immediately see speedup.

## Top-down (memoization) — climbing stairs

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def climb(n):
    if n <= 2:
        return n
    return climb(n - 1) + climb(n - 2)
```

**Concrete outputs:**

```python
climb(1)  # 1
climb(2)  # 2
climb(3)  # 3  (1+1+1 or 1+2 or 2+1)
climb(5)  # 8
```

Add caching to recursion; each `n` computed once → O(n) time.

## Bottom-up (tabulation)

```python
def climb(n):
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

**Walkthrough for n = 5:**

| step i | prev | curr | next curr |
|--------|------|------|-----------|
| start  | 1    | 2    | —         |
| 3      | 2    | 3    | 2+1       |
| 4      | 3    | 5    | 3+2       |
| 5      | 5    | 8    | 5+3       |

**Output:** `8`

Fill from base cases upward. No recursion stack — often better for large n.

**Why bottom-up?** You control iteration order explicitly and can often shrink the table to a few variables (`prev`, `curr`).

## The DP recipe

1. **Define state:** what subproblem does `dp[i]` represent?
2. **Write recurrence:** how does `dp[i]` relate to smaller states?
3. **Set base cases:** smallest inputs with known answers
4. **Choose iteration order:** usually forward (small → large)
5. **Return** `dp[target]`

Skipping step 1 is the most common mistake. Write in plain English: "`dp[i]` = number of ways to reach step i."

## Climbing stairs example

State: `ways(n)` = number of distinct ways to reach step n (1 or 2 steps at a time).

Recurrence: `ways(n) = ways(n-1) + ways(n-2)`

**Why?** To land on step n, you either came from step n-1 (one step) or step n-2 (two steps). Those are independent paths — add them.

Base cases: `ways(1) = 1`, `ways(2) = 2`.

Tabulation version:

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Input:** `n = 4` → `dp = [0,1,2,3,5]` → **Output:** `5`

## Worked example: min cost path

**Input:** `cost = [10, 15, 20]` (cost to step on each tile; start off array)

```python
def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    # dp[i] = min cost to reach step i (top is step n)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
```

**Step-by-step:**

- `dp[0] = dp[1] = 0` (free starting positions)
- `dp[2] = min(0+10, 0+15) = 10`
- `dp[3] = min(10+15, 0+20) = 20`

**Output:** `20` (step on index 0 costing 10, then jump to top; or 1→2)

**Why min of two predecessors?** You can only arrive at step `i` from `i-1` or `i-2`; pick the cheaper path.

## House robber preview

```python
def rob(nums):
    if not nums:
        return 0
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

**Input:** `[2, 7, 9, 3, 1]` → rob houses 0, 2, 4 → `2 + 9 + 1 = 12`

**State idea:** `dp[i]` = max money robbing houses up to index `i` without adjacent picks.

## Coin change preview

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Input:** `coins = [1, 2, 5]`, `amount = 11`

**Build table (selected entries):**

| amount a | dp[a] | how |
|----------|-------|-----|
| 0        | 0     | base |
| 1        | 1     | one 1-coin |
| 2        | 1     | one 2-coin |
| 3        | 2     | 2+1 |
| 5        | 1     | one 5-coin |
| 11       | 3     | 5+5+1 |

**Output:** `3` (5 + 5 + 1)

**Why unbounded knapsack flavor?** Each coin can be reused; inner loop tries every coin for each amount.

**Input:** `coins = [2]`, `amount = 3` → impossible → **Output:** `-1`

## Common pitfalls

- Unclear state definition → wrong recurrence
- Forgetting base cases for n=0 or n=1
- Using O(n²) nested loops when a 1D DP suffices
- Off-by-one in array indexing (dp size vs problem size)
- Not initializing `dp[0]` correctly in coin change (should be 0 ways, cost 0)

## Complexity

Climbing stairs: O(n) time, O(1) space with rolling variables.
Coin change: O(amount × len(coins)) time, O(amount) space.
Fibonacci with memo: O(n) time, O(n) cache space (O(1) with rolling).

## Practice

Solve climbing stairs, then coin change (unbounded knapsack flavor).

```python
climb_stairs(5)              # 8
coin_change([1, 2, 5], 11)   # 3
```

## Next steps

2D DP grids (edit distance), bitmask DP, and interval DP build on the same recipe: define state, write recurrence, set bases, fill table.
