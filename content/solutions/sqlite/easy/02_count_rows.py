import sqlite3

def count_rows(values: list[int]) -> int:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE nums (val INTEGER)')
    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])
    n = conn.execute('SELECT COUNT(*) FROM nums').fetchone()[0]
    conn.close()
    return n
