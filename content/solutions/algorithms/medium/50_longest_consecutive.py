def longest_consecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    best = 0
    for x in nums_set:
        if x - 1 in nums_set:
            continue
        length = 1
        while x + length in nums_set:
            length += 1
        best = max(best, length)
    return best
