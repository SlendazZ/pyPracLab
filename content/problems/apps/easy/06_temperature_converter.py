# title: Temperature Converter
# track: apps
# difficulty: easy
# tags: math
# description: |
# Convert between 'C', 'F', 'K'. Support any pair.
# examples:
# temp(0, 'C', 'F') -> 32.0
# temp(0, 'C', 'K') -> 273.15
# hint: |
# Convert to Celsius first, then to the target.
# syntax_hint: |
# if frm == 'F': c = (v - 32) * 5/9


def temp(value: float, frm: str, to: str) -> float:
    pass


def run_tests() -> None:
    assert abs(temp(0, 'C', 'F') - 32.0) < 1e-9
    assert abs(temp(0, 'C', 'K') - 273.15) < 1e-9
    assert abs(temp(32, 'F', 'C') - 0.0) < 1e-9
    assert abs(temp(100, 'C', 'C') - 100.0) < 1e-9
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
