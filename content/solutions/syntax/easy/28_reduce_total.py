from functools import reduce
import operator

def total(nums: list[int]) -> int:
    return reduce(operator.add, nums, 0)
