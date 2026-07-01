---
title: Click CLI Basics
track: click
difficulty: easy
tags: click, cli
exercise: content/problems/click/easy/01_option_greet.py
---

# Click CLI Basics

## Overview

Click is Python's most popular library for building command-line interfaces. Instead of manually parsing `sys.argv`, you decorate functions with `@click.command()`, `@click.option()`, and `@click.argument()` — Click handles parsing, help text, and error messages for you.

Before Click, CLI code looked like this:

```python
import sys
name = 'world'
for i, arg in enumerate(sys.argv[1:]):
    if arg == '--name' and i + 1 < len(sys.argv):
        name = sys.argv[i + 1]
print(f'Hello {name}!')
```

Click replaces that boilerplate with declarative decorators and gives you `--help` for free.

Real-world uses:

- Deployment scripts (`deploy --env staging`)
- Data tools (`csv-tool merge a.csv b.csv --output out.csv`)
- Dev utilities (`lint --fix`, `seed-db --count 100`)
- Packaging CLI entry points in `pyproject.toml`

Install with `pip install click`. Test CLIs with `CliRunner` — no subprocess, no real terminal required.

## A simple command

```python
import click

@click.command()
@click.option('--name', default='world', help='Who to greet.')
def greet(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    greet()
```

Run it:

```bash
python greet.py                  # Hello world!
python greet.py --name Ada         # Hello Ada!
python greet.py --help             # shows options and defaults
```

**Exercise pattern:** return a command from a factory function:

```python
def make_greet_command():
    @click.command()
    @click.option('--name', default='world')
    def greet(name):
        click.echo(f'Hello {name}!')
    return greet
```

`click.echo()` is preferred over `print()` because it handles encoding and Unicode correctly across platforms (especially Windows).

## Options vs arguments

- **Options** (`--flag`, `-f`) are usually optional and named
- **Arguments** are positional and often required

```python
@click.command()
@click.argument('filename')
@click.option('--verbose', '-v', is_flag=True, help='More output.')
def process(filename, verbose):
    if verbose:
        click.echo(f'Processing {filename}...')
    click.echo('done')
```

```bash
python process.py data.csv -v
python process.py --help
```

Think of arguments as nouns (what to act on) and options as modifiers (how to act).

## Typed options

Click converts strings from the shell to Python types automatically:

```python
@click.command()
@click.option('--count', default=1, type=int, help='Number of greetings.')
@click.option('--name', default='world')
def greet(count, name):
    for _ in range(count):
        click.echo(f'Hello {name}!')
```

Invalid input produces a friendly error:

```bash
python greet.py --count abc
# Error: Invalid value for '--count': 'abc' is not a valid integer.
```

Useful built-in types:

| Type                         | Validates                    |
|------------------------------|------------------------------|
| `int`, `float`, `str`        | Basic Python types           |
| `click.Path(exists=True)`    | File or directory exists     |
| `click.Choice(['a', 'b'])`   | Value in allowed list        |
| `click.DateTime()`           | Parses date strings          |

```python
@click.option('--env', type=click.Choice(['dev', 'staging', 'prod']), default='dev')
@click.argument('config', type=click.Path(exists=True))
def deploy(config, env):
    click.echo(f'Deploying {config} to {env}')
```

## Worked example: file line counter

```python
import click

@click.command()
@click.argument('path', type=click.Path(exists=True, dir_okay=False))
@click.option('--max', default=None, type=int, help='Stop after N lines.')
def linecount(path, max):
    with open(path, encoding='utf-8') as f:
        for i, _ in enumerate(f, start=1):
            if max is not None and i > max:
                break
    click.echo(i)
```

Click validates that the file exists **before** your function runs — you never get a confusing `FileNotFoundError` deep inside your logic.

## Worked example: deploy CLI

```python
import click

@click.command()
@click.option('--env', type=click.Choice(['staging', 'prod']), required=True)
@click.option('--dry-run', is_flag=True, help='Print plan without deploying.')
@click.option('--version', is_flag=True, help='Show version and exit.')
def deploy(env, dry_run, version):
    if version:
        click.echo('myapp 1.2.0')
        return
    if env == 'prod' and not dry_run:
        click.confirm('Deploy to PRODUCTION?', abort=True)
    action = 'Would deploy' if dry_run else 'Deploying'
    click.echo(f'{action} to {env}...')
```

