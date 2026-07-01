# title: Trust Env Disabled
# track: requests
# difficulty: easy
# tags: requests
# description: |
# Return a requests.Session with trust_env set to False.
# examples:
# session_no_env().trust_env is False
# hint: |
# Create Session then assign s.trust_env = False.
# syntax_hint: |
# s = requests.Session(); s.trust_env = False


def session_no_env():
    pass


def run_tests() -> None:
    s = session_no_env()
    import requests
    assert isinstance(s, requests.Session)
    assert s.trust_env is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
