# title: Decorator - Shout
# track: syntax
# difficulty: medium
# tags: decorator
# description: |
# Write a decorator `shout` that uppercases string return values. Non-string returns pass through unchanged.
# examples:
# shout(greet)("eli") -> "HELLO ELI"
# hint: |
# Define wrapper(*args, **kwargs); call func, then .upper() if the result is a str.
# syntax_hint: |
# functools.wraps(func) keeps the wrapped function's metadata.


def shout(func):
    pass


def run_tests() -> None:
    @shout
    def greet(name: str) -> str:
        return f"hello {name}"
    @shout
    def add(a: int, b: int) -> int:
        return a + b
    assert greet("eli") == "HELLO ELI"
    assert greet("world") == "HELLO WORLD"
    assert add(2, 3) == 5
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
