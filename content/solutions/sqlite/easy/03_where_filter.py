import sqlite3

def above(values: list[int], threshold: int) -> list[int]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE nums (val INTEGER)')
    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])
    rows = conn.execute('SELECT val FROM nums WHERE val > ? ORDER BY val', (threshold,)).fetchall()
    conn.close()
    return [r[0] for r in rows]
