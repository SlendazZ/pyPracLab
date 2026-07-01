# title: Merge Query Params
# track: apis
# difficulty: medium
# tags: url
# description: |
# Merge two query param dicts; values from the second override the first.
# examples:
# merge_params({'a':1},{'a':2,'b':3}) -> {'a':2,'b':3}
# hint: |
# Spread / dict union: {**a, **b}
# syntax_hint: |
# return {**first, **second}


def merge_params(a: dict, b: dict) -> dict:
    pass


def run_tests() -> None:
    assert merge_params({'a':1},{'a':2,'b':3}) == {'a':2,'b':3}
    assert merge_params({}, {'x':1}) == {'x':1}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
