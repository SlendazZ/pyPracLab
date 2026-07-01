# title: Method + Path Router
# track: servers
# difficulty: easy
# tags: routing
# description: |
# Return the handler for a (method, path) tuple from a routes dict, or 'not_found'.
# examples:
# route({("GET","/"): "home"}, ("GET","/")) -> "home"
# hint: |
# Use the tuple as a dict key.
# syntax_hint: |
# routes.get((method, path), 'not_found')


def route(routes: dict, method: str, path: str) -> str:
    pass


def run_tests() -> None:
    r = {("GET", "/"): "home", ("POST", "/items"): "create"}
    assert route(r, "GET", "/") == "home"
    assert route(r, "POST", "/items") == "create"
    assert route(r, "DELETE", "/x") == "not_found"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
