# title: Parse Query String
# track: servers
# difficulty: easy
# tags: url
# description: |
# Parse a query string 'a=1&b=2' into a dict. Return {} for an empty string.
# examples:
# parse_qs("a=1&b=2") -> {"a":"1","b":"2"}
# hint: |
# urllib.parse.parse_qs returns lists; or split on '&' and '='.
# syntax_hint: |
# from urllib.parse import parse_qs; {k: v[0] for k, v in parse_qs(q).items()}


def parse_qs(q: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    assert parse_qs("a=1&b=2") == {"a": "1", "b": "2"}
    assert parse_qs("") == {}
    assert parse_qs("single=5") == {"single": "5"}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
