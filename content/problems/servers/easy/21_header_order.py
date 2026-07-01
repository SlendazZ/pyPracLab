# title: Canonical Header Order
# track: servers
# difficulty: easy
# tags: http, headers
# description: |
# Return headers reordered by canonical name (case-insensitive sort), preserving original casing of values.
# examples:
# order_headers({'B':'2','A':'1'}) -> [('A','1'),('B','2')]
# hint: |
# Sort items by key.lower().
# syntax_hint: |
# sorted(headers.items(), key=lambda kv: kv[0].lower())


def order_headers(headers: dict[str, str]) -> list[tuple[str, str]]:
    pass


def run_tests() -> None:
    assert order_headers({'B': '2', 'A': '1'}) == [('A', '1'), ('B', '2')]
    assert order_headers({}) == []
    assert order_headers({'z': '1', 'a': '2'})[0][0] == 'a'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
