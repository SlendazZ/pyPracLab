def normalize(path: str) -> str:
    parts = [p for p in path.split('/') if p and p != '.']
    stack: list[str] = []
    for p in parts:
        if p == '..':
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return '/' + '/'.join(stack) if stack else '/'
