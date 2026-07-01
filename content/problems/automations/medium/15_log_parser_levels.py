# title: Count Log Levels
# track: automations
# difficulty: medium
# tags: log, parse
# description: |
# Given log lines like '2024-01-01 ERROR msg', count lines per level (ERROR, WARN, INFO). Unknown levels ignored.
# examples:
# count_levels(lines) -> {'ERROR':1,'INFO':2}
# hint: |
# Split line, second token is level.
# syntax_hint: |
# from collections import Counter


def count_levels(lines: list[str]) -> dict[str, int]:
    pass


def run_tests() -> None:
    lines = ["2024 ERROR x", "2024 INFO y", "2024 INFO z", "2024 DEBUG w"]
    assert count_levels(lines) == {'ERROR': 1, 'INFO': 2}
    assert count_levels([]) == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
