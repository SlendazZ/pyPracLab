# title: Typer Typed Command
# track: click
# difficulty: medium
# tags: typer, cli
# description: |
# Return a Typer app with one command that takes a required name: str and prints 'Hello {name}!'.
# examples:
# invoke with 'Ada' -> 'Hello Ada!'
# hint: |
# typer.Typer(); @app.command() with a typed name parameter.
# syntax_hint: |
# app = typer.Typer(); @app.command(); def greet(name: str): ...


def make_typer_app():
    pass


def run_tests() -> None:
    from typer.testing import CliRunner
    app = make_typer_app()
    runner = CliRunner()
    assert runner.invoke(app, ['Ada']).output.strip() == 'Hello Ada!'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
