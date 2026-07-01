import time

class CircuitBreaker:
    def __init__(self, threshold: int, cooldown: float):
        self.threshold = threshold
        self.cooldown = cooldown
        self.failures = 0
        self._state = 'closed'
        self.opened_at = 0.0

    def state(self) -> str:
        if self._state == 'open':
            if time.monotonic() - self.opened_at >= self.cooldown:
                self._state = 'half_open'
        return self._state

    def success(self) -> None:
        self.failures = 0
        self._state = 'closed'

    def failure(self) -> None:
        self.failures += 1
        if self.failures >= self.threshold:
            self._state = 'open'
            self.opened_at = time.monotonic()
