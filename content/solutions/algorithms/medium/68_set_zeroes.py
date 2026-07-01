def set_zeroes(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    mat = [row[:] for row in matrix]
    zr, zc = set(), set()
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                zr.add(r); zc.add(c)
    for r in zr:
        for c in range(n):
            mat[r][c] = 0
    for c in zc:
        for r in range(m):
            mat[r][c] = 0
    return mat
