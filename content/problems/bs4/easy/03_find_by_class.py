# title: Find Elements by Class
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Parse the HTML and return a list of text contents for all elements with the given CSS class.
# examples:
# texts_by_class('<p class="item">a</p><p class="item">b</p>', 'item') -> ['a', 'b']
# hint: |
# soup.find_all(class_=class_name) returns all matching tags.
# syntax_hint: |
# [t.get_text() for t in soup.find_all(class_='item')]


def texts_by_class(html: str, class_name: str) -> list[str]:
    pass


def run_tests() -> None:
    html = '<p class="item">a</p><p class="item">b</p><p class="other">c</p>'
    assert texts_by_class(html, 'item') == ['a', 'b']
    assert texts_by_class('<span class="x">z</span>', 'x') == ['z']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
