# title: Dependency Injection
# track: fastapi
# difficulty: hard
# tags: fastapi, di
# description: |
# Create an app using a dependency that reads the 'X-User' header; GET '/me' returns {"user": <header or 'anonymous'>}.
# examples:
# GET /me with X-User: eli -> {"user": "eli"}
# hint: |
# Define def get_user(x_user: str = Header(default='anonymous')) and Depends() it.
# syntax_hint: |
# from fastapi import Header, Depends


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    assert client.get('/me').json() == {'user': 'anonymous'}
    assert client.get('/me', headers={'X-User': 'eli'}).json() == {'user': 'eli'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
