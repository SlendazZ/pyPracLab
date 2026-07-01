# title: Form Data Route
# track: fastapi
# difficulty: medium
# tags: fastapi, forms
# description: |
# Implement register(app) adding POST /login parsing application/x-www-form-urlencoded body for username.
# examples:
# post form username=eli&password=secret -> {'user':'eli'}
# hint: |
# Read request.body and parse with urllib.parse.parse_qs.
# syntax_hint: |
# from urllib.parse import parse_qs; data = parse_qs(body.decode())


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.post('/login', data={'username': 'eli', 'password': 'secret'})
    assert r.status_code == 200
    assert r.json() == {'user': 'eli'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
