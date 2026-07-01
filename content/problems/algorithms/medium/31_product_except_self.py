# title: Product of Array Except Self
# track: algorithms
# difficulty: medium
# tags: prefix-product, array
# description: |
# Return a list where output[i] is the product of all elements except nums[i]. No division.
# examples:
# product_except([1,2,3,4]) -> [24,12,8,6]
# hint: |
# First pass: prefix products left to right. Second pass: suffix products right to left.
# syntax_hint: |
# for i in range(n): out[i] = prefix; prefix *= nums[i]


def product_except(nums: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert product_except([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except([2, 3]) == [3, 2]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
