class Stack:
    def __init__(self):
        self._data: list = []
    def push(self, x) -> None:
        self._data.append(x)
    def pop(self):
        if not self._data:
            raise IndexError('pop from empty stack')
        return self._data.pop()
    def peek(self):
        if not self._data:
            raise IndexError('peek from empty stack')
        return self._data[-1]
