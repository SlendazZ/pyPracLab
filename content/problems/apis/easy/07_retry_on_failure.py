# title: Retry On Failure
# track: apis
# difficulty: easy
# tags: loop, api
# description: |
# Call a function up to n times; return the first successful result, or raise the last exception.
# examples:
# retry(flaky, 3) -> result of first successful call
# hint: |
# try/except in a loop; keep last exception.
# syntax_hint: |
# for attempt in range(n): try: return fn() except Exception as e: last = e


def retry(fn, n: int):
    pass


def run_tests() -> None:
    calls = {'n': 0}
    def flaky():
        calls['n'] += 1
        if calls['n'] < 3:
            raise ValueError('boom')
        return 'ok'
    assert retry(flaky, 5) == 'ok'
    assert calls['n'] == 3
    def always():
        raise RuntimeError('nope')
    try:
        retry(always, 2)
        assert False
    except RuntimeError:
        pass
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
