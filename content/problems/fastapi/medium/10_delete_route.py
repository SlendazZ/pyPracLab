# title: DELETE Route
# track: fastapi
# difficulty: medium
# tags: fastapi
# description: |
# Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). Register DELETE /items/{item_id} returning 204 with empty body.
# examples:
# client.delete('/items/1').status_code == 204
# hint: |
# Use status_code=204 on decorator or Response.
# syntax_hint: |
# @app.delete('/items/{item_id}', status_code=204)


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.delete('/items/1')
    assert r.status_code == 204
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
