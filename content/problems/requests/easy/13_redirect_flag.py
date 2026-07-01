# title: Redirect Flag
# track: requests
# difficulty: easy
# tags: requests
# description: |
# Return whether a requests.Session should follow redirects for the given allow_redirects bool.
# examples:
# session_redirects(True) -> Session with allow_redirects behavior stored
# hint: |
# Store allow_redirects on a simple wrapper or return session max_redirects config.
# syntax_hint: |
# s = requests.Session(); note: allow_redirects is per-request; return dict flag


def should_follow(allow: bool, status: int) -> bool:
    pass


def run_tests() -> None:
    assert should_follow(True, 302) is True
    assert should_follow(False, 302) is False
    assert should_follow(True, 200) is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
