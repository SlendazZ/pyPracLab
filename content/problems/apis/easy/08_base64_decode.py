# title: Base64 Decode
# track: apis
# difficulty: easy
# tags: base64
# description: |
# Given a base64 string, return the decoded bytes.
# examples:
# decode('aGk=') -> b'hi'
# hint: |
# base64.b64decode decodes a base64 string.
# syntax_hint: |
# import base64; base64.b64decode(s)


def decode(s: str) -> bytes:
    pass


def run_tests() -> None:
    assert decode('aGk=') == b'hi'
    assert decode('') == b''
    assert decode('d29yaw==') == b'work'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
