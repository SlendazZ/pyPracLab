# title: Word Search
# track: algorithms
# difficulty: medium
# tags: backtracking, grid
# description: |
# 2D board of chars and word; return True if word exists by adjacent cells (no reuse).
# examples:
# exist([["A","B"],["C","D"]], "AB") -> True
# hint: |
# DFS from each cell; mark visited temporarily.
# syntax_hint: |
# def dfs(r,c,idx): backtrack four directions


def exist(board: list[list[str]], word: str) -> bool:
    pass


def run_tests() -> None:
    assert exist([["A","B"],["C","D"]], "AB") is True
    assert exist([["A","B"],["C","D"]], "AD") is False
    assert exist([["A"]], "A") is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
