# title: Counting Bits
# track: algorithms
# difficulty: easy
# tags: dp, bit-manipulation
# description: |
# For n, return list ans where ans[i] is number of 1 bits in i (0..n).
# examples:
# count_bits(5) -> [0,1,1,2,1,2]
# hint: |
# ans[i] = ans[i >> 1] + (i & 1).
# syntax_hint: |
# for i in range(1, n+1): ans[i] = ans[i>>1] + (i&1)


def count_bits(n: int) -> list[int]:
    pass


def run_tests() -> None:
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
    assert count_bits(0) == [0]
    assert count_bits(2) == [0, 1, 1]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
