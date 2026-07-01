# title: Typer Optional Fields
# track: click
# difficulty: hard
# tags: typer, cli
# description: |
# Return a Typer app with a greet command: required name, optional --title (default empty). Print 'Hello, {title} {name}!' with title omitted when empty.
# examples:
# Ada -> 'Hello, Ada!'; --title Dr Ada -> 'Hello, Dr Ada!'
# hint: |
# typer.Option('') for title; omit title and extra space when empty.
# syntax_hint: |
# optional --title via typer.Option('', '--title')


def make_titled_app():
    pass


def run_tests() -> None:
    from typer.testing import CliRunner
    app = make_titled_app()
    runner = CliRunner()
    assert runner.invoke(app, ['Ada']).output.strip() == 'Hello, Ada!'
    assert runner.invoke(app, ['Ada', '--title', 'Dr']).output.strip() == 'Hello, Dr Ada!'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
