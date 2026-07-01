# title: Hidden Option
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return click command with hidden --token option; when provided prints 'ok', else 'no'.
# examples:
# invoke --token x -> 'ok'
# hint: |
# @click.option('--token', hidden=True)
# syntax_hint: |
# hidden=True keeps option out of help


def make_token_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_token_cli()
    runner = CliRunner()
    assert runner.invoke(cli, ['--token', 'x']).output.strip() == 'ok'
    assert runner.invoke(cli, []).output.strip() == 'no'
    assert '--token' not in runner.invoke(cli, ['--help']).output
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
