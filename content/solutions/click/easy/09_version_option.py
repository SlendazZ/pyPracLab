import click

@click.command()
@click.version_option('1.0.0')
def _version_cli():
    click.echo('app')

def make_version_cli():
    return _version_cli
