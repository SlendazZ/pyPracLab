# title: Slicing - Every Nth
# track: syntax
# difficulty: easy
# tags: slicing
# description: |
# Return every nth element of a list using slicing (0-indexed, starting at index 0).
# examples:
# every_nth([0,1,2,3,4,5], 2) -> [0,2,4]
# hint: |
# lst[::n] steps by n.
# syntax_hint: |
# lst[::n]


def every_nth(lst: list, n: int) -> list:
    pass


def run_tests() -> None:
    assert every_nth([0, 1, 2, 3, 4, 5], 2) == [0, 2, 4]
    assert every_nth([0, 1, 2, 3, 4, 5], 3) == [0, 3]
    assert every_nth([1], 1) == [1]
    assert every_nth([], 2) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
