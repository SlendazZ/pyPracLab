---
title: sqlite3 and In-Memory Databases
track: sqlite
difficulty: easy
tags: sqlite, sql
exercise: content/problems/sqlite/easy/01_create_insert_query.py
---

# sqlite3 and In-Memory Databases

## Overview

SQLite is a full SQL database engine in a single file — or entirely in RAM. Python's `sqlite3` module is in the standard library, so there is nothing extra to install. It is ideal for local apps, prototypes, and fast unit tests.

Unlike client/server databases (PostgreSQL, MySQL), SQLite runs inside your Python process. No separate server to start or configure.

Real-world uses:

- Desktop app local storage (browser history, notes apps)
- Prototyping before moving to PostgreSQL
- Caching structured data between script runs
- Unit tests with `:memory:` databases (isolated, instant teardown)

## Connecting

```python
import sqlite3

conn = sqlite3.connect(':memory:')  # RAM only — gone when closed
conn = sqlite3.connect('app.db')    # persistent file on disk
```

Use `:memory:` in tests — each test gets a clean database with zero filesystem cleanup. Use a file path for apps that need data to survive restarts.

Context manager closes the connection automatically:

```python
with sqlite3.connect('app.db') as conn:
    conn.execute('SELECT 1')
# conn closed here
```

## DDL and DML

Create tables, insert rows, commit changes:

```python
conn = sqlite3.connect(':memory:')
conn.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')
conn.executemany(
    'INSERT INTO users (name, email) VALUES (?, ?)',
    [
        ('Ada Lovelace', 'ada@example.com'),
        ('Grace Hopper', 'grace@example.com'),
    ],
)
conn.commit()
```

**Worked example:** seed and query in a test fixture:

```python
def make_db():
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.executemany('INSERT INTO users (name) VALUES (?)', [('Ada',), ('Grace',)])
    conn.commit()
    return conn

conn = make_db()
rows = conn.execute('SELECT name FROM users ORDER BY name').fetchall()
# [('Ada',), ('Grace',)]
```

## Querying

```python
rows = conn.execute(
    'SELECT id, name FROM users ORDER BY name'
).fetchall()
# [(2, 'Grace Hopper'), (1, 'Ada Lovelace')]

one = conn.execute(
    'SELECT name FROM users WHERE id = ?', (1,)
).fetchone()
# ('Ada Lovelace',)
```

- `fetchone()` — one row or `None`
- `fetchall()` — list of all rows
- `fetchmany(n)` — batch for large result sets

**Always use `?` placeholders** — never f-string SQL with user input:

```python
# DANGEROUS — SQL injection
conn.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# SAFE
conn.execute('SELECT * FROM users WHERE name = ?', (user_input,))
```

## Row factories

By default rows are tuples. Enable dict-like access:

```python
conn.row_factory = sqlite3.Row
row = conn.execute('SELECT * FROM users WHERE id = 1').fetchone()
row['name']   # 'Ada Lovelace'
row.keys()    # column names
dict(row)     # plain dict
```

Much easier to read than `row[1]` when you have many columns.

## Transactions

Wrap related writes so they succeed or fail together:

```python
with conn:
    conn.execute('INSERT INTO users (name) VALUES (?)', ('New User',))
    conn.execute('INSERT INTO audit_log (action) VALUES (?)', ('user_created',))
# commits on success, rolls back on exception — no explicit commit needed
```

On persistent connections outside `with conn:`, call `conn.commit()` after writes or changes are lost on close.

**Worked example:** transfer between accounts:

```python
def transfer(conn, from_id: int, to_id: int, amount: float) -> None:
    with conn:
        conn.execute(
            'UPDATE accounts SET balance = balance - ? WHERE id = ?',
            (amount, from_id),
        )
        conn.execute(
            'UPDATE accounts SET balance = balance + ? WHERE id = ?',
            (amount, to_id),
        )
    # both updates commit together or neither does
```

## Inserts and last row id

```python
cur = conn.execute('INSERT INTO users (name) VALUES (?)', ('Linus',))
new_id = cur.lastrowid
conn.commit()
```

## Updates and deletes

```python
conn.execute('UPDATE users SET name = ? WHERE id = ?', ('Ada L.', 1))
conn.execute('DELETE FROM users WHERE id = ?', (99,))
conn.commit()
```

Check `cur.rowcount` to see how many rows were affected.

## SQLite types (flexible typing)

SQLite uses dynamic typing — a column declared `INTEGER` can store text. Enforce types in your application layer or with `CHECK` constraints:

```sql
CREATE TABLE scores (
    value INTEGER CHECK(value >= 0 AND value <= 100)
);
```

Storage classes: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`.

## Real-world scenario: simple key-value cache

```python
def init_cache(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS cache (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            expires_at REAL
        )
    ''')

def cache_set(conn, key: str, value: str) -> None:
    conn.execute(
        'INSERT OR REPLACE INTO cache (key, value) VALUES (?, ?)',
        (key, value),
    )
    conn.commit()

def cache_get(conn, key: str) -> str | None:
    row = conn.execute('SELECT value FROM cache WHERE key = ?', (key,)).fetchone()
    return row[0] if row else None
```

## Common pitfalls

- Forgetting `commit()` on persistent connections
- SQL injection via string formatting
- Assuming strict column types — SQLite is permissive
- Sharing one connection across threads without `check_same_thread=False` (usually use one connection per thread)
- Not closing connections — use context managers or `conn.close()`
- Unique constraint violations — wrap inserts in try/except or use `INSERT OR IGNORE` / `INSERT OR REPLACE`

## Practice

Create a table, insert rows, query ordered results.

## Summary

sqlite3 = zero-config SQL in Python. Connect with `:memory:` for tests, use parameterized `?` queries, enable `row_factory` for readable rows, and wrap writes in `with conn:` transactions.
