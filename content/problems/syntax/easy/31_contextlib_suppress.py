# title: Suppress KeyError
# track: syntax
# difficulty: easy
# tags: contextlib
# description: |
# Return value for key in dict d, or default if missing, using contextlib.suppress(KeyError) around d[key].
# examples:
# safe_get({'a':1}, 'b', 0) -> 0
# hint: |
# with suppress(KeyError): return d[key] else default.
# syntax_hint: |
# from contextlib import suppress


def safe_get(d: dict, key: str, default):
    pass


def run_tests() -> None:
    assert safe_get({'a': 1}, 'a', 0) == 1
    assert safe_get({'a': 1}, 'b', 0) == 0
    assert safe_get({}, 'x', 'missing') == 'missing'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
