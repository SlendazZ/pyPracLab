# title: Variadic Arguments
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return click command with nargs=-1 on files argument; prints space-joined args.
# examples:
# invoke a b c -> 'a b c'
# hint: |
# @click.argument('files', nargs=-1)
# syntax_hint: |
# click.echo(' '.join(files))


def make_files_cli():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cli = make_files_cli()
    runner = CliRunner()
    assert runner.invoke(cli, ['a', 'b', 'c']).output.strip() == 'a b c'
    assert runner.invoke(cli, []).output.strip() == ''
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
