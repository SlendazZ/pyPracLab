# title: Meeting Rooms II
# track: algorithms
# difficulty: medium
# tags: intervals, heap
# description: |
# Return minimum number of conference rooms required.
# examples:
# min_rooms([[0,30],[5,10],[15,20]]) -> 2
# hint: |
# Sort starts; min-heap of end times; pop ends <= new start.
# syntax_hint: |
# import heapq; heapq.heappush(heap, end); heapq.heappop(heap)


def min_rooms(intervals: list[list[int]]) -> int:
    pass


def run_tests() -> None:
    assert min_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_rooms([[7, 10], [2, 4]]) == 1
    assert min_rooms([[1, 5], [2, 6], [3, 7]]) == 3
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
