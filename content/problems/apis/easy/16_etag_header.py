# title: ETag Header
# track: apis
# difficulty: easy
# tags: http, hash
# description: |
# Given response body bytes, return an ETag string: double-quoted MD5 hex digest.
# examples:
# make_etag(b'hello') -> '"5d41402abc4b2a76b9719d911017c592"'
# hint: |
# hashlib.md5(body).hexdigest() wrapped in quotes.
# syntax_hint: |
# return f'"{hashlib.md5(body).hexdigest()}"'


def make_etag(body: bytes) -> str:
    pass


def run_tests() -> None:
    assert make_etag(b'hello') == '"5d41402abc4b2a76b9719d911017c592"'
    assert make_etag(b'') == '"d41d8cd98f00b204e9800998ecf8427e"'
    assert make_etag(b'hello').startswith('"')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
