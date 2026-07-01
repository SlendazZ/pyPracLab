# title: Next Sibling Text
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Return stripped text of the next sibling element after the first <h1>, or None.
# examples:
# next_after_h1('<h1>T</h1><p>body</p>') -> 'body'
# hint: |
# find('h1').find_next_sibling().get_text(strip=True)
# syntax_hint: |
# h1 = soup.find('h1'); sib = h1.find_next_sibling()


def next_after_h1(html: str) -> str | None:
    pass


def run_tests() -> None:
    assert next_after_h1('<h1>T</h1><p>body</p>') == 'body'
    assert next_after_h1('<h1>Only</h1>') is None
    assert next_after_h1('<p>x</p>') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
