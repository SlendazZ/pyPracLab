# title: Deep Dict Get
# track: syntax
# difficulty: medium
# tags: dict
# description: |
# Given a nested dict and a list of keys, return the nested value or default if any key is missing.
# examples:
# deep_get({"a":{"b":1}}, ["a","b"], 0) -> 1
# hint: |
# Walk keys one by one; return default on KeyError or non-dict.
# syntax_hint: |
# for k in keys: d = d[k]


def deep_get(d: dict, keys: list, default=None):
    pass


def run_tests() -> None:
    assert deep_get({"a":{"b":1}}, ["a","b"], 0) == 1
    assert deep_get({"a":{"b":1}}, ["a","c"], 9) == 9
    assert deep_get({}, ["x"], "missing") == "missing"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
