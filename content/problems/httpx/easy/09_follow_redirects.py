# title: Follow Redirects Config
# track: httpx
# difficulty: easy
# tags: httpx
# description: |
# Return an httpx.Client with follow_redirects=True and MockTransport (no network).
# examples:
# client_follow() -> Client with follow_redirects True
# hint: |
# httpx.Client(follow_redirects=True, transport=MockTransport(...))
# syntax_hint: |
# httpx.Client(follow_redirects=True, transport=httpx.MockTransport(handler))


def client_follow():
    pass


def run_tests() -> None:
    import httpx
    c = client_follow()
    assert isinstance(c, httpx.Client)
    assert c.follow_redirects is True
    c.close()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
