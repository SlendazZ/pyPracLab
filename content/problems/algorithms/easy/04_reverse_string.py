# title: Reverse String
# track: algorithms
# difficulty: easy
# tags: two-pointers, array
# description: |
# Reverse a list of characters in place and return it.
# examples:
# reverse(['h','e','l','l','o']) -> ['o','l','l','e','h']
# hint: |
# Swap elements from both ends moving toward the middle.
# syntax_hint: |
# for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]


def reverse(s: list[str]) -> list[str]:
    pass


def run_tests() -> None:
    assert reverse(['h','e','l','l','o']) == ['o','l','l','e','h']
    assert reverse(['a','b']) == ['b','a']
    assert reverse([]) == []
    assert reverse(['x']) == ['x']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
