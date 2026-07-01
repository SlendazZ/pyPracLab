# title: Header Parser
# track: servers
# difficulty: easy
# tags: http, string
# description: |
# Parse raw header lines 'Key: Value' into a dict with lowercased keys.
# examples:
# parse_headers("Content-Type: json\nX-Trace: 1") -> {"content-type":"json","x-trace":"1"}
# hint: |
# Split each line on the first ': '.
# syntax_hint: |
# k, v = line.split(': ', 1); d[k.lower()] = v


def parse_headers(text: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    assert parse_headers("Content-Type: json\nX-Trace: 1") == {"content-type": "json", "x-trace": "1"}
    assert parse_headers("") == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
