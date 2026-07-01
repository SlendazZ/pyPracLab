# title: Session Base Headers
# track: requests
# difficulty: medium
# tags: requests, session
# description: |
# Return a requests.Session whose default headers include 'User-Agent': 'pyprac/1.0'. (No network call.)
# examples:
# session.headers['User-Agent'] == 'pyprac/1.0'
# hint: |
# session.headers is a dict-like; assign into it.
# syntax_hint: |
# s = requests.Session(); s.headers['User-Agent'] = 'pyprac/1.0'


def make_session():
    pass


def run_tests() -> None:
    import requests
    s = make_session()
    assert isinstance(s, requests.Session)
    assert s.headers['User-Agent'] == 'pyprac/1.0'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
