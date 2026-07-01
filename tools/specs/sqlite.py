"""sqlite problem specs."""

PROBLEMS = [
    {
        "slug": "01_create_insert_query",
        "track": "sqlite", "difficulty": "easy",
        "title": "Create, Insert, Query",
        "tags": ["sqlite", "sql"],
        "description": "Create an in-memory sqlite3 db with table users(id INTEGER PRIMARY KEY, name TEXT), insert the given names, and return (id, name) rows ordered by name.",
        "examples": 'query_users(["bob", "alice"]) -> [(2, "alice"), (1, "bob")]',
        "hint": "sqlite3.connect(':memory:'); CREATE, INSERT, SELECT; fetchall().",
        "syntax_hint": "conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()",
        "signature": "def query_users(names: list[str]) -> list[tuple]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert query_users(["bob", "alice"]) == [(2, "alice"), (1, "bob")]\n'
            '    assert query_users([]) == []\n'
            '    assert query_users(["zoe"]) == [(1, "zoe")]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def query_users(names: list[str]) -> list[tuple]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\n"
            "    conn.executemany('INSERT INTO users (name) VALUES (?)', [(n,) for n in names])\n"
            "    rows = conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()\n"
            "    conn.close()\n"
            "    return rows\n"
        ),
    },
    {
        "slug": "02_count_rows",
        "track": "sqlite", "difficulty": "easy",
        "title": "Count Rows",
        "tags": ["sqlite", "sql"],
        "description": "Create an in-memory db, insert the given integers into a table 'nums(val)', and return COUNT(*).",
        "examples": "count_rows([1, 2, 3]) -> 3",
        "hint": "SELECT COUNT(*) returns one row; fetchone()[0].",
        "syntax_hint": "conn.execute('SELECT COUNT(*) FROM nums').fetchone()[0]",
        "signature": "def count_rows(values: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert count_rows([1, 2, 3]) == 3\n"
            "    assert count_rows([]) == 0\n"
            "    assert count_rows([5]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def count_rows(values: list[int]) -> int:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE nums (val INTEGER)')\n"
            "    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])\n"
            "    n = conn.execute('SELECT COUNT(*) FROM nums').fetchone()[0]\n"
            "    conn.close()\n"
            "    return n\n"
        ),
    },
    {
        "slug": "03_where_filter",
        "track": "sqlite", "difficulty": "easy",
        "title": "WHERE Filter",
        "tags": ["sqlite", "sql"],
        "description": "Create an in-memory db with nums(val), insert the values, and return those strictly greater than threshold (ascending).",
        "examples": "above([1, 5, 2, 7], 3) -> [5, 7]",
        "hint": "SELECT val FROM nums WHERE val > ? ORDER BY val.",
        "syntax_hint": "conn.execute('SELECT val FROM nums WHERE val > ? ORDER BY val', (threshold,))",
        "signature": "def above(values: list[int], threshold: int) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert above([1, 5, 2, 7], 3) == [5, 7]\n"
            "    assert above([1, 2], 5) == []\n"
            "    assert above([], 0) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def above(values: list[int], threshold: int) -> list[int]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE nums (val INTEGER)')\n"
            "    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])\n"
            "    rows = conn.execute('SELECT val FROM nums WHERE val > ? ORDER BY val', (threshold,)).fetchall()\n"
            "    conn.close()\n"
            "    return [r[0] for r in rows]\n"
        ),
    },
    {
        "slug": "04_aggregate_avg",
        "track": "sqlite", "difficulty": "easy",
        "title": "Average via SQL",
        "tags": ["sqlite", "sql"],
        "description": "Insert the given values into nums(val) and return AVG(val) as a float (0.0 for empty).",
        "examples": "average([2, 4, 6]) -> 4.0",
        "hint": "SELECT AVG(val); fetchone()[0] is None when empty.",
        "syntax_hint": "conn.execute('SELECT AVG(val) FROM nums').fetchone()[0]",
        "signature": "def average(values: list[int]) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert average([2, 4, 6]) == 4.0\n"
            "    assert average([10]) == 10.0\n"
            "    assert average([]) == 0.0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def average(values: list[int]) -> float:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE nums (val INTEGER)')\n"
            "    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])\n"
            "    result = conn.execute('SELECT AVG(val) FROM nums').fetchone()[0]\n"
            "    conn.close()\n"
            "    return float(result) if result is not None else 0.0\n"
        ),
    },
    {
        "slug": "05_named_params",
        "track": "sqlite", "difficulty": "medium",
        "title": "Named Parameters",
        "tags": ["sqlite", "sql"],
        "description": "Insert one row with named parameters into a people(name, age) table and return that single row as a dict {name, age}.",
        "examples": "insert_one('eli', 30) -> {'name': 'eli', 'age': 30}",
        "hint": "Use :name and :age placeholders and a dict params.",
        "syntax_hint": "conn.execute('INSERT INTO people VALUES (:name, :age)', {'name': name, 'age': age})",
        "signature": "def insert_one(name: str, age: int) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert insert_one('eli', 30) == {'name': 'eli', 'age': 30}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def insert_one(name: str, age: int) -> dict:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE people (name TEXT, age INTEGER)')\n"
            "    conn.execute('INSERT INTO people VALUES (:name, :age)', {'name': name, 'age': age})\n"
            "    row = conn.execute('SELECT name, age FROM people').fetchone()\n"
            "    conn.close()\n"
            "    return {'name': row[0], 'age': row[1]}\n"
        ),
    },
    {
        "slug": "06_row_factory",
        "track": "sqlite", "difficulty": "medium",
        "title": "Row Factory",
        "tags": ["sqlite", "sql"],
        "description": "Create an in-memory db with users(id, name), insert the given names, and return rows as dicts using sqlite3.Row (ordered by name).",
        "examples": "as_dicts(['a','b']) -> [{'id':1,'name':'a'},{'id':2,'name':'b'}]",
        "hint": "Set conn.row_factory = sqlite3.Row; dict(row) gives a dict.",
        "syntax_hint": "conn.row_factory = sqlite3.Row; [dict(r) for r in rows]",
        "signature": "def as_dicts(names: list[str]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    out = as_dicts(['a', 'b'])\n"
            "    assert out == [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]\n"
            "    assert as_dicts([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def as_dicts(names: list[str]) -> list[dict]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.row_factory = sqlite3.Row\n"
            "    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\n"
            "    conn.executemany('INSERT INTO users (name) VALUES (?)', [(n,) for n in names])\n"
            "    rows = conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()\n"
            "    conn.close()\n"
            "    return [dict(r) for r in rows]\n"
        ),
    },
    {
        "slug": "07_update_row",
        "track": "sqlite", "difficulty": "medium",
        "title": "Update a Row",
        "tags": ["sqlite", "sql"],
        "description": "Create a people(id, name) table, insert ('1','old'), UPDATE the name to 'new' where id=1, and return the resulting name.",
        "examples": "update_name() -> 'new'",
        "hint": "UPDATE people SET name=? WHERE id=?.",
        "syntax_hint": "conn.execute('UPDATE people SET name=? WHERE id=?', ('new', 1))",
        "signature": "def update_name() -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert update_name() == 'new'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def update_name() -> str:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE people (id INTEGER, name TEXT)')\n"
            "    conn.execute(\"INSERT INTO people VALUES (1, 'old')\")\n"
            "    conn.execute('UPDATE people SET name=? WHERE id=?', ('new', 1))\n"
            "    name = conn.execute('SELECT name FROM people WHERE id=1').fetchone()[0]\n"
            "    conn.close()\n"
            "    return name\n"
        ),
    },
    {
        "slug": "08_transaction_rollback",
        "track": "sqlite", "difficulty": "hard",
        "title": "Transaction Rollback",
        "tags": ["sqlite", "sql"],
        "description": "Insert 'a', then inside a try/except insert 'b' and raise; roll back on error. Return the list of names left in the table (should be just ['a']).",
        "examples": "with_rollback() -> ['a']",
        "hint": "Use conn as a context manager: with conn: ... to get automatic rollback on exception.",
        "syntax_hint": "try: with conn: conn.execute(...); raise ValueError; except: pass",
        "signature": "def with_rollback() -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert with_rollback() == ['a']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def with_rollback() -> list[str]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE items (name TEXT)')\n"
            "    conn.execute(\"INSERT INTO items VALUES ('a')\")\n"
            "    conn.commit()\n"
            "    try:\n"
            "        with conn:\n"
            "            conn.execute(\"INSERT INTO items VALUES ('b')\")\n"
            "            raise ValueError('boom')\n"
            "    except ValueError:\n"
            "        pass\n"
            "    rows = conn.execute('SELECT name FROM items ORDER BY name').fetchall()\n"
            "    conn.close()\n"
            "    return [r[0] for r in rows]\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_sqlite_intro",
        "track": "sqlite", "difficulty": "easy",
        "title": "sqlite3 In-Memory",
        "tags": ["sqlite", "sql"],
        "exercise": "content/problems/sqlite/easy/01_create_insert_query.py",
        "body": (
            "# sqlite3\n\n"
            "`sqlite3` is in the standard library. Use `:memory:` for fast, throwaway "
            "databases in tests:\n\n"
            "```python\nimport sqlite3\nconn = sqlite3.connect(':memory:')\n"
            "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\n"
            "conn.executemany('INSERT INTO users (name) VALUES (?)', [('a',), ('b',)])\n"
            "rows = conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()\n```\n\n"
            "Always use `?` placeholders to avoid SQL injection. Use `with conn:` to wrap "
            "a transaction (it rolls back automatically on exception)."
        ),
    },
]
