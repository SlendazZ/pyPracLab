# title: Set Matrix Zeroes
# track: algorithms
# difficulty: medium
# tags: matrix
# description: |
# If an element is 0, set its entire row and column to 0. Return the new matrix.
# examples:
# set_zeroes([[1,1,0],[1,1,1]]) -> [[0,0,0],[1,1,0]]
# hint: |
# Track zero rows/cols in sets or use first row/col as markers.
# syntax_hint: |
# zero_rows, zero_cols = set(), set()


def set_zeroes(matrix: list[list[int]]) -> list[list[int]]:
    pass


def run_tests() -> None:
    assert set_zeroes([[1,1,0],[1,1,1]]) == [[0,0,0],[1,1,0]]
    assert set_zeroes([[0,1]]) == [[0,0]]
    assert set_zeroes([[1]]) == [[1]]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
