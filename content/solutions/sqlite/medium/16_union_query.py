import sqlite3

def union_names(list_a: list[str], list_b: list[str]) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE a (name TEXT)')
    conn.execute('CREATE TABLE b (name TEXT)')
    conn.executemany('INSERT INTO a VALUES (?)', [(n,) for n in list_a])
    conn.executemany('INSERT INTO b VALUES (?)', [(n,) for n in list_b])
    rows = conn.execute(
        'SELECT name FROM a UNION SELECT name FROM b ORDER BY name'
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]
