# title: Merge Cookies
# track: requests
# difficulty: easy
# tags: requests, cookies
# description: |
# Merge two cookie dicts; values from the second override the first.
# examples:
# merge_cookies({'a':'1'},{'a':'2','b':'3'}) -> {'a':'2','b':'3'}
# hint: |
# Dict union {**a, **b}.
# syntax_hint: |
# return {**first, **second}


def merge_cookies(a: dict, b: dict) -> dict:
    pass


def run_tests() -> None:
    assert merge_cookies({'a': '1'}, {'a': '2', 'b': '3'}) == {'a': '2', 'b': '3'}
    assert merge_cookies({}, {'x': '1'}) == {'x': '1'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
