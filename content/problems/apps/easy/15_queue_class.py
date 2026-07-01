# title: Queue Class
# track: apps
# difficulty: easy
# tags: oop, queue
# description: |
# Implement a FIFO Queue with enqueue(x), dequeue() (raise IndexError if empty), and is_empty().
# examples:
# q = Queue(); q.enqueue(1); q.dequeue() -> 1
# hint: |
# Use collections.deque or a list with pop(0)/append.
# syntax_hint: |
# from collections import deque; self._items = deque()


class Queue:
    pass


def run_tests() -> None:
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(1); q.enqueue(2)
    assert q.dequeue() == 1
    assert q.is_empty() is False
    assert q.dequeue() == 2
    try:
        q.dequeue(); assert False
    except IndexError:
        pass
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
