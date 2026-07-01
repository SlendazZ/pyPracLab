from rich.progress import (
    Progress, SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn,
)

def make_progress() -> Progress:
    return Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        TaskProgressColumn(),
        transient=False,
    )
