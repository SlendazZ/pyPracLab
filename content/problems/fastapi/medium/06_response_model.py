# title: Response Model Filtering
# track: fastapi
# difficulty: medium
# tags: fastapi, pydantic
# description: |
# Create an app with GET '/user' returning a UserOut model {id, name} from internal data that also has a 'secret' field; the secret must NOT be in the response.
# examples:
# GET /user -> {"id":1,"name":"eli"} (no secret)
# hint: |
# Use response_model=UserOut on the route to filter fields.
# syntax_hint: |
# @app.get('/user', response_model=UserOut)


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    r = client.get('/user')
    assert r.status_code == 200
    body = r.json()
    assert body == {'id': 1, 'name': 'eli'}
    assert 'secret' not in body
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
