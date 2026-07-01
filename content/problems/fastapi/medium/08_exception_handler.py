# title: HTTPException
# track: fastapi
# difficulty: medium
# tags: fastapi, errors
# description: |
# Create an app with GET '/items/{item_id}' that raises HTTPException(404) when item_id is 0, else returns {"item_id": item_id}.
# examples:
# GET /items/0 -> 404
# hint: |
# from fastapi import HTTPException; raise HTTPException(status_code=404).
# syntax_hint: |
# if item_id == 0: raise HTTPException(status_code=404)


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    assert client.get('/items/5').json() == {'item_id': 5}
    assert client.get('/items/0').status_code == 404
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
