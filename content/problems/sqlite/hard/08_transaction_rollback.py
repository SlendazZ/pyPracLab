# title: Transaction Rollback
# track: sqlite
# difficulty: hard
# tags: sqlite, sql
# description: |
# Insert 'a', then inside a try/except insert 'b' and raise; roll back on error. Return the list of names left in the table (should be just ['a']).
# examples:
# with_rollback() -> ['a']
# hint: |
# Use conn as a context manager: with conn: ... to get automatic rollback on exception.
# syntax_hint: |
# try: with conn: conn.execute(...); raise ValueError; except: pass


def with_rollback() -> list[str]:
    pass


def run_tests() -> None:
    assert with_rollback() == ['a']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
