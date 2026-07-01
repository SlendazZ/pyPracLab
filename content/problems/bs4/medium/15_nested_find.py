# title: Nested Find
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Find div.main then the first a href inside it; return href or None.
# examples:
# main_link('<div class="main"><a href="/x">go</a></div>') -> '/x'
# hint: |
# soup.find('div', class_='main').find('a')['href']
# syntax_hint: |
# div = soup.find('div', class_='main'); a = div.find('a') if div else None


def main_link(html: str) -> str | None:
    pass


def run_tests() -> None:
    html = '<div class="main"><a href="/x">go</a></div>'
    assert main_link(html) == '/x'
    assert main_link('<div class="main"><p>x</p></div>') is None
    assert main_link('<a href="/y">y</a>') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
