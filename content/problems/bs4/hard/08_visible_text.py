# title: Visible Text Without Scripts
# track: bs4
# difficulty: hard
# tags: bs4, html
# description: |
# Parse the HTML, remove script and style elements, then return the remaining visible text with whitespace stripped.
# examples:
# visible_text('<p>hi</p><script>alert(1)</script>') -> 'hi'
# hint: |
# soup.find_all(['script', 'style']) then decompose() each before get_text.
# syntax_hint: |
# for tag in soup.find_all(['script', 'style']): tag.decompose()


def visible_text(html: str) -> str:
    pass


def run_tests() -> None:
    html = '<html><head><style>body{}</style></head><body><p>hi</p><script>x=1</script></body></html>'
    assert visible_text(html) == 'hi'
    assert visible_text('<style>.x{}</style><div> ok </div>') == 'ok'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
