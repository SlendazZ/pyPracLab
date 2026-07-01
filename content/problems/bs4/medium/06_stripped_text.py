# title: Stripped Text Content
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Parse the HTML and return all text from the body with whitespace stripped around each piece, joined by a single space.
# examples:
# stripped_text('<p>  hello  </p>') -> 'hello'
# hint: |
# get_text(' ', strip=True) joins text chunks with a space.
# syntax_hint: |
# BeautifulSoup(html, 'html.parser').get_text(' ', strip=True)


def stripped_text(html: str) -> str:
    pass


def run_tests() -> None:
    assert stripped_text('<p>  hello  </p>') == 'hello'
    assert stripped_text('<div><span> a </span><span> b </span></div>') == 'a b'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
