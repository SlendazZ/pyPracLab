# title: Markdown Headings
# track: automations
# difficulty: easy
# tags: regex, string
# description: |
# Return a list of heading texts (without the leading # marks) from a markdown string.
# examples:
# headings("# Title\n## Sub") -> ["Title","Sub"]
# hint: |
# Match lines starting with one or more # then a space.
# syntax_hint: |
# re.findall(r'^#+\s+(.+)$', text, re.MULTILINE)


def headings(text: str) -> list[str]:
    pass


def run_tests() -> None:
    assert headings("# Title\n## Sub") == ["Title", "Sub"]
    assert headings("no headings") == []
    assert headings("### Deep") == ["Deep"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
