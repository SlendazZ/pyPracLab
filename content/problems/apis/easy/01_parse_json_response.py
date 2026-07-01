# title: Parse JSON Response
# track: apis
# difficulty: easy
# tags: json, api
# description: |
# Given a JSON string, parse it and return the value of the 'data' key.
# examples:
# get_data('{"data": [1, 2, 3]}') -> [1, 2, 3]
# hint: |
# json.loads turns a JSON string into Python objects.
# syntax_hint: |
# import json; obj = json.loads(text); return obj['data']


def get_data(text: str):
    pass


def run_tests() -> None:
    assert get_data('{"data": [1, 2, 3]}') == [1, 2, 3]
    assert get_data('{"data": {"x": 1}}') == {"x": 1}
    assert get_data('{"data": "hi"}') == "hi"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
