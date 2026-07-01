# title: Dedupe Query Params
# track: requests
# difficulty: easy
# tags: requests, url
# description: |
# Given a dict of params (possibly with None values), return a PreparedRequest whose url contains only the non-None params.
# examples:
# url excludes None params
# hint: |
# Filter None before passing to Request.
# syntax_hint: |
# {k: v for k, v in params.items() if v is not None}


def build_clean(url: str, params: dict):
    pass


def run_tests() -> None:
    req = build_clean('https://x.test/api', {'q': 'py', 'n': None})
    assert 'q=py' in req.url
    assert 'n=' not in req.url
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
