# title: Horizontal Rule
# track: rich
# difficulty: easy
# tags: rich, rule
# description: |
# Return a rich.rule.Rule with the given title.
# examples:
# rule('Section') -> Rule
# hint: |
# Rule(title)
# syntax_hint: |
# from rich.rule import Rule; Rule(title)


def rule(title: str) -> object:
    pass


def run_tests() -> None:
    from rich.rule import Rule
    r = rule('Section')
    assert isinstance(r, Rule)
    assert r.title == 'Section'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
