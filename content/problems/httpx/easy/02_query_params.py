# title: Query Params on URL
# track: httpx
# difficulty: easy
# tags: httpx, url
# description: |
# Build an httpx Request whose URL includes the given query params (no network call).
# examples:
# build_with_params(url, {'q': 'py'}) -> url contains q=py
# hint: |
# Pass params= to httpx.Request; inspect str(request.url).
# syntax_hint: |
# httpx.Request('GET', url, params={'q': 'py'})


def build_with_params(url: str, params: dict):
    pass


def run_tests() -> None:
    req = build_with_params('https://x.test/api', {'q': 'py', 'page': '1'})
    u = str(req.url)
    assert 'q=py' in u and 'page=1' in u
    assert u.startswith('https://x.test/api')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
