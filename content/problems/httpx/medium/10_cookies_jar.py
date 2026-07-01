# title: Cookies on Client
# track: httpx
# difficulty: medium
# tags: httpx, cookies
# description: |
# Return httpx.Client with cookies set and MockTransport; GET returns cookie value in JSON.
# examples:
# client_with_cookies({'sid':'abc'}) sends Cookie header
# hint: |
# Pass cookies= to Client; verify via MockTransport handler.
# syntax_hint: |
# httpx.Client(cookies={'sid': 'abc'}, transport=MockTransport(handler))


def client_with_cookies(cookies: dict):
    pass


def run_tests() -> None:
    import httpx
    captured = {}
    def handler(request):
        captured['cookie'] = request.headers.get('cookie', '')
        return httpx.Response(200, json={'ok': True})
    c = client_with_cookies({'sid': 'abc'})
    c._transport = httpx.MockTransport(handler)
    c.get('https://x.test/')
    assert 'sid=abc' in captured.get('cookie', '')
    c.close()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
