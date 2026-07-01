# title: FastAPI Hello Route
# track: fastapi
# difficulty: easy
# tags: fastapi, http
# description: |
# Create and return a FastAPI app with GET '/' returning {"message": "hello"} and GET '/health' returning {"status": "ok"}.
# examples:
# create_app() testable with TestClient
# hint: |
# from fastapi import FastAPI; app = FastAPI(); use @app.get.
# syntax_hint: |
# @app.get("/") def root(): return {"message": "hello"}


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    r = client.get('/')
    assert r.status_code == 200
    assert r.json() == {"message": "hello"}
    assert client.get('/health').json() == {"status": "ok"}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
