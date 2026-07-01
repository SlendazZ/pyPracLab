# title: Circuit Breaker
# track: apis
# difficulty: hard
# tags: api, state
# description: |
# A CircuitBreaker starts 'closed'. Record success()/failure(). After `threshold` failures it 'opens'; success() after cooldown resets to 'closed'. Return the current state string.
# examples:
# cb.state() -> 'closed' / 'open' / 'half_open'
# hint: |
# Track consecutive failures and a state; use time.monotonic() for cooldown.
# syntax_hint: |
# if self.failures >= threshold: self.state = 'open'; self.opened_at = time.monotonic()


class CircuitBreaker:
    pass


def run_tests() -> None:
    cb = CircuitBreaker(threshold=2, cooldown=1.0)
    assert cb.state() == 'closed'
    cb.failure(); cb.failure()
    assert cb.state() == 'open'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
