# title: Custom Response Headers
# track: fastapi
# difficulty: medium
# tags: fastapi, headers
# description: |
# Implement register(app) adding GET /data returning JSON with custom header X-Custom: yes via Response.
# examples:
# get /data -> header X-Custom: yes
# hint: |
# Return JSONResponse or Response with headers dict.
# syntax_hint: |
# from fastapi.responses import JSONResponse; headers={'X-Custom': 'yes'}


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    r = c.get('/data')
    assert r.headers.get('x-custom') == 'yes'
    assert r.json() == {'ok': True}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
