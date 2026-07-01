# title: Decompose Script Tag
# track: bs4
# difficulty: medium
# tags: bs4, html
# description: |
# Parse HTML, decompose all <script> tags, return remaining text stripped.
# examples:
# without_scripts('<p>hi</p><script>x</script>') -> 'hi'
# hint: |
# for tag in soup.find_all('script'): tag.decompose()
# syntax_hint: |
# soup.find_all('script'); tag.decompose()


def without_scripts(html: str) -> str:
    pass


def run_tests() -> None:
    assert without_scripts('<p>hi</p><script>x</script>') == 'hi'
    assert without_scripts('<script>a</script><div>ok</div>') == 'ok'
    assert without_scripts('<p>plain</p>') == 'plain'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
