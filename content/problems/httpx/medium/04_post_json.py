# title: POST JSON Body
# track: httpx
# difficulty: medium
# tags: httpx, json
# description: |
# Build an httpx Request for POST with a JSON body from the given dict (no network call). Content-Type should be application/json.
# examples:
# post_json(url, {'name': 'eli'}) has JSON body
# hint: |
# Use json= in httpx.Request for automatic JSON encoding.
# syntax_hint: |
# httpx.Request('POST', url, json={'name': 'eli'})


def post_json(url: str, payload: dict):
    pass


def run_tests() -> None:
    import json
    req = post_json('https://x.test/api', {'name': 'eli', 'age': 30})
    assert req.method == 'POST'
    assert json.loads(req.content) == {'name': 'eli', 'age': 30}
    assert 'application/json' in req.headers.get('content-type', '')
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
