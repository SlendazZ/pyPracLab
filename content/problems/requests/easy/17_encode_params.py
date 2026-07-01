# title: Encode Query Params
# track: requests
# difficulty: easy
# tags: requests, url
# description: |
# Encode params dict into a query string using requests' prepared request or urllib.
# examples:
# encode_params({'a': 1, 'b': 2}) contains a=1 and b=2
# hint: |
# requests.models.RequestEncodingMixin._encode_params or urlencode
# syntax_hint: |
# from urllib.parse import urlencode


def encode_params(params: dict) -> str:
    pass


def run_tests() -> None:
    s = encode_params({'a': 1, 'b': 2})
    assert 'a=1' in s and 'b=2' in s
    assert encode_params({}) == ''
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
