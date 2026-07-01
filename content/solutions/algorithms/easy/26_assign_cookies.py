def assign(greed: list[int], size: list[int]) -> int:
    greed.sort()
    size.sort()
    i = j = 0
    while i < len(greed) and j < len(size):
        if size[j] >= greed[i]:
            i += 1
        j += 1
    return i
