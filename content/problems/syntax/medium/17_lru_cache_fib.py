# title: functools.lru_cache - Fibonacci
# track: syntax
# difficulty: medium
# tags: cache, recursion
# description: |
# Implement a recursive fibonacci using @functools.lru_cache to memoize.
# examples:
# fib(10) -> 55
# hint: |
# @lru_cache(None) on the recursive function caches results.
# syntax_hint: |
# from functools import lru_cache; @lru_cache(None)


def fib(n: int) -> int:
    pass


def run_tests() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(20) == 6765
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
