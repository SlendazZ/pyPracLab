# title: Daily Temperatures
# track: algorithms
# difficulty: medium
# tags: stack, array
# description: |
# For each day's temperature, return how many days until a warmer day, or 0.
# examples:
# daily([73,74,75,71,69,72,76,73]) -> [1,1,4,2,1,1,0,0]
# hint: |
# Monotonic decreasing stack of indices; pop when a warmer day arrives.
# syntax_hint: |
# stack = []; for i, t in enumerate(T): while stack and T[stack[-1]] < t: ...


def daily(temps: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert daily([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily([60, 50, 40]) == [0, 0, 0]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
