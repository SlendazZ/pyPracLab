# title: Timer Context Manager
# track: syntax
# difficulty: medium
# tags: contextmanager
# description: |
# Return a context manager class Timer that records elapsed seconds in .elapsed after the block exits (use time.perf_counter).
# examples:
# with Timer() as t: ...; t.elapsed >= 0
# hint: |
# __enter__ stores start; __exit__ sets elapsed.
# syntax_hint: |
# class Timer: def __enter__(self): self._start=perf_counter()


class Timer:
    elapsed: float = 0.0
    def __enter__(self): pass
    def __exit__(self, *args): pass


def run_tests() -> None:
    import time
    with Timer() as t:
        time.sleep(0.01)
    assert t.elapsed >= 0.005
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
