# title: Rate Limiter Class
# track: apps
# difficulty: medium
# tags: oop, rate-limit
# description: |
# Implement RateLimiter(max_calls, period_seconds) with allow() returning True only if under the limit in the sliding window.
# examples:
# rl = RateLimiter(2, 60); allow() twice True, third False
# hint: |
# Track call timestamps; prune those older than period.
# syntax_hint: |
# while calls and now - calls[0] >= period: calls.popleft()


class RateLimiter:
    pass


def run_tests() -> None:
    rl = RateLimiter(2, 3600)
    assert rl.allow() is True
    assert rl.allow() is True
    assert rl.allow() is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
