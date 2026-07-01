# title: Grep Lines
# track: automations
# difficulty: easy
# tags: regex, io
# description: |
# Return lines from text that contain the substring (case-sensitive).
# examples:
# grep_lines("a\nb\na", "a") -> ["a","a"]
# hint: |
# Splitlines; filter if needle in line.
# syntax_hint: |
# [ln for ln in text.splitlines() if needle in ln]


def grep_lines(text: str, needle: str) -> list[str]:
    pass


def run_tests() -> None:
    assert grep_lines("a\nb\na", "a") == ["a", "a"]
    assert grep_lines("hello", "z") == []
    assert grep_lines("", "a") == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
