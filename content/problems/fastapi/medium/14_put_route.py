# title: PUT Route
# track: fastapi
# difficulty: medium
# tags: fastapi, http
# description: |
# Implement register(app) adding PUT /items/{item_id} replacing the item; return {'id': item_id, 'data': body}.
# examples:
# put /items/3 {'a':1} -> {'id':3,'data':{'a':1}}
# hint: |
# PUT decorator with path param and dict body.
# syntax_hint: |
# @app.put('/items/{item_id}')


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.put('/items/3', json={'a': 1})
    assert r.json() == {'id': 3, 'data': {'a': 1}}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
