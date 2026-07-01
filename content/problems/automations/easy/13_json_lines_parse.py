# title: Parse JSON Lines
# track: automations
# difficulty: easy
# tags: json, file
# description: |
# Given a string with one JSON object per line, return a list of parsed dicts (skip blank lines).
# examples:
# parse_jsonl("{\"a\":1}\n{\"b\":2}") -> [{"a":1},{"b":2}]
# hint: |
# Splitlines, json.loads each non-empty line.
# syntax_hint: |
# [json.loads(line) for line in text.splitlines() if line.strip()]


def parse_jsonl(text: str) -> list[dict]:
    pass


def run_tests() -> None:
    assert parse_jsonl('{"a":1}\n{"b":2}') == [{"a":1},{"b":2}]
    assert parse_jsonl("") == []
    assert parse_jsonl("\n\n") == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