```bash
python deploy.py --env staging --dry-run
python deploy.py --env prod          # prompts for confirmation
```

## Testing with CliRunner

Never shell out to test a CLI. `CliRunner.invoke()` calls your command in-process:

```python
from click.testing import CliRunner

def test_greet_default():
    runner = CliRunner()
    result = runner.invoke(greet, [])
    assert result.exit_code == 0
    assert 'Hello world!' in result.output

def test_greet_named():
    runner = CliRunner()
    result = runner.invoke(greet, ['--name', 'Ada'])
    assert result.exit_code == 0
    assert 'Ada' in result.output
```

**Testing with files:** use `CliRunner.isolated_filesystem()` or pytest `tmp_path`:

```python
def test_linecount(tmp_path):
    f = tmp_path / 'sample.txt'
    f.write_text('one\ntwo\nthree\n', encoding='utf-8')
    runner = CliRunner()
    result = runner.invoke(linecount, [str(f)])
    assert result.exit_code == 0
    assert result.output.strip() == '3'
```

**Testing prompts:** pass `input=` to answer interactive questions:

```python
def test_deploy_prod_confirmed():
    runner = CliRunner()
    result = runner.invoke(deploy, ['--env', 'prod'], input='y\n')
    assert result.exit_code == 0
    assert 'Deploying' in result.output
```

## Subcommands (command groups)

Larger tools split into subcommands like `git commit` or `docker run`:

```python
@click.group()
def cli():
    """My toolkit."""

@cli.command()
@click.option('--name', default='world')
def greet(name):
    click.echo(f'Hello {name}!')

@cli.command()
def version():
    click.echo('1.0.0')

if __name__ == '__main__':
    cli()
```

```bash
python tool.py --help
python tool.py greet --name Ada
python tool.py version
```

## Environment variables

Read config from the environment with `envvar=`:

```python
@click.option('--api-key', envvar='MYAPP_API_KEY', required=True)
def upload(api_key):
    click.echo(f'Using key ending in ...{api_key[-4:]}')
```

```bash
export MYAPP_API_KEY=secret123
python upload.py   # --api-key not needed on command line
```

Keeps secrets out of shell history.

## Prompts and confirmations

```python
@click.command()
def setup():
    name = click.prompt('Project name')
    password = click.prompt('Password', hide_input=True)
    env = click.prompt('Environment', type=click.Choice(['staging', 'prod']))
    if env == 'prod':
        click.confirm('Deploy to PRODUCTION?', abort=True)
    click.echo(f'Creating {name} in {env}')
```

## Exit codes and errors

```python
@click.command()
def fail():
    click.echo('Something went wrong', err=True)
    raise SystemExit(1)
```

Or use Click's exception for formatted errors:

```python
raise click.ClickException('Config file not found')
# prints: Error: Config file not found
# exit code: 2
```

CliRunner captures `result.exit_code` and `result.exception`.

## Typer: type hints on top of Click

Typer builds on Click using annotations — great for new projects:

```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str = 'world'):
    typer.echo(f'Hello {name}!')

if __name__ == '__main__':
    app()
```

Under the hood it is still Click — same `CliRunner` patterns apply.

## Packaging as an installed command

In `pyproject.toml`:

```toml
[project.scripts]
mytool = "myapp.cli:main"
```

Where `main` is your `@click.group()` or `@click.command()` function. After `pip install -e .`, users run `mytool --help` from anywhere.

## Common pitfalls

- Forgetting `@click.command()` on the function you invoke
- Option names must use `--kebab-case` or `--snake_case`, not spaces
- Using `print()` instead of `click.echo()` (encoding issues on Windows)
- Testing via subprocess instead of `CliRunner` (slow and brittle)
- Boolean flags: use `is_flag=True`, not `type=bool` (Click treats `--flag False` oddly with `type=bool`)
- Decorator order: `@click.command()` goes **below** `@click.option()` (options closest to the function)
- Mutable default arguments in command callbacks — pass via option, not as function default list/dict

## Practice

Return a click command with a `--name` option.

## Summary

Click = decorators for commands, options, and arguments + automatic `--help`. Test with `CliRunner.invoke()` in pytest. Start with a single `@click.command()`, add typed options, then grow into `@click.group()` subcommands as your tool gets bigger. Typer offers the same runtime with type-hint ergonomics.
