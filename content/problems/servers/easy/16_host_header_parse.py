# title: Host Header Parse
# track: servers
# difficulty: easy
# tags: http, headers
# description: |
# Parse a Host header value into (hostname, port). Default port 80 when omitted.
# examples:
# parse_host('api.test:8080') -> ('api.test', 8080)
# hint: |
# Split on ':' once; int port or default 80.
# syntax_hint: |
# host, _, port = value.partition(':'); int(port) if port else 80


def parse_host(value: str) -> tuple[str, int]:
    pass


def run_tests() -> None:
    assert parse_host('api.test:8080') == ('api.test', 8080)
    assert parse_host('localhost') == ('localhost', 80)
    assert parse_host('x.test:443') == ('x.test', 443)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
