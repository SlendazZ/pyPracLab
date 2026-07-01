# title: Timeout Configuration
# track: httpx
# difficulty: medium
# tags: httpx
# description: |
# Given connect and read seconds, return an httpx.Timeout with those values (set all four phases explicitly).
# examples:
# make_timeout(2.0, 5.0) -> Timeout with connect=2.0 and read=5.0
# hint: |
# httpx.Timeout requires all four phases or a single default; set connect, read, write, and pool.
# syntax_hint: |
# httpx.Timeout(connect=2.0, read=5.0, write=5.0, pool=5.0)


def make_timeout(connect: float, read: float):
    pass


def run_tests() -> None:
    import httpx
    t = make_timeout(2.0, 5.0)
    assert isinstance(t, httpx.Timeout)
    assert t.connect == 2.0
    assert t.read == 5.0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
