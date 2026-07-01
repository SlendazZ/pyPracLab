import sqlite3

def with_rollback() -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE items (name TEXT)')
    conn.execute("INSERT INTO items VALUES ('a')")
    conn.commit()
    try:
        with conn:
            conn.execute("INSERT INTO items VALUES ('b')")
            raise ValueError('boom')
    except ValueError:
        pass
    rows = conn.execute('SELECT name FROM items ORDER BY name').fetchall()
    conn.close()
    return [r[0] for r in rows]
