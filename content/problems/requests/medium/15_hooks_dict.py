# title: Response Hooks Dict
# track: requests
# difficulty: medium
# tags: requests, hooks
# description: |
# Given a callback function, return a requests hooks dict that registers it for the 'response' event.
# examples:
# build_hooks(fn) -> {'response': [fn]}
# hint: |
# Hooks map event name to list of callables.
# syntax_hint: |
# return {'response': [callback]}


def build_hooks(callback) -> dict:
    pass


def run_tests() -> None:
    log = []
    def cb(r, *a, **k): log.append(r)
    h = build_hooks(cb)
    assert 'response' in h
    assert h['response'][0] is cb
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
