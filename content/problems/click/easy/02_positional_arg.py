# title: Positional Argument
# track: click
# difficulty: easy
# tags: click, cli
# description: |
# Return a click command that takes a required NAME argument and prints it uppercased.
# examples:
# invoke with 'ada' -> 'ADA'
# hint: |
# Use @click.argument('name') on the command function.
# syntax_hint: |
# @click.argument('name')


def make_upper_command():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cmd = make_upper_command()
    runner = CliRunner()
    assert runner.invoke(cmd, ['ada']).output.strip() == 'ADA'
    assert runner.invoke(cmd, ['py']).output.strip() == 'PY'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
