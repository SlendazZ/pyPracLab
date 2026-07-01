def leaf_keys(obj: dict) -> list[str]:
    keys: list[str] = []
    def walk(node, prefix):
        for k, v in node.items():
            path = prefix + k
            if isinstance(v, dict):
                walk(v, path + '.')
            else:
                keys.append(path)
    walk(obj, '')
    return keys
