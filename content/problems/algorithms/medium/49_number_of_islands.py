# title: Number of Islands
# track: algorithms
# difficulty: medium
# tags: dfs, grid
# description: |
# Given a grid of 1 (land) and 0 (water), return the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.
# examples:
# num_islands([[1,1,0],[1,0,0],[0,0,1]]) -> 2
# hint: |
# Scan the grid; when you find land, DFS/BFS to sink the whole island and increment the count.
# syntax_hint: |
# def dfs(r, c): grid[r][c] = 0; explore four neighbors


def num_islands(grid: list[list[int]]) -> int:
    pass


def run_tests() -> None:
    g1 = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]
    assert num_islands(g1) == 2
    g2 = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert num_islands(g2) == 1
    assert num_islands([]) == 0
    assert num_islands([[0, 0], [0, 0]]) == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
