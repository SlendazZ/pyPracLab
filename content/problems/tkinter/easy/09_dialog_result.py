# title: Dialog Result Mapping
# track: tkinter
# difficulty: easy
# tags: tkinter
# description: |
# Map dialog button labels ok/cancel to True/False; unknown labels -> None.
# examples:
# dialog_result('ok') -> True
# hint: |
# Simple if/elif on lowered label.
# syntax_hint: |
# return {'ok': True, 'cancel': False}.get(label.lower())


def dialog_result(label: str) -> bool | None:
    pass


def run_tests() -> None:
    assert dialog_result('ok') is True
    assert dialog_result('Cancel') is False
    assert dialog_result('maybe') is None
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
