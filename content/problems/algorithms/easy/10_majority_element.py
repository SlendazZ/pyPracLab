# title: Majority Element
# track: algorithms
# difficulty: easy
# tags: boyer-moore
# description: |
# A majority element appears more than n//2 times. Return it.
# examples:
# majority([3,2,3]) -> 3
# majority([2,2,1,1,1,2,2]) -> 2
# hint: |
# Use Boyer-Moore voting — keep a candidate and a count; +1 on match, -1 otherwise; reset when count hits 0.
# syntax_hint: |
# for x in nums: if count == 0: candidate = x; count += 1 if x==candidate else -1


def majority(nums: list[int]) -> int:
    pass


def run_tests() -> None:
    assert majority([3, 2, 3]) == 3
    assert majority([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority([1]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
