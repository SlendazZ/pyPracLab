def check(nums: list[int]) -> tuple[bool, bool]:
    return any(x < 0 for x in nums), all(x > 0 for x in nums)
