# title: JSON Key Count
# track: automations
# difficulty: easy
# tags: json
# description: |
# Parse JSON object string and return number of top-level keys.
# examples:
# key_count('{"a":1,"b":2}') -> 2
# hint: |
# len(json.loads(s)) for objects.
# syntax_hint: |
# len(json.loads(text))


def key_count(text: str) -> int:
    pass


def run_tests() -> None:
    assert key_count('{"a": 1, "b": 2}') == 2
    assert key_count("{}") == 0
    assert key_count('{"x": []}') == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
