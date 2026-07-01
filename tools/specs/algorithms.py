"""Algorithms problem specs."""

PROBLEMS = [
    {
        "slug": "01_two_sum_sorted",
        "track": "algorithms", "difficulty": "easy",
        "title": "Two Sum II - Input Array Is Sorted",
        "tags": ["two-pointers", "array"],
        "description": "Given a sorted list of numbers and a target, return the 1-based indexes of the two numbers that add up to target. Exactly one answer exists.",
        "examples": "two_sum_sorted([2, 7, 11, 15], 9) -> [1, 2]",
        "hint": "The list is sorted, so use two pointers: one at the start, one at the end.",
        "syntax_hint": "while left < right: ... ; list indexes are 0-based, so return +1.",
        "signature": "def two_sum_sorted(numbers: list[int], target: int) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]\n"
            "    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]\n"
            "    assert two_sum_sorted([-1, 0], -1) == [1, 2]\n"
            "    assert two_sum_sorted([1, 2, 3, 4, 6], 10) == [4, 5]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def two_sum_sorted(numbers: list[int], target: int) -> list[int]:\n"
            "    left, right = 0, len(numbers) - 1\n"
            "    while left < right:\n"
            "        current = numbers[left] + numbers[right]\n"
            "        if current == target:\n"
            "            return [left + 1, right + 1]\n"
            "        if current < target:\n"
            "            left += 1\n"
            "        else:\n"
            "            right -= 1\n"
            "    return []\n"
        ),
    },
    {
        "slug": "02_palindrome_number",
        "track": "algorithms", "difficulty": "easy",
        "title": "Palindrome Number",
        "tags": ["math"],
        "description": "Return True if the integer reads the same forwards and backwards, without converting it to a string. Negative numbers are not palindromes.",
        "examples": "is_palindrome(121) -> True\nis_palindrome(-121) -> False",
        "hint": "Reverse half of the number by repeatedly taking x % 10 and building a reversed value.",
        "syntax_hint": "while x > reversed_half: reversed_half = reversed_half * 10 + x % 10; x //= 10",
        "signature": "def is_palindrome(x: int) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert is_palindrome(121) is True\n"
            "    assert is_palindrome(-121) is False\n"
            "    assert is_palindrome(10) is False\n"
            "    assert is_palindrome(0) is True\n"
            "    assert is_palindrome(1221) is True\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def is_palindrome(x: int) -> bool:\n"
            "    if x < 0 or (x % 10 == 0 and x != 0):\n"
            "        return False\n"
            "    rev = 0\n"
            "    while x > rev:\n"
            "        rev = rev * 10 + x % 10\n"
            "        x //= 10\n"
            "    return x == rev or x == rev // 10\n"
        ),
    },
    {
        "slug": "03_longest_substring_without_repeating",
        "track": "algorithms", "difficulty": "medium",
        "title": "Longest Substring Without Repeating Characters",
        "tags": ["sliding-window", "hash-map"],
        "description": "Given a string, return the length of the longest substring that contains no repeating characters.",
        "examples": 'length_of_longest("abcabcbb") -> 3\nlength_of_longest("pwwkew") -> 3',
        "hint": "Slide a window with two pointers; store the last seen index of each character in a dict.",
        "syntax_hint": "for right, ch in enumerate(s): move left to max(left, last[ch] + 1)",
        "signature": "def length_of_longest(s: str) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert length_of_longest("abcabcbb") == 3\n'
            '    assert length_of_longest("bbbbb") == 1\n'
            '    assert length_of_longest("pwwkew") == 3\n'
            '    assert length_of_longest("") == 0\n'
            '    assert length_of_longest("abcdef") == 6\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def length_of_longest(s: str) -> int:\n"
            "    last: dict[str, int] = {}\n"
            "    left = 0\n"
            "    best = 0\n"
            "    for right, ch in enumerate(s):\n"
            "        if ch in last and last[ch] >= left:\n"
            "            left = last[ch] + 1\n"
            "        last[ch] = right\n"
            "        best = max(best, right - left + 1)\n"
            "    return best\n"
        ),
    },
    {
        "slug": "04_reverse_string",
        "track": "algorithms", "difficulty": "easy",
        "title": "Reverse String",
        "tags": ["two-pointers", "array"],
        "description": "Reverse a list of characters in place and return it.",
        "examples": "reverse(['h','e','l','l','o']) -> ['o','l','l','e','h']",
        "hint": "Swap elements from both ends moving toward the middle.",
        "syntax_hint": "for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]",
        "signature": "def reverse(s: list[str]) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert reverse(['h','e','l','l','o']) == ['o','l','l','e','h']\n"
            "    assert reverse(['a','b']) == ['b','a']\n"
            "    assert reverse([]) == []\n"
            "    assert reverse(['x']) == ['x']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def reverse(s: list[str]) -> list[str]:\n"
            "    left, right = 0, len(s) - 1\n"
            "    while left < right:\n"
            "        s[left], s[right] = s[right], s[left]\n"
            "        left += 1\n"
            "        right -= 1\n"
            "    return s\n"
        ),
    },
    {
        "slug": "05_contains_duplicate",
        "track": "algorithms", "difficulty": "easy",
        "title": "Contains Duplicate",
        "tags": ["set"],
        "description": "Return True if any value appears at least twice in the list.",
        "examples": "has_duplicate([1,2,3,1]) -> True\nhas_duplicate([1,2,3]) -> False",
        "hint": "A set removes duplicates; compare lengths.",
        "syntax_hint": "return len(set(nums)) != len(nums)",
        "signature": "def has_duplicate(nums: list[int]) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert has_duplicate([1, 2, 3, 1]) is True\n"
            "    assert has_duplicate([1, 2, 3]) is False\n"
            "    assert has_duplicate([]) is False\n"
            "    assert has_duplicate([1]) is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def has_duplicate(nums: list[int]) -> bool:\n"
            "    return len(set(nums)) != len(nums)\n"
        ),
    },
    {
        "slug": "06_valid_anagram",
        "track": "algorithms", "difficulty": "easy",
        "title": "Valid Anagram",
        "tags": ["hash-map", "string"],
        "description": "Return True if string t is an anagram of string s (same characters, same counts).",
        "examples": 'is_anagram("anagram","nagaram") -> True\nis_anagram("rat","car") -> False',
        "hint": "collections.Counter compares counts directly.",
        "syntax_hint": "from collections import Counter; return Counter(s) == Counter(t)",
        "signature": "def is_anagram(s: str, t: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert is_anagram("anagram", "nagaram") is True\n'
            '    assert is_anagram("rat", "car") is False\n'
            '    assert is_anagram("a", "a") is True\n'
            '    assert is_anagram("ab", "ba") is True\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def is_anagram(s: str, t: str) -> bool:\n"
            "    return Counter(s) == Counter(t)\n"
        ),
    },
    {
        "slug": "07_climbing_stairs",
        "track": "algorithms", "difficulty": "easy",
        "title": "Climbing Stairs",
        "tags": ["dp"],
        "description": "You can climb 1 or 2 stairs at a time. Return the number of distinct ways to climb n stairs.",
        "examples": "climb(2) -> 2\nclimb(3) -> 3",
        "hint": "It's the Fibonacci sequence: ways(n) = ways(n-1) + ways(n-2).",
        "syntax_hint": "a, b = 1, 1; for _ in range(n): a, b = b, a + b",
        "signature": "def climb(n: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert climb(1) == 1\n"
            "    assert climb(2) == 2\n"
            "    assert climb(3) == 3\n"
            "    assert climb(5) == 8\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def climb(n: int) -> int:\n"
            "    a, b = 1, 1\n"
            "    for _ in range(n):\n"
            "        a, b = b, a + b\n"
            "    return a\n"
        ),
    },
    {
        "slug": "08_missing_number",
        "track": "algorithms", "difficulty": "easy",
        "title": "Missing Number",
        "tags": ["math", "array"],
        "description": "A list contains n distinct numbers taken from 0..n. Return the missing one.",
        "examples": "missing([3,0,1]) -> 2\nmissing([0,1]) -> 2",
        "hint": "The expected sum of 0..n is n*(n+1)/2; subtract the actual sum.",
        "syntax_hint": "n = len(nums); return n*(n+1)//2 - sum(nums)",
        "signature": "def missing(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert missing([3, 0, 1]) == 2\n"
            "    assert missing([0, 1]) == 2\n"
            "    assert missing([0]) == 1\n"
            "    assert missing([1, 0]) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def missing(nums: list[int]) -> int:\n"
            "    n = len(nums)\n"
            "    return n * (n + 1) // 2 - sum(nums)\n"
        ),
    },
    {
        "slug": "09_fizz_buzz",
        "track": "algorithms", "difficulty": "easy",
        "title": "Fizz Buzz",
        "tags": ["loop", "string"],
        "description": "Return a list of strings for 1..n: 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for both, else the number as a string.",
        "examples": 'fizzbuzz(5) -> ["1","2","Fizz","4","Buzz"]',
        "hint": "Check the combined condition first (15), then 3, then 5.",
        "syntax_hint": 'str(i) if neither; build with if/elif/else',
        "signature": "def fizzbuzz(n: int) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]\n'
            '    assert fizzbuzz(15)[-1] == "FizzBuzz"\n'
            '    assert fizzbuzz(3)[2] == "Fizz"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def fizzbuzz(n: int) -> list[str]:\n"
            "    out = []\n"
            "    for i in range(1, n + 1):\n"
            '        if i % 15 == 0:\n            out.append("FizzBuzz")\n'
            '        elif i % 3 == 0:\n            out.append("Fizz")\n'
            '        elif i % 5 == 0:\n            out.append("Buzz")\n'
            "        else:\n            out.append(str(i))\n"
            "    return out\n"
        ),
    },
    {
        "slug": "10_majority_element",
        "track": "algorithms", "difficulty": "easy",
        "title": "Majority Element",
        "tags": ["boyer-moore"],
        "description": "A majority element appears more than n//2 times. Return it.",
        "examples": "majority([3,2,3]) -> 3\nmajority([2,2,1,1,1,2,2]) -> 2",
        "hint": "Use Boyer-Moore voting — keep a candidate and a count; +1 on match, -1 otherwise; reset when count hits 0.",
        "syntax_hint": "for x in nums: if count == 0: candidate = x; count += 1 if x==candidate else -1",
        "signature": "def majority(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert majority([3, 2, 3]) == 3\n"
            "    assert majority([2, 2, 1, 1, 1, 2, 2]) == 2\n"
            "    assert majority([1]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def majority(nums: list[int]) -> int:\n"
            "    count = 0\n"
            "    candidate = None\n"
            "    for x in nums:\n"
            "        if count == 0:\n"
            "            candidate = x\n"
            "        count += 1 if x == candidate else -1\n"
            "    return candidate\n"
        ),
    },
    {
        "slug": "11_valid_parentheses",
        "track": "algorithms", "difficulty": "easy",
        "title": "Valid Parentheses",
        "tags": ["stack"],
        "description": "Return True if the string of '()[]{}' is valid: every opener is closed by the same type in the correct order.",
        "examples": 'is_valid("()[]{}") -> True\nis_valid("(]") -> False',
        "hint": "Push openers on a stack; on a closer, check the top matches.",
        "syntax_hint": "pairs = {')': '(', ']': '[', '}': '{'}; stack.append or pop",
        "signature": "def is_valid(s: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert is_valid("()") is True\n'
            '    assert is_valid("()[]{}") is True\n'
            '    assert is_valid("(]") is False\n'
            '    assert is_valid("([)]") is False\n'
            '    assert is_valid("{[]}") is True\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def is_valid(s: str) -> bool:\n"
            "    pairs = {')': '(', ']': '[', '}': '{'}\n"
            "    stack = []\n"
            "    for ch in s:\n"
            "        if ch in pairs:\n"
            "            if not stack or stack.pop() != pairs[ch]:\n"
            "                return False\n"
            "        else:\n"
            "            stack.append(ch)\n"
            "    return not stack\n"
        ),
    },
    {
        "slug": "12_best_time_to_buy_sell",
        "track": "algorithms", "difficulty": "easy",
        "title": "Best Time to Buy and Sell Stock",
        "tags": ["array", "greedy"],
        "description": "Given daily prices, return the max profit from one buy then one sell. 0 if no profit.",
        "examples": "max_profit([7,1,5,3,6,4]) -> 5\nmax_profit([7,6,4,3,1]) -> 0",
        "hint": "Track the minimum price so far; profit = price - min_price.",
        "syntax_hint": "for p in prices: min_price = min(min_price, p); profit = max(profit, p - min_price)",
        "signature": "def max_profit(prices: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert max_profit([7, 1, 5, 3, 6, 4]) == 5\n"
            "    assert max_profit([7, 6, 4, 3, 1]) == 0\n"
            "    assert max_profit([1, 2]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def max_profit(prices: list[int]) -> int:\n"
            "    min_price = float('inf')\n"
            "    profit = 0\n"
            "    for p in prices:\n"
            "        min_price = min(min_price, p)\n"
            "        profit = max(profit, p - min_price)\n"
            "    return profit\n"
        ),
    },
    {
        "slug": "13_move_zeroes",
        "track": "algorithms", "difficulty": "easy",
        "title": "Move Zeroes",
        "tags": ["two-pointers"],
        "description": "Move all 0s to the end of the list in place, keeping the order of non-zero elements. Return the list.",
        "examples": "move_zeroes([0,1,0,3,12]) -> [1,3,12,0,0]",
        "hint": "Keep a write index for the next non-zero; swap into place.",
        "syntax_hint": "for x in nums: if x != 0: nums[pos] = x; pos += 1",
        "signature": "def move_zeroes(nums: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]\n"
            "    assert move_zeroes([0]) == [0]\n"
            "    assert move_zeroes([1]) == [1]\n"
            "    assert move_zeroes([1, 0]) == [1, 0]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def move_zeroes(nums: list[int]) -> list[int]:\n"
            "    pos = 0\n"
            "    for i in range(len(nums)):\n"
            "        if nums[i] != 0:\n"
            "            nums[pos], nums[i] = nums[i], nums[pos]\n"
            "            pos += 1\n"
            "    return nums\n"
        ),
    },
    {
        "slug": "14_single_number",
        "track": "algorithms", "difficulty": "easy",
        "title": "Single Number",
        "tags": ["bit-manipulation"],
        "description": "Every element appears twice except one. Find that single one using O(1) space.",
        "examples": "single([2,2,1]) -> 1\nsingle([4,1,2,1,2]) -> 4",
        "hint": "XOR cancels equal pairs: a ^ a == 0, and 0 ^ a == a.",
        "syntax_hint": "import functools, operator; functools.reduce(operator.xor, nums)",
        "signature": "def single(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert single([2, 2, 1]) == 1\n"
            "    assert single([4, 1, 2, 1, 2]) == 4\n"
            "    assert single([1]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import functools\nimport operator\n\n"
            "def single(nums: list[int]) -> int:\n"
            "    return functools.reduce(operator.xor, nums)\n"
        ),
    },
    {
        "slug": "15_ransom_note",
        "track": "algorithms", "difficulty": "easy",
        "title": "Ransom Note",
        "tags": ["hash-map", "string"],
        "description": "Return True if the ransom note can be constructed from the magazine's letters (each letter used once).",
        "examples": 'can_build("aa","ab") -> False\ncan_build("aa","aab") -> True',
        "hint": "Count magazine letters; ensure enough of each for the note.",
        "syntax_hint": "from collections import Counter; return not (Counter(note) - Counter(mag))",
        "signature": "def can_build(note: str, mag: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert can_build("aa", "ab") is False\n'
            '    assert can_build("aa", "aab") is True\n'
            '    assert can_build("", "a") is True\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def can_build(note: str, mag: str) -> bool:\n"
            "    return not (Counter(note) - Counter(mag))\n"
        ),
    },
    {
        "slug": "16_binary_search",
        "track": "algorithms", "difficulty": "easy",
        "title": "Binary Search",
        "tags": ["binary-search"],
        "description": "Return the index of target in a sorted list, or -1 if absent.",
        "examples": "bsearch([-1,0,3,5,9,12], 9) -> 4\nbsearch([-1,0,3,5,9,12], 2) -> -1",
        "hint": "Narrow the [lo, hi] window by comparing the midpoint to the target.",
        "syntax_hint": "while lo <= hi: mid = (lo + hi) // 2",
        "signature": "def bsearch(nums: list[int], target: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert bsearch([-1, 0, 3, 5, 9, 12], 9) == 4\n"
            "    assert bsearch([-1, 0, 3, 5, 9, 12], 2) == -1\n"
            "    assert bsearch([1], 1) == 0\n"
            "    assert bsearch([1], 0) == -1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def bsearch(nums: list[int], target: int) -> int:\n"
            "    lo, hi = 0, len(nums) - 1\n"
            "    while lo <= hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        if nums[mid] == target:\n"
            "            return mid\n"
            "        if nums[mid] < target:\n"
            "            lo = mid + 1\n"
            "        else:\n"
            "            hi = mid - 1\n"
            "    return -1\n"
        ),
    },
    {
        "slug": "17_plus_one",
        "track": "algorithms", "difficulty": "easy",
        "title": "Plus One",
        "tags": ["array", "math"],
        "description": "A non-empty list of digits represents a number. Return the list of digits after adding one.",
        "examples": "plus_one([1,2,3]) -> [1,2,4]\nplus_one([9,9]) -> [1,0,0]",
        "hint": "Add from the last digit, carrying over 9s.",
        "syntax_hint": "for i in reversed(range(len(d))): if d[i] == 9: d[i] = 0 else: d[i]+=1; return d",
        "signature": "def plus_one(digits: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert plus_one([1, 2, 3]) == [1, 2, 4]\n"
            "    assert plus_one([9, 9]) == [1, 0, 0]\n"
            "    assert plus_one([0]) == [1]\n"
            "    assert plus_one([1, 9, 9]) == [2, 0, 0]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def plus_one(digits: list[int]) -> list[int]:\n"
            "    for i in range(len(digits) - 1, -1, -1):\n"
            "        if digits[i] == 9:\n"
            "            digits[i] = 0\n"
            "        else:\n"
            "            digits[i] += 1\n"
            "            return digits\n"
            "    return [1] + digits\n"
        ),
    },
    {
        "slug": "18_first_unique_char",
        "track": "algorithms", "difficulty": "easy",
        "title": "First Unique Character",
        "tags": ["hash-map", "string"],
        "description": "Return the index of the first non-repeating character in s, or -1.",
        "examples": 'first_unique("leetcode") -> 0\nfirst_unique("aabb") -> -1',
        "hint": "Count characters, then find the first with count 1.",
        "syntax_hint": "counts = Counter(s); for i, ch in enumerate(s): if counts[ch]==1: return i",
        "signature": "def first_unique(s: str) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert first_unique("leetcode") == 0\n'
            '    assert first_unique("loveleetcode") == 2\n'
            '    assert first_unique("aabb") == -1\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def first_unique(s: str) -> int:\n"
            "    counts = Counter(s)\n"
            "    for i, ch in enumerate(s):\n"
            "        if counts[ch] == 1:\n"
            "            return i\n"
            "    return -1\n"
        ),
    },
    {
        "slug": "19_length_of_last_word",
        "track": "algorithms", "difficulty": "easy",
        "title": "Length of Last Word",
        "tags": ["string"],
        "description": "Return the length of the last word in s (words separated by spaces, possibly trailing spaces).",
        "examples": 'last_word_len("Hello World") -> 5\nlast_word_len("   fly me   to   the moon  ") -> 4',
        "hint": "Strip trailing spaces, split, take the last word's length.",
        "syntax_hint": "return len(s.rstrip().split()[-1])",
        "signature": "def last_word_len(s: str) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert last_word_len("Hello World") == 5\n'
            '    assert last_word_len("   fly me   to   the moon  ") == 4\n'
            '    assert last_word_len("a") == 1\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def last_word_len(s: str) -> int:\n"
            "    return len(s.rstrip().split()[-1])\n"
        ),
    },
    {
        "slug": "20_power_of_two",
        "track": "algorithms", "difficulty": "easy",
        "title": "Power of Two",
        "tags": ["bit-manipulation", "math"],
        "description": "Return True if n is a power of two.",
        "examples": "is_power_of_two(16) -> True\nis_power_of_two(3) -> False",
        "hint": "A power of two has exactly one bit set: n > 0 and (n & (n-1)) == 0.",
        "syntax_hint": "return n > 0 and (n & (n - 1)) == 0",
        "signature": "def is_power_of_two(n: int) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert is_power_of_two(16) is True\n"
            "    assert is_power_of_two(3) is False\n"
            "    assert is_power_of_two(1) is True\n"
            "    assert is_power_of_two(0) is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def is_power_of_two(n: int) -> bool:\n"
            "    return n > 0 and (n & (n - 1)) == 0\n"
        ),
    },
    {
        "slug": "21_running_sum",
        "track": "algorithms", "difficulty": "easy",
        "title": "Running Sum",
        "tags": ["prefix-sum", "array"],
        "description": "Return the running sum of a 1D list: output[i] is the sum of nums[0..i].",
        "examples": "running_sum([1,2,3,4]) -> [1,3,6,10]",
        "hint": "Accumulate as you iterate.",
        "syntax_hint": "from itertools import accumulate; list(accumulate(nums))",
        "signature": "def running_sum(nums: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]\n"
            "    assert running_sum([1, 1, 1]) == [1, 2, 3]\n"
            "    assert running_sum([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from itertools import accumulate\n\n"
            "def running_sum(nums: list[int]) -> list[int]:\n"
            "    return list(accumulate(nums))\n"
        ),
    },
    {
        "slug": "22_pivot_index",
        "track": "algorithms", "difficulty": "easy",
        "title": "Find Pivot Index",
        "tags": ["prefix-sum"],
        "description": "The pivot index is where the sum of elements to the left equals the sum to the right. Return it, or -1.",
        "examples": "pivot([1,7,3,6,5,6]) -> 3\npivot([1,2,3]) -> -1",
        "hint": "Total sum minus left_sum minus nums[i] gives the right sum.",
        "syntax_hint": "for i, x in enumerate(nums): if left == total - left - x: return i",
        "signature": "def pivot(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert pivot([1, 7, 3, 6, 5, 6]) == 3\n"
            "    assert pivot([1, 2, 3]) == -1\n"
            "    assert pivot([2, 1, -1]) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def pivot(nums: list[int]) -> int:\n"
            "    total = sum(nums)\n"
            "    left = 0\n"
            "    for i, x in enumerate(nums):\n"
            "        if left == total - left - x:\n"
            "            return i\n"
            "        left += x\n"
            "    return -1\n"
        ),
    },
    {
        "slug": "23_isomorphic_strings",
        "track": "algorithms", "difficulty": "easy",
        "title": "Isomorphic Strings",
        "tags": ["hash-map", "string"],
        "description": "Two strings are isomorphic if chars in s map 1-1 to chars in t. Return True/False.",
        "examples": 'isomorphic("egg","add") -> True\nisomorphic("foo","bar") -> False',
        "hint": "Two dicts track s->t and t->s mappings; reject on mismatch.",
        "syntax_hint": "return len(set(zip(s,t))) == len(set(s)) == len(set(t))",
        "signature": "def isomorphic(s: str, t: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert isomorphic("egg", "add") is True\n'
            '    assert isomorphic("foo", "bar") is False\n'
            '    assert isomorphic("paper", "title") is True\n'
            '    assert isomorphic("badc", "baba") is False\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def isomorphic(s: str, t: str) -> bool:\n"
            "    return len(set(zip(s, t))) == len(set(s)) == len(set(t))\n"
        ),
    },
    {
        "slug": "24_reverse_words",
        "track": "algorithms", "difficulty": "easy",
        "title": "Reverse Words in a String III",
        "tags": ["string"],
        "description": "Reverse the order of characters in each word of s, keeping word order and single spaces.",
        "examples": 'reverse_words("Let us take contest") -> "teL su ekat tsetnoc"',
        "hint": "Split, reverse each word, join.",
        "syntax_hint": "' '.join(w[::-1] for w in s.split())",
        "signature": "def reverse_words(s: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert reverse_words("Let us go") == "teL su og"\n'
            '    assert reverse_words("hello") == "olleh"\n'
            '    assert reverse_words("a b c") == "a b c"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def reverse_words(s: str) -> str:\n"
            "    return ' '.join(w[::-1] for w in s.split())\n"
        ),
    },
    {
        "slug": "25_happy_number",
        "track": "algorithms", "difficulty": "easy",
        "title": "Happy Number",
        "tags": ["set", "math"],
        "description": "A happy number repeatedly replaces itself with the sum of the squares of its digits until it reaches 1. Return True if n is happy.",
        "examples": "is_happy(19) -> True\nis_happy(2) -> False",
        "hint": "Detect cycles with a set of seen numbers.",
        "syntax_hint": "while n != 1 and n not in seen: seen.add(n); n = sum(int(d)**2 for d in str(n))",
        "signature": "def is_happy(n: int) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert is_happy(19) is True\n"
            "    assert is_happy(2) is False\n"
            "    assert is_happy(1) is True\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def is_happy(n: int) -> bool:\n"
            "    seen = set()\n"
            "    while n != 1 and n not in seen:\n"
            "        seen.add(n)\n"
            "        n = sum(int(d) ** 2 for d in str(n))\n"
            "    return n == 1\n"
        ),
    },
    {
        "slug": "26_assign_cookies",
        "track": "algorithms", "difficulty": "easy",
        "title": "Assign Cookies",
        "tags": ["greedy", "two-pointers"],
        "description": "Each child i is content if given a cookie with size >= greed[i]. Return the max number of content children.",
        "examples": "assign([1,2,3],[1,1]) -> 1\nassign([1,2],[1,2,3]) -> 2",
        "hint": "Sort both; give the smallest sufficient cookie to each child.",
        "syntax_hint": "g.sort(); s.sort(); i = j = 0; while ...",
        "signature": "def assign(greed: list[int], size: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert assign([1, 2, 3], [1, 1]) == 1\n"
            "    assert assign([1, 2], [1, 2, 3]) == 2\n"
            "    assert assign([], [1]) == 0\n"
            "    assert assign([1], []) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def assign(greed: list[int], size: list[int]) -> int:\n"
            "    greed.sort()\n"
            "    size.sort()\n"
            "    i = j = 0\n"
            "    while i < len(greed) and j < len(size):\n"
            "        if size[j] >= greed[i]:\n"
            "            i += 1\n"
            "        j += 1\n"
            "    return i\n"
        ),
    },
    {
        "slug": "27_sorted_squares",
        "track": "algorithms", "difficulty": "easy",
        "title": "Squares of a Sorted Array",
        "tags": ["two-pointers", "array"],
        "description": "Given a non-decreasing list that may have negatives, return the squares in non-decreasing order.",
        "examples": "sorted_squares([-4,-1,0,3,10]) -> [0,1,9,16,100]",
        "hint": "Fill from the end using two pointers at both ends (largest absolute).",
        "syntax_hint": "result = [0]*n; for k in reversed(range(n)): ...",
        "signature": "def sorted_squares(nums: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]\n"
            "    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]\n"
            "    assert sorted_squares([0]) == [0]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def sorted_squares(nums: list[int]) -> list[int]:\n"
            "    n = len(nums)\n"
            "    result = [0] * n\n"
            "    left, right = 0, n - 1\n"
            "    for k in range(n - 1, -1, -1):\n"
            "        if abs(nums[left]) > abs(nums[right]):\n"
            "            result[k] = nums[left] ** 2\n"
            "            left += 1\n"
            "        else:\n"
            "            result[k] = nums[right] ** 2\n"
            "            right -= 1\n"
            "    return result\n"
        ),
    },
    {
        "slug": "28_max_average_subarray",
        "track": "algorithms", "difficulty": "easy",
        "title": "Maximum Average Subarray I",
        "tags": ["sliding-window"],
        "description": "Return the max average of any contiguous subarray of length k.",
        "examples": "max_avg([1,12,-5,-6,50,3], 4) -> 12.75",
        "hint": "Maintain a window sum of size k; slide and track the best.",
        "syntax_hint": "window = sum(nums[:k]); for i in range(k, len(nums)): window += nums[i] - nums[i-k]",
        "signature": "def max_avg(nums: list[int], k: int) -> float:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert max_avg([1, 12, -5, -6, 50, 3], 4) == 12.75\n"
            "    assert max_avg([5], 1) == 5.0\n"
            "    assert abs(max_avg([0, 4, 0], 2) - 2.0) < 1e-9\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def max_avg(nums: list[int], k: int) -> float:\n"
            "    window = sum(nums[:k])\n"
            "    best = window\n"
            "    for i in range(k, len(nums)):\n"
            "        window += nums[i] - nums[i - k]\n"
            "        best = max(best, window)\n"
            "    return best / k\n"
        ),
    },
    {
        "slug": "29_remove_duplicates_sorted",
        "track": "algorithms", "difficulty": "easy",
        "title": "Remove Duplicates from Sorted Array",
        "tags": ["two-pointers"],
        "description": "Remove duplicates in place from a sorted list and return the count of unique elements (the first k slots hold them).",
        "examples": "remove_dups([1,1,2]) -> 2  (list becomes [1,2,_])",
        "hint": "Keep a write index; advance it only when a new value appears.",
        "syntax_hint": "for x in nums: if write == 0 or x != nums[write-1]: nums[write] = x; write += 1",
        "signature": "def remove_dups(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    a = [1, 1, 2]\n"
            "    k = remove_dups(a)\n"
            "    assert k == 2 and a[:k] == [1, 2]\n"
            "    b = [0, 0, 1, 1, 2, 2, 3]\n"
            "    k = remove_dups(b)\n"
            "    assert k == 4 and b[:k] == [0, 1, 2, 3]\n"
            "    assert remove_dups([1]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def remove_dups(nums: list[int]) -> int:\n"
            "    write = 0\n"
            "    for x in nums:\n"
            "        if write == 0 or x != nums[write - 1]:\n"
            "            nums[write] = x\n"
            "            write += 1\n"
            "    return write\n"
        ),
    },
    {
        "slug": "30_max_subarray",
        "track": "algorithms", "difficulty": "medium",
        "title": "Maximum Subarray",
        "tags": ["dp", "array"],
        "description": "Find the contiguous subarray with the largest sum and return the sum.",
        "examples": "max_subarray([-2,1,-3,4,-1,2,1,-5,4]) -> 6",
        "hint": "Kadane's algorithm: keep a running sum; reset to 0 when it goes negative.",
        "syntax_hint": "for x in nums: cur = max(x, cur + x); best = max(best, cur)",
        "signature": "def max_subarray(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6\n"
            "    assert max_subarray([1]) == 1\n"
            "    assert max_subarray([-1]) == -1\n"
            "    assert max_subarray([5, 4, -1, 7, 8]) == 23\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def max_subarray(nums: list[int]) -> int:\n"
            "    cur = best = nums[0]\n"
            "    for x in nums[1:]:\n"
            "        cur = max(x, cur + x)\n"
            "        best = max(best, cur)\n"
            "    return best\n"
        ),
    },
    {
        "slug": "31_product_except_self",
        "track": "algorithms", "difficulty": "medium",
        "title": "Product of Array Except Self",
        "tags": ["prefix-product", "array"],
        "description": "Return a list where output[i] is the product of all elements except nums[i]. No division.",
        "examples": "product_except([1,2,3,4]) -> [24,12,8,6]",
        "hint": "First pass: prefix products left to right. Second pass: suffix products right to left.",
        "syntax_hint": "for i in range(n): out[i] = prefix; prefix *= nums[i]",
        "signature": "def product_except(nums: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert product_except([1, 2, 3, 4]) == [24, 12, 8, 6]\n"
            "    assert product_except([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]\n"
            "    assert product_except([2, 3]) == [3, 2]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def product_except(nums: list[int]) -> list[int]:\n"
            "    n = len(nums)\n"
            "    out = [1] * n\n"
            "    prefix = 1\n"
            "    for i in range(n):\n"
            "        out[i] = prefix\n"
            "        prefix *= nums[i]\n"
            "    suffix = 1\n"
            "    for i in range(n - 1, -1, -1):\n"
            "        out[i] *= suffix\n"
            "        suffix *= nums[i]\n"
            "    return out\n"
        ),
    },
    {
        "slug": "32_three_sum",
        "track": "algorithms", "difficulty": "medium",
        "title": "3Sum",
        "tags": ["two-pointers", "array"],
        "description": "Return all unique triplets [a,b,c] from nums that sum to 0 (no duplicate triplets).",
        "examples": "three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]",
        "hint": "Sort; for each index, two-pointer the rest; skip duplicates.",
        "syntax_hint": "nums.sort(); for i,a in enumerate(nums): if i>0 and a==nums[i-1]: continue",
        "signature": "def three_sum(nums: list[int]) -> list[list[int]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    r = three_sum([-1, 0, 1, 2, -1, -4])\n"
            "    r = sorted([sorted(t) for t in r])\n"
            "    assert r == [[-1, -1, 2], [-1, 0, 1]]\n"
            "    assert three_sum([]) == []\n"
            "    assert three_sum([0]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def three_sum(nums: list[int]) -> list[list[int]]:\n"
            "    nums.sort()\n"
            "    result = []\n"
            "    n = len(nums)\n"
            "    for i in range(n - 2):\n"
            "        if i > 0 and nums[i] == nums[i - 1]:\n"
            "            continue\n"
            "        left, right = i + 1, n - 1\n"
            "        while left < right:\n"
            "            total = nums[i] + nums[left] + nums[right]\n"
            "            if total == 0:\n"
            "                result.append([nums[i], nums[left], nums[right]])\n"
            "                left += 1\n"
            "                right -= 1\n"
            "                while left < right and nums[left] == nums[left - 1]:\n"
            "                    left += 1\n"
            "                while left < right and nums[right] == nums[right + 1]:\n"
            "                    right -= 1\n"
            "            elif total < 0:\n"
            "                left += 1\n"
            "            else:\n"
            "                right -= 1\n"
            "    return result\n"
        ),
    },
    {
        "slug": "33_container_with_most_water",
        "track": "algorithms", "difficulty": "medium",
        "title": "Container With Most Water",
        "tags": ["two-pointers"],
        "description": "Each element is a wall height. Return the max water a pair of walls can hold (area = width * min height).",
        "examples": "max_area([1,8,6,2,5,4,8,3,7]) -> 49",
        "hint": "Two pointers from the ends; move the shorter wall inward.",
        "syntax_hint": "while left < right: area = (right-left)*min(h[l], h[r])",
        "signature": "def max_area(height: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49\n"
            "    assert max_area([1, 1]) == 1\n"
            "    assert max_area([4, 3, 2, 1, 4]) == 16\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def max_area(height: list[int]) -> int:\n"
            "    left, right = 0, len(height) - 1\n"
            "    best = 0\n"
            "    while left < right:\n"
            "        best = max(best, (right - left) * min(height[left], height[right]))\n"
            "        if height[left] < height[right]:\n"
            "            left += 1\n"
            "        else:\n"
            "            right -= 1\n"
            "    return best\n"
        ),
    },
    {
        "slug": "34_group_anagrams",
        "track": "algorithms", "difficulty": "medium",
        "title": "Group Anagrams",
        "tags": ["hash-map", "string"],
        "description": "Group the strings that are anagrams of each other. Return a list of groups (any order).",
        "examples": 'group(["eat","tea","tan","ate","nat","bat"]) -> [["eat","tea","ate"],["tan","nat"],["bat"]]',
        "hint": "Key each word by its sorted-tuple of characters.",
        "syntax_hint": "key = tuple(sorted(w)); defaultdict(list).append(w)",
        "signature": "def group(words: list[str]) -> list[list[str]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    r = group(["eat", "tea", "tan", "ate", "nat", "bat"])\n'
            "    r = sorted(sorted(g) for g in r)\n"
            '    assert r == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]\n'
            '    assert group([]) == []\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import defaultdict\n\n"
            "def group(words: list[str]) -> list[list[str]]:\n"
            "    buckets: dict = defaultdict(list)\n"
            "    for w in words:\n"
            "        buckets[tuple(sorted(w))].append(w)\n"
            "    return list(buckets.values())\n"
        ),
    },
    {
        "slug": "35_top_k_frequent",
        "track": "algorithms", "difficulty": "medium",
        "title": "Top K Frequent Elements",
        "tags": ["hash-map", "heap"],
        "description": "Return the k most frequent elements from nums (any order).",
        "examples": "top_k([1,1,1,2,2,3], 2) -> [1,2]",
        "hint": "Counter, then take the k largest by frequency.",
        "syntax_hint": "from collections import Counter; Counter(nums).most_common(k)",
        "signature": "def top_k(nums: list[int], k: int) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert sorted(top_k([1, 1, 1, 2, 2, 3], 2)) == [1, 2]\n"
            "    assert top_k([1], 1) == [1]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def top_k(nums: list[int], k: int) -> list[int]:\n"
            "    return [x for x, _ in Counter(nums).most_common(k)]\n"
        ),
    },
    {
        "slug": "36_merge_intervals",
        "track": "algorithms", "difficulty": "medium",
        "title": "Merge Intervals",
        "tags": ["intervals", "sort"],
        "description": "Given a list of [start, end] intervals, merge all overlapping ones and return the merged list.",
        "examples": "merge([[1,3],[2,6],[8,10]]) -> [[1,6],[8,10]]",
        "hint": "Sort by start; extend the current interval when they overlap.",
        "syntax_hint": "for start, end in sorted(intervals): if start <= cur_end: cur_end = max(...)",
        "signature": "def merge(intervals: list[list[int]]) -> list[list[int]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]\n"
            "    assert merge([[1, 4], [4, 5]]) == [[1, 5]]\n"
            "    assert merge([[1, 2]]) == [[1, 2]]\n"
            "    assert merge([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def merge(intervals: list[list[int]]) -> list[list[int]]:\n"
            "    if not intervals:\n"
            "        return []\n"
            "    intervals.sort()\n"
            "    merged = [intervals[0]]\n"
            "    for start, end in intervals[1:]:\n"
            "        last = merged[-1]\n"
            "        if start <= last[1]:\n"
            "            last[1] = max(last[1], end)\n"
            "        else:\n"
            "            merged.append([start, end])\n"
            "    return merged\n"
        ),
    },
    {
        "slug": "37_generate_parentheses",
        "track": "algorithms", "difficulty": "medium",
        "title": "Generate Parentheses",
        "tags": ["backtracking"],
        "description": "Return all well-formed combinations of n pairs of parentheses.",
        "examples": 'generate(3) -> ["((()))","(()())","(())()","()(())","()()()"]',
        "hint": "Recurse with counts of open and close used; only add ')' if close < open.",
        "syntax_hint": "def back(cur, open, close): if len(cur)==2*n: ...",
        "signature": "def generate(n: int) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert sorted(generate(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])\n'
            '    assert generate(1) == ["()"]\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def generate(n: int) -> list[str]:\n"
            "    result = []\n"
            "    def back(cur: str, open_n: int, close_n: int) -> None:\n"
            "        if len(cur) == 2 * n:\n"
            "            result.append(cur)\n"
            "            return\n"
            "        if open_n < n:\n"
            "            back(cur + '(', open_n + 1, close_n)\n"
            "        if close_n < open_n:\n"
            "            back(cur + ')', open_n, close_n + 1)\n"
            "    back('', 0, 0)\n"
            "    return result\n"
        ),
    },
    {
        "slug": "38_coin_change",
        "track": "algorithms", "difficulty": "medium",
        "title": "Coin Change",
        "tags": ["dp"],
        "description": "Given coin denominations and an amount, return the fewest coins to make the amount, or -1.",
        "examples": "coins([1,2,5], 11) -> 3\ncoins([2], 3) -> -1",
        "hint": "Bottom-up DP: dp[a] = min(dp[a-coin] + 1) for each coin.",
        "syntax_hint": "dp = [inf]*(amount+1); dp[0] = 0; for a in range(1, amount+1): ...",
        "signature": "def coins(coins: list[int], amount: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert coins([1, 2, 5], 11) == 3\n"
            "    assert coins([2], 3) == -1\n"
            "    assert coins([1], 0) == 0\n"
            "    assert coins([1], 2) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def coins(coins: list[int], amount: int) -> int:\n"
            "    dp = [float('inf')] * (amount + 1)\n"
            "    dp[0] = 0\n"
            "    for a in range(1, amount + 1):\n"
            "        for c in coins:\n"
            "            if c <= a:\n"
            "                dp[a] = min(dp[a], dp[a - c] + 1)\n"
            "    return dp[amount] if dp[amount] != float('inf') else -1\n"
        ),
    },
    {
        "slug": "39_min_size_subarray_sum",
        "track": "algorithms", "difficulty": "medium",
        "title": "Minimum Size Subarray Sum",
        "tags": ["sliding-window"],
        "description": "Return the minimal length of a contiguous subarray whose sum >= target, or 0.",
        "examples": "min_subarray(7, [2,3,1,2,4,3]) -> 2",
        "hint": "Expand the right pointer; once the window hits the target, shrink from the left.",
        "syntax_hint": "while total >= target: best = min(best, right-left); total -= nums[left]",
        "signature": "def min_subarray(target: int, nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert min_subarray(7, [2, 3, 1, 2, 4, 3]) == 2\n"
            "    assert min_subarray(4, [1, 4, 4]) == 1\n"
            "    assert min_subarray(11, [1, 1, 1]) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def min_subarray(target: int, nums: list[int]) -> int:\n"
            "    left = 0\n"
            "    total = 0\n"
            "    best = float('inf')\n"
            "    for right in range(len(nums)):\n"
            "        total += nums[right]\n"
            "        while total >= target:\n"
            "            best = min(best, right - left + 1)\n"
            "            total -= nums[left]\n"
            "            left += 1\n"
            "    return 0 if best == float('inf') else best\n"
        ),
    },
    {
        "slug": "40_daily_temperatures",
        "track": "algorithms", "difficulty": "medium",
        "title": "Daily Temperatures",
        "tags": ["stack", "array"],
        "description": "For each day's temperature, return how many days until a warmer day, or 0.",
        "examples": "daily([73,74,75,71,69,72,76,73]) -> [1,1,4,2,1,1,0,0]",
        "hint": "Monotonic decreasing stack of indices; pop when a warmer day arrives.",
        "syntax_hint": "stack = []; for i, t in enumerate(T): while stack and T[stack[-1]] < t: ...",
        "signature": "def daily(temps: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert daily([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]\n"
            "    assert daily([30, 40, 50, 60]) == [1, 1, 1, 0]\n"
            "    assert daily([60, 50, 40]) == [0, 0, 0]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def daily(temps: list[int]) -> list[int]:\n"
            "    n = len(temps)\n"
            "    result = [0] * n\n"
            "    stack: list[int] = []\n"
            "    for i, t in enumerate(temps):\n"
            "        while stack and temps[stack[-1]] < t:\n"
            "            j = stack.pop()\n"
            "            result[j] = i - j\n"
            "        stack.append(i)\n"
            "    return result\n"
        ),
    },
]

