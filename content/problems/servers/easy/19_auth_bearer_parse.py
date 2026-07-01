# title: Bearer Token Parse
# track: servers
# difficulty: easy
# tags: auth, http
# description: |
# Extract the bearer token from an Authorization header, or None if missing/invalid.
# examples:
# bearer_token('Bearer abc123') -> 'abc123'
# hint: |
# Split on space; require scheme Bearer (case-insensitive).
# syntax_hint: |
# parts = header.split(); scheme.lower() == 'bearer'


def bearer_token(header: str) -> str | None:
    pass


def run_tests() -> None:
    assert bearer_token('Bearer abc123') == 'abc123'
    assert bearer_token('bearer xyz') == 'xyz'
    assert bearer_token('Basic abc') is None
    assert bearer_token('') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
