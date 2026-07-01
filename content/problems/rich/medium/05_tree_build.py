# title: Build a Tree
# track: rich
# difficulty: medium
# tags: rich, tree
# description: |
# Return a rich.tree.Tree with root label 'root' and one child per item in items.
# examples:
# tree(['a','b']) -> Tree with 2 children
# hint: |
# tree.add(label) adds a child branch.
# syntax_hint: |
# from rich.tree import Tree; t = Tree('root'); for x in items: t.add(x)


def tree(items: list[str]) -> object:
    pass


def run_tests() -> None:
    from rich.tree import Tree
    t = tree(['a', 'b'])
    assert isinstance(t, Tree)
    assert len(t.children) == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
