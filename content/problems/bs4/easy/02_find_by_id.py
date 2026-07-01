# title: Find Element by ID
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Parse the HTML and return the text of the element with the given id attribute.
# examples:
# text_by_id('<p id="main">hi</p>', 'main') -> 'hi'
# hint: |
# soup.find(id=element_id) or soup.find(attrs={'id': element_id}).
# syntax_hint: |
# BeautifulSoup(html, 'html.parser').find(id='main').get_text()


def text_by_id(html: str, element_id: str) -> str:
    pass


def run_tests() -> None:
    assert text_by_id('<p id="main">hi</p>', 'main') == 'hi'
    assert text_by_id('<div id="x">one</div><div id="y">two</div>', 'y') == 'two'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
