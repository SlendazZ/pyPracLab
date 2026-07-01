import sqlite3

def search(words: list[str], pattern: str) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE words (name TEXT)')
    conn.executemany('INSERT INTO words VALUES (?)', [(w,) for w in words])
    rows = conn.execute('SELECT name FROM words WHERE name LIKE ? ORDER BY name', (pattern,)).fetchall()
    conn.close()
    return [r[0] for r in rows]
