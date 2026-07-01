# title: itertools.chain - Flatten
# track: syntax
# difficulty: easy
# tags: itertools
# description: |
# Flatten a list of lists into one list using itertools.chain.
# examples:
# flatten([[1,2],[3],[4,5]]) -> [1,2,3,4,5]
# hint: |
# itertools.chain.from_iterable chains an iterable of iterables.
# syntax_hint: |
# from itertools import chain; list(chain.from_iterable(items))


def flatten(items: list[list]) -> list:
    pass


def run_tests() -> None:
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[], [1]]) == [1]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
