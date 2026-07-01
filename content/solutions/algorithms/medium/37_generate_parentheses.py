def generate(n: int) -> list[str]:
    result = []
    def back(cur: str, open_n: int, close_n: int) -> None:
        if len(cur) == 2 * n:
            result.append(cur)
            return
        if open_n < n:
            back(cur + '(', open_n + 1, close_n)
        if close_n < open_n:
            back(cur + ')', open_n, close_n + 1)
    back('', 0, 0)
    return result
