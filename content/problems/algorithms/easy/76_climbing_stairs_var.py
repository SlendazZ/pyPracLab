# title: Min Cost Climbing Stairs
# track: algorithms
# difficulty: easy
# tags: dp, array
# description: |
# Each step has cost; can climb 1 or 2 steps from index 0 or 1. Return min cost to reach top beyond last index.
# examples:
# min_cost([10,15,20]) -> 15
# hint: |
# Same recurrence as climbing stairs but take min not sum.
# syntax_hint: |
# a, b = 0, 0; for c in cost: a, b = b, min(a,b)+c


def min_cost(cost: list[int]) -> int:
    pass


def run_tests() -> None:
    assert min_cost([10, 15, 20]) == 15
    assert min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost([0, 0, 0, 1]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
