import heapq

class PriorityQueue:
    def __init__(self):
        self._heap: list = []
    def push(self, priority: int, item) -> None:
        heapq.heappush(self._heap, (priority, item))
    def pop(self):
        if not self._heap:
            raise IndexError('pop from empty priority queue')
        return heapq.heappop(self._heap)[1]
