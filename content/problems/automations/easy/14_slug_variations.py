# title: Slug Variants
# track: automations
# difficulty: easy
# tags: string
# description: |
# Return three slug variants for a title: snake_case, kebab-case, and dot.case (all lowercase, spaces to separator).
# examples:
# slug_variants("Hello World") -> ("hello_world","hello-world","hello.world")
# hint: |
# Lowercase, replace spaces with _, -, and .
# syntax_hint: |
# s.lower().replace(' ', sep)


def slug_variants(title: str) -> tuple[str, str, str]:
    pass


def run_tests() -> None:
    assert slug_variants("Hello World") == ("hello_world","hello-world","hello.world")
    assert slug_variants("A") == ("a","a","a")
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
