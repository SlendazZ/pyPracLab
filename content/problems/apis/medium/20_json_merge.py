# title: Deep JSON Merge
# track: apis
# difficulty: medium
# tags: json, dict
# description: |
# Deep-merge dict b into dict a; nested dicts merge recursively, other values from b win.
# examples:
# merge({'a':1,'b':{'x':1}}, {'b':{'y':2}}) -> {'a':1,'b':{'x':1,'y':2}}
# hint: |
# Recurse when both values are dicts; else assign b's value.
# syntax_hint: |
# if isinstance(a[k], dict) and isinstance(v, dict): merge(a[k], v)


def merge(a: dict, b: dict) -> dict:
    pass


def run_tests() -> None:
    assert merge({'a': 1, 'b': {'x': 1}}, {'b': {'y': 2}}) == {'a': 1, 'b': {'x': 1, 'y': 2}}
    assert merge({'a': 1}, {'a': 2}) == {'a': 2}
    assert merge({}, {'z': 3}) == {'z': 3}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
