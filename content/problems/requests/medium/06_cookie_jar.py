# title: Preload Cookies
# track: requests
# difficulty: medium
# tags: requests, cookies
# description: |
# Return a requests.Session with cookies from the given dict set on it (no network call).
# examples:
# session.cookies.get('token') == 'abc'
# hint: |
# session.cookies.update(dict) sets cookies.
# syntax_hint: |
# s.cookies.update({'token': 'abc'})


def make_session_with_cookies(cookies: dict):
    pass


def run_tests() -> None:
    s = make_session_with_cookies({'token': 'abc', 'theme': 'dark'})
    assert s.cookies.get('token') == 'abc'
    assert s.cookies.get('theme') == 'dark'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
