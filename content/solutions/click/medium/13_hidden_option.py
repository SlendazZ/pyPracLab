import click

def make_token_cli():
    @click.command()
    @click.option('--token', hidden=True, default=None)
    def cli(token):
        click.echo('ok' if token else 'no')
    return cli
