# title: Progress Tracks
# track: rich
# difficulty: hard
# tags: rich, progress
# description: |
# Return a rich.progress.Progress configured with a spinner, a bar, and percentage columns (no transient).
# examples:
# make_progress() -> Progress
# hint: |
# Use Progress with SpinnerColumn, BarColumn, TextColumn, TaskProgressColumn.
# syntax_hint: |
# from rich.progress import Progress, SpinnerColumn, BarColumn, TaskProgressColumn, TextColumn


def make_progress() -> object:
    pass


def run_tests() -> None:
    from rich.progress import Progress
    p = make_progress()
    assert isinstance(p, Progress)
    assert p.live.transient is False
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
