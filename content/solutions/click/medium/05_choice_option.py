import click

def make_color_command():
    @click.command()
    @click.option('--color', type=click.Choice(['red', 'green', 'blue']), required=True)
    def color(color):
        click.echo(color)
    return color
