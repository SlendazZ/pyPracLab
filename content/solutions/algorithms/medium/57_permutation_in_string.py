from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False
    need = Counter(s1)
    have = Counter(s2[:n])
    if have == need:
        return True
    for i in range(n, m):
        have[s2[i]] += 1
        have[s2[i - n]] -= 1
        if have[s2[i - n]] == 0:
            del have[s2[i - n]]
        if have == need:
            return True
    return False
