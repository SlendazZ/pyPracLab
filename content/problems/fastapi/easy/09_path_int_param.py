# title: Integer Path Param Route
# track: fastapi
# difficulty: easy
# tags: fastapi
# description: |
# Implement register(app) to add routes to the given FastAPI app. Tests create a FastAPI() instance and call register(app) before using TestClient. Register GET /items/{item_id} returning {'id': item_id}.
# examples:
# client.get('/items/5').json() -> {'id': 5}
# hint: |
# Path parameter typed as int.
# syntax_hint: |
# @app.get('/items/{item_id}')


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    assert c.get('/items/5').json() == {'id': 5}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
