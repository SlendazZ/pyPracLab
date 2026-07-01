# title: Build Query URL
# track: apis
# difficulty: easy
# tags: url, api
# description: |
# Given a base URL and a dict of query params, return the full URL with query string. Skip params whose value is None.
# examples:
# build_url("https://x.test/api", {"q":"py","page":1}) -> "https://x.test/api?q=py&page=1"
# hint: |
# urllib.parse.urlencode encodes a dict into a query string.
# syntax_hint: |
# f"{base}?{urlencode(params)}" ; filter None values first.


def build_url(base: str, params: dict) -> str:
    pass


def run_tests() -> None:
    url = build_url("https://x.test/api", {"q": "py", "page": 1})
    assert url == "https://x.test/api?q=py&page=1"
    assert build_url("https://x.test/api", {}) == "https://x.test/api"
    assert build_url("https://x.test/api", {"q": "py", "n": None}) == "https://x.test/api?q=py"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
