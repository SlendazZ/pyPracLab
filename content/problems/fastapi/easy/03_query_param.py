# title: Query Parameters
# track: fastapi
# difficulty: easy
# tags: fastapi, http
# description: |
# Create an app with GET '/search' that takes a 'q' query param and returns {"q": q}. Use a default of empty string.
# examples:
# GET /search?q=py -> {"q": "py"}
# hint: |
# Function parameters with defaults become query params.
# syntax_hint: |
# def search(q: str = ""): return {"q": q}


def create_app():
    pass


def run_tests() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(create_app())
    assert client.get('/search?q=py').json() == {"q": "py"}
    assert client.get('/search').json() == {"q": ""}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
