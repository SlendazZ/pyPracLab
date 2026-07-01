# title: Generator - Batches
# track: syntax
# difficulty: medium
# tags: generator
# description: |
# Write a generator that yields successive sublists of size n from a list (the last batch may be smaller).
# examples:
# list(batches([1,2,3,4,5], 2)) -> [[1,2],[3,4],[5]]
# hint: |
# yield items[i:i+n] in a loop; slicing handles the remainder.
# syntax_hint: |
# for i in range(0, len(items), n): yield items[i:i+n]


def batches(items: list, n: int):
    pass


def run_tests() -> None:
    assert list(batches([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(batches([1, 2], 5)) == [[1, 2]]
    assert list(batches([], 2)) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
