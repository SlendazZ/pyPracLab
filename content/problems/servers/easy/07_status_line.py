# title: Build Status Line
# track: servers
# difficulty: easy
# tags: http
# description: |
# Return an HTTP status line like 'HTTP/1.1 200 OK' given a status code and reason.
# examples:
# status_line(200, "OK") -> "HTTP/1.1 200 OK"
# hint: |
# Simple f-string formatting.
# syntax_hint: |
# f"HTTP/1.1 {code} {reason}"


def status_line(code: int, reason: str) -> str:
    pass


def run_tests() -> None:
    assert status_line(200, "OK") == "HTTP/1.1 200 OK"
    assert status_line(404, "Not Found") == "HTTP/1.1 404 Not Found"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
