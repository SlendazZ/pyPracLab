# title: Rotate Lines
# track: automations
# difficulty: easy
# tags: string
# description: |
# Rotate lines of text up by k (k=1 moves first line to end).
# examples:
# rotate_lines("a\nb\nc", 1) -> "b\nc\na"
# hint: |
# lines = text.splitlines(); lines[k:]+lines[:k]
# syntax_hint: |
# lines = text.splitlines()


def rotate_lines(text: str, k: int) -> str:
    pass


def run_tests() -> None:
    assert rotate_lines("a\nb\nc", 1) == "b\nc\na"
    assert rotate_lines("a\nb", 2) == "a\nb"
    assert rotate_lines("", 3) == ""
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
