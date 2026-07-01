# title: Walrus Operator - Read Until Blank
# track: syntax
# difficulty: easy
# tags: walrus
# description: |
# Read lines from the iterator until a blank line appears; return the non-blank lines. Use the walrus operator.
# examples:
# read_until_blank(iter(["a","b","","c"])) -> ["a","b"]
# hint: |
# while (line := next(it, None)) is not None: stop on empty string.
# syntax_hint: |
# while (line := next(it, None)) is not None: if line == '': break


def read_until_blank(it) -> list[str]:
    pass


def run_tests() -> None:
    assert read_until_blank(iter(["a", "b", "", "c"])) == ["a", "b"]
    assert read_until_blank(iter(["x", "y"])) == ["x", "y"]
    assert read_until_blank(iter([])) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
