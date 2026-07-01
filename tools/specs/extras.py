"""Extra problems: hard/medium gaps and easy variations per track."""

PROBLEMS = [
    # --- algorithms (hard) ---
    {
        "slug": "41_trapping_rain_water",
        "track": "algorithms", "difficulty": "hard",
        "title": "Trapping Rain Water",
        "tags": ["two-pointers", "array"],
        "description": "Given non-negative elevation bars, return how much water can be trapped after raining.",
        "examples": "trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6",
        "hint": "Two pointers from both ends; track left_max and right_max.",
        "syntax_hint": "while left < right: move the side with smaller max.",
        "signature": "def trap(height: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6\n"
            "    assert trap([4,2,0,3,2,5]) == 9\n"
            "    assert trap([]) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def trap(height: list[int]) -> int:\n"
            "    if not height:\n"
            "        return 0\n"
            "    left, right = 0, len(height) - 1\n"
            "    left_max = right_max = 0\n"
            "    water = 0\n"
            "    while left < right:\n"
            "        if height[left] < height[right]:\n"
            "            left_max = max(left_max, height[left])\n"
            "            water += left_max - height[left]\n"
            "            left += 1\n"
            "        else:\n"
            "            right_max = max(right_max, height[right])\n"
            "            water += right_max - height[right]\n"
            "            right -= 1\n"
            "    return water\n"
        ),
    },
    {
        "slug": "42_longest_increasing_subsequence",
        "track": "algorithms", "difficulty": "hard",
        "title": "Longest Increasing Subsequence Length",
        "tags": ["dp", "binary-search"],
        "description": "Return the length of the longest strictly increasing subsequence.",
        "examples": "lis_length([10,9,2,5,3,7,101,18]) -> 4",
        "hint": "Patience sorting: maintain a tails array; binary search insertion point.",
        "syntax_hint": "import bisect; bisect_left(tails, x)",
        "signature": "def lis_length(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert lis_length([10,9,2,5,3,7,101,18]) == 4\n"
            "    assert lis_length([0,1,0,3,2,3]) == 4\n"
            "    assert lis_length([7,7,7,7]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import bisect\n\n"
            "def lis_length(nums: list[int]) -> int:\n"
            "    tails: list[int] = []\n"
            "    for x in nums:\n"
            "        i = bisect.bisect_left(tails, x)\n"
            "        if i == len(tails):\n"
            "            tails.append(x)\n"
            "        else:\n"
            "            tails[i] = x\n"
            "    return len(tails)\n"
        ),
    },
    {
        "slug": "43_edit_distance",
        "track": "algorithms", "difficulty": "hard",
        "title": "Edit Distance",
        "tags": ["dp", "string"],
        "description": "Return the minimum number of single-character edits (insert, delete, replace) to turn word1 into word2.",
        "examples": 'edit_distance("horse", "ros") -> 3',
        "hint": "Classic 2D DP: dp[i][j] from prefixes of word1 and word2.",
        "syntax_hint": "if w1[i-1]==w2[j-1]: dp[i][j]=dp[i-1][j-1] else min of three neighbors +1",
        "signature": "def edit_distance(word1: str, word2: str) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert edit_distance("horse", "ros") == 3\n'
            '    assert edit_distance("", "a") == 1\n'
            '    assert edit_distance("abc", "abc") == 0\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def edit_distance(word1: str, word2: str) -> int:\n"
            "    m, n = len(word1), len(word2)\n"
            "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n"
            "    for i in range(m + 1):\n"
            "        dp[i][0] = i\n"
            "    for j in range(n + 1):\n"
            "        dp[0][j] = j\n"
            "    for i in range(1, m + 1):\n"
            "        for j in range(1, n + 1):\n"
            "            if word1[i - 1] == word2[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1]\n"
            "            else:\n"
            "                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])\n"
            "    return dp[m][n]\n"
        ),
    },
    {
        "slug": "44_two_sum_unsorted",
        "track": "algorithms", "difficulty": "easy",
        "title": "Two Sum (Unsorted)",
        "tags": ["hash-map", "array"],
        "description": "Given an unsorted list and a target, return 0-based indexes of two numbers that add to target. Exactly one solution exists.",
        "examples": "two_sum([2,7,11,15], 9) -> [0,1]",
        "hint": "Store value -> index as you scan; check if target - x was seen.",
        "syntax_hint": "seen = {}; for i, x in enumerate(nums): ...",
        "signature": "def two_sum(nums: list[int], target: int) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert two_sum([2,7,11,15], 9) == [0,1]\n"
            "    assert two_sum([3,2,4], 6) == [1,2]\n"
            "    assert two_sum([3,3], 6) == [0,1]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def two_sum(nums: list[int], target: int) -> list[int]:\n"
            "    seen = {}\n"
            "    for i, x in enumerate(nums):\n"
            "        need = target - x\n"
            "        if need in seen:\n"
            "            return [seen[need], i]\n"
            "        seen[x] = i\n"
            "    return []\n"
        ),
    },
    {
        "slug": "45_merge_sorted",
        "track": "algorithms", "difficulty": "easy",
        "title": "Merge Two Sorted Lists",
        "tags": ["two-pointers", "array"],
        "description": "Given two sorted lists of integers, return a new sorted list containing all elements from both.",
        "examples": "merge_sorted([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]",
        "hint": "Compare the fronts of both lists with two pointers; append the smaller value each step.",
        "syntax_hint": "while i < len(a) and j < len(b): pick a[i] or b[j]",
        "signature": "def merge_sorted(a: list[int], b: list[int]) -> list[int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]\n"
            "    assert merge_sorted([], [1, 2]) == [1, 2]\n"
            "    assert merge_sorted([1], []) == [1]\n"
            "    assert merge_sorted([], []) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def merge_sorted(a: list[int], b: list[int]) -> list[int]:\n"
            "    out: list[int] = []\n"
            "    i = j = 0\n"
            "    while i < len(a) and j < len(b):\n"
            "        if a[i] <= b[j]:\n"
            "            out.append(a[i])\n"
            "            i += 1\n"
            "        else:\n"
            "            out.append(b[j])\n"
            "            j += 1\n"
            "    out.extend(a[i:])\n"
            "    out.extend(b[j:])\n"
            "    return out\n"
        ),
    },
    {
        "slug": "46_valid_palindrome",
        "track": "algorithms", "difficulty": "easy",
        "title": "Valid Palindrome",
        "tags": ["two-pointers", "string"],
        "description": "Return True if a string is a palindrome after considering only alphanumeric characters and ignoring case.",
        "examples": 'valid_palindrome("A man, a plan, a canal: Panama") -> True',
        "hint": "Two pointers from both ends; skip non-alphanumeric chars and compare lowered letters.",
        "syntax_hint": "while left < right: advance past non-alnum; compare s[left].lower()",
        "signature": "def valid_palindrome(s: str) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert valid_palindrome("A man, a plan, a canal: Panama") is True\n'
            '    assert valid_palindrome("race a car") is False\n'
            '    assert valid_palindrome(" ") is True\n'
            '    assert valid_palindrome("0P") is False\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def valid_palindrome(s: str) -> bool:\n"
            "    left, right = 0, len(s) - 1\n"
            "    while left < right:\n"
            "        while left < right and not s[left].isalnum():\n"
            "            left += 1\n"
            "        while left < right and not s[right].isalnum():\n"
            "            right -= 1\n"
            "        if s[left].lower() != s[right].lower():\n"
            "            return False\n"
            "        left += 1\n"
            "        right -= 1\n"
            "    return True\n"
        ),
    },
    {
        "slug": "47_sqrt_x",
        "track": "algorithms", "difficulty": "easy",
        "title": "Integer Square Root",
        "tags": ["binary-search", "math"],
        "description": "Given a non-negative integer x, return the largest integer whose square is less than or equal to x.",
        "examples": "sqrt_x(8) -> 2; sqrt_x(16) -> 4",
        "hint": "Binary search on the answer range [0, x]; check mid * mid against x.",
        "syntax_hint": "lo, hi = 0, x; while lo <= hi: mid = (lo + hi) // 2",
        "signature": "def sqrt_x(x: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert sqrt_x(8) == 2\n"
            "    assert sqrt_x(16) == 4\n"
            "    assert sqrt_x(0) == 0\n"
            "    assert sqrt_x(1) == 1\n"
            "    assert sqrt_x(15) == 3\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def sqrt_x(x: int) -> int:\n"
            "    if x < 2:\n"
            "        return x\n"
            "    lo, hi = 1, x\n"
            "    ans = 0\n"
            "    while lo <= hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        if mid * mid <= x:\n"
            "            ans = mid\n"
            "            lo = mid + 1\n"
            "        else:\n"
            "            hi = mid - 1\n"
            "    return ans\n"
        ),
    },
    {
        "slug": "48_subarray_sum_k",
        "track": "algorithms", "difficulty": "medium",
        "title": "Subarray Sum Equals K",
        "tags": ["hash-map", "prefix-sum"],
        "description": "Given a list of integers (may include negatives) and an integer k, return the number of contiguous subarrays whose sum equals k.",
        "examples": "subarray_sum_k([1,1,1], 2) -> 2",
        "hint": "Track prefix sums in a dict; for each prefix p, add count of prefixes equal to p - k.",
        "syntax_hint": "counts = {0: 1}; running = 0; running += x; ans += counts.get(running - k, 0)",
        "signature": "def subarray_sum_k(nums: list[int], k: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert subarray_sum_k([1, 1, 1], 2) == 2\n"
            "    assert subarray_sum_k([1, 2, 3], 3) == 2\n"
            "    assert subarray_sum_k([1, -1, 0], 0) == 3\n"
            "    assert subarray_sum_k([], 0) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def subarray_sum_k(nums: list[int], k: int) -> int:\n"
            "    counts = {0: 1}\n"
            "    running = 0\n"
            "    ans = 0\n"
            "    for x in nums:\n"
            "        running += x\n"
            "        ans += counts.get(running - k, 0)\n"
            "        counts[running] = counts.get(running, 0) + 1\n"
            "    return ans\n"
        ),
    },
    {
        "slug": "49_number_of_islands",
        "track": "algorithms", "difficulty": "medium",
        "title": "Number of Islands",
        "tags": ["dfs", "grid"],
        "description": "Given a grid of 1 (land) and 0 (water), return the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.",
        "examples": "num_islands([[1,1,0],[1,0,0],[0,0,1]]) -> 2",
        "hint": "Scan the grid; when you find land, DFS/BFS to sink the whole island and increment the count.",
        "syntax_hint": "def dfs(r, c): grid[r][c] = 0; explore four neighbors",
        "signature": "def num_islands(grid: list[list[int]]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    g1 = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]\n"
            "    assert num_islands(g1) == 2\n"
            "    g2 = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]\n"
            "    assert num_islands(g2) == 1\n"
            "    assert num_islands([]) == 0\n"
            "    assert num_islands([[0, 0], [0, 0]]) == 0\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def num_islands(grid: list[list[int]]) -> int:\n"
            "    if not grid or not grid[0]:\n"
            "        return 0\n"
            "    rows, cols = len(grid), len(grid[0])\n"
            "    count = 0\n\n"
            "    def dfs(r: int, c: int) -> None:\n"
            "        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:\n"
            "            return\n"
            "        grid[r][c] = 0\n"
            "        dfs(r + 1, c)\n"
            "        dfs(r - 1, c)\n"
            "        dfs(r, c + 1)\n"
            "        dfs(r, c - 1)\n\n"
            "    for r in range(rows):\n"
            "        for c in range(cols):\n"
            "            if grid[r][c] == 1:\n"
            "                count += 1\n"
            "                dfs(r, c)\n"
            "    return count\n"
        ),
    },
    {
        "slug": "50_longest_consecutive",
        "track": "algorithms", "difficulty": "medium",
        "title": "Longest Consecutive Sequence",
        "tags": ["hash-set", "array"],
        "description": "Given an unsorted list of integers, return the length of the longest consecutive elements sequence. Must run in O(n) time.",
        "examples": "longest_consecutive([100,4,200,1,3,2]) -> 4  # sequence 1,2,3,4",
        "hint": "Put all numbers in a set; only start counting from numbers with no predecessor (n-1 not in set).",
        "syntax_hint": "nums_set = set(nums); if (x - 1) not in nums_set: walk x, x+1, ...",
        "signature": "def longest_consecutive(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4\n"
            "    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9\n"
            "    assert longest_consecutive([]) == 0\n"
            "    assert longest_consecutive([1]) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def longest_consecutive(nums: list[int]) -> int:\n"
            "    nums_set = set(nums)\n"
            "    best = 0\n"
            "    for x in nums_set:\n"
            "        if x - 1 in nums_set:\n"
            "            continue\n"
            "        length = 1\n"
            "        while x + length in nums_set:\n"
            "            length += 1\n"
            "        best = max(best, length)\n"
            "    return best\n"
        ),
    },
    {
        "slug": "51_kth_largest",
        "track": "algorithms", "difficulty": "medium",
        "title": "Kth Largest Element",
        "tags": ["heap", "array"],
        "description": "Given an unsorted list and integer k, return the kth largest element (1-based: k=1 is the maximum).",
        "examples": "kth_largest([3,2,1,5,6,4], 2) -> 5",
        "hint": "Use heapq.nlargest(k, nums)[-1] or maintain a size-k min-heap.",
        "syntax_hint": "import heapq; return heapq.nlargest(k, nums)[-1]",
        "signature": "def kth_largest(nums: list[int], k: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5\n"
            "    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4\n"
            "    assert kth_largest([1], 1) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import heapq\n\n"
            "def kth_largest(nums: list[int], k: int) -> int:\n"
            "    return heapq.nlargest(k, nums)[-1]\n"
        ),
    },
    {
        "slug": "52_max_product_subarray",
        "track": "algorithms", "difficulty": "medium",
        "title": "Maximum Product Subarray",
        "tags": ["dp", "array"],
        "description": "Given a list of integers, return the largest product of any contiguous non-empty subarray.",
        "examples": "max_product([2,3,-2,4]) -> 6",
        "hint": "Track both max and min ending here because a negative flip can make a new max.",
        "syntax_hint": "cur_max = cur_min = best = nums[0]; update with x, cur_max*x, cur_min*x",
        "signature": "def max_product(nums: list[int]) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert max_product([2, 3, -2, 4]) == 6\n"
            "    assert max_product([-2, 0, -1]) == 0\n"
            "    assert max_product([-2]) == -2\n"
            "    assert max_product([2, -5, -2, -4, 3]) == 24\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def max_product(nums: list[int]) -> int:\n"
            "    cur_max = cur_min = best = nums[0]\n"
            "    for x in nums[1:]:\n"
            "        candidates = (x, cur_max * x, cur_min * x)\n"
            "        cur_max = max(candidates)\n"
            "        cur_min = min(candidates)\n"
            "        best = max(best, cur_max)\n"
            "    return best\n"
        ),
    },
    {
        "slug": "53_search_rotated",
        "track": "algorithms", "difficulty": "hard",
        "title": "Search in Rotated Sorted Array",
        "tags": ["binary-search", "array"],
        "description": "A sorted list was rotated at an unknown pivot. Given the rotated list and a target, return its index or -1 if absent. All values are distinct.",
        "examples": "search_rotated([4,5,6,7,0,1,2], 0) -> 4",
        "hint": "Binary search; one half is always sorted — check which half contains target.",
        "syntax_hint": "mid = (lo + hi) // 2; if nums[lo] <= nums[mid]: left half sorted",
        "signature": "def search_rotated(nums: list[int], target: int) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4\n"
            "    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1\n"
            "    assert search_rotated([1], 0) == -1\n"
            "    assert search_rotated([1], 1) == 0\n"
            "    assert search_rotated([3, 1], 1) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def search_rotated(nums: list[int], target: int) -> int:\n"
            "    lo, hi = 0, len(nums) - 1\n"
            "    while lo <= hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        if nums[mid] == target:\n"
            "            return mid\n"
            "        if nums[lo] <= nums[mid]:\n"
            "            if nums[lo] <= target < nums[mid]:\n"
            "                hi = mid - 1\n"
            "            else:\n"
            "                lo = mid + 1\n"
            "        else:\n"
            "            if nums[mid] < target <= nums[hi]:\n"
            "                lo = mid + 1\n"
            "            else:\n"
            "                hi = mid - 1\n"
            "    return -1\n"
        ),
    },
    # --- syntax ---
    {
        "slug": "21_itertools_combinations",
        "track": "syntax", "difficulty": "easy",
        "title": "All Pairs",
        "tags": ["itertools"],
        "description": "Return all 2-element combinations from items as sorted tuples (order within tuple sorted).",
        "examples": "all_pairs([1,2,3]) -> [(1,2),(1,3),(2,3)]",
        "hint": "itertools.combinations(items, 2)",
        "syntax_hint": "from itertools import combinations; sorted(combinations(items, 2))",
        "signature": "def all_pairs(items: list) -> list[tuple]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert all_pairs([1,2,3]) == [(1,2),(1,3),(2,3)]\n"
            "    assert all_pairs(['a']) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from itertools import combinations\n\n"
            "def all_pairs(items: list) -> list[tuple]:\n"
            "    return [tuple(c) for c in combinations(items, 2)]\n"
        ),
    },
    {
        "slug": "22_context_manager_timer",
        "track": "syntax", "difficulty": "medium",
        "title": "Timer Context Manager",
        "tags": ["contextmanager"],
        "description": "Return a context manager class Timer that records elapsed seconds in .elapsed after the block exits (use time.perf_counter).",
        "examples": "with Timer() as t: ...; t.elapsed >= 0",
        "hint": "__enter__ stores start; __exit__ sets elapsed.",
        "syntax_hint": "class Timer: def __enter__(self): self._start=perf_counter()",
        "signature": "class Timer:\n    elapsed: float = 0.0\n    def __enter__(self): pass\n    def __exit__(self, *args): pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import time\n"
            "    with Timer() as t:\n"
            "        time.sleep(0.01)\n"
            "    assert t.elapsed >= 0.005\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import time\n\n"
            "class Timer:\n"
            "    elapsed: float = 0.0\n"
            "    def __enter__(self):\n"
            "        self._start = time.perf_counter()\n"
            "        return self\n"
            "    def __exit__(self, *args):\n"
            "        self.elapsed = time.perf_counter() - self._start\n"
            "        return False\n"
        ),
    },
    {
        "slug": "23_deep_get",
        "track": "syntax", "difficulty": "medium",
        "title": "Deep Dict Get",
        "tags": ["dict"],
        "description": "Given a nested dict and a list of keys, return the nested value or default if any key is missing.",
        "examples": 'deep_get({"a":{"b":1}}, ["a","b"], 0) -> 1',
        "hint": "Walk keys one by one; return default on KeyError or non-dict.",
        "syntax_hint": "for k in keys: d = d[k]",
        "signature": "def deep_get(d: dict, keys: list, default=None):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert deep_get({"a":{"b":1}}, ["a","b"], 0) == 1\n'
            '    assert deep_get({"a":{"b":1}}, ["a","c"], 9) == 9\n'
            '    assert deep_get({}, ["x"], "missing") == "missing"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def deep_get(d: dict, keys: list, default=None):\n"
            "    cur = d\n"
            "    for k in keys:\n"
            "        if not isinstance(cur, dict) or k not in cur:\n"
            "            return default\n"
            "        cur = cur[k]\n"
            "    return cur\n"
        ),
    },
    {
        "slug": "24_flatten_nested_list",
        "track": "syntax", "difficulty": "hard",
        "title": "Flatten Nested List",
        "tags": ["recursion", "list"],
        "description": "Flatten a list that may contain nested lists to a single flat list of non-list items.",
        "examples": "flatten([1,[2,[3]],4]) -> [1,2,3,4]",
        "hint": "Recursively extend when you see a list.",
        "syntax_hint": "for x in items: if isinstance(x, list): out.extend(flatten(x)) else: out.append(x)",
        "signature": "def flatten(items: list) -> list:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert flatten([1,[2,[3]],4]) == [1,2,3,4]\n"
            "    assert flatten([]) == []\n"
            "    assert flatten([1,2,3]) == [1,2,3]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def flatten(items: list) -> list:\n"
            "    out = []\n"
            "    for x in items:\n"
            "        if isinstance(x, list):\n"
            "            out.extend(flatten(x))\n"
            "        else:\n"
            "            out.append(x)\n"
            "    return out\n"
        ),
    },
    # --- automations ---
    {
        "slug": "13_json_lines_parse",
        "track": "automations", "difficulty": "easy",
        "title": "Parse JSON Lines",
        "tags": ["json", "file"],
        "description": "Given a string with one JSON object per line, return a list of parsed dicts (skip blank lines).",
        "examples": 'parse_jsonl("{\\"a\\":1}\\n{\\"b\\":2}") -> [{"a":1},{"b":2}]',
        "hint": "Splitlines, json.loads each non-empty line.",
        "syntax_hint": "[json.loads(line) for line in text.splitlines() if line.strip()]",
        "signature": "def parse_jsonl(text: str) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert parse_jsonl(\'{"a":1}\\n{"b":2}\') == [{"a":1},{"b":2}]\n'
            '    assert parse_jsonl("") == []\n'
            '    assert parse_jsonl("\\n\\n") == []\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import json\n\n"
            "def parse_jsonl(text: str) -> list[dict]:\n"
            "    out = []\n"
            "    for line in text.splitlines():\n"
            "        line = line.strip()\n"
            "        if line:\n"
            "            out.append(json.loads(line))\n"
            "    return out\n"
        ),
    },
    {
        "slug": "14_slug_variations",
        "track": "automations", "difficulty": "easy",
        "title": "Slug Variants",
        "tags": ["string"],
        "description": "Return three slug variants for a title: snake_case, kebab-case, and dot.case (all lowercase, spaces to separator).",
        "examples": 'slug_variants("Hello World") -> ("hello_world","hello-world","hello.world")',
        "hint": "Lowercase, replace spaces with _, -, and .",
        "syntax_hint": "s.lower().replace(' ', sep)",
        "signature": "def slug_variants(title: str) -> tuple[str, str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert slug_variants("Hello World") == ("hello_world","hello-world","hello.world")\n'
            '    assert slug_variants("A") == ("a","a","a")\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def slug_variants(title: str) -> tuple[str, str, str]:\n"
            "    s = title.lower()\n"
            "    return (s.replace(' ', '_'), s.replace(' ', '-'), s.replace(' ', '.'))\n"
        ),
    },
    {
        "slug": "15_log_parser_levels",
        "track": "automations", "difficulty": "medium",
        "title": "Count Log Levels",
        "tags": ["log", "parse"],
        "description": "Given log lines like '2024-01-01 ERROR msg', count lines per level (ERROR, WARN, INFO). Unknown levels ignored.",
        "examples": "count_levels(lines) -> {'ERROR':1,'INFO':2}",
        "hint": "Split line, second token is level.",
        "syntax_hint": "from collections import Counter",
        "signature": "def count_levels(lines: list[str]) -> dict[str, int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    lines = ["2024 ERROR x", "2024 INFO y", "2024 INFO z", "2024 DEBUG w"]\n'
            "    assert count_levels(lines) == {'ERROR': 1, 'INFO': 2}\n"
            "    assert count_levels([]) == {}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def count_levels(lines: list[str]) -> dict[str, int]:\n"
            "    levels = {'ERROR', 'WARN', 'INFO'}\n"
            "    c = Counter()\n"
            "    for line in lines:\n"
            "        parts = line.split()\n"
            "        if len(parts) >= 2 and parts[1] in levels:\n"
            "            c[parts[1]] += 1\n"
            "    return dict(c)\n"
        ),
    },
    {
        "slug": "16_batch_rename_plan",
        "track": "automations", "difficulty": "hard",
        "title": "Batch Rename Plan",
        "tags": ["files"],
        "description": "Given filenames and a prefix, return list of (old, new) rename pairs adding zero-padded index: prefix_001.ext.",
        "examples": 'plan(["a.txt","b.txt"], "img") -> [("a.txt","img_001.txt"),("b.txt","img_002.txt")]',
        "hint": "Enumerate starting at 1; keep extension from old name.",
        "syntax_hint": "from pathlib import Path; Path(name).suffix",
        "signature": "def plan(names: list[str], prefix: str) -> list[tuple[str, str]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert plan(["a.txt","b.txt"], "img") == [("a.txt","img_001.txt"),("b.txt","img_002.txt")]\n'
            "    assert plan([], \"x\") == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from pathlib import Path\n\n"
            "def plan(names: list[str], prefix: str) -> list[tuple[str, str]]:\n"
            "    out = []\n"
            "    width = max(3, len(str(len(names))))\n"
            "    for i, name in enumerate(names, 1):\n"
            "        ext = Path(name).suffix\n"
            "        new = f\"{prefix}_{i:0{width}d}{ext}\"\n"
            "        out.append((name, new))\n"
            "    return out\n"
        ),
    },
    # --- apis ---
    {
        "slug": "11_nested_json_get",
        "track": "apis", "difficulty": "easy",
        "title": "Nested JSON Get",
        "tags": ["json"],
        "description": "Parse JSON text and return data['user']['name'] or None if missing.",
        "examples": 'user_name(\'{"user":{"name":"eli"}}\') -> "eli"',
        "hint": "json.loads then chained .get calls.",
        "syntax_hint": "obj.get('user', {}).get('name')",
        "signature": "def user_name(text: str) -> str | None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert user_name(\'{"user":{"name":"eli"}}\') == "eli"\n'
            '    assert user_name(\'{"user":{}}\') is None\n'
            '    assert user_name("{}") is None\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import json\n\n"
            "def user_name(text: str) -> str | None:\n"
            "    obj = json.loads(text)\n"
            "    return obj.get('user', {}).get('name')\n"
        ),
    },
    {
        "slug": "12_merge_query_params",
        "track": "apis", "difficulty": "medium",
        "title": "Merge Query Params",
        "tags": ["url"],
        "description": "Merge two query param dicts; values from the second override the first.",
        "examples": "merge_params({'a':1},{'a':2,'b':3}) -> {'a':2,'b':3}",
        "hint": "Spread / dict union: {**a, **b}",
        "syntax_hint": "return {**first, **second}",
        "signature": "def merge_params(a: dict, b: dict) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert merge_params({'a':1},{'a':2,'b':3}) == {'a':2,'b':3}\n"
            "    assert merge_params({}, {'x':1}) == {'x':1}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def merge_params(a: dict, b: dict) -> dict:\n"
            "    return {**a, **b}\n"
        ),
    },
    {
        "slug": "13_api_error_mapper",
        "track": "apis", "difficulty": "hard",
        "title": "API Error Mapper",
        "tags": ["api", "errors"],
        "description": "Map HTTP status codes to short labels: 2xx ok, 4xx client, 5xx server, else unknown.",
        "examples": "error_label(404) -> 'client'",
        "hint": "status // 100 gives the class digit.",
        "syntax_hint": "cls = code // 100",
        "signature": "def error_label(code: int) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert error_label(200) == 'ok'\n"
            "    assert error_label(404) == 'client'\n"
            "    assert error_label(500) == 'server'\n"
            "    assert error_label(999) == 'unknown'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def error_label(code: int) -> str:\n"
            "    cls = code // 100\n"
            "    if cls == 2:\n"
            "        return 'ok'\n"
            "    if cls == 4:\n"
            "        return 'client'\n"
            "    if cls == 5:\n"
            "        return 'server'\n"
            "    return 'unknown'\n"
        ),
    },
    {
        "slug": "14_paginate_offset",
        "track": "apis", "difficulty": "medium",
        "title": "Offset Pagination",
        "tags": ["api"],
        "description": "Slice items for page (1-based) and page_size; return (items_slice, total_pages).",
        "examples": "page_items([1,2,3,4,5], page=2, size=2) -> ([3,4], 3)",
        "hint": "start = (page-1)*size; math.ceil for total pages.",
        "syntax_hint": "import math; math.ceil(len(items)/size)",
        "signature": "def page_items(items: list, page: int, size: int) -> tuple[list, int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert page_items([1,2,3,4,5], 2, 2) == ([3,4], 3)\n"
            "    assert page_items([], 1, 10) == ([], 0)\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import math\n\n"
            "def page_items(items: list, page: int, size: int) -> tuple[list, int]:\n"
            "    if not items or size <= 0:\n"
            "        return [], 0\n"
            "    total = math.ceil(len(items) / size)\n"
            "    start = (page - 1) * size\n"
            "    return items[start:start + size], total\n"
        ),
    },
    # --- servers ---
    {
        "slug": "11_cors_headers",
        "track": "servers", "difficulty": "easy",
        "title": "CORS Headers",
        "tags": ["http"],
        "description": "Return a dict of CORS headers allowing origin * and methods GET, POST.",
        "examples": "cors_headers() -> {'Access-Control-Allow-Origin':'*', ...}",
        "hint": "Standard Access-Control-* header names.",
        "syntax_hint": "return {'Access-Control-Allow-Origin': '*', ...}",
        "signature": "def cors_headers() -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    h = cors_headers()\n"
            "    assert h['Access-Control-Allow-Origin'] == '*'\n"
            "    assert 'GET' in h['Access-Control-Allow-Methods']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def cors_headers() -> dict[str, str]:\n"
            "    return {\n"
            "        'Access-Control-Allow-Origin': '*',\n"
            "        'Access-Control-Allow-Methods': 'GET, POST',\n"
            "    }\n"
        ),
    },
    {
        "slug": "12_round_robin",
        "track": "servers", "difficulty": "medium",
        "title": "Round Robin Picker",
        "tags": ["load-balancer"],
        "description": "Implement RoundRobin(hosts) with .next() cycling through hosts in order.",
        "examples": "rb=RoundRobin(['a','b']); rb.next(); rb.next() -> 'a' then 'b'",
        "hint": "Store index modulo len(hosts).",
        "syntax_hint": "self._i = (self._i + 1) % len(self.hosts)",
        "signature": "class RoundRobin:\n    def __init__(self, hosts: list[str]): pass\n    def next(self) -> str: pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    rb = RoundRobin(['a','b','c'])\n"
            "    assert rb.next() == 'a'\n"
            "    assert rb.next() == 'b'\n"
            "    assert rb.next() == 'c'\n"
            "    assert rb.next() == 'a'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class RoundRobin:\n"
            "    def __init__(self, hosts: list[str]):\n"
            "        self.hosts = hosts\n"
            "        self._i = 0\n"
            "    def next(self) -> str:\n"
            "        host = self.hosts[self._i]\n"
            "        self._i = (self._i + 1) % len(self.hosts)\n"
            "        return host\n"
        ),
    },
    {
        "slug": "13_request_id_middleware",
        "track": "servers", "difficulty": "medium",
        "title": "Request ID Middleware",
        "tags": ["middleware"],
        "description": "Given headers dict, add X-Request-Id with the given id if not already present; return new dict.",
        "examples": "add_request_id({}, 'abc') -> {'X-Request-Id':'abc'}",
        "hint": "Copy headers, set key if missing.",
        "syntax_hint": "h = dict(headers); h.setdefault('X-Request-Id', rid)",
        "signature": "def add_request_id(headers: dict, rid: str) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert add_request_id({}, 'abc') == {'X-Request-Id': 'abc'}\n"
            "    assert add_request_id({'X-Request-Id': 'x'}, 'abc') == {'X-Request-Id': 'x'}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def add_request_id(headers: dict, rid: str) -> dict:\n"
            "    h = dict(headers)\n"
            "    h.setdefault('X-Request-Id', rid)\n"
            "    return h\n"
        ),
    },
    {
        "slug": "14_rate_limit_window",
        "track": "servers", "difficulty": "hard",
        "title": "Fixed Window Rate Limit",
        "tags": ["rate-limit"],
        "description": "FixedWindow(limit) tracks .allow() calls per window_seconds; return True if under limit else False.",
        "examples": "w=FixedWindow(2, window_seconds=60); w.allow(); w.allow(); w.allow() -> False",
        "hint": "Reset count when time window elapses.",
        "syntax_hint": "import time; if now - start >= window: reset",
        "signature": "class FixedWindow:\n    def __init__(self, limit: int, window_seconds: float = 60.0): pass\n    def allow(self) -> bool: pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    w = FixedWindow(2, window_seconds=3600)\n"
            "    assert w.allow() is True\n"
            "    assert w.allow() is True\n"
            "    assert w.allow() is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import time\n\n"
            "class FixedWindow:\n"
            "    def __init__(self, limit: int, window_seconds: float = 60.0):\n"
            "        self.limit = limit\n"
            "        self.window = window_seconds\n"
            "        self.count = 0\n"
            "        self.start = time.monotonic()\n"
            "    def allow(self) -> bool:\n"
            "        now = time.monotonic()\n"
            "        if now - self.start >= self.window:\n"
            "            self.start = now\n"
            "            self.count = 0\n"
            "        if self.count < self.limit:\n"
            "            self.count += 1\n"
            "            return True\n"
            "        return False\n"
        ),
    },
    # --- apps ---
    {
        "slug": "11_bank_account",
        "track": "apps", "difficulty": "medium",
        "title": "Bank Account",
        "tags": ["class"],
        "description": "BankAccount with deposit, withdraw (no overdraft), and balance.",
        "examples": "a=BankAccount(100); a.withdraw(30); a.balance() -> 70",
        "hint": "Reject withdraw if amount > balance.",
        "syntax_hint": "if amount > self._bal: raise ValueError",
        "signature": "class BankAccount:\n    def __init__(self, balance: float = 0): pass\n    def deposit(self, amount: float) -> None: pass\n    def withdraw(self, amount: float) -> None: pass\n    def balance(self) -> float: pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    a = BankAccount(100)\n"
            "    a.withdraw(30)\n"
            "    assert a.balance() == 70\n"
            "    a.deposit(10)\n"
            "    assert a.balance() == 80\n"
            "    try:\n"
            "        a.withdraw(100)\n"
            "        assert False\n"
            "    except ValueError:\n"
            "        pass\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class BankAccount:\n"
            "    def __init__(self, balance: float = 0):\n"
            "        self._bal = balance\n"
            "    def deposit(self, amount: float) -> None:\n"
            "        self._bal += amount\n"
            "    def withdraw(self, amount: float) -> None:\n"
            "        if amount > self._bal:\n"
            "            raise ValueError('insufficient funds')\n"
            "        self._bal -= amount\n"
            "    def balance(self) -> float:\n"
            "        return self._bal\n"
        ),
    },
    {
        "slug": "12_shopping_cart",
        "track": "apps", "difficulty": "medium",
        "title": "Shopping Cart Total",
        "tags": ["class"],
        "description": "Cart stores (name, price, qty) items; total() sums price*qty.",
        "examples": "c.add('apple', 1.0, 3); c.total() -> 3.0",
        "hint": "List of tuples or small dicts.",
        "syntax_hint": "sum(price * qty for ...)",
        "signature": "class Cart:\n    def __init__(self): pass\n    def add(self, name: str, price: float, qty: int) -> None: pass\n    def total(self) -> float: pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    c = Cart()\n"
            "    c.add('apple', 1.0, 3)\n"
            "    c.add('bread', 2.5, 1)\n"
            "    assert c.total() == 5.5\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "class Cart:\n"
            "    def __init__(self):\n"
            "        self._items = []\n"
            "    def add(self, name: str, price: float, qty: int) -> None:\n"
            "        self._items.append((name, price, qty))\n"
            "    def total(self) -> float:\n"
            "        return sum(p * q for _, p, q in self._items)\n"
        ),
    },
    {
        "slug": "13_lru_cache_class",
        "track": "apps", "difficulty": "hard",
        "title": "Simple LRU Cache",
        "tags": ["class", "cache"],
        "description": "LRUCache(capacity) with get(key) and put(key, val); evict least recently used when full.",
        "examples": "c=LRUCache(2); c.put(1,1); c.put(2,2); c.put(3,3); c.get(1) is None",
        "hint": "OrderedDict move_to_end on access; popitem(last=False) to evict.",
        "syntax_hint": "from collections import OrderedDict",
        "signature": "class LRUCache:\n    def __init__(self, capacity: int): pass\n    def get(self, key): pass\n    def put(self, key, value) -> None: pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    c = LRUCache(2)\n"
            "    c.put(1, 'a')\n"
            "    c.put(2, 'b')\n"
            "    assert c.get(1) == 'a'\n"
            "    c.put(3, 'c')\n"
            "    assert c.get(2) is None\n"
            "    assert c.get(3) == 'c'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import OrderedDict\n\n"
            "class LRUCache:\n"
            "    def __init__(self, capacity: int):\n"
            "        self.cap = capacity\n"
            "        self.data = OrderedDict()\n"
            "    def get(self, key):\n"
            "        if key not in self.data:\n"
            "            return None\n"
            "        self.data.move_to_end(key)\n"
            "        return self.data[key]\n"
            "    def put(self, key, value) -> None:\n"
            "        if key in self.data:\n"
            "            self.data.move_to_end(key)\n"
            "        self.data[key] = value\n"
            "        if len(self.data) > self.cap:\n"
            "            self.data.popitem(last=False)\n"
        ),
    },
    {
        "slug": "14_word_counter",
        "track": "apps", "difficulty": "easy",
        "title": "Word Counter App",
        "tags": ["dict"],
        "description": "Given a sentence, return a dict of lowercase word counts.",
        "examples": 'count_words("Hi hi there") -> {"hi":2,"there":1}',
        "hint": "Split on whitespace, lower, Counter.",
        "syntax_hint": "from collections import Counter",
        "signature": "def count_words(sentence: str) -> dict[str, int]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert count_words("Hi hi there") == {"hi": 2, "there": 1}\n'
            '    assert count_words("") == {}\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from collections import Counter\n\n"
            "def count_words(sentence: str) -> dict[str, int]:\n"
            "    words = sentence.lower().split()\n"
            "    return dict(Counter(words))\n"
        ),
    },
    # --- fastapi ---
    {
        "slug": "09_path_int_param",
        "track": "fastapi", "difficulty": "easy",
        "title": "Integer Path Param Route",
        "tags": ["fastapi"],
        "description": "Implement register(app) to add routes to the given FastAPI app. Tests create a FastAPI() instance and call register(app) before using TestClient. Register GET /items/{item_id} returning {'id': item_id}.",
        "examples": "client.get('/items/5').json() -> {'id': 5}",
        "hint": "Path parameter typed as int.",
        "syntax_hint": "@app.get('/items/{item_id}')",
        "signature": "def register(app) -> None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi import FastAPI\n"
            "    from fastapi.testclient import TestClient\n"
            "    app = FastAPI()\n"
            "    register(app)\n"
            "    c = TestClient(app)\n"
            "    assert c.get('/items/5').json() == {'id': 5}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def register(app) -> None:\n"
            "    @app.get('/items/{item_id}')\n"
            "    def get_item(item_id: int):\n"
            "        return {'id': item_id}\n"
        ),
    },
    {
        "slug": "10_delete_route",
        "track": "fastapi", "difficulty": "medium",
        "title": "DELETE Route",
        "tags": ["fastapi"],
        "description": "Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). Register DELETE /items/{item_id} returning 204 with empty body.",
        "examples": "client.delete('/items/1').status_code == 204",
        "hint": "Use status_code=204 on decorator or Response.",
        "syntax_hint": "@app.delete('/items/{item_id}', status_code=204)",
        "signature": "def register(app) -> None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi import FastAPI\n"
            "    from fastapi.testclient import TestClient\n"
            "    app = FastAPI()\n"
            "    register(app)\n"
            "    c = TestClient(app)\n"
            "    r = c.delete('/items/1')\n"
            "    assert r.status_code == 204\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def register(app) -> None:\n"
            "    @app.delete('/items/{item_id}', status_code=204)\n"
            "    def delete_item(item_id: int):\n"
            "        return None\n"
        ),
    },
    {
        "slug": "11_query_optional",
        "track": "fastapi", "difficulty": "easy",
        "title": "Optional Query Param",
        "tags": ["fastapi"],
        "description": "Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). GET /search takes optional q query param; return {'q': q} where q defaults to empty string.",
        "examples": "get('/search') -> {'q': ''}",
        "hint": "q: str = Query(default='') or q: str = ''",
        "syntax_hint": "def search(q: str = ''): return {'q': q}",
        "signature": "def register(app) -> None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi import FastAPI\n"
            "    from fastapi.testclient import TestClient\n"
            "    app = FastAPI()\n"
            "    register(app)\n"
            "    c = TestClient(app)\n"
            "    assert c.get('/search').json() == {'q': ''}\n"
            "    assert c.get('/search', params={'q': 'py'}).json() == {'q': 'py'}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def register(app) -> None:\n"
            "    @app.get('/search')\n"
            "    def search(q: str = ''):\n"
            "        return {'q': q}\n"
        ),
    },
    {
        "slug": "12_header_api_key",
        "track": "fastapi", "difficulty": "hard",
        "title": "API Key Header Check",
        "tags": ["fastapi"],
        "description": "Implement register(app) to add routes to the given FastAPI app. Tests create FastAPI() and call register(app). GET /secure requires header X-API-Key == 'secret'; return 401 via HTTPException if wrong.",
        "examples": "missing key -> 401; correct -> 200",
        "hint": "Read Header alias X-API-Key; raise HTTPException(401).",
        "syntax_hint": "from fastapi import Header, HTTPException",
        "signature": "def register(app) -> None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from fastapi import FastAPI\n"
            "    from fastapi.testclient import TestClient\n"
            "    app = FastAPI()\n"
            "    register(app)\n"
            "    c = TestClient(app)\n"
            "    assert c.get('/secure').status_code == 401\n"
            "    assert c.get('/secure', headers={'X-API-Key': 'secret'}).status_code == 200\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from fastapi import Header, HTTPException\n\n"
            "def register(app) -> None:\n"
            "    @app.get('/secure')\n"
            "    def secure(x_api_key: str = Header(default='')):\n"
            "        if x_api_key != 'secret':\n"
            "            raise HTTPException(status_code=401)\n"
            "        return {'ok': True}\n"
        ),
    },
    # --- tkinter ---
    {
        "slug": "07_button_specs",
        "track": "tkinter", "difficulty": "easy",
        "title": "Button Specs",
        "tags": ["tkinter"],
        "description": "Given (label, command_name) pairs, return button specs with text and command fields.",
        "examples": 'buttons([("Save","save")]) -> [{"text":"Save","command":"save"}]',
        "hint": "List comprehension building dicts.",
        "syntax_hint": "[{'text': l, 'command': c} for l, c in pairs]",
        "signature": "def buttons(pairs: list[tuple[str, str]]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert buttons([("Save","save")]) == [{"text":"Save","command":"save"}]\n'
            "    assert buttons([]) == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def buttons(pairs: list[tuple[str, str]]) -> list[dict]:\n"
            "    return [{'text': l, 'command': c} for l, c in pairs]\n"
        ),
    },
    {
        "slug": "08_tab_order",
        "track": "tkinter", "difficulty": "medium",
        "title": "Tab Order",
        "tags": ["tkinter", "focus"],
        "description": "Given widget names in tab order, return list of dicts {name, tab_index}.",
        "examples": "tab_order(['a','b']) -> [{'name':'a','tab_index':0},...]",
        "hint": "Enumerate names.",
        "syntax_hint": "[{'name': n, 'tab_index': i} for i, n in enumerate(names)]",
        "signature": "def tab_order(names: list[str]) -> list[dict]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert tab_order(['a','b']) == [{'name':'a','tab_index':0},{'name':'b','tab_index':1}]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def tab_order(names: list[str]) -> list[dict]:\n"
            "    return [{'name': n, 'tab_index': i} for i, n in enumerate(names)]\n"
        ),
    },
    {
        "slug": "09_dialog_result",
        "track": "tkinter", "difficulty": "easy",
        "title": "Dialog Result Mapping",
        "tags": ["tkinter"],
        "description": "Map dialog button labels ok/cancel to True/False; unknown labels -> None.",
        "examples": "dialog_result('ok') -> True",
        "hint": "Simple if/elif on lowered label.",
        "syntax_hint": "return {'ok': True, 'cancel': False}.get(label.lower())",
        "signature": "def dialog_result(label: str) -> bool | None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert dialog_result('ok') is True\n"
            "    assert dialog_result('Cancel') is False\n"
            "    assert dialog_result('maybe') is None\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def dialog_result(label: str) -> bool | None:\n"
            "    m = {'ok': True, 'cancel': False}\n"
            "    return m.get(label.lower())\n"
        ),
    },
    {
        "slug": "10_widget_tree_depth",
        "track": "tkinter", "difficulty": "hard",
        "title": "Widget Tree Max Depth",
        "tags": ["tkinter", "tree"],
        "description": "Given nested dict tree {name: {child: {}}}, return max nesting depth (leaf = 1).",
        "examples": "depth({'root':{'a':{}}}) -> 2",
        "hint": "Recurse into dict values.",
        "syntax_hint": "1 + max(depth(v) for v in node.values()) if node else 0",
        "signature": "def depth(tree: dict) -> int:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert depth({'root': {'a': {}}}) == 2\n"
            "    assert depth({}) == 0\n"
            "    assert depth({'x': {}}) == 1\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import tkinter  # noqa: F401\n\n"
            "def depth(tree: dict) -> int:\n"
            "    if not tree:\n"
            "        return 0\n"
            "    return 1 + max((depth(v) for v in tree.values()), default=0)\n"
        ),
    },
    # --- requests ---
    {
        "slug": "08_basic_auth_header",
        "track": "requests", "difficulty": "easy",
        "title": "Basic Auth Header Value",
        "tags": ["requests", "auth"],
        "description": "Return the Authorization header value for HTTP basic auth (user:pass base64).",
        "examples": "auth_header('u','p') starts with 'Basic '",
        "hint": "Base64-encode 'user:pass' and prefix with 'Basic '.",
        "syntax_hint": "import base64; 'Basic ' + b64encode(f'{u}:{p}'.encode()).decode()",
        "signature": "def auth_header(user: str, password: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    h = auth_header('u', 'p')\n"
            "    assert h.startswith('Basic ')\n"
            "    import base64\n"
            "    assert base64.b64decode(h[6:]) == b'u:p'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import base64\n\n"
            "def auth_header(user: str, password: str) -> str:\n"
            "    token = base64.b64encode(f'{user}:{password}'.encode()).decode()\n"
            "    return f'Basic {token}'\n"
        ),
    },
    {
        "slug": "09_json_post_headers",
        "track": "requests", "difficulty": "medium",
        "title": "JSON POST Headers",
        "tags": ["requests"],
        "description": "Return headers dict for a JSON POST: Content-Type application/json and Accept application/json.",
        "examples": "json_headers()['Content-Type'] == 'application/json'",
        "hint": "Static dict.",
        "syntax_hint": "return {'Content-Type': 'application/json', 'Accept': 'application/json'}",
        "signature": "def json_headers() -> dict[str, str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    h = json_headers()\n"
            "    assert h['Content-Type'] == 'application/json'\n"
            "    assert h['Accept'] == 'application/json'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def json_headers() -> dict[str, str]:\n"
            "    return {'Content-Type': 'application/json', 'Accept': 'application/json'}\n"
        ),
    },
    {
        "slug": "10_merge_session_headers",
        "track": "requests", "difficulty": "medium",
        "title": "Merge Session Headers",
        "tags": ["requests"],
        "description": "Merge default session headers with per-request headers; request wins on conflict.",
        "examples": "merge({'A':'1'},{'A':'2','B':'3'}) -> {'A':'2','B':'3'}",
        "hint": "{**session, **request}",
        "syntax_hint": "return {**session, **request}",
        "signature": "def merge(session: dict, request: dict) -> dict:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert merge({'A':'1'},{'A':'2','B':'3'}) == {'A':'2','B':'3'}\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def merge(session: dict, request: dict) -> dict:\n"
            "    return {**session, **request}\n"
        ),
    },
    {
        "slug": "11_retry_statuses",
        "track": "requests", "difficulty": "hard",
        "title": "Retry Status Set",
        "tags": ["requests"],
        "description": "Return True if status code should be retried (408, 429, 500-599).",
        "examples": "should_retry(503) -> True; should_retry(404) -> False",
        "hint": "Membership in known codes or 5xx range.",
        "syntax_hint": "code in (408, 429) or 500 <= code <= 599",
        "signature": "def should_retry(code: int) -> bool:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert should_retry(503) is True\n"
            "    assert should_retry(429) is True\n"
            "    assert should_retry(404) is False\n"
            "    assert should_retry(200) is False\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def should_retry(code: int) -> bool:\n"
            "    if code in (408, 429):\n"
            "        return True\n"
            "    return 500 <= code <= 599\n"
        ),
    },
    # --- pandas ---
    {
        "slug": "09_drop_na_rows",
        "track": "pandas", "difficulty": "easy",
        "title": "Drop NA Rows",
        "tags": ["pandas"],
        "description": "Return a DataFrame with rows containing any NaN removed.",
        "examples": "drop_na(df) removes rows with NaN",
        "hint": "df.dropna()",
        "syntax_hint": "df.dropna()",
        "signature": "def drop_na(df):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    import numpy as np\n"
            "    df = pd.DataFrame({'a': [1, np.nan, 3]})\n"
            "    out = drop_na(df)\n"
            "    assert len(out) == 2\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def drop_na(df):\n"
            "    return df.dropna()\n"
        ),
    },
    {
        "slug": "10_rename_columns",
        "track": "pandas", "difficulty": "easy",
        "title": "Rename Columns",
        "tags": ["pandas"],
        "description": "Rename DataFrame columns using the given mapping dict.",
        "examples": "rename_cols(df, {'old':'new'})",
        "hint": "df.rename(columns=mapping)",
        "syntax_hint": "df.rename(columns=mapping)",
        "signature": "def rename_cols(df, mapping: dict):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({'old': [1]})\n"
            "    out = rename_cols(df, {'old': 'new'})\n"
            "    assert 'new' in out.columns\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def rename_cols(df, mapping: dict):\n"
            "    return df.rename(columns=mapping)\n"
        ),
    },
    {
        "slug": "11_rolling_mean",
        "track": "pandas", "difficulty": "medium",
        "title": "Rolling Mean",
        "tags": ["pandas"],
        "description": "Return a Series that is the rolling mean of values with the given window (min_periods=1).",
        "examples": "rolling_mean(s, 2)",
        "hint": "s.rolling(window, min_periods=1).mean()",
        "syntax_hint": "s.rolling(window, min_periods=1).mean()",
        "signature": "def rolling_mean(s, window: int):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    s = pd.Series([1, 2, 3, 4])\n"
            "    out = rolling_mean(s, 2)\n"
            "    assert abs(out.iloc[1] - 1.5) < 0.001\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def rolling_mean(s, window: int):\n"
            "    return s.rolling(window, min_periods=1).mean()\n"
        ),
    },
    {
        "slug": "12_pivot_sum",
        "track": "pandas", "difficulty": "hard",
        "title": "Pivot Table Sum",
        "tags": ["pandas", "pivot"],
        "description": "Pivot df with index='dept', columns='month', values='sales', aggfunc='sum'.",
        "examples": "pivot_sales(df) -> pivoted frame",
        "hint": "df.pivot_table(index='dept', columns='month', values='sales', aggfunc='sum')",
        "syntax_hint": "df.pivot_table(..., fill_value=0)",
        "signature": "def pivot_sales(df):\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    import pandas as pd\n"
            "    df = pd.DataFrame({\n"
            "        'dept': ['a', 'a', 'b'],\n"
            "        'month': ['jan', 'feb', 'jan'],\n"
            "        'sales': [10, 20, 5],\n"
            "    })\n"
            "    out = pivot_sales(df)\n"
            "    assert out.loc['a', 'jan'] == 10\n"
            "    assert out.loc['b', 'jan'] == 5\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def pivot_sales(df):\n"
            "    return df.pivot_table(\n"
            "        index='dept', columns='month', values='sales', aggfunc='sum', fill_value=0\n"
            "    )\n"
        ),
    },
    # --- rich ---
    {
        "slug": "09_text_pad",
        "track": "rich", "difficulty": "easy",
        "title": "Pad Text",
        "tags": ["rich", "text"],
        "description": "Return a rich.text.Text with the string padded to width with spaces on the right.",
        "examples": "pad_text('hi', 5) -> Text 'hi   '",
        "hint": "Text(s.ljust(width))",
        "syntax_hint": "from rich.text import Text; Text(s.ljust(width))",
        "signature": "def pad_text(s: str, width: int) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.text import Text\n"
            "    t = pad_text('hi', 5)\n"
            "    assert isinstance(t, Text)\n"
            "    assert str(t) == 'hi   '\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.text import Text\n\n"
            "def pad_text(s: str, width: int) -> Text:\n"
            "    return Text(s.ljust(width))\n"
        ),
    },
    {
        "slug": "10_rule_line",
        "track": "rich", "difficulty": "easy",
        "title": "Horizontal Rule",
        "tags": ["rich", "rule"],
        "description": "Return a rich.rule.Rule with the given title.",
        "examples": "rule('Section') -> Rule",
        "hint": "Rule(title)",
        "syntax_hint": "from rich.rule import Rule; Rule(title)",
        "signature": "def rule(title: str) -> object:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    from rich.rule import Rule\n"
            "    r = rule('Section')\n"
            "    assert isinstance(r, Rule)\n"
            "    assert r.title == 'Section'\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "from rich.rule import Rule\n\n"
            "def rule(title: str) -> Rule:\n"
            "    return Rule(title)\n"
        ),
    },
    {
        "slug": "11_align_columns",
        "track": "rich", "difficulty": "medium",
        "title": "Aligned Column Text",
        "tags": ["rich"],
        "description": "Given rows of strings, return one line with columns left-aligned in widths.",
        "examples": "format_row(['a','bb'], [3,3]) -> 'a  bb '",
        "hint": "str.ljust for each cell.",
        "syntax_hint": "''.join(cell.ljust(w) for cell, w in zip(cells, widths))",
        "signature": "def format_row(cells: list[str], widths: list[int]) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert format_row(['a', 'bb'], [3, 3]) == 'a  bb '\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def format_row(cells: list[str], widths: list[int]) -> str:\n"
            "    return ''.join(c.ljust(w) for c, w in zip(cells, widths))\n"
        ),
    },
    {
        "slug": "12_markup_escape",
        "track": "rich", "difficulty": "hard",
        "title": "Escape Rich Markup",
        "tags": ["rich"],
        "description": "Escape [ and ] in user text for safe rich markup by replacing with \\\\[ and \\\\].",
        "examples": 'escape_markup("[bold]") -> "\\\\[bold\\\\]"',
        "hint": "Replace [ with \\\\[ and ] with \\\\]",
        "syntax_hint": "s.replace('[', '\\\\[').replace(']', '\\\\]')",
        "signature": "def escape_markup(s: str) -> str:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert escape_markup("[bold]") == "\\\\[bold\\\\]"\n'
            '    assert escape_markup("plain") == "plain"\n'
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "def escape_markup(s: str) -> str:\n"
            "    return s.replace('[', '\\\\[').replace(']', '\\\\]')\n"
        ),
    },
    # --- sqlite ---
    {
        "slug": "09_join_users_orders",
        "track": "sqlite", "difficulty": "medium",
        "title": "Join Users and Orders",
        "tags": ["sqlite", "join"],
        "description": "In-memory DB: users(id,name), orders(user_id,amount). Insert data and return (name, total_amount) per user.",
        "examples": "totals([('a',10),('a',5),('b',3)]) -> [('a',15),('b',3)]",
        "hint": "JOIN + GROUP BY + SUM.",
        "syntax_hint": "SELECT u.name, SUM(o.amount) ... GROUP BY u.id",
        "signature": "def totals(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    out = totals([('a', 10), ('a', 5), ('b', 3)])\n"
            "    assert sorted(out) == [('a', 15.0), ('b', 3.0)]\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def totals(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\n"
            "    conn.execute('CREATE TABLE orders (user_id INTEGER, amount REAL)')\n"
            "    name_to_id = {}\n"
            "    for name, amount in rows:\n"
            "        if name not in name_to_id:\n"
            "            cur = conn.execute('INSERT INTO users (name) VALUES (?)', (name,))\n"
            "            name_to_id[name] = cur.lastrowid\n"
            "        conn.execute('INSERT INTO orders VALUES (?, ?)', (name_to_id[name], amount))\n"
            "    q = '''SELECT u.name, SUM(o.amount) FROM users u\n"
            "           JOIN orders o ON u.id = o.user_id GROUP BY u.name ORDER BY u.name'''\n"
            "    result = conn.execute(q).fetchall()\n"
            "    conn.close()\n"
            "    return [(r[0], float(r[1])) for r in result]\n"
        ),
    },
    {
        "slug": "10_exists_subquery",
        "track": "sqlite", "difficulty": "hard",
        "title": "EXISTS Subquery",
        "tags": ["sqlite"],
        "description": "Given names, insert into users and return names that have at least one order.",
        "examples": "with_orders([('a',True),('b',False)]) -> ['a']",
        "hint": "WHERE EXISTS (SELECT 1 FROM orders ...).",
        "syntax_hint": "SELECT name FROM users u WHERE EXISTS (...)",
        "signature": "def with_orders(entries: list[tuple[str, bool]]) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert with_orders([('a', True), ('b', False)]) == ['a']\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def with_orders(entries: list[tuple[str, bool]]) -> list[str]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')\n"
            "    conn.execute('CREATE TABLE orders (user_id INTEGER)')\n"
            "    for name, has_order in entries:\n"
            "        cur = conn.execute('INSERT INTO users (name) VALUES (?)', (name,))\n"
            "        uid = cur.lastrowid\n"
            "        if has_order:\n"
            "            conn.execute('INSERT INTO orders (user_id) VALUES (?)', (uid,))\n"
            "    q = '''SELECT name FROM users u\n"
            "           WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id)\n"
            "           ORDER BY name'''\n"
            "    rows = [r[0] for r in conn.execute(q).fetchall()]\n"
            "    conn.close()\n"
            "    return rows\n"
        ),
    },
    {
        "slug": "11_like_search",
        "track": "sqlite", "difficulty": "easy",
        "title": "LIKE Search",
        "tags": ["sqlite"],
        "description": "Insert words into a words(name) table and return names matching LIKE pattern.",
        "examples": 'search(["cat","cart","dog"], "ca%") -> ["cat","cart"]',
        "hint": "SELECT ... WHERE name LIKE ?",
        "syntax_hint": "conn.execute('SELECT name FROM words WHERE name LIKE ?', (pat,))",
        "signature": "def search(words: list[str], pattern: str) -> list[str]:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            '    assert search(["cat", "cart", "dog"], "ca%") == ["cart", "cat"]\n'
            "    assert search([], 'a%') == []\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def search(words: list[str], pattern: str) -> list[str]:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE words (name TEXT)')\n"
            "    conn.executemany('INSERT INTO words VALUES (?)', [(w,) for w in words])\n"
            "    rows = conn.execute('SELECT name FROM words WHERE name LIKE ? ORDER BY name', (pattern,)).fetchall()\n"
            "    conn.close()\n"
            "    return [r[0] for r in rows]\n"
        ),
    },
    {
        "slug": "12_replace_upsert",
        "track": "sqlite", "difficulty": "medium",
        "title": "REPLACE Upsert",
        "tags": ["sqlite"],
        "description": "Use REPLACE INTO kv(k,v) to set keys; return final value for key after all ops.",
        "examples": "upsert_get([('a','1'),('a','2')], 'a') -> '2'",
        "hint": "REPLACE INTO is SQLite upsert by primary key.",
        "syntax_hint": "REPLACE INTO kv VALUES (?, ?)",
        "signature": "def upsert_get(ops: list[tuple[str, str]], key: str) -> str | None:\n    pass",
        "tests": (
            "def run_tests() -> None:\n"
            "    assert upsert_get([('a', '1'), ('a', '2')], 'a') == '2'\n"
            "    assert upsert_get([], 'x') is None\n"
            '    print("All tests passed.")\n'
        ),
        "solution": (
            "import sqlite3\n\n"
            "def upsert_get(ops: list[tuple[str, str]], key: str) -> str | None:\n"
            "    conn = sqlite3.connect(':memory:')\n"
            "    conn.execute('CREATE TABLE kv (k TEXT PRIMARY KEY, v TEXT)')\n"
            "    for k, v in ops:\n"
            "        conn.execute('REPLACE INTO kv VALUES (?, ?)', (k, v))\n"
            "    row = conn.execute('SELECT v FROM kv WHERE k=?', (key,)).fetchone()\n"
            "    conn.close()\n"
            "    return row[0] if row else None\n"
        ),
    },
]

LESSONS: list[dict] = []
