class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._data: list = [None] * capacity
        self._start = 0
        self._size = 0
    def write(self, x) -> None:
        if self._size < self.capacity:
            idx = (self._start + self._size) % self.capacity
            self._data[idx] = x
            self._size += 1
        else:
            self._data[self._start] = x
            self._start = (self._start + 1) % self.capacity
    def read_all(self) -> list:
        return [self._data[(self._start + i) % self.capacity] for i in range(self._size)]
