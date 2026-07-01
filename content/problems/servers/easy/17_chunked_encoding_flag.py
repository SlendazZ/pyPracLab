# title: Chunked Encoding Flag
# track: servers
# difficulty: easy
# tags: http, headers
# description: |
# Return True if headers dict indicates chunked Transfer-Encoding (case-insensitive).
# examples:
# is_chunked({'Transfer-Encoding': 'chunked'}) -> True
# hint: |
# Check Transfer-Encoding header for 'chunked' substring.
# syntax_hint: |
# 'chunked' in headers.get('Transfer-Encoding', '').lower()


def is_chunked(headers: dict[str, str]) -> bool:
    pass


def run_tests() -> None:
    assert is_chunked({'Transfer-Encoding': 'chunked'}) is True
    assert is_chunked({'Transfer-Encoding': 'gzip, chunked'}) is True
    assert is_chunked({'Content-Length': '10'}) is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
