import sqlite3

def as_dicts(names: list[str]) -> list[dict]:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.executemany('INSERT INTO users (name) VALUES (?)', [(n,) for n in names])
    rows = conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()
    conn.close()
    return [dict(r) for r in rows]
