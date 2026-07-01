# title: Frozen Dataclass
# track: syntax
# difficulty: medium
# tags: dataclass
# description: |
# Return a frozen dataclass Point(x, y) factory that rejects mutation.
# examples:
# p = make_point(1,2); p.x == 1
# hint: |
# Use @dataclass(frozen=True).
# syntax_hint: |
# @dataclass(frozen=True)


def make_point(x: int, y: int):
    pass


def run_tests() -> None:
    p = make_point(1, 2)
    assert p.x == 1 and p.y == 2
    try:
        p.x = 3
        raised = False
    except Exception:
        raised = True
    assert raised
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
