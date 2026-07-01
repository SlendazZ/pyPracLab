# title: HTTP/2 Flag
# track: httpx
# difficulty: easy
# tags: httpx
# description: |
# Return httpx.Client with http2=False and MockTransport (explicitly disable HTTP/2).
# examples:
# client_no_http2()._transport is MockTransport
# hint: |
# httpx.Client(http2=False, transport=...)
# syntax_hint: |
# httpx.Client(http2=False, transport=httpx.MockTransport(handler))


def client_no_http2():
    pass


def run_tests() -> None:
    import httpx
    c = client_no_http2()
    assert isinstance(c, httpx.Client)
    assert c._transport is not None
    c.close()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
