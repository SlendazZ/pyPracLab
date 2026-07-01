# title: Line Checksum
# track: automations
# difficulty: medium
# tags: hashlib
# description: |
# Return first 8 hex chars of sha256 of UTF-8 encoded text.
# examples:
# line_checksum('abc') -> 8 hex chars
# hint: |
# hashlib.sha256(text.encode()).hexdigest()[:8]
# syntax_hint: |
# import hashlib


def line_checksum(text: str) -> str:
    pass


def run_tests() -> None:
    assert len(line_checksum('abc')) == 8
    assert line_checksum('abc') == line_checksum('abc')
    assert line_checksum('a') != line_checksum('b')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
