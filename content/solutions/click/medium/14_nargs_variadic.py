import click

def make_files_cli():
    @click.command()
    @click.argument('files', nargs=-1)
    def cli(files):
        click.echo(' '.join(files))
    return cli
