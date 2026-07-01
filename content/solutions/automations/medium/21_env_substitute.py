import re

def substitute(template: str, env: dict[str, str]) -> str:
    return re.sub(r'\$\{([^}]+)\}', lambda m: env.get(m.group(1), ''), template)
