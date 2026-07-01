import click

def make_cli_group():
    @click.group()
    def cli():
        pass

    @cli.command()
    def hello():
        click.echo('hi')

    @cli.command()
    def bye():
        click.echo('ciao')
    return cli
