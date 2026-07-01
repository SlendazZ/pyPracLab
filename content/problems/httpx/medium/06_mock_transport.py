# title: MockTransport Handler
# track: httpx
# difficulty: medium
# tags: httpx, testing
# description: |
# Return a function that uses httpx.Client with MockTransport to GET the url and return the JSON body from a fixed {'message': 'ok'} response.
# examples:
# fetch_json('https://x.test/api') -> {'message': 'ok'}
# hint: |
# Define a handler returning httpx.Response(200, json={...}); use MockTransport(handler).
# syntax_hint: |
# def handler(req): return httpx.Response(200, json={'message': 'ok'})


def fetch_json(url: str) -> dict:
    pass


def run_tests() -> None:
    assert fetch_json('https://x.test/api') == {'message': 'ok'}
    assert fetch_json('https://other.test/') == {'message': 'ok'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
