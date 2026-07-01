import click

def make_greet_cli():
    @click.command()
    @click.option('--name', default='world')
    def cli(name: str):
        click.echo(f'Hello {name}!')
    return cli
