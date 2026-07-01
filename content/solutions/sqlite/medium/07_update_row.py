import sqlite3

def update_name() -> str:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE people (id INTEGER, name TEXT)')
    conn.execute("INSERT INTO people VALUES (1, 'old')")
    conn.execute('UPDATE people SET name=? WHERE id=?', ('new', 1))
    name = conn.execute('SELECT name FROM people WHERE id=1').fetchone()[0]
    conn.close()
    return name
