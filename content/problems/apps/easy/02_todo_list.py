# title: Todo List
# track: apps
# difficulty: easy
# tags: oop
# description: |
# A TodoList with add(task), complete(task), and pending() -> list of unfinished tasks. Completing an unknown task is a no-op.
# examples:
# t.pending() after add('a') -> ['a']
# hint: |
# Keep a list of dicts with a 'done' flag.
# syntax_hint: |
# [t['title'] for t in self.items if not t['done']]


class TodoList:
    pass


def run_tests() -> None:
    t = TodoList()
    t.add('a'); t.add('b')
    assert t.pending() == ['a', 'b']
    t.complete('a')
    assert t.pending() == ['b']
    t.complete('nope')
    assert t.pending() == ['b']
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
