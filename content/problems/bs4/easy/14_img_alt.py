# title: Image Alt Texts
# track: bs4
# difficulty: easy
# tags: bs4, html
# description: |
# Return list of alt attribute values from all <img> tags (empty string if missing).
# examples:
# img_alts('<img alt="logo"><img>') -> ['logo','']
# hint: |
# [img.get('alt','') for img in soup.find_all('img')]
# syntax_hint: |
# soup.find_all('img')


def img_alts(html: str) -> list[str]:
    pass


def run_tests() -> None:
    assert img_alts('<img alt="logo"><img>') == ['logo', '']
    assert img_alts('<p>x</p>') == []
    assert img_alts('<img alt="a"><img alt="b">') == ['a', 'b']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
