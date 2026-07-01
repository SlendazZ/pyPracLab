import click

def make_confirm_cli():
    @click.command()
    @click.option('--yes', is_flag=True)
    def cli(yes: bool):
        click.echo('confirmed' if yes else 'skipped')
    return cli
