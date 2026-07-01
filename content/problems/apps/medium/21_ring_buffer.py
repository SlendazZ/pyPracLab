# title: Ring Buffer
# track: apps
# difficulty: medium
# tags: oop, buffer
# description: |
# Implement RingBuffer(capacity) with write(x) overwriting oldest when full, and read_all() returning items oldest-first.
# examples:
# rb = RingBuffer(2); write 1,2,3; read_all() -> [2,3]
# hint: |
# Use a list and index pointer modulo capacity.
# syntax_hint: |
# self._data = [None]*capacity; self._start = self._size = 0


class RingBuffer:
    pass


def run_tests() -> None:
    rb = RingBuffer(2)
    rb.write(1); rb.write(2)
    assert rb.read_all() == [1, 2]
    rb.write(3)
    assert rb.read_all() == [2, 3]
    rb.write(4); rb.write(5)
    assert rb.read_all() == [4, 5]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
