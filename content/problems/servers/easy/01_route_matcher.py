# title: Route Matcher
# track: servers
# difficulty: easy
# tags: routing
# description: |
# Given a dict mapping path -> handler name and a request path, return the handler name, or 'not_found'.
# examples:
# match({"/": "home"}, "/health") -> "not_found"
# hint: |
# dict.get with a default.
# syntax_hint: |
# routes.get(path, 'not_found')


def match(routes: dict[str, str], path: str) -> str:
    pass


def run_tests() -> None:
    assert match({"/": "home", "/health": "health"}, "/health") == "health"
    assert match({"/": "home"}, "/missing") == "not_found"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
