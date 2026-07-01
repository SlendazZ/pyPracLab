# title: URL Join
# track: apis
# difficulty: easy
# tags: url
# description: |
# Join a base URL and path segments into one URL without duplicate slashes.
# examples:
# join_url('https://api.test/v1/', '/users/', '42') -> 'https://api.test/v1/users/42'
# hint: |
# Strip slashes from segments; urllib.parse.urljoin handles the base.
# syntax_hint: |
# from urllib.parse import urljoin; urljoin(base.rstrip('/')+'/', segment)


def join_url(base: str, *parts: str) -> str:
    pass


def run_tests() -> None:
    assert join_url('https://api.test/v1/', '/users/', '42') == 'https://api.test/v1/users/42'
    assert join_url('https://x.test/', 'a', 'b') == 'https://x.test/a/b'
    assert join_url('https://x.test/api', '') == 'https://x.test/api'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
