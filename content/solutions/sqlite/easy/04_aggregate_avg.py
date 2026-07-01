import sqlite3

def average(values: list[int]) -> float:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE nums (val INTEGER)')
    conn.executemany('INSERT INTO nums VALUES (?)', [(v,) for v in values])
    result = conn.execute('SELECT AVG(val) FROM nums').fetchone()[0]
    conn.close()
    return float(result) if result is not None else 0.0
