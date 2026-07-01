def read_until_blank(it) -> list[str]:
    result = []
    while (line := next(it, None)) is not None:
        if line == '':
            break
        result.append(line)
    return result
