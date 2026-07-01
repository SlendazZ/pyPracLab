# title: Memoize Decorator Class
# track: apps
# difficulty: medium
# tags: oop, decorator
# description: |
# Implement Memoize as a class decorator that caches function results by arguments tuple.
# examples:
# @Memoize def f(x): ...; f(1) computed once
# hint: |
# Use a dict keyed by args tuple in __call__.
# syntax_hint: |
# self.cache: dict = {}; key = args


class Memoize:
    pass


def run_tests() -> None:
    calls = {'n': 0}
    @Memoize
    def f(x):
        calls['n'] += 1
        return x * 2
    assert f(3) == 6
    assert f(3) == 6
    assert calls['n'] == 1
    assert f(4) == 8
    assert calls['n'] == 2
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
