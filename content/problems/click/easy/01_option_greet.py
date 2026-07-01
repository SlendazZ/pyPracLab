# title: Command with an Option
# track: click
# difficulty: easy
# tags: click, cli
# description: |
# Return a click command that prints 'Hello {name}!' where name defaults to 'world' and can be set via --name.
# examples:
# invoke with --name Ada -> 'Hello Ada!'
# hint: |
# @click.command() with @click.option('--name', default='world').
# syntax_hint: |
# @click.option('--name', default='world')


def make_greet_command():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cmd = make_greet_command()
    runner = CliRunner()
    assert runner.invoke(cmd).output.strip() == 'Hello world!'
    assert runner.invoke(cmd, ['--name', 'Ada']).output.strip() == 'Hello Ada!'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
