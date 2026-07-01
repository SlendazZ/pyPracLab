"""Click and Typer problem specs."""

PROBLEMS = [
    {
        "slug": "01_option_greet",
        "track": "click", "difficulty": "easy",
        "title": "Command with an Option",
        "tags": ["click", "cli"],
        "description": "Return a click command that prints 'Hello {name}!' where name defaults to 'world' and can be set via --name.",
        "examples": "invoke with --name Ada -> 'Hello Ada!'",
        "hint": "@click.command() with @click.option('--name', default='world').",
        "syntax_hint": "@click.option('--name', default='world')",
        "signature": "def make_greet_command():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cmd = make_greet_command()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cmd).output.strip() == 'Hello world!'\n"
            "    assert runner.invoke(cmd, ['--name', 'Ada']).output.strip() == 'Hello Ada!'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_greet_command():\n"
            "    @click.command()\n"
            "    @click.option('--name', default='world')\n"
            "    def greet(name):\n"
            "        click.echo(f'Hello {name}!')\n"
            "    return greet\n"
        ),
    },
    {
        "slug": "02_positional_arg",
        "track": "click", "difficulty": "easy",
        "title": "Positional Argument",
        "tags": ["click", "cli"],
        "description": "Return a click command that takes a required NAME argument and prints it uppercased.",
        "examples": "invoke with 'ada' -> 'ADA'",
        "hint": "Use @click.argument('name') on the command function.",
        "syntax_hint": "@click.argument('name')",
        "signature": "def make_upper_command():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cmd = make_upper_command()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cmd, ['ada']).output.strip() == 'ADA'\n"
            "    assert runner.invoke(cmd, ['py']).output.strip() == 'PY'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_upper_command():\n"
            "    @click.command()\n"
            "    @click.argument('name')\n"
            "    def upper(name):\n"
            "        click.echo(name.upper())\n"
            "    return upper\n"
        ),
    },
    {
        "slug": "03_multiple_options",
        "track": "click", "difficulty": "medium",
        "title": "Multiple Options with Defaults",
        "tags": ["click", "cli"],
        "description": "Return a click command with --host (default 'localhost') and --port (default 8000) that prints 'host:port'.",
        "examples": "default -> 'localhost:8000'; --host x --port 90 -> 'x:90'",
        "hint": "Two @click.option decorators; port is passed as int by click.",
        "syntax_hint": "@click.option('--host', default='localhost'); @click.option('--port', default=8000)",
        "signature": "def make_bind_command():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cmd = make_bind_command()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cmd).output.strip() == 'localhost:8000'\n"
            "    assert runner.invoke(cmd, ['--host', 'x', '--port', '90']).output.strip() == 'x:90'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_bind_command():\n"
            "    @click.command()\n"
            "    @click.option('--host', default='localhost')\n"
            "    @click.option('--port', default=8000)\n"
            "    def bind(host, port):\n"
            "        click.echo(f'{host}:{port}')\n"
            "    return bind\n"
        ),
    },
    {
        "slug": "04_boolean_flag",
        "track": "click", "difficulty": "medium",
        "title": "Boolean Flag",
        "tags": ["click", "cli"],
        "description": "Return a click command with --verbose/--no-verbose that prints 'verbose' or 'quiet' accordingly.",
        "examples": "default -> 'quiet'; --verbose -> 'verbose'",
        "hint": "Use --verbose/--no-verbose as a boolean flag pair.",
        "syntax_hint": "@click.option('--verbose/--no-verbose', default=False)",
        "signature": "def make_mode_command():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cmd = make_mode_command()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cmd).output.strip() == 'quiet'\n"
            "    assert runner.invoke(cmd, ['--verbose']).output.strip() == 'verbose'\n"
            "    assert runner.invoke(cmd, ['--no-verbose']).output.strip() == 'quiet'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_mode_command():\n"
            "    @click.command()\n"
            "    @click.option('--verbose/--no-verbose', default=False)\n"
            "    def mode(verbose):\n"
            "        click.echo('verbose' if verbose else 'quiet')\n"
            "    return mode\n"
        ),
    },
    {
        "slug": "05_choice_option",
        "track": "click", "difficulty": "medium",
        "title": "Choice Option",
        "tags": ["click", "cli"],
        "description": "Return a click command with --color choice of red, green, or blue that prints the selected color.",
        "examples": "--color green -> 'green'",
        "hint": "click.Choice(['red', 'green', 'blue']) as the type= for the option.",
        "syntax_hint": "@click.option('--color', type=click.Choice(['red', 'green', 'blue']))",
        "signature": "def make_color_command():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cmd = make_color_command()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cmd, ['--color', 'green']).output.strip() == 'green'\n"
            "    assert runner.invoke(cmd, ['--color', 'blue']).exit_code == 0\n"
            "    assert runner.invoke(cmd, ['--color', 'purple']).exit_code != 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_color_command():\n"
            "    @click.command()\n"
            "    @click.option('--color', type=click.Choice(['red', 'green', 'blue']), required=True)\n"
            "    def color(color):\n"
            "        click.echo(color)\n"
            "    return color\n"
        ),
    },
    {
        "slug": "06_command_group",
        "track": "click", "difficulty": "medium",
        "title": "Command Group",
        "tags": ["click", "cli"],
        "description": "Return a click group with subcommands 'hello' (prints 'hi') and 'bye' (prints 'ciao').",
        "examples": "invoke hello -> 'hi'; invoke bye -> 'ciao'",
        "hint": "@click.group() on the parent; @cli.command() on each subcommand.",
        "syntax_hint": "@click.group(); @cli.command()",
        "signature": "def make_cli_group():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from click.testing import CliRunner\n"
            "    cli = make_cli_group()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(cli, ['hello']).output.strip() == 'hi'\n"
            "    assert runner.invoke(cli, ['bye']).output.strip() == 'ciao'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import click\n\n"
            "def make_cli_group():\n"
            "    @click.group()\n"
            "    def cli():\n"
            "        pass\n\n"
            "    @cli.command()\n"
            "    def hello():\n"
            "        click.echo('hi')\n\n"
            "    @cli.command()\n"
            "    def bye():\n"
            "        click.echo('ciao')\n"
            "    return cli\n"
        ),
    },
    {
        "slug": "07_typer_greet",
        "track": "click", "difficulty": "medium",
        "title": "Typer Typed Command",
        "tags": ["typer", "cli"],
        "description": "Return a Typer app with one command that takes a required name: str and prints 'Hello {name}!'.",
        "examples": "invoke with 'Ada' -> 'Hello Ada!'",
        "hint": "typer.Typer(); @app.command() with a typed name parameter.",
        "syntax_hint": "app = typer.Typer(); @app.command(); def greet(name: str): ...",
        "signature": "def make_typer_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from typer.testing import CliRunner\n"
            "    app = make_typer_app()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(app, ['Ada']).output.strip() == 'Hello Ada!'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import typer\n\n"
            "def make_typer_app():\n"
            "    app = typer.Typer()\n\n"
            "    @app.command()\n"
            "    def greet(name: str):\n"
            "        typer.echo(f'Hello {name}!')\n\n"
            "    return app\n"
        ),
    },
    {
        "slug": "08_typer_optional",
        "track": "click", "difficulty": "hard",
        "title": "Typer Optional Fields",
        "tags": ["typer", "cli"],
        "description": "Return a Typer app with a greet command: required name, optional --title (default empty). Print 'Hello, {title} {name}!' with title omitted when empty.",
        "examples": "Ada -> 'Hello, Ada!'; --title Dr Ada -> 'Hello, Dr Ada!'",
        "hint": "typer.Option('') for title; omit title and extra space when empty.",
        "syntax_hint": "optional --title via typer.Option('', '--title')",
        "signature": "def make_titled_app():\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from typer.testing import CliRunner\n"
            "    app = make_titled_app()\n"
            "    runner = CliRunner()\n"
            "    assert runner.invoke(app, ['Ada']).output.strip() == 'Hello, Ada!'\n"
            "    assert runner.invoke(app, ['Ada', '--title', 'Dr']).output.strip() == 'Hello, Dr Ada!'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import typer\n\n"
            "def make_titled_app():\n"
            "    app = typer.Typer()\n\n"
            "    @app.command()\n"
            "    def greet(\n"
            "        name: str,\n"
            "        title: str = typer.Option('', '--title'),\n"
            "    ):\n"
            "        prefix = f'{title} ' if title else ''\n"
            "        typer.echo(f'Hello, {prefix}{name}!')\n\n"
            "    return app\n"
        ),
    },
]
