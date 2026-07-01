# title: any() and all() - Checks
# track: syntax
# difficulty: easy
# tags: any, all
# description: |
# Return (has_negatives, all_positive): whether any number is negative, and whether all are strictly positive.
# examples:
# check([1,2,-3]) -> (True, False)
# check([1,2]) -> (False, True)
# hint: |
# any(x < 0 for x in nums); all(x > 0 for x in nums).
# syntax_hint: |
# any() short-circuits on True; all() short-circuits on False.


def check(nums: list[int]) -> tuple[bool, bool]:
    pass


def run_tests() -> None:
    assert check([1, 2, -3]) == (True, False)
    assert check([1, 2]) == (False, True)
    assert check([]) == (False, True)
    assert check([-1]) == (True, False)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
