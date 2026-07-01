from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def moved(self, dx: int, dy: int) -> 'Point':
        return Point(self.x + dx, self.y + dy)
