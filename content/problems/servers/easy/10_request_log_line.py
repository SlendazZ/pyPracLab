# title: Request Log Line
# track: servers
# difficulty: easy
# tags: string
# description: |
# Return a common-log-format style line: 'METHOD PATH STATUS SIZE'.
# examples:
# log_line("GET", "/a", 200, 12) -> "GET /a 200 12"
# hint: |
# f-string joins the four parts.
# syntax_hint: |
# f"{method} {path} {status} {size}"


def log_line(method: str, path: str, status: int, size: int) -> str:
    pass


def run_tests() -> None:
    assert log_line("GET", "/a", 200, 12) == "GET /a 200 12"
    assert log_line("POST", "/x", 500, 0) == "POST /x 500 0"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
