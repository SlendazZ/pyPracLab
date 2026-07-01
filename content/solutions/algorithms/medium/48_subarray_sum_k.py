def subarray_sum_k(nums: list[int], k: int) -> int:
    counts = {0: 1}
    running = 0
    ans = 0
    for x in nums:
        running += x
        ans += counts.get(running - k, 0)
        counts[running] = counts.get(running, 0) + 1
    return ans
