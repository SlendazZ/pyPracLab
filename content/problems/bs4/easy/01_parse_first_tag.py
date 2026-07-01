# title: Parse HTML and Find First Tag
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Parse the HTML string with BeautifulSoup and return the name of the first tag in the document.
# examples:
# first_tag('<p>hi</p>') -> 'p'
# hint: |
# BeautifulSoup(html, 'html.parser'); soup.find() returns the first element.
# syntax_hint: |
# from bs4 import BeautifulSoup; BeautifulSoup(html, 'html.parser').find().name


def first_tag(html: str) -> str:
    pass


def run_tests() -> None:
    assert first_tag('<p>hi</p>') == 'p'
    assert first_tag('<div><span>x</span></div>') == 'div'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
