# title: Request ID Middleware
# track: servers
# difficulty: medium
# tags: middleware
# description: |
# Given headers dict, add X-Request-Id with the given id if not already present; return new dict.
# examples:
# add_request_id({}, 'abc') -> {'X-Request-Id':'abc'}
# hint: |
# Copy headers, set key if missing.
# syntax_hint: |
# h = dict(headers); h.setdefault('X-Request-Id', rid)


def add_request_id(headers: dict, rid: str) -> dict:
    pass


def run_tests() -> None:
    assert add_request_id({}, 'abc') == {'X-Request-Id': 'abc'}
    assert add_request_id({'X-Request-Id': 'x'}, 'abc') == {'X-Request-Id': 'x'}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
