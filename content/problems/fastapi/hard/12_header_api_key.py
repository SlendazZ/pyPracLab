# title: API Key Header Check
# track: fastapi
# difficulty: hard
# tags: fastapi
# description: |
# Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). GET /secure requires header X-API-Key == 'secret'; return 401 via HTTPException if wrong.
# examples:
# missing key -> 401; correct -> 200
# hint: |
# Read Header alias X-API-Key; raise HTTPException(401).
# syntax_hint: |
# from fastapi import Header, HTTPException


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    assert c.get('/secure').status_code == 401
    assert c.get('/secure', headers={'X-API-Key': 'secret'}).status_code == 200
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
