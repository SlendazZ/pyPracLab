# title: Base URL Client
# track: httpx
# difficulty: medium
# tags: httpx, url
# description: |
# Return function using httpx.Client(base_url=...) with MockTransport to GET relative path and return status.
# examples:
# get_status('/api') with base_url returns 200
# hint: |
# Client(base_url='https://x.test', transport=MockTransport(...))
# syntax_hint: |
# with httpx.Client(base_url=base, transport=...) as c: c.get(path)


def get_status(base: str, path: str) -> int:
    pass


def run_tests() -> None:
    assert get_status('https://x.test', '/api') == 200
    assert get_status('https://x.test', '/health') == 200
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
