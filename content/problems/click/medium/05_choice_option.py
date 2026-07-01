# title: Choice Option
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return a click command with --color choice of red, green, or blue that prints the selected color.
# examples:
# --color green -> 'green'
# hint: |
# click.Choice(['red', 'green', 'blue']) as the type= for the option.
# syntax_hint: |
# @click.option('--color', type=click.Choice(['red', 'green', 'blue']))


def make_color_command():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cmd = make_color_command()
    runner = CliRunner()
    assert runner.invoke(cmd, ['--color', 'green']).output.strip() == 'green'
    assert runner.invoke(cmd, ['--color', 'blue']).exit_code == 0
    assert runner.invoke(cmd, ['--color', 'purple']).exit_code != 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
