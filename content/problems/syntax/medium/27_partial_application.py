# title: Partial Application
# track: syntax
# difficulty: medium
# tags: functools
# description: |
# Return a function add_n(n) that returns a function adding n to its argument.
# examples:
# add5 = add_n(5); add5(3) -> 8
# hint: |
# functools.partial or closure.
# syntax_hint: |
# def add_n(n): return lambda x: x + n


def add_n(n: int):
    pass


def run_tests() -> None:
    add5 = add_n(5)
    assert add5(3) == 8
    assert add_n(0)(10) == 10
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
