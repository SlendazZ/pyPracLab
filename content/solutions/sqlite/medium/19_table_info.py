import sqlite3

def table_columns(columns: dict[str, str]) -> list[str]:
    conn = sqlite3.connect(':memory:')
    parts = ', '.join(f'{name} {ctype}' for name, ctype in columns.items())
    conn.execute(f'CREATE TABLE users ({parts})')
    rows = conn.execute('PRAGMA table_info(users)').fetchall()
    conn.close()
    return [r[1] for r in rows]
