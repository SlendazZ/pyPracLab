# title: Path Parameter
# track: fastapi
# difficulty: easy
# tags: fastapi, http
# description: |
# Create an app with GET '/items/{item_id}' returning {"item_id": item_id} (as an int).
# examples:
# GET /items/42 -> {"item_id": 42}
# hint: |
# Declare the path param with a Python type annotation to get conversion.
# syntax_hint: |
# def read(item_id: int): return {"item_id": item_id}


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    r = client.get('/items/42')
    assert r.status_code == 200
    assert r.json() == {"item_id": 42}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
