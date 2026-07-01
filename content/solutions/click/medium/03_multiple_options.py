import click

def make_bind_command():
    @click.command()
    @click.option('--host', default='localhost')
    @click.option('--port', default=8000)
    def bind(host, port):
        click.echo(f'{host}:{port}')
    return bind
