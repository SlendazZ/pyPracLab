import sqlite3

def label_scores(scores: list[int]) -> list[str]:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE t (score INTEGER)')
    conn.executemany('INSERT INTO t VALUES (?)', [(s,) for s in scores])
    rows = conn.execute(
        "SELECT CASE WHEN score >= 60 THEN 'pass' ELSE 'fail' END FROM t"
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]
