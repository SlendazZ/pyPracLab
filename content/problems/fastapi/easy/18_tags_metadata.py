# title: Route Tags Metadata
# track: fastapi
# difficulty: easy
# tags: fastapi, openapi
# description: |
# Implement register(app) adding GET /pets tagged 'animals' returning {'pets': []}. OpenAPI route must include tag.
# examples:
# route appears under 'animals' tag in openapi
# hint: |
# Pass tags=['animals'] to decorator.
# syntax_hint: |
# @app.get('/pets', tags=['animals'])


def register(app) -> None:
    pass


def run_tests() -> None:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    register(app)
    c = TestClient(app)
    assert c.get('/pets').json() == {'pets': []}
    schema = app.openapi()
    paths = schema['paths']['/pets']['get']['tags']
    assert 'animals' in paths
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
