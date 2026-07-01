import sqlite3

def depts_over(rows: list[tuple[str, int]], threshold: int) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE t (dept TEXT, sales INTEGER)')
    conn.executemany('INSERT INTO t VALUES (?, ?)', rows)
    cur = conn.execute(
        'SELECT dept FROM t GROUP BY dept HAVING SUM(sales) > ? ORDER BY dept',
        (threshold,),
    )
    result = [r[0] for r in cur.fetchall()]
    conn.close()
    return result
