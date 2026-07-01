import click

def make_sum_group():
    @click.group()
    def cli():
        pass

    @cli.result_callback()
    def process(result):
        if result is not None:
            click.echo(str(sum(result)))

    @cli.command()
    @click.argument('x', type=int)
    @click.argument('y', type=int)
    def add(x: int, y: int):
        return [x, y]

    return cli
