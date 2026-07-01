# title: Merge Session Headers
# track: requests
# difficulty: medium
# tags: requests
# description: |
# Merge default session headers with per-request headers; request wins on conflict.
# examples:
# merge({'A':'1'},{'A':'2','B':'3'}) -> {'A':'2','B':'3'}
# hint: |
# {**session, **request}
# syntax_hint: |
# return {**session, **request}


def merge(session: dict, request: dict) -> dict:
    pass


def run_tests() -> None:
    assert merge({'A':'1'},{'A':'2','B':'3'}) == {'A':'2','B':'3'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
