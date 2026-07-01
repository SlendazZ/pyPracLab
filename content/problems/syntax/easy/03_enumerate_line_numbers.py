# title: Enumerate - Line Numbers
# track: syntax
# difficulty: easy
# tags: enumerate, string
# description: |
# Given a list of lines, return a list of strings like '1: line' using enumerate starting at 1.
# examples:
# number_lines(["a","b"]) -> ["1: a","2: b"]
# hint: |
# enumerate(lines, start=1) yields (index, value).
# syntax_hint: |
# f"{i}: {line}" for i, line in enumerate(lines, start=1)


def number_lines(lines: list[str]) -> list[str]:
    pass


def run_tests() -> None:
    assert number_lines(["a", "b"]) == ["1: a", "2: b"]
    assert number_lines([]) == []
    assert number_lines(["only"]) == ["1: only"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
