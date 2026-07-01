def remove_dups(nums: list[int]) -> int:
    write = 0
    for x in nums:
        if write == 0 or x != nums[write - 1]:
            nums[write] = x
            write += 1
    return write
