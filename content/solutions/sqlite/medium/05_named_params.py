import sqlite3

def insert_one(name: str, age: int) -> dict:
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE people (name TEXT, age INTEGER)')
    conn.execute('INSERT INTO people VALUES (:name, :age)', {'name': name, 'age': age})
    row = conn.execute('SELECT name, age FROM people').fetchone()
    conn.close()
    return {'name': row[0], 'age': row[1]}
