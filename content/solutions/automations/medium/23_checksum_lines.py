import hashlib

def line_checksum(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:8]
