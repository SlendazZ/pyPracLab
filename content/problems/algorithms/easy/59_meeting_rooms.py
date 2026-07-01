# title: Meeting Rooms
# track: algorithms
# difficulty: easy
# tags: intervals, sorting
# description: |
# Given list of [start, end] meetings, return True if a person can attend all (no overlap).
# examples:
# can_attend([[0,30],[5,10],[15,20]]) -> False
# hint: |
# Sort by start; check each start >= previous end.
# syntax_hint: |
# intervals.sort(); for s,e in intervals: if s < prev_end: return False


def can_attend(intervals: list[list[int]]) -> bool:
    pass


def run_tests() -> None:
    assert can_attend([[0, 30], [5, 10], [15, 20]]) is False
    assert can_attend([[7, 10], [2, 4]]) is True
    assert can_attend([]) is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
