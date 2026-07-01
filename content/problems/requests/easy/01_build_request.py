# title: Build a Prepared Request
# track: requests
# difficulty: easy
# tags: requests, url
# description: |
# Using requests, build and return a PreparedRequest for the given method, url, and query params (no network call).
# examples:
# build_request('GET', 'https://x.test/api', {'q': 'py'}) -> req with q=py in url
# hint: |
# requests.Request(method, url, params=...).prepare().
# syntax_hint: |
# from requests import Request; Request('GET', url, params=p).prepare()


def build_request(method: str, url: str, params: dict):
    pass


def run_tests() -> None:
    req = build_request('GET', 'https://x.test/api', {'q': 'py', 'page': '1'})
    assert req.method == 'GET'
    assert 'q=py' in req.url and 'page=1' in req.url
    assert req.url.startswith('https://x.test/api')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
