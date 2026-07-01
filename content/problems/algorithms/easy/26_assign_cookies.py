# title: Assign Cookies
# track: algorithms
# difficulty: easy
# tags: greedy, two-pointers
# description: |
# Each child i is content if given a cookie with size >= greed[i]. Return the max number of content children.
# examples:
# assign([1,2,3],[1,1]) -> 1
# assign([1,2],[1,2,3]) -> 2
# hint: |
# Sort both; give the smallest sufficient cookie to each child.
# syntax_hint: |
# g.sort(); s.sort(); i = j = 0; while ...


def assign(greed: list[int], size: list[int]) -> int:
    pass


def run_tests() -> None:
    assert assign([1, 2, 3], [1, 1]) == 1
    assert assign([1, 2], [1, 2, 3]) == 2
    assert assign([], [1]) == 0
    assert assign([1], []) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
