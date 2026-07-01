import click

def make_upper_command():
    @click.command()
    @click.argument('name')
    def upper(name):
        click.echo(name.upper())
    return upper
