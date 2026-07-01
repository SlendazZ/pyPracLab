# title: Extract Link Hrefs
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Parse the HTML and return a list of href attribute values from all anchor tags, in document order.
# examples:
# link_hrefs('<a href="/a">A</a><a href="/b">B</a>') -> ['/a', '/b']
# hint: |
# soup.find_all('a') then read tag['href'] for each.
# syntax_hint: |
# [a['href'] for a in soup.find_all('a')]


def link_hrefs(html: str) -> list[str]:
    pass


def run_tests() -> None:
    html = '<a href="/a">A</a><a href="/b">B</a>'
    assert link_hrefs(html) == ['/a', '/b']
    assert link_hrefs('<p>no links</p>') == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
