# title: Build an HTTPX Request
# track: httpx
# difficulty: easy
# tags: httpx, url
# description: |
# Using httpx, build and return a Request for the given method and url (no network call).
# examples:
# build_request('GET', 'https://x.test/api') -> Request with method GET
# hint: |
# httpx.Request(method, url) constructs a request object.
# syntax_hint: |
# import httpx; return httpx.Request('GET', url)


def build_request(method: str, url: str):
    pass


def run_tests() -> None:
    import httpx
    req = build_request('GET', 'https://x.test/api')
    assert isinstance(req, httpx.Request)
    assert req.method == 'GET'
    assert str(req.url) == 'https://x.test/api'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
