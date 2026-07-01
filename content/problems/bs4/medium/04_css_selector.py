# title: CSS Selector
# track: bs4
# difficulty: medium
# tags: bs4, css
# description: |
# Parse the HTML and return the text of the first element matching the CSS selector.
# examples:
# select_text('<div><p class="lead">hi</p></div>', 'p.lead') -> 'hi'
# hint: |
# soup.select_one(selector) finds the first CSS match.
# syntax_hint: |
# BeautifulSoup(html, 'html.parser').select_one('p.lead').get_text()


def select_text(html: str, selector: str) -> str:
    pass


def run_tests() -> None:
    html = '<div><p class="lead">hi</p><p class="lead">bye</p></div>'
    assert select_text(html, 'p.lead') == 'hi'
    assert select_text('<a href="#">link</a>', 'a') == 'link'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
