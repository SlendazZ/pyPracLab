# title: List Comprehension - Evens
# track: syntax
# difficulty: easy
# tags: comprehension, list
# description: |
# Return a list of the even numbers from the input list, squared, using a list comprehension.
# examples:
# even_squares([1,2,3,4]) -> [4,16]
# hint: |
# Filter with `if x % 2 == 0` inside the comprehension, then square.
# syntax_hint: |
# [x * x for x in numbers if x % 2 == 0]


def even_squares(numbers: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert even_squares([1, 2, 3, 4]) == [4, 16]
    assert even_squares([2, 4]) == [4, 16]
    assert even_squares([1, 3, 5]) == []
    assert even_squares([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
