# title: Find Duplicate Lines
# track: automations
# difficulty: medium
# tags: set, io
# description: |
# Return the set of lines that appear more than once in a multi-line string (stripped).
# examples:
# dup_lines("a\nb\na\nc") -> {"a"}
# hint: |
# Count lines; keep those with count > 1.
# syntax_hint: |
# from collections import Counter; {l for l, c in Counter(lines).items() if c > 1}


def dup_lines(text: str) -> set[str]:
    pass


def run_tests() -> None:
    assert dup_lines("a\nb\na\nc") == {"a"}
    assert dup_lines("one\ntwo") == set()
    assert dup_lines("x\nx\ny\ny") == {"x", "y"}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
