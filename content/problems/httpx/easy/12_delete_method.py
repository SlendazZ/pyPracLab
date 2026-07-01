# title: DELETE Request
# track: httpx
# difficulty: easy
# tags: httpx
# description: |
# Build httpx.Request for DELETE method (no network).
# examples:
# delete_request(url) -> Request with method DELETE
# hint: |
# httpx.Request('DELETE', url)
# syntax_hint: |
# httpx.Request('DELETE', url)


def delete_request(url: str):
    pass


def run_tests() -> None:
    import httpx
    req = delete_request('https://x.test/items/1')
    assert isinstance(req, httpx.Request)
    assert req.method == 'DELETE'
    assert str(req.url) == 'https://x.test/items/1'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
