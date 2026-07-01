# title: Retry Status Set
# track: requests
# difficulty: hard
# tags: requests
# description: |
# Return True if status code should be retried (408, 429, 500-599).
# examples:
# should_retry(503) -> True; should_retry(404) -> False
# hint: |
# Membership in known codes or 5xx range.
# syntax_hint: |
# code in (408, 429) or 500 <= code <= 599


def should_retry(code: int) -> bool:
    pass


def run_tests() -> None:
    assert should_retry(503) is True
    assert should_retry(429) is True
    assert should_retry(404) is False
    assert should_retry(200) is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
