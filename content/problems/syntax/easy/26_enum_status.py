# title: Status Enum
# track: syntax
# difficulty: easy
# tags: enum
# description: |
# Return the Enum class Status with members PENDING, ACTIVE, DONE (values same as names).
# examples:
# Status.ACTIVE.name == 'ACTIVE'
# hint: |
# class Status(Enum): PENDING = 'PENDING' ...
# syntax_hint: |
# from enum import Enum


def make_status_enum():
    pass


def run_tests() -> None:
    Status = make_status_enum()
    assert Status.ACTIVE.name == 'ACTIVE'
    assert Status.PENDING.value == 'PENDING'
    assert list(Status) != []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
