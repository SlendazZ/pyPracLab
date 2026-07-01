# title: Confirmation Flag
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return click command with --yes flag; with --yes prints 'confirmed', without prints 'skipped'.
# examples:
# invoke --yes -> 'confirmed'
# hint: |
# @click.option('--yes', is_flag=True)
# syntax_hint: |
# if yes: echo confirmed else skipped


def make_confirm_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_confirm_cli()
    runner = CliRunner()
    assert runner.invoke(cli, ['--yes']).output.strip() == 'confirmed'
    assert runner.invoke(cli, []).output.strip() == 'skipped'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
