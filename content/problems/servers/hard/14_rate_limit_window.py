# title: Fixed Window Rate Limit
# track: servers
# difficulty: hard
# tags: rate-limit
# description: |
# FixedWindow(limit) tracks .allow() calls per window_seconds; return True if under limit else False.
# examples:
# w=FixedWindow(2, window_seconds=60); w.allow(); w.allow(); w.allow() -> False
# hint: |
# Reset count when time window elapses.
# syntax_hint: |
# import time; if now - start >= window: reset


class FixedWindow:
    def __init__(self, limit: int, window_seconds: float = 60.0): pass
    def allow(self) -> bool: pass


def run_tests() -> None:
    w = FixedWindow(2, window_seconds=3600)
    assert w.allow() is True
    assert w.allow() is True
    assert w.allow() is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
