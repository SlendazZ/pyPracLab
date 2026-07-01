# title: Redirect Response Builder
# track: servers
# difficulty: easy
# tags: http, redirect
# description: |
# Build a redirect response dict with status, Location header, and empty body.
# examples:
# redirect('/login', 302) -> {'status':302,'headers':{'Location':'/login'},'body':''}
# hint: |
# Return a plain dict with the three keys.
# syntax_hint: |
# return {'status': code, 'headers': {'Location': url}, 'body': ''}


def redirect(url: str, status: int = 302) -> dict:
    pass


def run_tests() -> None:
    r = redirect('/login', 302)
    assert r['status'] == 302
    assert r['headers']['Location'] == '/login'
    assert r['body'] == ''
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
