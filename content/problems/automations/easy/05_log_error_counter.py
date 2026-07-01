# title: Log Error Counter
# track: automations
# difficulty: easy
# tags: string
# description: |
# Given multi-line log text, return the number of lines containing the word ERROR.
# examples:
# count_errors("INFO ok\nERROR bad\nERROR worse") -> 2
# hint: |
# Split into lines and count those containing 'ERROR'.
# syntax_hint: |
# sum('ERROR' in line for line in text.splitlines())


def count_errors(text: str) -> int:
    pass


def run_tests() -> None:
    assert count_errors("INFO ok\nERROR bad\nERROR worse") == 2
    assert count_errors("all good") == 0
    assert count_errors("") == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
