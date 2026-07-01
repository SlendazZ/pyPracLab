# title: Multiple Options with Defaults
# track: click
# difficulty: medium
# tags: click, cli
# description: |
# Return a click command with --host (default 'localhost') and --port (default 8000) that prints 'host:port'.
# examples:
# default -> 'localhost:8000'; --host x --port 90 -> 'x:90'
# hint: |
# Two @click.option decorators; port is passed as int by click.
# syntax_hint: |
# @click.option('--host', default='localhost'); @click.option('--port', default=8000)


def make_bind_command():
    pass


def run_tests() -> None:
    from click.testing import CliRunner
    cmd = make_bind_command()
    runner = CliRunner()
    assert runner.invoke(cmd).output.strip() == 'localhost:8000'
    assert runner.invoke(cmd, ['--host', 'x', '--port', '90']).output.strip() == 'x:90'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
