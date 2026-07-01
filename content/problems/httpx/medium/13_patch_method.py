# title: PATCH JSON Request
# track: httpx
# difficulty: medium
# tags: httpx, json
# description: |
# Build httpx.Request for PATCH with JSON body (no network).
# examples:
# patch_json(url, {'name':'x'}) has JSON body
# hint: |
# httpx.Request('PATCH', url, json=payload)
# syntax_hint: |
# httpx.Request('PATCH', url, json=payload)


def patch_json(url: str, payload: dict):
    pass


def run_tests() -> None:
    import json
    import httpx
    req = patch_json('https://x.test/items/1', {'name': 'x'})
    assert req.method == 'PATCH'
    assert json.loads(req.content) == {'name': 'x'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
