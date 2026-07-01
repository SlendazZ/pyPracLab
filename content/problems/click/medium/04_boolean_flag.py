# title: Boolean Flag
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return a click command with --verbose/--no-verbose that prints 'verbose' or 'quiet' accordingly.
# examples:
# default -> 'quiet'; --verbose -> 'verbose'
# hint: |
# Use --verbose/--no-verbose as a boolean flag pair.
# syntax_hint: |
# @click.option('--verbose/--no-verbose', default=False)


def make_mode_command():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cmd = make_mode_command()
    runner = CliRunner()
    assert runner.invoke(cmd).output.strip() == 'quiet'
    assert runner.invoke(cmd, ['--verbose']).output.strip() == 'verbose'
    assert runner.invoke(cmd, ['--no-verbose']).output.strip() == 'quiet'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
