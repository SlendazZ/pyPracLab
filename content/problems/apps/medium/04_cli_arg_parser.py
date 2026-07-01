# title: Simple CLI Arg Parser
# track: apps
# difficulty: medium
# tags: cli
# description: |
# Parse argv like ['--name','eli','--count','3'] into {'name':'eli','count':'3'}. Support '--flag' (sets True).
# examples:
# parse(['--name','eli','--verbose']) -> {'name':'eli','verbose':True}
# hint: |
# Walk argv; a '--key value' pair sets the key; a lone '--flag' sets True.
# syntax_hint: |
# if arg.startswith('--'): if next doesn't start with '--': set key=next


def parse(argv: list[str]) -> dict:
    pass


def run_tests() -> None:
    assert parse(['--name', 'eli', '--verbose']) == {'name': 'eli', 'verbose': True}
    assert parse(['--count', '3']) == {'count': '3'}
    assert parse([]) == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
