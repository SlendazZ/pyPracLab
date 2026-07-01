from collections import deque

class Queue:
    def __init__(self):
        self._items: deque = deque()
    def enqueue(self, x) -> None:
        self._items.append(x)
    def dequeue(self):
        if not self._items:
            raise IndexError('dequeue from empty queue')
        return self._items.popleft()
    def is_empty(self) -> bool:
        return len(self._items) == 0
