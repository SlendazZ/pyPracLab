from collections import Counter

def top_k(nums: list[int], k: int) -> list[int]:
    return [x for x, _ in Counter(nums).most_common(k)]
