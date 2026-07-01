import sqlite3

def distinct_count(names: list[str]) -> int:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE tags (name TEXT)')
    conn.executemany('INSERT INTO tags VALUES (?)', [(n,) for n in names])
    n = conn.execute('SELECT COUNT(DISTINCT name) FROM tags').fetchone()[0]
    conn.close()
    return n
