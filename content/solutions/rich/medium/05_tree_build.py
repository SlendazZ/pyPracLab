from rich.tree import Tree

def tree(items: list[str]) -> Tree:
    t = Tree('root')
    for x in items:
        t.add(x)
    return t
