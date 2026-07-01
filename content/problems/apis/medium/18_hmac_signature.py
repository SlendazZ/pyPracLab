# title: HMAC Signature
# track: apis
# difficulty: medium
# tags: crypto, api
# description: |
# Return the hex HMAC-SHA256 digest of message using the given secret key (both as str, UTF-8 encoded).
# examples:
# sign('payload', 'secret') -> hex digest string
# hint: |
# hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()
# syntax_hint: |
# import hmac, hashlib; hmac.new(key.encode(), msg.encode(), 'sha256').hexdigest()


def sign(message: str, secret: str) -> str:
    pass


def run_tests() -> None:
    assert sign('payload', 'secret') == sign('payload', 'secret')
    assert sign('a', 'k') != sign('b', 'k')
    assert len(sign('x', 'y')) == 64
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
