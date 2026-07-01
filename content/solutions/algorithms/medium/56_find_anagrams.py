from collections import Counter

def find_anagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    need = Counter(p)
    have = Counter(s[:len(p)])
    result = []
    if have == need:
        result.append(0)
    for i in range(len(p), len(s)):
        have[s[i]] += 1
        have[s[i - len(p)]] -= 1
        if have[s[i - len(p)]] == 0:
            del have[s[i - len(p)]]
        if have == need:
            result.append(i - len(p) + 1)
    return result
