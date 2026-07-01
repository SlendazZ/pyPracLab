# title: Priority Queue
# track: apps
# difficulty: medium
# tags: oop, heap
# description: |
# Implement PriorityQueue with push(priority, item) and pop() returning lowest-priority item first (min-heap).
# examples:
# pq.push(2,'b'); pq.push(1,'a'); pq.pop() -> 'a'
# hint: |
# heapq.heappush / heappop with (priority, item) tuples.
# syntax_hint: |
# import heapq; heapq.heappush(self._heap, (priority, item))


class PriorityQueue:
    pass


def run_tests() -> None:
    pq = PriorityQueue()
    pq.push(2, 'b')
    pq.push(1, 'a')
    assert pq.pop() == 'a'
    assert pq.pop() == 'b'
    try:
        pq.pop(); assert False
    except IndexError:
        pass
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
