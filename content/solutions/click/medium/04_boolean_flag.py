import click

def make_mode_command():
    @click.command()
    @click.option('--verbose/--no-verbose', default=False)
    def mode(verbose):
        click.echo('verbose' if verbose else 'quiet')
    return mode
