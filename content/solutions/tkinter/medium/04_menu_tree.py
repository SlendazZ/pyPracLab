import tkinter  # noqa: F401

def paths(spec: dict) -> list[str]:
    result: list[str] = []
    def walk(node, prefix):
        for label, value in node.items():
            path = f'{prefix} > {label}' if prefix else label
            if value is None:
                result.append(path)
            else:
                walk(value, path)
    walk(spec, '')
    return result
