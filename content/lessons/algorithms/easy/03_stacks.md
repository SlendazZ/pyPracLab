---
title: Stacks for Parsing
track: algorithms
difficulty: easy
tags: stack
exercise: content/problems/algorithms/easy/11_valid_parentheses.py
---

# Stacks for Parsing and Matching

## Overview

A stack is last-in, first-out (LIFO). Python lists with `.append()` and `.pop()` make a perfect stack. Use one whenever the problem involves nesting, matching pairs, or "undo the most recent" logic.

**Why LIFO?** The most recently opened bracket must close first — exactly like a stack of plates. The last item you push is the first one you pop.

Stacks appear in browsers (back button), undo editors, call stacks during recursion, and syntax parsers. If the problem says "most recent unmatched", think stack.

## When to use a stack

- Valid parentheses / HTML tags / bracket matching
- Evaluate postfix or prefix expressions
- Next greater/smaller element (monotonic stack variant)
- DFS on trees/graphs (explicit stack or recursion call stack)
- Undo operations, browser back button, syntax parsing

## Valid parentheses template

```python
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

Openers push; closers must match the most recent opener.

**Why map closers to openers?** When you see `)`, you need to know the expected opener is `(`. The dict makes that lookup O(1).

**Why `return not stack`?** A leftover opener like `'('` means the string ended before everything closed.

Only brackets, ignore other characters:

```python
def is_valid_ignore_noise(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
        # else: ignore letters, digits, spaces
    return not stack
```

## Worked trace: valid string

`s = "({[]})"`:

| ch | action        | stack after   |
|----|---------------|---------------|
| (  | push          | ['(']         |
| {  | push          | ['(', '{']    |
| [  | push          | ['(', '{', '[']|
| ]  | pop, matches [| ['(', '{']     |
| }  | pop, matches { | ['(']         |
| )  | pop, matches ( | []            |

Stack empty at end → **Output:** `True`

## Worked trace: invalid strings

`s = "(]"`:

- `(` push → stack `['(']`
- `]` pop → top is `'('` but `pairs[']']` is `'['` → mismatch
- **Output:** `False`

`s = "(()"`:

- Process all chars → stack `['(']` not empty
- **Output:** `False` (unclosed opener)

`s = ")("`:

- `)` seen with empty stack → **Output:** `False` immediately

## Reverse a string with a stack

```python
def reverse_string(s):
    stack = list(s)
    out = []
    while stack:
        out.append(stack.pop())
    return ''.join(out)
```

**Input:** `'stack'` → **Output:** `'kcats'`

**Why a stack for reversal?** Pop order is opposite of push order — LIFO naturally reverses a sequence.

## Evaluate postfix notation

```python
def eval_postfix(tokens):
    stack = []
    ops = {'+', '-', '*', '/'}
    for tok in tokens:
        if tok not in ops:
            stack.append(int(tok))
        else:
            b, a = stack.pop(), stack.pop()
            if tok == '+': stack.append(a + b)
            elif tok == '-': stack.append(a - b)
            elif tok == '*': stack.append(a * b)
            else: stack.append(a // b)
    return stack[0]
```

**Input:** `tokens = ['2', '3', '+', '4', '*']`

- Push 2, push 3 → stack `[2, 3]`
- `+` → pop 3, 2 → push 5 → `[5]`
- Push 4 → `[5, 4]`
- `*` → pop 4, 5 → push 20 → `[20]`

**Output:** `20` (because `(2 + 3) * 4 = 20`)

**Input:** `['4', '13', '5', '/', '+']` → `4 + (13 // 5) = 4 + 2 = 6`

**Why a stack?** Operators apply to the most recent operands — LIFO again.

**Why pop `b` then `a`?** For subtraction and division, order matters: `a - b`, not `b - a`.

## Monotonic stack (preview)

Find how many days until a warmer temperature:

```python
def daily_temperatures(temps):
    n = len(temps)
    answer = [0] * n
    stack = []  # indices of decreasing temperatures
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    return answer
```

**Input:** `temps = [73, 74, 75, 71, 69, 72, 76, 73]`

**Output:** `[1, 1, 4, 2, 1, 1, 0, 0]`

**Trace for index 0 (73°):** Next warmer day is index 1 (74°) → wait 1 day.

When a warmer day arrives, pop colder days from the stack and record distances. Each index is pushed and popped at most once → O(n).

**Why monotonic?** Stack temperatures stay in decreasing order. A warmer day resolves all colder pending days stacked below it.

Next greater element for each position:

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            result[stack.pop()] = n
        stack.append(i)
    return result
```

**Input:** `[2, 1, 2, 4, 3]` → **Output:** `[4, 2, 4, -1, -1]`

## Common pitfalls

- Forgetting to check stack empty before pop (causes `IndexError`)
- Returning True when stack still has openers at the end
- Confusing stack with queue (FIFO) for BFS problems
- Popping operands in wrong order for non-commutative ops (`a - b` vs `b - a`)
- Using `stack.pop(0)` — that is queue behavior and is O(n) on lists

## Complexity

One push/pop per character or element → O(n) time, O(n) space worst case (when input is all openers like `"(((("`).

## Practice

Implement valid parentheses, then try daily temperatures (monotonic stack).

```python
is_valid('()[]{}')  # True
is_valid('(]')      # False
```

## Summary

Stack = "most recent unmatched item." If your problem sounds like nesting, matching, or undo, reach for a stack first.
