# title: Build a Timeout Tuple
# track: requests
# difficulty: easy
# tags: requests
# description: |
# Given connect and read seconds, return the requests-style timeout tuple (connect, read).
# examples:
# timeout_tuple(2, 5) -> (2, 5)
# hint: |
# requests accepts a (connect, read) tuple for timeout.
# syntax_hint: |
# return (connect, read)


def timeout_tuple(connect: float, read: float) -> tuple:
    pass


def run_tests() -> None:
    assert timeout_tuple(2, 5) == (2, 5)
    assert timeout_tuple(0.5, 1.5) == (0.5, 1.5)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
