# title: Dataclass - Point
# track: syntax
# difficulty: medium
# tags: dataclass
# description: |
# Define a Point dataclass with x and y, plus a method moved(dx, dy) returning a new Point.
# examples:
# Point(1,2).moved(3,4) -> Point(4,6)
# hint: |
# @dataclass(frozen=True) gives you __init__ and __eq__ for free.
# syntax_hint: |
# from dataclasses import dataclass; @dataclass(frozen=True)


from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    pass


def run_tests() -> None:
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2
    q = p.moved(3, 4)
    assert q == Point(4, 6)
    assert p == Point(1, 2)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
