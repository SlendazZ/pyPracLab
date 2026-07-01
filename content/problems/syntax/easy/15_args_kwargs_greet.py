# title: *args and **kwargs - Greet
# track: syntax
# difficulty: easy
# tags: args, kwargs
# description: |
# Write greet(greeting, *names, **punctuation) that returns 'Hi, a and b!' where '!' comes from the punct keyword.
# examples:
# greet("Hi","a","b",punct="!") -> "Hi, a and b!"
# hint: |
# *names collects extra positional args; **punctuation collects keyword args.
# syntax_hint: |
# " and ".join(names); punct = punctuation.get("punct", "")


def greet(greeting: str, *names, **punctuation) -> str:
    pass


def run_tests() -> None:
    assert greet("Hi", "a", "b", punct="!") == "Hi, a and b!"
    assert greet("Hey", "solo") == "Hey, solo"
    assert greet("Yo", "a", "b", "c", punct="?") == "Yo, a and b and c?"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
