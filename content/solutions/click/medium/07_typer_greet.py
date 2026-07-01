import typer

def make_typer_app():
    app = typer.Typer()

    @app.command()
    def greet(name: str):
        typer.echo(f'Hello {name}!')

    return app
