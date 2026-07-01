from itertools import combinations

def all_pairs(items: list) -> list[tuple]:
    return [tuple(c) for c in combinations(items, 2)]
