import sqlite3

def upsert_get(ops: list[tuple[str, str]], key: str) -> str | None:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE kv (k TEXT PRIMARY KEY, v TEXT)')
    for k, v in ops:
        conn.execute('REPLACE INTO kv VALUES (?, ?)', (k, v))
    row = conn.execute('SELECT v FROM kv WHERE k=?', (key,)).fetchone()
    conn.close()
    return row[0] if row else None
