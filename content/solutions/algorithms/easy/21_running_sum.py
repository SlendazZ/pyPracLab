from itertools import accumulate

def running_sum(nums: list[int]) -> list[int]:
    return list(accumulate(nums))
