# title: Prepared POST
# track: requests
# difficulty: medium
# tags: requests
# description: |
# Build and return a PreparedRequest for POST to url with form data dict (no network).
# examples:
# prepare_post(url, {'a':'1'}) -> PreparedRequest with method POST
# hint: |
# Request('POST', url, data=data); Session().prepare_request(req)
# syntax_hint: |
# from requests import Request, Session


def prepare_post(url: str, data: dict):
    pass


def run_tests() -> None:
    from requests import PreparedRequest
    p = prepare_post('https://x.test/api', {'a': '1'})
    assert isinstance(p, PreparedRequest)
    assert p.method == 'POST'
    body = p.body if isinstance(p.body, str) else p.body.decode()
    assert 'a=1' in body
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
