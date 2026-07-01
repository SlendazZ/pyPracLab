# title: Find All Paragraph Text
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Return list of stripped text from all <p> tags in order.
# examples:
# paragraph_texts('<p>a</p><p>b</p>') -> ['a','b']
# hint: |
# [p.get_text(strip=True) for p in soup.find_all('p')]
# syntax_hint: |
# soup.find_all('p')


def paragraph_texts(html: str) -> list[str]:
    pass


def run_tests() -> None:
    assert paragraph_texts('<p>a</p><p>b</p>') == ['a', 'b']
    assert paragraph_texts('<div>x</div>') == []
    assert paragraph_texts('<p> one </p>') == ['one']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
