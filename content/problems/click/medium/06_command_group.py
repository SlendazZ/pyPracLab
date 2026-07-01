# title: Command Group
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return a click group with subcommands 'hello' (prints 'hi') and 'bye' (prints 'ciao').
# examples:
# invoke hello -> 'hi'; invoke bye -> 'ciao'
# hint: |
# @click.group() on the parent; @cli.command() on each subcommand.
# syntax_hint: |
# @click.group(); @cli.command()


def make_cli_group():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_cli_group()
    runner = CliRunner()
    assert runner.invoke(cli, ['hello']).output.strip() == 'hi'
    assert runner.invoke(cli, ['bye']).output.strip() == 'ciao'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
