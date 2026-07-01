import click

def make_count_cli():
    @click.command()
    @click.argument('count', type=int)
    def cli(count: int):
        click.echo('x' * count)
    return cli
