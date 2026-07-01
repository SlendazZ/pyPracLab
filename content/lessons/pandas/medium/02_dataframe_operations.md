---
title: DataFrame Operations
track: pandas
difficulty: medium
tags: pandas, dataframe
exercise: content/problems/pandas/easy/02_filter_dataframe.py
---

# DataFrame Operations

## Overview

A `DataFrame` is a table of Series sharing one index — rows are records, columns are fields. Most real data work (filter, group, join, export) happens at the DataFrame level.

Real-world uses:

- Sales reports from CSV exports
- Log analysis (filter errors, count by service)
- Joining customer data with order history
- Preparing cleaned data for charts or ML pipelines

## Creating and inspecting

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Ada', 'Grace', 'Linus'],
    'score': [98, 95, 88],
    'department': ['eng', 'eng', 'ops'],
})
df.head()       # first 5 rows
df.tail(3)      # last 3 rows
df.info()       # dtypes, non-null counts, memory
df.describe()   # numeric summary stats
df.shape        # (rows, columns)
df.columns.tolist()
```

Load from CSV — the most common entry point:

```python
df = pd.read_csv('sales.csv')
df = pd.read_csv('sales.csv', parse_dates=['order_date'], usecols=['id', 'amount', 'region'])
df.to_csv('cleaned.csv', index=False)
```

## Selecting columns and rows

```python
df['name']                  # Series — one column
df[['name', 'score']]       # DataFrame — multiple columns
df.loc[0]                   # row by label
df.iloc[0]                  # row by position
df.loc[0, 'name']           # single cell
df[df['score'] >= 96]       # filter rows — boolean mask
```

**Worked example:** high performers in engineering:

```python
top_eng = df[(df['department'] == 'eng') & (df['score'] >= 96)]
```

Combine conditions with `&` (and), `|` (or). Wrap each condition in parentheses.

**Worked example:** filter with `.query()`:

```python
top_eng = df.query("department == 'eng' and score >= 96")
```

## Adding and mutating columns

```python
df['passed'] = df['score'] >= 60
df['grade'] = pd.cut(df['score'], bins=[0, 60, 80, 100], labels=['C', 'B', 'A'])
```

Prefer `.assign` for method chains — avoids mutating the original:

```python
result = (
    df.assign(doubled=lambda d: d['score'] * 2)
      .assign(passed=lambda d: d['score'] >= 60)
      .query('passed')
)
```

## Sorting and ranking

```python
df.sort_values('score', ascending=False)
df.sort_values(['department', 'score'], ascending=[True, False])
df['rank'] = df['score'].rank(ascending=False)
```

## Groupby aggregations

```python
df.groupby('department')['score'].mean()
df.groupby('department').agg(
    avg_score=('score', 'mean'),
    headcount=('name', 'count'),
    top_score=('score', 'max'),
)
```

**Worked example:** monthly revenue by region:

```python
sales = pd.read_csv('orders.csv', parse_dates=['order_date'])
sales['month'] = sales['order_date'].dt.to_period('M')
revenue = sales.groupby(['region', 'month'])['amount'].sum().reset_index()
```

**Worked example:** top customer per region:

```python
idx = sales.groupby('region')['amount'].idxmax()
top_customers = sales.loc[idx, ['region', 'customer', 'amount']]
```

## Merge and concat

Join two tables on a shared key (like SQL JOIN):

```python
users = pd.DataFrame({'user_id': [1, 2], 'name': ['Ada', 'Grace']})
orders = pd.DataFrame({'user_id': [1, 1, 2], 'total': [50, 30, 80]})
pd.merge(users, orders, on='user_id', how='left')
```

Stack tables vertically:

```python
pd.concat([df2024, df2025], ignore_index=True)
```

| how=    | Keeps rows from...                    |
|----------|---------------------------------------|
| inner    | both tables (intersection)            |
| left     | left table + matches from right       |
| right    | right table + matches from left       |
| outer    | both tables (union, NaN where missing)|

## String and datetime columns

```python
df['email_domain'] = df['email'].str.split('@').str[-1]
df['year'] = df['order_date'].dt.year
df['weekday'] = df['order_date'].dt.day_name()
```

Access string methods via `.str`; datetime parts via `.dt`.

## Handling missing data

```python
df.isna().sum()              # count NaN per column
df.dropna(subset=['score'])  # drop rows with NaN in score
df.fillna({'score': 0})      # replace NaN with 0
df['score'].fillna(df['score'].mean())  # fill with column mean
```

## Real-world scenario: clean a CSV export

```python
def clean_sales(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['date'])
    df = df.dropna(subset=['amount'])
    df = df[df['amount'] > 0]
    df['amount'] = df['amount'].round(2)
    return df.sort_values('date')
```

## Common pitfalls

- Chained indexing `df[df.a]['b'] = x` — use `.loc` once: `df.loc[df['a'], 'b'] = x`
- Duplicate column names after merge — suffixes with `suffixes=('_left', '_right')`
- Loading entire CSV when `usecols` or `dtype` would save memory
- Forgetting `index=False` when writing CSV (extra unnamed index column)
- `groupby` without `.reset_index()` when you need a flat DataFrame
- Comparing strings with `==` when whitespace differs — use `.str.strip()` first

## Practice

Filter rows where a numeric column meets a condition.

## Summary

DataFrame workflow: load → inspect → filter/select → transform → group/merge → export. Stay vectorized end to end — let pandas do the looping in C, not Python.
