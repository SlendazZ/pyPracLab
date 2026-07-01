# title: HTTP Status Class
# track: apis
# difficulty: easy
# tags: http
# description: |
# Given an HTTP status code, return 'success' for 2xx, 'redirect' for 3xx, 'client' for 4xx, 'server' for 5xx, else 'unknown'.
# examples:
# status_class(200) -> 'success'
# status_class(404) -> 'client'
# hint: |
# Integer division by 100 gives the class.
# syntax_hint: |
# code // 100


def status_class(code: int) -> str:
    pass


def run_tests() -> None:
    assert status_class(200) == 'success'
    assert status_class(301) == 'redirect'
    assert status_class(404) == 'client'
    assert status_class(500) == 'server'
    assert status_class(99) == 'unknown'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
