# title: Echo Greet
# track: click
# difficulty: easy
# tags: click, cli
# description: |
# Return click command with --name option defaulting to 'world'; echoes 'Hello {name}!'.
# examples:
# invoke -> 'Hello world!'; --name Ada -> 'Hello Ada!'
# hint: |
# @click.option('--name', default='world')
# syntax_hint: |
# click.echo(f'Hello {name}!')


def make_greet_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_greet_cli()
    runner = CliRunner()
    assert runner.invoke(cli, []).output.strip() == 'Hello world!'
    assert runner.invoke(cli, ['--name', 'Ada']).output.strip() == 'Hello Ada!'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
