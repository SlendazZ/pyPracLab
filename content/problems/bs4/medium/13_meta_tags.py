# title: Meta Tag Content
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Return dict of meta name -> content for <meta name='...' content='...'> tags.
# examples:
# meta_dict(html) -> {'description': '...'}
# hint: |
# find_all('meta'); read name and content attrs.
# syntax_hint: |
# m.get('name'): m.get('content') for m in soup.find_all('meta') if m.get('name')


def meta_dict(html: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    html = '<meta name="description" content="demo"><meta name="author" content="eli">'
    assert meta_dict(html) == {'description': 'demo', 'author': 'eli'}
    assert meta_dict('<p>x</p>') == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
