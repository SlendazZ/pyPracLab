# title: Pattern Router
# track: servers
# difficulty: medium
# tags: routing, regex
# description: |
# Given routes as a list of (pattern, handler) where pattern may contain '<name>', return (handler, params_dict) for the first matching path, or (None, {}).
# examples:
# route([("/users/<id>", "show")], "/users/42") -> ("show", {"id": "42"})
# hint: |
# Convert '<name>' to a named regex group and match.
# syntax_hint: |
# re.sub(r'<(\w+)>', r'(?P<\1>[^/]+)', pattern)


def route(routes: list[tuple[str, str]], path: str) -> tuple:
    pass


def run_tests() -> None:
    routes = [('/users/<id>', 'show'), ('/', 'index')]
    assert route(routes, "/users/42") == ("show", {"id": "42"})
    assert route(routes, "/") == ("index", {})
    assert route(routes, "/missing") == (None, {})
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
