# title: Result Callback
# track: click
# difficulty: hard
# tags: click, cli
# description: |
# Return click group where subcommand 'add' returns two ints and group result callback prints their sum.
# examples:
# invoke add 2 3 -> '5'
# hint: |
# @cli.result_callback(); @click.argument x,y on subcommand
# syntax_hint: |
# @cli.result_callback() def process(result): click.echo(sum(result))


def make_sum_group():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_sum_group()
    runner = CliRunner()
    assert runner.invoke(cli, ['add', '2', '3']).output.strip() == '5'
    assert runner.invoke(cli, ['add', '4', '5']).output.strip() == '9'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
