# title: Unpacking - Head and Tail
# track: syntax
# difficulty: easy
# tags: unpacking
# description: |
# Return (first, rest) where rest is a list of the remaining elements, using unpacking.
# examples:
# head_tail([1,2,3,4]) -> (1, [2,3,4])
# hint: |
# first, *rest = items unpacks the head from the tail.
# syntax_hint: |
# first, *rest = items; return first, rest


def head_tail(items: list) -> tuple:
    pass


def run_tests() -> None:
    assert head_tail([1, 2, 3, 4]) == (1, [2, 3, 4])
    assert head_tail(['a']) == ('a', [])
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
