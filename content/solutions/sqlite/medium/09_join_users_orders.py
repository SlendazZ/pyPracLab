import sqlite3

def totals(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute('CREATE TABLE orders (user_id INTEGER, amount REAL)')
    name_to_id = {}
    for name, amount in rows:
        if name not in name_to_id:
            cur = conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
            name_to_id[name] = cur.lastrowid
        conn.execute('INSERT INTO orders VALUES (?, ?)', (name_to_id[name], amount))
    q = '''SELECT u.name, SUM(o.amount) FROM users u
           JOIN orders o ON u.id = o.user_id GROUP BY u.name ORDER BY u.name'''
    result = conn.execute(q).fetchall()
    conn.close()
    return [(r[0], float(r[1])) for r in result]
