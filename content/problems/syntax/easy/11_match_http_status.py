# title: Match - HTTP Status
# track: syntax
# difficulty: easy
# tags: match
# description: |
# Use a match statement to return 'ok' for 200, 'created' for 201, 'not found' for 404, 'error' otherwise.
# examples:
# describe(200) -> 'ok'
# describe(500) -> 'error'
# hint: |
# match status: case 200: ... case 404: ... case _: ...
# syntax_hint: |
# match/case with a default case _ catches everything else.


def describe(status: int) -> str:
    pass


def run_tests() -> None:
    assert describe(200) == 'ok'
    assert describe(201) == 'created'
    assert describe(404) == 'not found'
    assert describe(500) == 'error'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
