# title: Basic Auth Header Value
# track: requests
# difficulty: easy
# tags: requests, auth
# description: |
# Return the Authorization header value for HTTP basic auth (user:pass base64).
# examples:
# auth_header('u','p') starts with 'Basic '
# hint: |
# Base64-encode 'user:pass' and prefix with 'Basic '.
# syntax_hint: |
# import base64; 'Basic ' + b64encode(f'{u}:{p}'.encode()).decode()


def auth_header(user: str, password: str) -> str:
    pass


def run_tests() -> None:
    h = auth_header('u', 'p')
    assert h.startswith('Basic ')
    import base64
    assert base64.b64decode(h[6:]) == b'u:p'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
