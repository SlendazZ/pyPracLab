# title: Version Option
# track: click
# difficulty: easy
# tags: click, cli
# description: |
# Return a click command that prints version when --version is passed.
# examples:
# invoke --version -> '1.0.0'
# hint: |
# @click.version_option(version='1.0.0')
# syntax_hint: |
# @click.version_option('1.0.0')


def make_version_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_version_cli()
    runner = CliRunner()
    r = runner.invoke(cli, ['--version'])
    assert '1.0.0' in r.output
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
