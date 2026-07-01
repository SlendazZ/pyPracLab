# title: Custom Request Headers
# track: httpx
# difficulty: easy
# tags: httpx, headers
# description: |
# Build an httpx Request with the given headers dict (no network call).
# examples:
# request.headers['Authorization'] == 'Bearer x'
# hint: |
# Pass headers= to httpx.Request.
# syntax_hint: |
# httpx.Request('GET', url, headers={'Authorization': 'Bearer x'})


def build_with_headers(url: str, headers: dict):
    pass


def run_tests() -> None:
    req = build_with_headers('https://x.test/api', {'Authorization': 'Bearer x'})
    assert req.headers['Authorization'] == 'Bearer x'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
