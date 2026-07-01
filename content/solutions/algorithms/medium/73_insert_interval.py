def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:
        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1
    result.append(new)
    result.extend(intervals[i:])
    return result
