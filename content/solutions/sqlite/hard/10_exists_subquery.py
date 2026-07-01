import sqlite3

def with_orders(entries: list[tuple[str, bool]]) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute('CREATE TABLE orders (user_id INTEGER)')
    for name, has_order in entries:
        cur = conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
        uid = cur.lastrowid
        if has_order:
            conn.execute('INSERT INTO orders (user_id) VALUES (?)', (uid,))
    q = '''SELECT name FROM users u
           WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id)
           ORDER BY name'''
    rows = [r[0] for r in conn.execute(q).fetchall()]
    conn.close()
    return rows
