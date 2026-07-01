# title: Nested JSON Get
# track: apis
# difficulty: easy
# tags: json
# description: |
# Parse JSON text and return data['user']['name'] or None if missing.
# examples:
# user_name('{"user":{"name":"eli"}}') -> "eli"
# hint: |
# json.loads then chained .get calls.
# syntax_hint: |
# obj.get('user', {}).get('name')


def user_name(text: str) -> str | None:
    pass


def run_tests() -> None:
    assert user_name('{"user":{"name":"eli"}}') == "eli"
    assert user_name('{"user":{}}') is None
    assert user_name("{}") is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
