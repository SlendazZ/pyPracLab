# title: LIMIT OFFSET Page
# track: sqlite
# difficulty: easy
# tags: sqlite, sql
# description: |
# Query items(name) with ORDER BY name LIMIT size OFFSET (page-1)*size; page is 1-based.
# examples:
# page_names(names, page=2, size=2) -> third and fourth names
# hint: |
# OFFSET (page-1)*size LIMIT size
# syntax_hint: |
# ORDER BY name LIMIT ? OFFSET ?


def page_names(names: list[str], page: int, size: int) -> list[str]:
    pass


def run_tests() -> None:
    names = ['a', 'b', 'c', 'd', 'e']
    assert page_names(names, 1, 2) == ['a', 'b']
    assert page_names(names, 2, 2) == ['c', 'd']
    assert page_names(names, 3, 2) == ['e']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
