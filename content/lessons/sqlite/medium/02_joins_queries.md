---
title: JOINs and Analytical Queries
track: sqlite
difficulty: medium
tags: sql, join
exercise: content/problems/sqlite/medium/09_join_users_orders.py
---

# JOINs and Analytical Queries

## Overview

Real data lives in multiple related tables. JOIN combines rows across tables; GROUP BY aggregates them. These patterns appear in every app beyond single-table CRUD.

Real-world uses:

- Order history per customer (users + orders)
- Revenue by product category (products + line_items)
- Active users who never placed an order (LEFT JOIN + NULL check)
- Monthly expense totals (GROUP BY month)

## Sample schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Seed data for examples:

```python
conn.executemany('INSERT INTO users (id, name) VALUES (?, ?)', [(1, 'Ada'), (2, 'Grace'), (3, 'Linus')])
conn.executemany('INSERT INTO orders (user_id, total) VALUES (?, ?)', [(1, 50), (1, 30), (2, 80)])
conn.commit()
```

Ada has two orders; Grace has one; Linus has none.

## INNER JOIN

Returns only rows with matches on **both** sides:

```sql
SELECT u.name, o.id AS order_id, o.total
FROM users u
INNER JOIN orders o ON o.user_id = u.id
WHERE o.total > 100
ORDER BY o.total DESC;
```

Users with no orders are excluded. Orders with invalid `user_id` are excluded.

**From Python:**

```python
sql = '''
    SELECT u.name, o.total
    FROM users u
    INNER JOIN orders o ON o.user_id = u.id
    WHERE o.total > ?
'''
rows = conn.execute(sql, (100,)).fetchall()
```

## LEFT JOIN

Keeps **all** rows from the left table; missing right-side matches are NULL:

```sql
SELECT u.name, COUNT(o.id) AS order_count, COALESCE(SUM(o.total), 0) AS spent
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name
ORDER BY spent DESC;
```

Users with zero orders appear with `order_count = 0` and `spent = 0`.

**Worked example:** find users who never ordered:

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE o.id IS NULL;
```

Returns `Linus` — he has no matching orders.

**Worked example:** join users to order totals (exercise pattern):

```python
def user_order_totals(conn) -> list[tuple]:
    sql = '''
        SELECT u.name, o.total
        FROM users u
        JOIN orders o ON o.user_id = u.id
        ORDER BY u.name, o.total
    '''
    return conn.execute(sql).fetchall()
# [('Ada', 50), ('Ada', 30), ('Grace', 80)]
```

## Aggregations

```sql
SELECT category, SUM(amount) AS total, COUNT(*) AS txn_count
FROM expenses
GROUP BY category
HAVING total > 500
ORDER BY total DESC;
```

- `WHERE` filters rows **before** grouping
- `HAVING` filters groups **after** aggregation
- Common aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`

**Worked example:** top spender:

```sql
SELECT u.name, SUM(o.total) AS lifetime_total
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name
ORDER BY lifetime_total DESC
LIMIT 1;
```

## Subqueries and EXISTS

Sometimes a subquery is clearer than a JOIN:

```sql
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.total > 1000
);
```

`EXISTS` stops at the first match — often efficient for "has any" checks.

## Indexes for performance

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

Speeds up JOINs and WHERE clauses on `user_id`. For small test databases it does not matter; for production SQLite files with millions of rows, indexes are essential.

## JOIN types at a glance

| Type        | Result                                      |
|-------------|---------------------------------------------|
| INNER JOIN  | only matching rows from both tables         |
| LEFT JOIN   | all left rows + matches from right (or NULL)|
| CROSS JOIN  | every left row paired with every right row  |

Missing `ON` clause on INNER JOIN → Cartesian product (huge, usually wrong).

## Python integration pattern

```python
def get_user_totals(conn, min_total: float) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    sql = '''
        SELECT u.name, SUM(o.total) AS lifetime_total
        FROM users u
        JOIN orders o ON o.user_id = u.id
        GROUP BY u.id, u.name
        HAVING lifetime_total >= ?
        ORDER BY lifetime_total DESC
    '''
    return conn.execute(sql, (min_total,)).fetchall()
```

## Real-world scenario: monthly sales report

```python
def monthly_sales(conn, year: int) -> list[sqlite3.Row]:
    conn.row_factory = sqlite3.Row
    sql = '''
        SELECT strftime('%Y-%m', created_at) AS month,
               COUNT(*) AS order_count,
               SUM(total) AS revenue
        FROM orders
        WHERE strftime('%Y', created_at) = ?
        GROUP BY month
        ORDER BY month
    '''
    return conn.execute(sql, (str(year),)).fetchall()
```

SQLite's `strftime` extracts date parts from ISO-8601 text timestamps.

## Common pitfalls

- Cartesian product from missing or wrong `ON` clause
- Selecting non-aggregated columns not in `GROUP BY` (SQLite allows loosely; other databases error — write portable SQL)
- Duplicate rows from many-to-many joins without `DISTINCT` or proper grouping
- Using INNER JOIN when you need users with zero orders (use LEFT JOIN)
- Forgetting parameterized `HAVING`/`WHERE` values in Python tuples
- Comparing NULL with `= NULL` — use `IS NULL` instead

## Practice

Join users to orders and list names with order totals.

## Summary

Master INNER vs LEFT JOIN, GROUP BY with aggregates, and WHERE vs HAVING. Combine with parameterized queries from Python — that covers most application SQL you will write.
