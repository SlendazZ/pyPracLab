def min_cost(cost: list[int]) -> int:
    a = b = 0
    for c in cost:
        a, b = b, min(a, b) + c
    return min(a, b)