LESSONS = [
    {
        "slug": "01_two_pointers",
        "track": "algorithms", "difficulty": "easy",
        "title": "Two Pointers",
        "tags": ["two-pointers", "array"],
        "exercise": "content/problems/algorithms/easy/01_two_sum_sorted.py",
        "body": (
            "# Two Pointers\n\n"
            "When data is **sorted** (or has a natural order), two pointers often beat "
            "nested loops. Place one pointer at each end and move them inward based on a "
            "comparison.\n\n"
            "## Pattern\n\n"
            "```python\nleft, right = 0, len(arr) - 1\nwhile left < right:\n"
            "    total = arr[left] + arr[right]\n"
            "    if total == target:\n        return [left, right]\n"
            "    elif total < target:\n        left += 1\n"
            "    else:\n        right -= 1\n```\n\n"
            "## Why it works\n\n"
            "Each step removes one impossible candidate, so the search is O(n) instead of "
            "O(n^2). The companion exercise walks you through it on a sorted array."
        ),
    },
    {
        "slug": "02_sliding_window",
        "track": "algorithms", "difficulty": "medium",
        "title": "Sliding Window",
        "tags": ["sliding-window"],
        "exercise": "content/problems/algorithms/medium/03_longest_substring_without_repeating.py",
        "body": (
            "# Sliding Window\n\n"
            "A sliding window tracks a range `[left, right]` that you grow and shrink "
            "to keep an invariant (sum, uniqueness, length).\n\n"
            "## Fixed vs variable\n\n"
            "- **Fixed size k**: keep a sum of the last k elements.\n"
            "- **Variable**: expand `right`, and shrink `left` while the invariant breaks.\n\n"
            "## Example\n\n"
            "```python\nleft = 0\nfor right, ch in enumerate(s):\n"
            "    while violates_invariant():\n        shrink_from_left()\n"
            "    update_best(right - left + 1)\n```\n\n"
            "It turns O(n^2) nested loops into O(n)."
        ),
    },
    {
        "slug": "03_stacks",
        "track": "algorithms", "difficulty": "easy",
        "title": "Stacks for Parsing",
        "tags": ["stack"],
        "exercise": "content/problems/algorithms/easy/11_valid_parentheses.py",
        "body": (
            "# Stacks\n\n"
            "A stack is last-in, first-out. It is the right tool when a problem is about "
            "matching, nesting, or 'most recent' relationships.\n\n"
            "## Valid parentheses\n\n"
            "```python\nfor ch in s:\n    if ch in '([{':\n        stack.append(ch)\n"
            "    else:\n        if not stack or not matches(stack.pop(), ch):\n            return False\n```\n\n"
            "## When to reach for one\n\n"
            "- Matching brackets / tags\n- Evaluating postfix expressions\n"
            "- 'Next greater element' patterns (monotonic stack)"
        ),
    },
]
