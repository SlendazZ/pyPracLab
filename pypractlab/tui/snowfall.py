"""Light snowfall animation for the TUI background."""

from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass
class _Flake:
    x: float
    y: float
    speed: float
    drift: float
    char: str
    phase: float = field(default=0.0)


class Snowfall:
    """Gentle layered snowfall — small dots drifting down with slight sway."""

    _CHARS = (".", ".", ".", "'", ":", "`")

    def __init__(self, count: int = 55) -> None:
        self.flakes: list[_Flake] = []
        self._target = count
        self._wind = 0.0

    def reset(self, width: int, height: int) -> None:
        n = min(self._target, max(12, (width * height) // 80))
        self.flakes = [self._spawn(width, height, random.uniform(0, height)) for _ in range(n)]

    def _spawn(self, width: int, height: int, y: float = 0.0) -> _Flake:
        layer = random.random()
        if layer < 0.6:
            speed = random.uniform(0.08, 0.18)
            char = "."
        elif layer < 0.85:
            speed = random.uniform(0.18, 0.32)
            char = random.choice(("'", "`"))
        else:
            speed = random.uniform(0.32, 0.55)
            char = ":"
        return _Flake(
            x=random.uniform(0, max(1, width - 1)),
            y=y,
            speed=speed,
            drift=random.uniform(-0.15, 0.15),
            char=char,
            phase=random.uniform(0, 6.28),
        )

    def tick(self, width: int, height: int) -> None:
        if not self.flakes or width < 1 or height < 1:
            return
        # Slow wind shift
        self._wind += random.uniform(-0.02, 0.02)
        self._wind = max(-0.3, min(0.3, self._wind))

        import math

        for i, f in enumerate(self.flakes):
            f.y += f.speed
            sway = math.sin(f.y * 0.08 + f.phase) * 0.25
            f.x += f.drift + self._wind + sway
            if f.y >= height or f.x < 0 or f.x >= width - 1:
                self.flakes[i] = self._spawn(width, height, y=random.uniform(-2, 0))
