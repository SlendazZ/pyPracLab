# title: Unit Converter
# track: apps
# difficulty: easy
# tags: dict
# description: |
# Convert a value between units of the same kind using a factor table: convert(100, 'cm', 'm') -> 1.0 where factors store meters-per-unit.
# examples:
# convert(100, 'cm', 'm') -> 1.0
# hint: |
# value_in_base = value * factor[from]; result = value_in_base / factor[to].
# syntax_hint: |
# factors = {'cm': 0.01, 'm': 1.0, 'km': 1000.0}


def convert(value: float, frm: str, to: str) -> float:
    pass


def run_tests() -> None:
    assert abs(convert(100, 'cm', 'm') - 1.0) < 1e-9
    assert abs(convert(1, 'km', 'm') - 1000.0) < 1e-9
    assert abs(convert(2, 'm', 'm') - 2.0) < 1e-9
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
