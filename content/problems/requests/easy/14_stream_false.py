# title: Stream Disabled
# track: requests
# difficulty: easy
# tags: requests
# description: |
# Return kwargs dict for requests.get with stream=False explicitly.
# examples:
# no_stream() -> {'stream': False}
# hint: |
# Return {'stream': False}.
# syntax_hint: |
# return {'stream': False}


def no_stream() -> dict:
    pass


def run_tests() -> None:
    assert no_stream() == {'stream': False}
    assert no_stream()['stream'] is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
