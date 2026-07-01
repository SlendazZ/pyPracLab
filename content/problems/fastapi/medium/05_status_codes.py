# title: Custom Status Codes
# track: fastapi
# difficulty: medium
# tags: fastapi, http
# description: |
# Create an app with POST '/create' that returns status 201 and {"created": True}.
# examples:
# POST /create -> 201 {"created": true}
# hint: |
# from fastapi import status; use status_code=status.HTTP_201_CREATED.
# syntax_hint: |
# @app.post('/create', status_code=status.HTTP_201_CREATED)


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    r = client.post('/create')
    assert r.status_code == 201
    assert r.json() == {"created": True}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
