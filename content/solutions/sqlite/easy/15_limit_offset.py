import sqlite3

def page_names(names: list[str], page: int, size: int) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE items (name TEXT)')
    conn.executemany('INSERT INTO items VALUES (?)', [(n,) for n in names])
    offset = (page - 1) * size
    rows = conn.execute(
        'SELECT name FROM items ORDER BY name LIMIT ? OFFSET ?',
        (size, offset),
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]
