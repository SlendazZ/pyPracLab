# title: Filename Cleaner
# track: automations
# difficulty: easy
# tags: regex, string
# description: |
# Turn a messy title into a slug: lowercase, spaces to dashes, strip non-alphanumeric except dashes.
# examples:
# slugify("Hello, World!") -> "hello-world"
# hint: |
# re.sub(r'[^a-z0-9-]', '', ...) after replacing spaces.
# syntax_hint: |
# re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def slugify(text: str) -> str:
    pass


def run_tests() -> None:
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  Py   Prac Lab  ") == "py-prac-lab"
    assert slugify("ok") == "ok"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
