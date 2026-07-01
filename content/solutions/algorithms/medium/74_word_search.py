def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:
            return False
        ch = board[r][c]
        board[r][c] = '#'
        found = any(dfs(r+dr, c+dc, idx+1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
        board[r][c] = ch
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
