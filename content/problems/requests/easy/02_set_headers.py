# title: Set Request Headers
# track: requests
# difficulty: easy
# tags: requests, headers
# description: |
# Build a PreparedRequest with the given headers dict and verify via .headers.
# examples:
# headers on req include 'Authorization'
# hint: |
# Request(method, url, headers=...).prepare().
# syntax_hint: |
# Request('GET', url, headers={'Authorization': 'Bearer x'}).prepare()


def build_with_headers(method: str, url: str, headers: dict):
    pass


def run_tests() -> None:
    req = build_with_headers('GET', 'https://x.test/api', {'Authorization': 'Bearer x'})
    assert req.headers['Authorization'] == 'Bearer x'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
