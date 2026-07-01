# title: Count Argument
# track: click
# difficulty: easy
# tags: click, cli
# description: |
# Return click command taking integer count arg; prints 'x' repeated count times on one line.
# examples:
# invoke 3 -> 'xxx'
# hint: |
# @click.argument('count', type=int)
# syntax_hint: |
# click.echo('x' * count)


def make_count_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_count_cli()
    runner = CliRunner()
    assert runner.invoke(cli, ['3']).output.strip() == 'xxx'
    assert runner.invoke(cli, ['0']).output.strip() == ''
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
