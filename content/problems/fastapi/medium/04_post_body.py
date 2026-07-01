# title: POST with a Pydantic Body
# track: fastapi
# difficulty: medium
# tags: fastapi, pydantic
# description: |
# Create an app with POST '/echo' that accepts a Pydantic model {name: str, age: int} and returns it unchanged.
# examples:
# POST /echo {name,age} -> same body
# hint: |
# Define a BaseModel and type the request body parameter.
# syntax_hint: |
# class Person(BaseModel): name: str; age: int


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    r = client.post('/echo', json={'name': 'eli', 'age': 30})
    assert r.status_code == 200
    assert r.json() == {'name': 'eli', 'age': 30}
    assert client.post('/echo', json={'name': 'eli'}).status_code == 422
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
