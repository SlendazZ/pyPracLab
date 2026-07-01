# title: Escape Rich Markup
# track: rich
# difficulty: hard
# tags: rich
# description: |
# Escape [ and ] in user text for safe rich markup by replacing with \\[ and \\].
# examples:
# escape_markup("[bold]") -> "\\[bold\\]"
# hint: |
# Replace [ with \\[ and ] with \\]
# syntax_hint: |
# s.replace('[', '\\[').replace(']', '\\]')


def escape_markup(s: str) -> str:
    pass


def run_tests() -> None:
    assert escape_markup("[bold]") == "\\[bold\\]"
    assert escape_markup("plain") == "plain"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
