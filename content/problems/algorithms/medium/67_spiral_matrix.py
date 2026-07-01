# title: Spiral Matrix
# track: algorithms
# difficulty: medium
# tags: matrix, simulation
# description: |
# Return elements of m x n matrix in spiral order.
# examples:
# spiral_order([[1,2,3],[4,5,6],[7,8,9]]) -> [1,2,3,6,9,8,7,4,5]
# hint: |
# Shrink boundaries top/bottom/left/right while traversing.
# syntax_hint: |
# while top <= bottom and left <= right: go right, down, left, up


def spiral_order(matrix: list[list[int]]) -> list[int]:
    pass


def run_tests() -> None:
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiral_order([[1,2,3,4]]) == [1,2,3,4]
    assert spiral_order([]) == []
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
