# title: Config Loader
# track: apps
# difficulty: easy
# tags: config, io
# description: |
# Parse key=value lines (skip blanks and # comments) into a dict.
# examples:
# load_config('host=localhost\nport=80') -> {'host':'localhost','port':'80'}
# hint: |
# Split each line on first '='; strip whitespace.
# syntax_hint: |
# if line.startswith('#'): continue


def load_config(text: str) -> dict[str, str]:
    pass


def run_tests() -> None:
    assert load_config('host=localhost\nport=80') == {'host': 'localhost', 'port': '80'}
    assert load_config('# comment\n\na=1') == {'a': '1'}
    assert load_config('') == {}
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
