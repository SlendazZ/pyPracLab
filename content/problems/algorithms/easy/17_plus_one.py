# title: Plus One
# track: algorithms
# difficulty: easy
# tags: array, math
# description: |
# A non-empty list of digits represents a number. Return the list of digits after adding one.
# examples:
# plus_one([1,2,3]) -> [1,2,4]
# plus_one([9,9]) -> [1,0,0]
# hint: |
# Add from the last digit, carrying over 9s.
# syntax_hint: |
# for i in reversed(range(len(d))): if d[i] == 9: d[i] = 0 else: d[i]+=1; return d


def plus_one(digits: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([9, 9]) == [1, 0, 0]
    assert plus_one([0]) == [1]
    assert plus_one([1, 9, 9]) == [2, 0, 0]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
