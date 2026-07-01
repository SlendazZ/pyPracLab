# title: Event Hooks
# track: httpx
# difficulty: medium
# tags: httpx, hooks
# description: |
# Build httpx.Client with event hook that records request method; return recorded list via GET.
# examples:
# fetch_with_hook() records 'GET'
# hint: |
# event_hooks={'request': [callback]} on Client.
# syntax_hint: |
# event_hooks={'request': [lambda req: log.append(req.method)]}


def fetch_with_hook(url: str) -> list[str]:
    pass


def run_tests() -> None:
    log = fetch_with_hook('https://x.test/api')
    assert log == ['GET']
    assert fetch_with_hook('https://other.test/') == ['GET']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
