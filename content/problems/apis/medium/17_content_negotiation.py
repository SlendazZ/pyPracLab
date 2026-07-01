# title: Content Negotiation
# track: apis
# difficulty: medium
# tags: http, headers
# description: |
# Given an Accept header string and a list of offered MIME types, return the best matching offered type or None.
# examples:
# pick_type('application/json, text/plain', ['text/html','application/json']) -> 'application/json'
# hint: |
# Parse Accept by comma; prefer exact MIME matches in listed order.
# syntax_hint: |
# for offered in types: if offered in accept_parts: return offered


def pick_type(accept: str, offered: list[str]) -> str | None:
    pass


def run_tests() -> None:
    assert pick_type('application/json, text/plain', ['text/html', 'application/json']) == 'application/json'
    assert pick_type('text/plain', ['application/json']) is None
    assert pick_type('text/html', ['text/html', 'text/plain']) == 'text/html'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
