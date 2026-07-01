# title: PATCH Route
# track: fastapi
# difficulty: medium
# tags: fastapi, http
# description: |
# Implement register(app) adding PATCH /items/{item_id} that accepts JSON body {'name': str} and returns it with id.
# examples:
# patch /items/5 {'name':'x'} -> {'id':5,'name':'x'}
# hint: |
# Use @app.patch with path param and body dict.
# syntax_hint: |
# @app.patch('/items/{item_id}')


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.patch('/items/5', json={'name': 'x'})
    assert r.status_code == 200
    assert r.json() == {'id': 5, 'name': 'x'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
