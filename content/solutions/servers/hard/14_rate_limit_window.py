import time

class FixedWindow:
    def __init__(self, limit: int, window_seconds: float = 60.0):
        self.limit = limit
        self.window = window_seconds
        self.count = 0
        self.start = time.monotonic()
    def allow(self) -> bool:
        now = time.monotonic()
        if now - self.start >= self.window:
            self.start = now
            self.count = 0
        if self.count < self.limit:
            self.count += 1
            return True
        return False
