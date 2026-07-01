# title: Flatten Nested List
# track: syntax
# difficulty: hard
# tags: recursion, list
# description: |
# Flatten a list that may contain nested lists to a single flat list of non-list items.
# examples:
# flatten([1,[2,[3]],4]) -> [1,2,3,4]
# hint: |
# Recursively extend when you see a list.
# syntax_hint: |
# for x in items: if isinstance(x, list): out.extend(flatten(x)) else: out.append(x)


def flatten(items: list) -> list:
    pass


def run_tests() -> None:
    assert flatten([1,[2,[3]],4]) == [1,2,3,4]
    assert flatten([]) == []
    assert flatten([1,2,3]) == [1,2,3]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
