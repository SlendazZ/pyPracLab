# title: Strip Emoji
# track: rich
# difficulty: easy
# tags: rich, text
# description: |
# Remove emoji characters from text using a simple regex (Unicode emoji ranges not required; strip chars with ord > 0xFFFF or common emoji).
# examples:
# strip_emoji('hi 👋') -> 'hi '
# hint: |
# Filter chars where ord(c) < 0x10000 or use regex.
# syntax_hint: |
# ''.join(c for c in s if ord(c) < 0x10000)


def strip_emoji(s: str) -> str:
    pass


def run_tests() -> None:
    assert strip_emoji('hi 👋') == 'hi '
    assert strip_emoji('plain') == 'plain'
    assert '🎉' not in strip_emoji('x 🎉 y')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
