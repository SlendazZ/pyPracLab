import sqlite3

def query_users(names: list[str]) -> list[tuple]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.executemany('INSERT INTO users (name) VALUES (?)', [(n,) for n in names])
    rows = conn.execute('SELECT id, name FROM users ORDER BY name').fetchall()
    conn.close()
    return rows
