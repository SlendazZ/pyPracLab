import typer

def make_titled_app():
    app = typer.Typer()

    @app.command()
    def greet(
        name: str,
        title: str = typer.Option('', '--title'),
    ):
        prefix = f'{title} ' if title else ''
        typer.echo(f'Hello, {prefix}{name}!')

    return app
