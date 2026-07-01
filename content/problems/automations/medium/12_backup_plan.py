# title: Backup Plan
# track: automations
# difficulty: medium
# tags: pathlib, logic
# description: |
# Given a list of file paths and a backup dir, return a list of (source, dest) pairs where dest is backup_dir / source.name with a '.bak' suffix appended.
# examples:
# backup_plan([Path('a.txt')], Path('bk')) -> [(Path('a.txt'), Path('bk/a.txt.bak'))]
# hint: |
# dest = backup_dir / (p.name + '.bak').
# syntax_hint: |
# backup_dir / (p.name + '.bak')


def backup_plan(files: list, backup_dir) -> list[tuple]:
    pass


def run_tests() -> None:
    from pathlib import Path
    plan = backup_plan([Path('a.txt'), Path('b.log')], Path('bk'))
    assert plan == [(Path('a.txt'), Path('bk/a.txt.bak')), (Path('b.log'), Path('bk/b.log.bak'))]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
