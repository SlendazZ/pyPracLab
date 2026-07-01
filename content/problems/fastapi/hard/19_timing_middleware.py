# title: Timing Middleware
# track: fastapi
# difficulty: hard
# tags: fastapi, middleware
# description: |
# Implement register(app) adding HTTP middleware that sets response header X-Processed: 1 on every request.
# examples:
# any route returns X-Processed: 1 header
# hint: |
# Use @app.middleware('http') async wrapper.
# syntax_hint: |
# @app.middleware('http'); response.headers['X-Processed'] = '1'


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    @app.get('/ping')
    def ping():
        return {'pong': True}
    register(app)
    c = TestClient(app)
    r = c.get('/ping')
    assert r.headers.get('x-processed') == '1'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
