# title: Middleware Chain
# track: servers
# difficulty: medium
# tags: pipeline
# description: |
# Each middleware takes (req, next) and returns a response. Compose a list of middlewares around a final handler into one callable.
# examples:
# compose(middlewares, final)(req) -> response
# hint: |
# Build the chain from the inside out, wrapping each middleware around the next.
# syntax_hint: |
# for mw in reversed(middlewares): handler = wrap(mw, handler)


def compose(middlewares: list, final):
    pass


def run_tests() -> None:
    log = []
    def mw_a(req, nxt):
        log.append('a-in'); r = nxt(req); log.append('a-out'); return r
    def mw_b(req, nxt):
        log.append('b-in'); r = nxt(req); log.append('b-out'); return r
    def final(req):
        log.append('final'); return {'status': 200}
    handler = compose([mw_a, mw_b], final)
    assert handler({'path': '/'}) == {'status': 200}
    assert log == ['a-in', 'b-in', 'final', 'b-out', 'a-out']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
