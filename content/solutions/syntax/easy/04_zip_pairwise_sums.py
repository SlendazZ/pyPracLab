def pairwise_sum(xs: list[int], ys: list[int]) -> list[int]:
    return [a + b for a, b in zip(xs, ys)]
