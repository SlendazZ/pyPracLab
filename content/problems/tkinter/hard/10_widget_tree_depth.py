# title: Widget Tree Max Depth
# track: tkinter
# difficulty: hard
# tags: tkinter, tree
# description: |
# Given nested dict tree {name: {child: {}}}, return max nesting depth (leaf = 1).
# examples:
# depth({'root':{'a':{}}}) -> 2
# hint: |
# Recurse into dict values.
# syntax_hint: |
# 1 + max(depth(v) for v in node.values()) if node else 0


def depth(tree: dict) -> int:
    pass


def run_tests() -> None:
    assert depth({'root': {'a': {}}}) == 2
    assert depth({}) == 0
    assert depth({'x': {}}) == 1
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
