# title: Key-Value Parser
# track: automations
# difficulty: easy
# tags: string
# description: |
# Parse lines 'key=value' into a dict. Skip blank lines and lines without '='.
# examples:
# parse_kv("a=1\nb=2\n# no") -> {"a":"1","b":"2"}
# hint: |
# line.split('=', 1) gives key and value.
# syntax_hint: |
# if '=' in line: k, v = line.split('=', 1); d[k.strip()] = v.strip()


def parse_kv(text: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    assert parse_kv("a=1\nb=2\n# no") == {"a": "1", "b": "2"}
    assert parse_kv("name = eli") == {"name": "eli"}
    assert parse_kv("") == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
