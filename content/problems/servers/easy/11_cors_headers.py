# title: CORS Headers
# track: servers
# difficulty: easy
# tags: http
# description: |
# Return a dict of CORS headers allowing origin * and methods GET, POST.
# examples:
# cors_headers() -> {'Access-Control-Allow-Origin':'*', ...}
# hint: |
# Standard Access-Control-* header names.
# syntax_hint: |
# return {'Access-Control-Allow-Origin': '*', ...}


def cors_headers() -> dict[str, str]:
    pass


def run_tests() -> None:
    h = cors_headers()
    assert h['Access-Control-Allow-Origin'] == '*'
    assert 'GET' in h['Access-Control-Allow-Methods']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
