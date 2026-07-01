# title: Stack Class
# track: apps
# difficulty: easy
# tags: oop
# description: |
# Implement a Stack with push(x), pop() (raise IndexError if empty), and peek().
# examples:
# s.pop() after push(1) -> 1
# hint: |
# Backed by a list; use append and pop.
# syntax_hint: |
# if not self._data: raise IndexError


class Stack:
    pass


def run_tests() -> None:
    s = Stack()
    s.push(1); s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    try:
        s.pop(); assert False
    except IndexError:
        pass
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
