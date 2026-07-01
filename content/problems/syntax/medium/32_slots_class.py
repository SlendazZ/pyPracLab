# title: Slots Point Class
# track: syntax
# difficulty: medium
# tags: class
# description: |
# Return a Point class with __slots__ = ('x','y') and x,y set in __init__.
# examples:
# P = make_point_cls(); P(1,2).x == 1
# hint: |
# class Point: __slots__ = ('x','y')
# syntax_hint: |
# __slots__ = ('x', 'y')


def make_point_cls():
    pass


def run_tests() -> None:
    P = make_point_cls()
    p = P(1, 2)
    assert p.x == 1 and p.y == 2
    assert '__slots__' in dir(P) or hasattr(P, '__slots__')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
