# title: REPLACE Upsert
# track: sqlite
# difficulty: medium
# tags: sqlite
# description: |
# Use REPLACE INTO kv(k,v) to set keys; return final value for key after all ops.
# examples:
# upsert_get([('a','1'),('a','2')], 'a') -> '2'
# hint: |
# REPLACE INTO is SQLite upsert by primary key.
# syntax_hint: |
# REPLACE INTO kv VALUES (?, ?)


def upsert_get(ops: list[tuple[str, str]], key: str) -> str | None:
    pass


def run_tests() -> None:
    assert upsert_get([('a', '1'), ('a', '2')], 'a') == '2'
    assert upsert_get([], 'x') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
