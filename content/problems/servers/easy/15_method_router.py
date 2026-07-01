# title: Method Router
# track: servers
# difficulty: easy
# tags: routing, http
# description: |
# Given a dict mapping HTTP method -> handler name and a method string, return the handler or 'not_found'.
# examples:
# route_method({'GET':'list','POST':'create'}, 'POST') -> 'create'
# hint: |
# Use dict.get with default.
# syntax_hint: |
# handlers.get(method.upper(), 'not_found')


def route_method(handlers: dict[str, str], method: str) -> str:
    pass


def run_tests() -> None:
    assert route_method({'GET': 'list', 'POST': 'create'}, 'POST') == 'create'
    assert route_method({'GET': 'list'}, 'DELETE') == 'not_found'
    assert route_method({}, 'GET') == 'not_found'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
