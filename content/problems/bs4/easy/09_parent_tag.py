# title: Parent Tag Name
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Parse HTML and return the parent tag name of the first <span> element, or None.
# examples:
# parent_name('<div><span>x</span></div>') -> 'div'
# hint: |
# soup.find('span').parent.name
# syntax_hint: |
# tag = soup.find('span'); tag.parent.name if tag else None


def parent_name(html: str) -> str | None:
    pass


def run_tests() -> None:
    assert parent_name('<div><span>x</span></div>') == 'div'
    assert parent_name('<span>lonely</span>') in ('[document]', 'html', 'body')
    assert parent_name('<p>no span</p>') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
