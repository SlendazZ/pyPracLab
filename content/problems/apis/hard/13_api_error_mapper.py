# title: API Error Mapper
# track: apis
# difficulty: hard
# tags: api, errors
# description: |
# Map HTTP status codes to short labels: 2xx ok, 4xx client, 5xx server, else unknown.
# examples:
# error_label(404) -> 'client'
# hint: |
# status // 100 gives the class digit.
# syntax_hint: |
# cls = code // 100


def error_label(code: int) -> str:
    pass


def run_tests() -> None:
    assert error_label(200) == 'ok'
    assert error_label(404) == 'client'
    assert error_label(500) == 'server'
    assert error_label(999) == 'unknown'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
