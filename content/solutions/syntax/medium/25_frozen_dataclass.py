from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def make_point(x: int, y: int):
    return Point(x, y)
