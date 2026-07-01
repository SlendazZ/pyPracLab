# title: Optional Query Param
# track: fastapi
# difficulty: easy
# tags: fastapi
# description: |
# Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). GET /search takes optional q query param; return {'q': q} where q defaults to empty string.
# examples:
# get('/search') -> {'q': ''}
# hint: |
# q: str = Query(default='') or q: str = ''
# syntax_hint: |
# def search(q: str = ''): return {'q': q}


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    assert c.get('/search').json() == {'q': ''}
    assert c.get('/search', params={'q': 'py'}).json() == {'q': 'py'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
