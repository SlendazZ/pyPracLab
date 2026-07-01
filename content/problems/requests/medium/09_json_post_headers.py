# title: JSON POST Headers
# track: requests
# difficulty: medium
# tags: requests
# description: |
# Return headers dict for a JSON POST: Content-Type application/json and Accept application/json.
# examples:
# json_headers()['Content-Type'] == 'application/json'
# hint: |
# Static dict.
# syntax_hint: |
# return {'Content-Type': 'application/json', 'Accept': 'application/json'}


def json_headers() -> dict[str, str]:
    pass


def run_tests() -> None:
    h = json_headers()
    assert h['Content-Type'] == 'application/json'
    assert h['Accept'] == 'application/json'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
