import click

def make_greet_command():
    @click.command()
    @click.option('--name', default='world')
    def greet(name):
        click.echo(f'Hello {name}!')
    return greet
