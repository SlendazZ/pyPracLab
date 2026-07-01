# title: Basic Auth on Client
# track: httpx
# difficulty: medium
# tags: httpx, auth
# description: |
# Return an httpx.Client configured with HTTP basic auth for the given username and password, using MockTransport so no real network call is made.
# examples:
# client built with auth=('u', 'p')
# hint: |
# httpx.Client(auth=(user, password), transport=MockTransport(handler)).
# syntax_hint: |
# import httpx; httpx.Client(auth=('u', 'p'), transport=httpx.MockTransport(handler))


def make_auth_client(user: str, password: str):
    pass


def run_tests() -> None:
    import httpx
    import base64
    captured = {}
    def handler(request):
        captured['auth'] = request.headers.get('authorization')
        return httpx.Response(200, json={'ok': True})
    client = make_auth_client('u', 'p')
    client._transport = httpx.MockTransport(handler)
    r = client.get('https://x.test/secure')
    assert r.status_code == 200
    token = base64.b64encode(b'u:p').decode()
    assert captured['auth'] == f'Basic {token}'
    client.close()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
