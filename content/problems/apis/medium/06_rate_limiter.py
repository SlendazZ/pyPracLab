# title: Simple Rate Limiter
# track: apis
# difficulty: medium
# tags: time, api
# description: |
# Implement allow() on a RateLimiter that returns True only if at most `limit` calls happen per `window` seconds. Use time.monotonic().
# examples:
# rl = RateLimiter(2, 1.0); rl.allow() x2 -> True, rl.allow() -> False
# hint: |
# Keep timestamps of recent calls; drop those older than the window; compare count.
# syntax_hint: |
# import time; self.calls = []; prune calls older than window


class RateLimiter:
    pass


def run_tests() -> None:
    import time
    rl = RateLimiter(2, 1.0)
    assert rl.allow() is True
    assert rl.allow() is True
    assert rl.allow() is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
