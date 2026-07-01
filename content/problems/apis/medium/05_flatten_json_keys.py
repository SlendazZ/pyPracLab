# title: Flatten JSON Keys
# track: apis
# difficulty: medium
# tags: json, recursion
# description: |
# Given a nested dict, return a list of dotted-path keys for every leaf (non-dict) value.
# examples:
# leaf_keys({"a":{"b":1},"c":2}) -> ["a.b","c"]
# hint: |
# Recurse with a prefix; append the dotted path when the value is not a dict.
# syntax_hint: |
# if isinstance(v, dict): recurse(prefix + k + '.') else: keys.append(prefix + k)


def leaf_keys(obj: dict) -> list[str]:
    pass


def run_tests() -> None:
    assert sorted(leaf_keys({"a": {"b": 1}, "c": 2})) == ["a.b", "c"]
    assert leaf_keys({}) == []
    assert leaf_keys({"x": {"y": {"z": 0}}}) == ["x.y.z"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
