---
title: Pandas Series Basics
track: pandas
difficulty: easy
tags: pandas, series
exercise: content/problems/pandas/easy/01_double_series.py
---

# Pandas Series Basics

## Overview

A `Series` is a one-dimensional labeled array — like a single column in a spreadsheet or a Python dict with a fixed order. It is the building block of DataFrames and the first pandas type to master.

If you know Python lists and dicts, a Series combines both: ordered values with optional labels (the index).

Real-world uses:

- Daily temperature readings with date labels
- Stock prices indexed by timestamp
- Survey scores for each respondent ID
- Any column you pull out of a larger table

Install with `pip install pandas` (NumPy is installed automatically).

## Creating a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30])                    # default index 0, 1, 2
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s = pd.Series({'a': 10, 'b': 20, 'c': 30})     # keys become index
```

Print a Series to see values aligned with their labels:

```
a    10
b    20
c    30
dtype: int64
```

## Index and values

```python
s.index    # Index(['a', 'b', 'c'])
s.values   # numpy array: array([10, 20, 30])
s.dtype    # int64
len(s)     # 3
s.name     # optional name (useful when Series becomes a DataFrame column)
```

Two ways to access elements:

```python
s['b']      # label-based (loc style)
s.iloc[1]   # position-based — always 0, 1, 2...
s.loc['b']  # explicit label access
```

**Watch out:** if your index is integers, `s[0]` might mean label `0`, not the first row. Prefer `.iloc` for position and `.loc` for labels.

## Vectorized operations

The core pandas idea: operate on the whole Series at once, not element by element in a Python loop.

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
doubled = s * 2           # a→20, b→40, c→60
shifted = s + 100
avg = s.mean()            # 20.0
summary = s.describe()    # count, mean, std, min, quartiles, max
```

**Worked example:** price with tax:

```python
prices = pd.Series({'widget': 9.99, 'gadget': 14.50, 'gizmo': 3.25})
with_tax = (prices * 1.08).round(2)
# widget    10.79
# gadget    15.66
# gizmo      3.51
```

**Worked example:** temperature conversion (Fahrenheit to Celsius):

```python
fahrenheit = pd.Series([32, 68, 98.6], index=['freezing', 'room', 'body'])
celsius = (fahrenheit - 32) * 5/9
# freezing      0.0
# room         20.0
# body         37.0
```

## Alignment on index

When you combine two Series, pandas aligns by label:

```python
a = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
b = pd.Series([10, 20], index=['y', 'z'])
a + b
# x     NaN  (no match in b)
# y    12.0
# z    23.0
```

Missing labels become `NaN` (Not a Number). Use `.fillna(0)` if you need zeros instead:

```python
(a + b).fillna(0)
```

## Boolean filtering

```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
s[s > 15]              # b→20, c→30, d→40
s[s.isin([10, 30])]    # a→10, c→30
s[s.between(15, 35)]   # b→20, c→30
```

The expression inside `s[...]` must be a boolean Series of the same length.

**Worked example:** filter and transform:

```python
scores = pd.Series([55, 72, 88, 91, 63], index=['A', 'B', 'C', 'D', 'E'])
passing = scores[scores >= 60]
curved = passing + 5
```

## Useful methods

```python
s.sort_values()          # ascending by value
s.sort_index()           # ascending by label
s.unique()               # array of distinct values
s.value_counts()         # frequency table
s.isna().sum()           # count missing values
s.apply(lambda x: x * 2) # element-wise function (slower than vectorized ops)
```

## Handling missing data in Series

```python
s = pd.Series([10, None, 30])
s.isna()           # False, True, False
s.dropna()         # remove NaN rows
s.fillna(0)        # replace NaN with 0
s.interpolate()    # fill gaps by interpolation
```

## Why vectorization matters

Loops over rows are slow; NumPy/pandas C-backed ops are fast:

```python
# slow — avoid for large data
doubled = pd.Series([x * 2 for x in s])

# fast — preferred
doubled = s * 2
```

On millions of rows the difference is seconds vs minutes.

## Real-world scenario: daily sales totals

```python
sales = pd.Series(
    [1200, 980, 1450, 1100, 1320],
    index=pd.date_range('2025-01-01', periods=5, freq='D'),
)
sales.mean()                    # average daily sales
sales[sales > sales.mean()]     # above-average days
sales.pct_change()              # day-over-day percent change
```

## Common pitfalls

- SettingWithCopyWarning — use `.loc` for assignment: `s.loc[mask] = value`
- Mixing `s[0]` (label if index is int) vs `s.iloc[0]` (always position)
- Forgetting NaN propagates in arithmetic (`10 + NaN = NaN`)
- Assuming `.sort_values()` mutates in place — it returns a new Series unless `inplace=True`
- Using Python loops when a vectorized operation exists

## Practice

Double every value in a Series without a Python loop.

## Summary

Series = values + index + vectorized methods. Create with lists or dicts, access with `.loc`/`.iloc`, transform with arithmetic and boolean masks. Master Series before moving to multi-column DataFrames.
