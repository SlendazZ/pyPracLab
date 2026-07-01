import functools
import operator

def single(nums: list[int]) -> int:
    return functools.reduce(operator.xor, nums)
