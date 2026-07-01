# title: LIKE Search
# track: sqlite
# difficulty: easy
# tags: sqlite
# description: |
# Insert words into a words(name) table and return names matching LIKE pattern.
# examples:
# search(["cat","cart","dog"], "ca%") -> ["cat","cart"]
# hint: |
# SELECT ... WHERE name LIKE ?
# syntax_hint: |
# conn.execute('SELECT name FROM words WHERE name LIKE ?', (pat,))


def search(words: list[str], pattern: str) -> list[str]:
    pass


def run_tests() -> None:
    assert search(["cat", "cart", "dog"], "ca%") == ["cart", "cat"]
    assert search([], 'a%') == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
