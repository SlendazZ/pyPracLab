# title: Rotting Oranges
# track: algorithms
# difficulty: medium
# tags: bfs, grid
# description: |
# Grid: 2=rotten, 1=fresh, 0=empty. Each minute rot spreads to adjacent fresh. Return minutes to rot all or -1.
# examples:
# oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) -> 4
# hint: |
# Multi-source BFS from all 2s; track minutes and fresh count.
# syntax_hint: |
# from collections import deque; queue all rotten cells


def oranges_rotting(grid: list[list[int]]) -> int:
    pass


def run_tests() -> None:
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
