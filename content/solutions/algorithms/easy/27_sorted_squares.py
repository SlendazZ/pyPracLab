def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for k in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[k] = nums[left] ** 2
            left += 1
        else:
            result[k] = nums[right] ** 2
            right -= 1
    return result
