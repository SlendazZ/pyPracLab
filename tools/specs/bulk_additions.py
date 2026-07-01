"""Bulk problem additions (122 problems: 228 -> 350)."""

PROBLEMS = [{'slug': '54_remove_element',
  'track': 'algorithms',
  'difficulty': 'easy',
  'title': 'Remove Element',
  'tags': ['array', 'two-pointers'],
  'description': 'Return a new list with all occurrences of val removed, preserving order of remaining elements.',
  'examples': 'remove_val([3,2,2,3], 3) -> [2,2]',
  'hint': 'Scan and keep elements not equal to val.',
  'syntax_hint': 'return [x for x in nums if x != val]',
  'signature': 'def remove_val(nums: list[int], val: int) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert remove_val([3, 2, 2, 3], 3) == [2, 2]\n'
           '    assert remove_val([0, 1, 2, 2, 3, 0, 4, 2], 2) == [0, 1, 3, 0, 4]\n'
           '    assert remove_val([], 1) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'def remove_val(nums: list[int], val: int) -> list[int]:\n    return [x for x in nums if x != val]\n'},
 {'slug': '55_sort_colors',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Sort Colors',
  'tags': ['array', 'two-pointers'],
  'description': 'Sort a list of 0s, 1s, and 2s in-place style — return a new sorted list.',
  'examples': 'sort_colors([2,0,2,1,1,0]) -> [0,0,1,1,2,2]',
  'hint': 'Dutch national flag with three pointers low, mid, high.',
  'syntax_hint': 'while mid <= high: swap 0 to front, 2 to back',
  'signature': 'def sort_colors(nums: list[int]) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]\n'
           '    assert sort_colors([2, 0, 1]) == [0, 1, 2]\n'
           '    assert sort_colors([]) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'def sort_colors(nums: list[int]) -> list[int]:\n'
              '    arr = nums[:]\n'
              '    lo, mid, hi = 0, 0, len(arr) - 1\n'
              '    while mid <= hi:\n'
              '        if arr[mid] == 0:\n'
              '            arr[lo], arr[mid] = arr[mid], arr[lo]\n'
              '            lo += 1; mid += 1\n'
              '        elif arr[mid] == 1:\n'
              '            mid += 1\n'
              '        else:\n'
              '            arr[mid], arr[hi] = arr[hi], arr[mid]\n'
              '            hi -= 1\n'
              '    return arr\n'},
 {'slug': '56_find_anagrams',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Find All Anagrams',
  'tags': ['sliding-window', 'string'],
  'description': 'Given strings s and p, return sorted list of start indices in s where an anagram of p begins.',
  'examples': 'find_anagrams("cbaebabacd", "abc") -> [0, 6]',
  'hint': 'Fixed window of len(p); compare character counts.',
  'syntax_hint': 'from collections import Counter; need = Counter(p)',
  'signature': 'def find_anagrams(s: str, p: str) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert find_anagrams("cbaebabacd", "abc") == [0, 6]\n'
           '    assert find_anagrams("abab", "ab") == [0, 1, 2]\n'
           '    assert find_anagrams("aaaa", "aa") == [0, 1, 2]\n'
           '    print("All tests passed.")\n',
  'solution': 'from collections import Counter\n'
              '\n'
              'def find_anagrams(s: str, p: str) -> list[int]:\n'
              '    if len(p) > len(s):\n'
              '        return []\n'
              '    need = Counter(p)\n'
              '    have = Counter(s[:len(p)])\n'
              '    result = []\n'
              '    if have == need:\n'
              '        result.append(0)\n'
              '    for i in range(len(p), len(s)):\n'
              '        have[s[i]] += 1\n'
              '        have[s[i - len(p)]] -= 1\n'
              '        if have[s[i - len(p)]] == 0:\n'
              '            del have[s[i - len(p)]]\n'
              '        if have == need:\n'
              '            result.append(i - len(p) + 1)\n'
              '    return result\n'},
 {'slug': '57_permutation_in_string',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Permutation in String',
  'tags': ['sliding-window', 'string'],
  'description': 'Return True if s2 contains a substring that is a permutation of s1.',
  'examples': 'check_inclusion("ab", "eidbaooo") -> True',
  'hint': 'Same fixed-window count technique as anagram finder.',
  'syntax_hint': 'window size len(s1); compare Counter each step',
  'signature': 'def check_inclusion(s1: str, s2: str) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert check_inclusion("ab", "eidbaooo") is True\n'
           '    assert check_inclusion("ab", "eidboaoo") is False\n'
           '    assert check_inclusion("a", "a") is True\n'
           '    print("All tests passed.")\n',
  'solution': 'from collections import Counter\n'
              '\n'
              'def check_inclusion(s1: str, s2: str) -> bool:\n'
              '    n, m = len(s1), len(s2)\n'
              '    if n > m:\n'
              '        return False\n'
              '    need = Counter(s1)\n'
              '    have = Counter(s2[:n])\n'
              '    if have == need:\n'
              '        return True\n'
              '    for i in range(n, m):\n'
              '        have[s2[i]] += 1\n'
              '        have[s2[i - n]] -= 1\n'
              '        if have[s2[i - n]] == 0:\n'
              '            del have[s2[i - n]]\n'
              '        if have == need:\n'
              '            return True\n'
              '    return False\n'},
 {'slug': '58_char_replacement',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Longest Repeating Character Replacement',
  'tags': ['sliding-window', 'string'],
  'description': 'Given string s and int k, return length of longest substring containing same letter after at most k '
                 'replacements.',
  'examples': 'character_replacement("ABAB", 2) -> 4',
  'hint': 'Expand window; track max char frequency; shrink when window - max_freq > k.',
  'syntax_hint': 'max_freq = max(counts.values()); while right-left+1-max_freq > k: shrink',
  'signature': 'def character_replacement(s: str, k: int) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert character_replacement("ABAB", 2) == 4\n'
           '    assert character_replacement("AABABBA", 1) == 4\n'
           '    assert character_replacement("AAAA", 0) == 4\n'
           '    print("All tests passed.")\n',
  'solution': 'def character_replacement(s: str, k: int) -> int:\n'
              '    counts: dict[str, int] = {}\n'
              '    left = max_freq = best = 0\n'
              '    for right, ch in enumerate(s):\n'
              '        counts[ch] = counts.get(ch, 0) + 1\n'
              '        max_freq = max(max_freq, counts[ch])\n'
              '        while (right - left + 1) - max_freq > k:\n'
              '            counts[s[left]] -= 1\n'
              '            left += 1\n'
              '        best = max(best, right - left + 1)\n'
              '    return best\n'},
 {'slug': '59_meeting_rooms',
  'track': 'algorithms',
  'difficulty': 'easy',
  'title': 'Meeting Rooms',
  'tags': ['intervals', 'sorting'],
  'description': 'Given list of [start, end] meetings, return True if a person can attend all (no overlap).',
  'examples': 'can_attend([[0,30],[5,10],[15,20]]) -> False',
  'hint': 'Sort by start; check each start >= previous end.',
  'syntax_hint': 'intervals.sort(); for s,e in intervals: if s < prev_end: return False',
  'signature': 'def can_attend(intervals: list[list[int]]) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert can_attend([[0, 30], [5, 10], [15, 20]]) is False\n'
           '    assert can_attend([[7, 10], [2, 4]]) is True\n'
           '    assert can_attend([]) is True\n'
           '    print("All tests passed.")\n',
  'solution': 'def can_attend(intervals: list[list[int]]) -> bool:\n'
              '    intervals.sort(key=lambda x: x[0])\n'
              '    for i in range(1, len(intervals)):\n'
              '        if intervals[i][0] < intervals[i - 1][1]:\n'
              '            return False\n'
              '    return True\n'},
 {'slug': '60_meeting_rooms_ii',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Meeting Rooms II',
  'tags': ['intervals', 'heap'],
  'description': 'Return minimum number of conference rooms required.',
  'examples': 'min_rooms([[0,30],[5,10],[15,20]]) -> 2',
  'hint': 'Sort starts; min-heap of end times; pop ends <= new start.',
  'syntax_hint': 'import heapq; heapq.heappush(heap, end); heapq.heappop(heap)',
  'signature': 'def min_rooms(intervals: list[list[int]]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert min_rooms([[0, 30], [5, 10], [15, 20]]) == 2\n'
           '    assert min_rooms([[7, 10], [2, 4]]) == 1\n'
           '    assert min_rooms([[1, 5], [2, 6], [3, 7]]) == 3\n'
           '    print("All tests passed.")\n',
  'solution': 'import heapq\n'
              '\n'
              'def min_rooms(intervals: list[list[int]]) -> int:\n'
              '    if not intervals:\n'
              '        return 0\n'
              '    intervals.sort(key=lambda x: x[0])\n'
              '    heap: list[int] = []\n'
              '    heapq.heappush(heap, intervals[0][1])\n'
              '    for i in range(1, len(intervals)):\n'
              '        if intervals[i][0] >= heap[0]:\n'
              '            heapq.heappop(heap)\n'
              '        heapq.heappush(heap, intervals[i][1])\n'
              '    return len(heap)\n'},
 {'slug': '61_house_robber',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'House Robber',
  'tags': ['dp', 'array'],
  'description': 'Rob non-adjacent houses for max money; return maximum loot.',
  'examples': 'rob([2,7,9,3,1]) -> 12',
  'hint': 'DP: at each house take max(skip, take+prev_skip).',
  'syntax_hint': 'prev2, prev1 = 0, 0; for x: prev2, prev1 = prev1, max(prev1, prev2+x)',
  'signature': 'def rob(nums: list[int]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert rob([2, 7, 9, 3, 1]) == 12\n'
           '    assert rob([1, 2, 3, 1]) == 4\n'
           '    assert rob([0]) == 0\n'
           '    print("All tests passed.")\n',
  'solution': 'def rob(nums: list[int]) -> int:\n'
              '    prev2 = prev1 = 0\n'
              '    for x in nums:\n'
              '        prev2, prev1 = prev1, max(prev1, prev2 + x)\n'
              '    return prev1\n'},
 {'slug': '62_word_break',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Word Break',
  'tags': ['dp', 'string'],
  'description': 'Return True if s can be segmented into space-separated words from the dictionary.',
  'examples': 'word_break("leetcode", ["leet","code"]) -> True',
  'hint': 'dp[i] = any dp[j] and s[j:i] in word_set for j < i.',
  'syntax_hint': 'dp = [False]*(n+1); dp[0]=True',
  'signature': 'def word_break(s: str, word_dict: list[str]) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert word_break("leetcode", ["leet", "code"]) is True\n'
           '    assert word_break("applepenapple", ["apple", "pen"]) is True\n'
           '    assert word_break("catsandog", ["cats","dog","sand","and","cat"]) is False\n'
           '    print("All tests passed.")\n',
  'solution': 'def word_break(s: str, word_dict: list[str]) -> bool:\n'
              '    words = set(word_dict)\n'
              '    n = len(s)\n'
              '    dp = [False] * (n + 1)\n'
              '    dp[0] = True\n'
              '    for i in range(1, n + 1):\n'
              '        for j in range(i):\n'
              '            if dp[j] and s[j:i] in words:\n'
              '                dp[i] = True\n'
              '                break\n'
              '    return dp[n]\n'},
 {'slug': '63_unique_paths',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Unique Paths',
  'tags': ['dp', 'grid'],
  'description': 'Robot at top-left of m x n grid; only move right/down. Return number of paths to bottom-right.',
  'examples': 'unique_paths(3, 7) -> 28',
  'hint': 'dp[r][c] = dp[r-1][c] + dp[r][c-1]; first row/col are 1.',
  'syntax_hint': 'dp = [[1]*n for _ in range(m)]',
  'signature': 'def unique_paths(m: int, n: int) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert unique_paths(3, 7) == 28\n'
           '    assert unique_paths(3, 2) == 3\n'
           '    assert unique_paths(1, 1) == 1\n'
           '    print("All tests passed.")\n',
  'solution': 'def unique_paths(m: int, n: int) -> int:\n'
              '    dp = [[1] * n for _ in range(m)]\n'
              '    for r in range(1, m):\n'
              '        for c in range(1, n):\n'
              '            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]\n'
              '    return dp[m - 1][n - 1]\n'},
 {'slug': '64_decode_ways',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Decode Ways',
  'tags': ['dp', 'string'],
  'description': 'A=1..Z=26 mapping; count how many ways to decode digit string.',
  'examples': 'num_decodings("12") -> 2',
  'hint': 'dp[i] += dp[i-1] if valid single; += dp[i-2] if valid pair.',
  'syntax_hint': "if s[i-1] != '0': dp[i] += dp[i-1]",
  'signature': 'def num_decodings(s: str) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert num_decodings("12") == 2\n'
           '    assert num_decodings("226") == 3\n'
           '    assert num_decodings("06") == 0\n'
           '    print("All tests passed.")\n',
  'solution': 'def num_decodings(s: str) -> int:\n'
              "    if not s or s[0] == '0':\n"
              '        return 0\n'
              '    n = len(s)\n'
              '    dp = [0] * (n + 1)\n'
              '    dp[0] = dp[1] = 1\n'
              '    for i in range(2, n + 1):\n'
              "        if s[i - 1] != '0':\n"
              '            dp[i] += dp[i - 1]\n'
              '        two = int(s[i - 2:i])\n'
              '        if 10 <= two <= 26:\n'
              '            dp[i] += dp[i - 2]\n'
              '    return dp[n]\n'},
 {'slug': '65_rotting_oranges',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Rotting Oranges',
  'tags': ['bfs', 'grid'],
  'description': 'Grid: 2=rotten, 1=fresh, 0=empty. Each minute rot spreads to adjacent fresh. Return minutes to rot '
                 'all or -1.',
  'examples': 'oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) -> 4',
  'hint': 'Multi-source BFS from all 2s; track minutes and fresh count.',
  'syntax_hint': 'from collections import deque; queue all rotten cells',
  'signature': 'def oranges_rotting(grid: list[list[int]]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4\n'
           '    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1\n'
           '    assert oranges_rotting([[0, 2]]) == 0\n'
           '    print("All tests passed.")\n',
  'solution': 'from collections import deque\n'
              '\n'
              'def oranges_rotting(grid: list[list[int]]) -> int:\n'
              '    if not grid or not grid[0]:\n'
              '        return 0\n'
              '    rows, cols = len(grid), len(grid[0])\n'
              '    q = deque()\n'
              '    fresh = 0\n'
              '    for r in range(rows):\n'
              '        for c in range(cols):\n'
              '            if grid[r][c] == 2:\n'
              '                q.append((r, c, 0))\n'
              '            elif grid[r][c] == 1:\n'
              '                fresh += 1\n'
              '    minutes = 0\n'
              '    while q:\n'
              '        r, c, minutes = q.popleft()\n'
              '        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):\n'
              '            nr, nc = r + dr, c + dc\n'
              '            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:\n'
              '                grid[nr][nc] = 2\n'
              '                fresh -= 1\n'
              '                q.append((nr, nc, minutes + 1))\n'
              '    return minutes if fresh == 0 else -1\n'},
 {'slug': '66_course_schedule',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Course Schedule',
  'tags': ['graph', 'dfs'],
  'description': 'prerequisites[i]=[a,b] means take b before a. Return True if all courses can finish.',
  'examples': 'can_finish(2, [[1,0]]) -> True',
  'hint': 'Detect cycle in directed graph via DFS three-color or Kahn topo.',
  'syntax_hint': 'build adjacency; dfs detect back edge',
  'signature': 'def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert can_finish(2, [[1, 0]]) is True\n'
           '    assert can_finish(2, [[1, 0], [0, 1]]) is False\n'
           '    assert can_finish(3, [[1, 0], [2, 0]]) is True\n'
           '    print("All tests passed.")\n',
  'solution': 'def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:\n'
              '    graph: dict[int, list[int]] = {i: [] for i in range(num_courses)}\n'
              '    for a, b in prerequisites:\n'
              '        graph[b].append(a)\n'
              '    state = [0] * num_courses\n'
              '    def dfs(node: int) -> bool:\n'
              '        if state[node] == 1:\n'
              '            return False\n'
              '        if state[node] == 2:\n'
              '            return True\n'
              '        state[node] = 1\n'
              '        for nxt in graph[node]:\n'
              '            if not dfs(nxt):\n'
              '                return False\n'
              '        state[node] = 2\n'
              '        return True\n'
              '    return all(dfs(i) for i in range(num_courses))\n'},
 {'slug': '67_spiral_matrix',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Spiral Matrix',
  'tags': ['matrix', 'simulation'],
  'description': 'Return elements of m x n matrix in spiral order.',
  'examples': 'spiral_order([[1,2,3],[4,5,6],[7,8,9]]) -> [1,2,3,6,9,8,7,4,5]',
  'hint': 'Shrink boundaries top/bottom/left/right while traversing.',
  'syntax_hint': 'while top <= bottom and left <= right: go right, down, left, up',
  'signature': 'def spiral_order(matrix: list[list[int]]) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]\n'
           '    assert spiral_order([[1,2,3,4]]) == [1,2,3,4]\n'
           '    assert spiral_order([]) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'def spiral_order(matrix: list[list[int]]) -> list[int]:\n'
              '    if not matrix or not matrix[0]:\n'
              '        return []\n'
              '    top, bottom = 0, len(matrix) - 1\n'
              '    left, right = 0, len(matrix[0]) - 1\n'
              '    out: list[int] = []\n'
              '    while top <= bottom and left <= right:\n'
              '        for c in range(left, right + 1):\n'
              '            out.append(matrix[top][c])\n'
              '        top += 1\n'
              '        for r in range(top, bottom + 1):\n'
              '            out.append(matrix[r][right])\n'
              '        right -= 1\n'
              '        if top <= bottom:\n'
              '            for c in range(right, left - 1, -1):\n'
              '                out.append(matrix[bottom][c])\n'
              '            bottom -= 1\n'
              '        if left <= right:\n'
              '            for r in range(bottom, top - 1, -1):\n'
              '                out.append(matrix[r][left])\n'
              '            left += 1\n'
              '    return out\n'},
 {'slug': '68_set_zeroes',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Set Matrix Zeroes',
  'tags': ['matrix'],
  'description': 'If an element is 0, set its entire row and column to 0. Return the new matrix.',
  'examples': 'set_zeroes([[1,1,0],[1,1,1]]) -> [[0,0,0],[1,1,0]]',
  'hint': 'Track zero rows/cols in sets or use first row/col as markers.',
  'syntax_hint': 'zero_rows, zero_cols = set(), set()',
  'signature': 'def set_zeroes(matrix: list[list[int]]) -> list[list[int]]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert set_zeroes([[1,1,0],[1,1,1]]) == [[0,0,0],[1,1,0]]\n'
           '    assert set_zeroes([[0,1]]) == [[0,0]]\n'
           '    assert set_zeroes([[1]]) == [[1]]\n'
           '    print("All tests passed.")\n',
  'solution': 'def set_zeroes(matrix: list[list[int]]) -> list[list[int]]:\n'
              '    if not matrix:\n'
              '        return []\n'
              '    m, n = len(matrix), len(matrix[0])\n'
              '    mat = [row[:] for row in matrix]\n'
              '    zr, zc = set(), set()\n'
              '    for r in range(m):\n'
              '        for c in range(n):\n'
              '            if mat[r][c] == 0:\n'
              '                zr.add(r); zc.add(c)\n'
              '    for r in zr:\n'
              '        for c in range(n):\n'
              '            mat[r][c] = 0\n'
              '    for c in zc:\n'
              '        for r in range(m):\n'
              '            mat[r][c] = 0\n'
              '    return mat\n'},
 {'slug': '69_count_bits',
  'track': 'algorithms',
  'difficulty': 'easy',
  'title': 'Counting Bits',
  'tags': ['dp', 'bit-manipulation'],
  'description': 'For n, return list ans where ans[i] is number of 1 bits in i (0..n).',
  'examples': 'count_bits(5) -> [0,1,1,2,1,2]',
  'hint': 'ans[i] = ans[i >> 1] + (i & 1).',
  'syntax_hint': 'for i in range(1, n+1): ans[i] = ans[i>>1] + (i&1)',
  'signature': 'def count_bits(n: int) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert count_bits(5) == [0, 1, 1, 2, 1, 2]\n'
           '    assert count_bits(0) == [0]\n'
           '    assert count_bits(2) == [0, 1, 1]\n'
           '    print("All tests passed.")\n',
  'solution': 'def count_bits(n: int) -> list[int]:\n'
              '    ans = [0] * (n + 1)\n'
              '    for i in range(1, n + 1):\n'
              '        ans[i] = ans[i >> 1] + (i & 1)\n'
              '    return ans\n'},
 {'slug': '70_find_duplicate',
  'track': 'algorithms',
  'difficulty': 'easy',
  'title': 'Find Duplicate Number',
  'tags': ['array', 'two-pointers'],
  'description': 'Array of n+1 integers in range 1..n with exactly one duplicate. Return the duplicate.',
  'examples': 'find_duplicate([1,3,4,2,2]) -> 2',
  'hint': 'Treat as linked list cycle (Floyd); or binary search on value range.',
  'syntax_hint': 'slow=fast=nums[0]; cycle detection',
  'signature': 'def find_duplicate(nums: list[int]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert find_duplicate([1, 3, 4, 2, 2]) == 2\n'
           '    assert find_duplicate([3, 1, 3, 4, 2]) == 3\n'
           '    assert find_duplicate([1, 1]) == 1\n'
           '    print("All tests passed.")\n',
  'solution': 'def find_duplicate(nums: list[int]) -> int:\n'
              '    slow = fast = nums[0]\n'
              '    while True:\n'
              '        slow = nums[slow]\n'
              '        fast = nums[nums[fast]]\n'
              '        if slow == fast:\n'
              '            break\n'
              '    slow = nums[0]\n'
              '    while slow != fast:\n'
              '        slow = nums[slow]\n'
              '        fast = nums[fast]\n'
              '    return slow\n'},
 {'slug': '71_eval_rpn',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Evaluate Reverse Polish Notation',
  'tags': ['stack', 'math'],
  'description': 'Evaluate valid RPN expression with + - * / on integers.',
  'examples': 'eval_rpn(["2","1","+","3","*"]) -> 9',
  'hint': 'Stack numbers; on operator pop two and push result.',
  'syntax_hint': 'stack = []; int(token) push else apply op',
  'signature': 'def eval_rpn(tokens: list[str]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert eval_rpn(["2","1","+","3","*"]) == 9\n'
           '    assert eval_rpn(["4","13","5","/","+"]) == 6\n'
           '    assert eval_rpn(["10"]) == 10\n'
           '    print("All tests passed.")\n',
  'solution': 'def eval_rpn(tokens: list[str]) -> int:\n'
              '    stack: list[int] = []\n'
              "    ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,\n"
              "           '*': lambda a, b: a * b, '/': lambda a, b: int(a / b)}\n"
              '    for tok in tokens:\n'
              '        if tok in ops:\n'
              '            b, a = stack.pop(), stack.pop()\n'
              '            stack.append(ops[tok](a, b))\n'
              '        else:\n'
              '            stack.append(int(tok))\n'
              '    return stack[0]\n'},
 {'slug': '72_asteroid_collision',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Asteroid Collision',
  'tags': ['stack', 'simulation'],
  'description': 'Positive moves right, negative left; same size destroy each other. Return final asteroids.',
  'examples': 'asteroid_collision([5,10,-5]) -> [5,10]',
  'hint': 'Stack; negative asteroid collides with stack top while applicable.',
  'syntax_hint': 'while stack and x < 0 < stack[-1]: compare sizes',
  'signature': 'def asteroid_collision(asteroids: list[int]) -> list[int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert asteroid_collision([5, 10, -5]) == [5, 10]\n'
           '    assert asteroid_collision([8, -8]) == []\n'
           '    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]\n'
           '    print("All tests passed.")\n',
  'solution': 'def asteroid_collision(asteroids: list[int]) -> list[int]:\n'
              '    stack: list[int] = []\n'
              '    for x in asteroids:\n'
              '        while stack and x < 0 < stack[-1]:\n'
              '            if stack[-1] < -x:\n'
              '                stack.pop()\n'
              '                continue\n'
              '            if stack[-1] == -x:\n'
              '                stack.pop()\n'
              '            x = 0\n'
              '            break\n'
              '        if x:\n'
              '            stack.append(x)\n'
              '    return stack\n'},
 {'slug': '73_insert_interval',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Insert Interval',
  'tags': ['intervals'],
  'description': 'Insert new interval into sorted non-overlapping intervals; merge overlaps.',
  'examples': 'insert([[1,3],[6,9]], [2,5]) -> [[1,5],[6,9]]',
  'hint': 'Add new; merge overlapping by expanding end.',
  'syntax_hint': 'result = []; for interval: merge or append',
  'signature': 'def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]\n'
           '    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]\n'
           '    assert insert([], [5,7]) == [[5,7]]\n'
           '    print("All tests passed.")\n',
  'solution': 'def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:\n'
              '    result: list[list[int]] = []\n'
              '    i = 0\n'
              '    n = len(intervals)\n'
              '    while i < n and intervals[i][1] < new[0]:\n'
              '        result.append(intervals[i]); i += 1\n'
              '    while i < n and intervals[i][0] <= new[1]:\n'
              '        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1\n'
              '    result.append(new)\n'
              '    result.extend(intervals[i:])\n'
              '    return result\n'},
 {'slug': '74_word_search',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Word Search',
  'tags': ['backtracking', 'grid'],
  'description': '2D board of chars and word; return True if word exists by adjacent cells (no reuse).',
  'examples': 'exist([["A","B"],["C","D"]], "AB") -> True',
  'hint': 'DFS from each cell; mark visited temporarily.',
  'syntax_hint': 'def dfs(r,c,idx): backtrack four directions',
  'signature': 'def exist(board: list[list[str]], word: str) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert exist([["A","B"],["C","D"]], "AB") is True\n'
           '    assert exist([["A","B"],["C","D"]], "AD") is False\n'
           '    assert exist([["A"]], "A") is True\n'
           '    print("All tests passed.")\n',
  'solution': 'def exist(board: list[list[str]], word: str) -> bool:\n'
              '    rows, cols = len(board), len(board[0])\n'
              '    def dfs(r: int, c: int, idx: int) -> bool:\n'
              '        if idx == len(word):\n'
              '            return True\n'
              '        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:\n'
              '            return False\n'
              '        ch = board[r][c]\n'
              "        board[r][c] = '#'\n"
              '        found = any(dfs(r+dr, c+dc, idx+1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))\n'
              '        board[r][c] = ch\n'
              '        return found\n'
              '    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))\n'},
 {'slug': '75_max_consecutive_ones_iii',
  'track': 'algorithms',
  'difficulty': 'medium',
  'title': 'Max Consecutive Ones III',
  'tags': ['sliding-window', 'array'],
  'description': 'Binary array and k flips allowed; return max length of subarray of all 1s after at most k flips.',
  'examples': 'longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) -> 6',
  'hint': 'Sliding window; shrink when zeros in window > k.',
  'syntax_hint': 'while zeros > k: shrink left',
  'signature': 'def longest_ones(nums: list[int], k: int) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6\n'
           '    assert longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10\n'
           '    assert longest_ones([1], 0) == 1\n'
           '    print("All tests passed.")\n',
  'solution': 'def longest_ones(nums: list[int], k: int) -> int:\n'
              '    left = zeros = best = 0\n'
              '    for right, x in enumerate(nums):\n'
              '        if x == 0:\n'
              '            zeros += 1\n'
              '        while zeros > k:\n'
              '            if nums[left] == 0:\n'
              '                zeros -= 1\n'
              '            left += 1\n'
              '        best = max(best, right - left + 1)\n'
              '    return best\n'},
 {'slug': '76_climbing_stairs_var',
  'track': 'algorithms',
  'difficulty': 'easy',
  'title': 'Min Cost Climbing Stairs',
  'tags': ['dp', 'array'],
  'description': 'Each step has cost; can climb 1 or 2 steps from index 0 or 1. Return min cost to reach top beyond '
                 'last index.',
  'examples': 'min_cost([10,15,20]) -> 15',
  'hint': 'Same recurrence as climbing stairs but take min not sum.',
  'syntax_hint': 'a, b = 0, 0; for c in cost: a, b = b, min(a,b)+c',
  'signature': 'def min_cost(cost: list[int]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert min_cost([10, 15, 20]) == 15\n'
           '    assert min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6\n'
           '    assert min_cost([0, 0, 0, 1]) == 0\n'
           '    print("All tests passed.")\n',
  'solution': 'def min_cost(cost: list[int]) -> int:\n'
              '    a = b = 0\n'
              '    for c in cost:\n'
              '        a, b = b, min(a, b) + c\n'
              '    return min(a, b)\n'},
 {'slug': '25_frozen_dataclass',
  'track': 'syntax',
  'difficulty': 'medium',
  'title': 'Frozen Dataclass',
  'tags': ['dataclass'],
  'description': 'Return a frozen dataclass Point(x, y) factory that rejects mutation.',
  'examples': 'p = make_point(1,2); p.x == 1',
  'hint': 'Use @dataclass(frozen=True).',
  'syntax_hint': '@dataclass(frozen=True)',
  'signature': 'def make_point(x: int, y: int):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    p = make_point(1, 2)\n'
           '    assert p.x == 1 and p.y == 2\n'
           '    try:\n'
           '        p.x = 3\n'
           '        raised = False\n'
           '    except Exception:\n'
           '        raised = True\n'
           '    assert raised\n'
           '    print("All tests passed.")\n',
  'solution': 'from dataclasses import dataclass\n'
              '\n'
              '@dataclass(frozen=True)\n'
              'class Point:\n'
              '    x: int\n'
              '    y: int\n'
              '\n'
              'def make_point(x: int, y: int):\n'
              '    return Point(x, y)\n'},
 {'slug': '26_enum_status',
  'track': 'syntax',
  'difficulty': 'easy',
  'title': 'Status Enum',
  'tags': ['enum'],
  'description': 'Return the Enum class Status with members PENDING, ACTIVE, DONE (values same as names).',
  'examples': "Status.ACTIVE.name == 'ACTIVE'",
  'hint': "class Status(Enum): PENDING = 'PENDING' ...",
  'syntax_hint': 'from enum import Enum',
  'signature': 'def make_status_enum():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    Status = make_status_enum()\n'
           "    assert Status.ACTIVE.name == 'ACTIVE'\n"
           "    assert Status.PENDING.value == 'PENDING'\n"
           '    assert list(Status) != []\n'
           '    print("All tests passed.")\n',
  'solution': 'from enum import Enum\n'
              '\n'
              'def make_status_enum():\n'
              '    class Status(Enum):\n'
              "        PENDING = 'PENDING'\n"
              "        ACTIVE = 'ACTIVE'\n"
              "        DONE = 'DONE'\n"
              '    return Status\n'},
 {'slug': '27_partial_application',
  'track': 'syntax',
  'difficulty': 'medium',
  'title': 'Partial Application',
  'tags': ['functools'],
  'description': 'Return a function add_n(n) that returns a function adding n to its argument.',
  'examples': 'add5 = add_n(5); add5(3) -> 8',
  'hint': 'functools.partial or closure.',
  'syntax_hint': 'def add_n(n): return lambda x: x + n',
  'signature': 'def add_n(n: int):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    add5 = add_n(5)\n'
           '    assert add5(3) == 8\n'
           '    assert add_n(0)(10) == 10\n'
           '    print("All tests passed.")\n',
  'solution': 'def add_n(n: int):\n    return lambda x: x + n\n'},
 {'slug': '28_reduce_total',
  'track': 'syntax',
  'difficulty': 'easy',
  'title': 'Reduce to Total',
  'tags': ['functools'],
  'description': 'Return the sum of a list of integers using functools.reduce.',
  'examples': 'total([1,2,3]) -> 6',
  'hint': 'functools.reduce(operator.add, nums, 0)',
  'syntax_hint': 'from functools import reduce; import operator',
  'signature': 'def total(nums: list[int]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert total([1, 2, 3]) == 6\n'
           '    assert total([]) == 0\n'
           '    assert total([5]) == 5\n'
           '    print("All tests passed.")\n',
  'solution': 'from functools import reduce\n'
              'import operator\n'
              '\n'
              'def total(nums: list[int]) -> int:\n'
              '    return reduce(operator.add, nums, 0)\n'},
 {'slug': '29_typed_dict_shape',
  'track': 'syntax',
  'difficulty': 'medium',
  'title': 'TypedDict User',
  'tags': ['typing'],
  'description': 'Given name and age, return a dict matching TypedDict User with keys name (str) and age (int).',
  'examples': "user('Ada', 36) -> {'name':'Ada','age':36}",
  'hint': "Define TypedDict User; return {'name': name, 'age': age}.",
  'syntax_hint': 'class User(TypedDict): name: str; age: int',
  'signature': 'def user(name: str, age: int) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert user('Ada', 36) == {'name': 'Ada', 'age': 36}\n"
           "    assert user('Bob', 0)['age'] == 0\n"
           '    print("All tests passed.")\n',
  'solution': 'from typing import TypedDict\n'
              '\n'
              'class User(TypedDict):\n'
              '    name: str\n'
              '    age: int\n'
              '\n'
              'def user(name: str, age: int) -> dict:\n'
              '    return User(name=name, age=age)\n'},
 {'slug': '30_pathlib_parts',
  'track': 'syntax',
  'difficulty': 'easy',
  'title': 'Path Parts',
  'tags': ['pathlib'],
  'description': 'Given a POSIX path string, return (parent, name, suffix) using pathlib.',
  'examples': "path_parts('/tmp/data.csv') -> ('/tmp', 'data.csv', '.csv')",
  'hint': 'Path(p).parent, .name, .suffix — str(parent) for compare.',
  'syntax_hint': 'from pathlib import Path; p = Path(s)',
  'signature': 'def path_parts(p: str) -> tuple[str, str, str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert path_parts('/tmp/data.csv') == ('/tmp', 'data.csv', '.csv')\n"
           "    assert path_parts('file.txt')[1] == 'file.txt'\n"
           "    assert path_parts('/a/b')[0] == '/a'\n"
           '    print("All tests passed.")\n',
  'solution': 'from pathlib import Path\n'
              '\n'
              'def path_parts(p: str) -> tuple[str, str, str]:\n'
              '    path = Path(p)\n'
              '    return str(path.parent), path.name, path.suffix\n'},
 {'slug': '31_contextlib_suppress',
  'track': 'syntax',
  'difficulty': 'easy',
  'title': 'Suppress KeyError',
  'tags': ['contextlib'],
  'description': 'Return value for key in dict d, or default if missing, using contextlib.suppress(KeyError) around '
                 'd[key].',
  'examples': "safe_get({'a':1}, 'b', 0) -> 0",
  'hint': 'with suppress(KeyError): return d[key] else default.',
  'syntax_hint': 'from contextlib import suppress',
  'signature': 'def safe_get(d: dict, key: str, default):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert safe_get({'a': 1}, 'a', 0) == 1\n"
           "    assert safe_get({'a': 1}, 'b', 0) == 0\n"
           "    assert safe_get({}, 'x', 'missing') == 'missing'\n"
           '    print("All tests passed.")\n',
  'solution': 'from contextlib import suppress\n'
              '\n'
              'def safe_get(d: dict, key: str, default):\n'
              '    with suppress(KeyError):\n'
              '        return d[key]\n'
              '    return default\n'},
 {'slug': '32_slots_class',
  'track': 'syntax',
  'difficulty': 'medium',
  'title': 'Slots Point Class',
  'tags': ['class'],
  'description': "Return a Point class with __slots__ = ('x','y') and x,y set in __init__.",
  'examples': 'P = make_point_cls(); P(1,2).x == 1',
  'hint': "class Point: __slots__ = ('x','y')",
  'syntax_hint': "__slots__ = ('x', 'y')",
  'signature': 'def make_point_cls():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    P = make_point_cls()\n'
           '    p = P(1, 2)\n'
           '    assert p.x == 1 and p.y == 2\n'
           "    assert '__slots__' in dir(P) or hasattr(P, '__slots__')\n"
           '    print("All tests passed.")\n',
  'solution': 'def make_point_cls():\n'
              '    class Point:\n'
              "        __slots__ = ('x', 'y')\n"
              '        def __init__(self, x, y):\n'
              '            self.x = x\n'
              '            self.y = y\n'
              '    return Point\n'},
 {'slug': '17_ini_parser',
  'track': 'automations',
  'difficulty': 'easy',
  'title': 'Parse INI Section',
  'tags': ['config'],
  'description': 'Parse simple INI text with one [section] and key=value lines into dict for that section.',
  'examples': "[app]\\nname=demo -> {'name':'demo'}",
  'hint': 'Split lines; on [section] start; key=value split once.',
  'syntax_hint': "line.strip(); if line.startswith('['): ...",
  'signature': 'def parse_section(text: str, section: str) -> dict[str, str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    t = '[app]\\nname=demo\\nport=80\\n[db]\\nhost=localhost'\n"
           "    assert parse_section(t, 'app') == {'name': 'demo', 'port': '80'}\n"
           "    assert parse_section(t, 'db') == {'host': 'localhost'}\n"
           '    print("All tests passed.")\n',
  'solution': 'def parse_section(text: str, section: str) -> dict[str, str]:\n'
              '    result: dict[str, str] = {}\n'
              '    current = None\n'
              '    for raw in text.splitlines():\n'
              '        line = raw.strip()\n'
              "        if not line or line.startswith('#'):\n"
              '            continue\n'
              "        if line.startswith('[') and line.endswith(']'):\n"
              '            current = line[1:-1]\n'
              '            continue\n'
              "        if current == section and '=' in line:\n"
              "            k, v = line.split('=', 1)\n"
              '            result[k.strip()] = v.strip()\n'
              '    return result\n'},
 {'slug': '18_grep_lines',
  'track': 'automations',
  'difficulty': 'easy',
  'title': 'Grep Lines',
  'tags': ['regex', 'io'],
  'description': 'Return lines from text that contain the substring (case-sensitive).',
  'examples': 'grep_lines("a\\nb\\na", "a") -> ["a","a"]',
  'hint': 'Splitlines; filter if needle in line.',
  'syntax_hint': '[ln for ln in text.splitlines() if needle in ln]',
  'signature': 'def grep_lines(text: str, needle: str) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert grep_lines("a\\nb\\na", "a") == ["a", "a"]\n'
           '    assert grep_lines("hello", "z") == []\n'
           '    assert grep_lines("", "a") == []\n'
           '    print("All tests passed.")\n',
  'solution': 'def grep_lines(text: str, needle: str) -> list[str]:\n'
              '    return [ln for ln in text.splitlines() if needle in ln]\n'},
 {'slug': '19_csv_to_dicts',
  'track': 'automations',
  'difficulty': 'medium',
  'title': 'CSV to Dicts',
  'tags': ['csv'],
  'description': 'Parse CSV text with header row into list of dicts (strings).',
  'examples': 'csv_dicts("a,b\\n1,2") -> [{"a":"1","b":"2"}]',
  'hint': 'csv.DictReader over io.StringIO.',
  'syntax_hint': 'import csv, io; list(csv.DictReader(io.StringIO(text)))',
  'signature': 'def csv_dicts(text: str) -> list[dict[str, str]]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert csv_dicts("a,b\\n1,2") == [{"a": "1", "b": "2"}]\n'
           '    assert csv_dicts("x\\ny") == [{"x": "y"}]\n'
           '    assert csv_dicts("h\\n") == []\n'
           '    print("All tests passed.")\n',
  'solution': 'import csv\n'
              'import io\n'
              '\n'
              'def csv_dicts(text: str) -> list[dict[str, str]]:\n'
              '    return list(csv.DictReader(io.StringIO(text)))\n'},
 {'slug': '20_json_pretty_size',
  'track': 'automations',
  'difficulty': 'easy',
  'title': 'JSON Key Count',
  'tags': ['json'],
  'description': 'Parse JSON object string and return number of top-level keys.',
  'examples': 'key_count(\'{"a":1,"b":2}\') -> 2',
  'hint': 'len(json.loads(s)) for objects.',
  'syntax_hint': 'len(json.loads(text))',
  'signature': 'def key_count(text: str) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert key_count(\'{"a": 1, "b": 2}\') == 2\n'
           '    assert key_count("{}") == 0\n'
           '    assert key_count(\'{"x": []}\') == 1\n'
           '    print("All tests passed.")\n',
  'solution': 'import json\n\ndef key_count(text: str) -> int:\n    return len(json.loads(text))\n'},
 {'slug': '21_env_substitute',
  'track': 'automations',
  'difficulty': 'medium',
  'title': 'Env Substitute',
  'tags': ['string'],
  'description': 'Replace ${VAR} in template with values from env dict; leave unknown as empty string.',
  'examples': 'substitute("hi ${NAME}", {"NAME":"Ada"}) -> "hi Ada"',
  'hint': "re.sub r'\\$\\{([^}]+)\\}' lambda m: env.get(m.group(1),'').",
  'syntax_hint': 'import re; re.sub(pattern, repl, template)',
  'signature': 'def substitute(template: str, env: dict[str, str]) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert substitute("hi ${NAME}", {"NAME": "Ada"}) == "hi Ada"\n'
           '    assert substitute("${X}-${Y}", {"X": "1"}) == "1-"\n'
           '    assert substitute("plain", {}) == "plain"\n'
           '    print("All tests passed.")\n',
  'solution': 'import re\n'
              '\n'
              'def substitute(template: str, env: dict[str, str]) -> str:\n'
              "    return re.sub(r'\\$\\{([^}]+)\\}', lambda m: env.get(m.group(1), ''), template)\n"},
 {'slug': '22_rotate_lines',
  'track': 'automations',
  'difficulty': 'easy',
  'title': 'Rotate Lines',
  'tags': ['string'],
  'description': 'Rotate lines of text up by k (k=1 moves first line to end).',
  'examples': 'rotate_lines("a\\nb\\nc", 1) -> "b\\nc\\na"',
  'hint': 'lines = text.splitlines(); lines[k:]+lines[:k]',
  'syntax_hint': 'lines = text.splitlines()',
  'signature': 'def rotate_lines(text: str, k: int) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert rotate_lines("a\\nb\\nc", 1) == "b\\nc\\na"\n'
           '    assert rotate_lines("a\\nb", 2) == "a\\nb"\n'
           '    assert rotate_lines("", 3) == ""\n'
           '    print("All tests passed.")\n',
  'solution': 'def rotate_lines(text: str, k: int) -> str:\n'
              '    if not text:\n'
              "        return ''\n"
              '    lines = text.splitlines()\n'
              '    if not lines:\n'
              "        return ''\n"
              '    k %= len(lines)\n'
              "    return '\\n'.join(lines[k:] + lines[:k])\n"},
 {'slug': '23_checksum_lines',
  'track': 'automations',
  'difficulty': 'medium',
  'title': 'Line Checksum',
  'tags': ['hashlib'],
  'description': 'Return first 8 hex chars of sha256 of UTF-8 encoded text.',
  'examples': "line_checksum('abc') -> 8 hex chars",
  'hint': 'hashlib.sha256(text.encode()).hexdigest()[:8]',
  'syntax_hint': 'import hashlib',
  'signature': 'def line_checksum(text: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert len(line_checksum('abc')) == 8\n"
           "    assert line_checksum('abc') == line_checksum('abc')\n"
           "    assert line_checksum('a') != line_checksum('b')\n"
           '    print("All tests passed.")\n',
  'solution': 'import hashlib\n'
              '\n'
              'def line_checksum(text: str) -> str:\n'
              '    return hashlib.sha256(text.encode()).hexdigest()[:8]\n'},
 {'slug': '15_jwt_payload_decode',
  'track': 'apis',
  'difficulty': 'medium',
  'title': 'JWT Payload Decode',
  'tags': ['jwt', 'base64'],
  'description': 'Decode the payload section of a JWT string (no signature verification) and return the claims dict.',
  'examples': 'decode_payload("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.sig") -> {"sub": "1234"}',
  'hint': "Split on '.'; base64url-decode the middle segment; json.loads.",
  'syntax_hint': "payload + '=' * (-len(payload) % 4); base64.urlsafe_b64decode",
  'signature': 'def decode_payload(token: str) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    tok = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.sig"\n'
           "    assert decode_payload(tok) == {'sub': '1234'}\n"
           '    tok2 = "a.eyJuYW1lIjoiZWxpIn0.b"\n'
           "    assert decode_payload(tok2) == {'name': 'eli'}\n"
           '    print("All tests passed.")\n',
  'solution': 'import base64\n'
              'import json\n'
              '\n'
              'def decode_payload(token: str) -> dict:\n'
              "    payload = token.split('.')[1]\n"
              "    padded = payload + '=' * (-len(payload) % 4)\n"
              '    return json.loads(base64.urlsafe_b64decode(padded))\n'},
 {'slug': '16_etag_header',
  'track': 'apis',
  'difficulty': 'easy',
  'title': 'ETag Header',
  'tags': ['http', 'hash'],
  'description': 'Given response body bytes, return an ETag string: double-quoted MD5 hex digest.',
  'examples': 'make_etag(b\'hello\') -> \'"5d41402abc4b2a76b9719d911017c592"\'',
  'hint': 'hashlib.md5(body).hexdigest() wrapped in quotes.',
  'syntax_hint': 'return f\'"{hashlib.md5(body).hexdigest()}"\'',
  'signature': 'def make_etag(body: bytes) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert make_etag(b\'hello\') == \'"5d41402abc4b2a76b9719d911017c592"\'\n'
           '    assert make_etag(b\'\') == \'"d41d8cd98f00b204e9800998ecf8427e"\'\n'
           '    assert make_etag(b\'hello\').startswith(\'"\')\n'
           '    print("All tests passed.")\n',
  'solution': 'import hashlib\n'
              '\n'
              'def make_etag(body: bytes) -> str:\n'
              '    return f\'"{hashlib.md5(body).hexdigest()}"\'\n'},
 {'slug': '17_content_negotiation',
  'track': 'apis',
  'difficulty': 'medium',
  'title': 'Content Negotiation',
  'tags': ['http', 'headers'],
  'description': 'Given an Accept header string and a list of offered MIME types, return the best matching offered '
                 'type or None.',
  'examples': "pick_type('application/json, text/plain', ['text/html','application/json']) -> 'application/json'",
  'hint': 'Parse Accept by comma; prefer exact MIME matches in listed order.',
  'syntax_hint': 'for offered in types: if offered in accept_parts: return offered',
  'signature': 'def pick_type(accept: str, offered: list[str]) -> str | None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert pick_type('application/json, text/plain', ['text/html', 'application/json']) == "
           "'application/json'\n"
           "    assert pick_type('text/plain', ['application/json']) is None\n"
           "    assert pick_type('text/html', ['text/html', 'text/plain']) == 'text/html'\n"
           '    print("All tests passed.")\n',
  'solution': 'def pick_type(accept: str, offered: list[str]) -> str | None:\n'
              "    parts = [p.split(';')[0].strip() for p in accept.split(',')]\n"
              '    for mime in parts:\n'
              '        if mime in offered:\n'
              '            return mime\n'
              '    return None\n'},
 {'slug': '18_hmac_signature',
  'track': 'apis',
  'difficulty': 'medium',
  'title': 'HMAC Signature',
  'tags': ['crypto', 'api'],
  'description': 'Return the hex HMAC-SHA256 digest of message using the given secret key (both as str, UTF-8 '
                 'encoded).',
  'examples': "sign('payload', 'secret') -> hex digest string",
  'hint': 'hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()',
  'syntax_hint': "import hmac, hashlib; hmac.new(key.encode(), msg.encode(), 'sha256').hexdigest()",
  'signature': 'def sign(message: str, secret: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert sign('payload', 'secret') == sign('payload', 'secret')\n"
           "    assert sign('a', 'k') != sign('b', 'k')\n"
           "    assert len(sign('x', 'y')) == 64\n"
           '    print("All tests passed.")\n',
  'solution': 'import hashlib\n'
              'import hmac\n'
              '\n'
              'def sign(message: str, secret: str) -> str:\n'
              '    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()\n'},
 {'slug': '19_url_join',
  'track': 'apis',
  'difficulty': 'easy',
  'title': 'URL Join',
  'tags': ['url'],
  'description': 'Join a base URL and path segments into one URL without duplicate slashes.',
  'examples': "join_url('https://api.test/v1/', '/users/', '42') -> 'https://api.test/v1/users/42'",
  'hint': 'Strip slashes from segments; urllib.parse.urljoin handles the base.',
  'syntax_hint': "from urllib.parse import urljoin; urljoin(base.rstrip('/')+'/', segment)",
  'signature': 'def join_url(base: str, *parts: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert join_url('https://api.test/v1/', '/users/', '42') == 'https://api.test/v1/users/42'\n"
           "    assert join_url('https://x.test/', 'a', 'b') == 'https://x.test/a/b'\n"
           "    assert join_url('https://x.test/api', '') == 'https://x.test/api'\n"
           '    print("All tests passed.")\n',
  'solution': 'from urllib.parse import urljoin\n'
              '\n'
              'def join_url(base: str, *parts: str) -> str:\n'
              '    url = base\n'
              '    for part in parts:\n'
              '        if not part:\n'
              '            continue\n'
              "        url = urljoin(url.rstrip('/') + '/', part.lstrip('/'))\n"
              '    return url\n'},
 {'slug': '20_json_merge',
  'track': 'apis',
  'difficulty': 'medium',
  'title': 'Deep JSON Merge',
  'tags': ['json', 'dict'],
  'description': 'Deep-merge dict b into dict a; nested dicts merge recursively, other values from b win.',
  'examples': "merge({'a':1,'b':{'x':1}}, {'b':{'y':2}}) -> {'a':1,'b':{'x':1,'y':2}}",
  'hint': "Recurse when both values are dicts; else assign b's value.",
  'syntax_hint': 'if isinstance(a[k], dict) and isinstance(v, dict): merge(a[k], v)',
  'signature': 'def merge(a: dict, b: dict) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert merge({'a': 1, 'b': {'x': 1}}, {'b': {'y': 2}}) == {'a': 1, 'b': {'x': 1, 'y': 2}}\n"
           "    assert merge({'a': 1}, {'a': 2}) == {'a': 2}\n"
           "    assert merge({}, {'z': 3}) == {'z': 3}\n"
           '    print("All tests passed.")\n',
  'solution': 'def merge(a: dict, b: dict) -> dict:\n'
              '    out = dict(a)\n'
              '    for k, v in b.items():\n'
              '        if k in out and isinstance(out[k], dict) and isinstance(v, dict):\n'
              '            out[k] = merge(out[k], v)\n'
              '        else:\n'
              '            out[k] = v\n'
              '    return out\n'},
 {'slug': '21_cache_key',
  'track': 'apis',
  'difficulty': 'easy',
  'title': 'Cache Key Builder',
  'tags': ['cache', 'url'],
  'description': "Build a cache key from url and params dict: url + '?' + sorted query string.",
  'examples': "cache_key('https://x.test', {'b':2,'a':1}) -> 'https://x.test?a=1&b=2'",
  'hint': 'Sort param keys; urllib.parse.urlencode.',
  'syntax_hint': "from urllib.parse import urlencode; f'{url}?{urlencode(sorted(params.items()))}'",
  'signature': 'def cache_key(url: str, params: dict) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert cache_key('https://x.test', {'b': 2, 'a': 1}) == 'https://x.test?a=1&b=2'\n"
           "    assert cache_key('https://x.test', {}) == 'https://x.test'\n"
           "    assert 'q=py' in cache_key('https://x.test/api', {'q': 'py'})\n"
           '    print("All tests passed.")\n',
  'solution': 'from urllib.parse import urlencode\n'
              '\n'
              'def cache_key(url: str, params: dict) -> str:\n'
              '    if not params:\n'
              '        return url\n'
              '    return f"{url}?{urlencode(sorted(params.items()))}"\n'},
 {'slug': '15_method_router',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Method Router',
  'tags': ['routing', 'http'],
  'description': 'Given a dict mapping HTTP method -> handler name and a method string, return the handler or '
                 "'not_found'.",
  'examples': "route_method({'GET':'list','POST':'create'}, 'POST') -> 'create'",
  'hint': 'Use dict.get with default.',
  'syntax_hint': "handlers.get(method.upper(), 'not_found')",
  'signature': 'def route_method(handlers: dict[str, str], method: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert route_method({'GET': 'list', 'POST': 'create'}, 'POST') == 'create'\n"
           "    assert route_method({'GET': 'list'}, 'DELETE') == 'not_found'\n"
           "    assert route_method({}, 'GET') == 'not_found'\n"
           '    print("All tests passed.")\n',
  'solution': 'def route_method(handlers: dict[str, str], method: str) -> str:\n'
              "    return handlers.get(method.upper(), 'not_found')\n"},
 {'slug': '16_host_header_parse',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Host Header Parse',
  'tags': ['http', 'headers'],
  'description': 'Parse a Host header value into (hostname, port). Default port 80 when omitted.',
  'examples': "parse_host('api.test:8080') -> ('api.test', 8080)",
  'hint': "Split on ':' once; int port or default 80.",
  'syntax_hint': "host, _, port = value.partition(':'); int(port) if port else 80",
  'signature': 'def parse_host(value: str) -> tuple[str, int]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert parse_host('api.test:8080') == ('api.test', 8080)\n"
           "    assert parse_host('localhost') == ('localhost', 80)\n"
           "    assert parse_host('x.test:443') == ('x.test', 443)\n"
           '    print("All tests passed.")\n',
  'solution': 'def parse_host(value: str) -> tuple[str, int]:\n'
              "    host, _, port = value.partition(':')\n"
              '    return host, int(port) if port else 80\n'},
 {'slug': '17_chunked_encoding_flag',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Chunked Encoding Flag',
  'tags': ['http', 'headers'],
  'description': 'Return True if headers dict indicates chunked Transfer-Encoding (case-insensitive).',
  'examples': "is_chunked({'Transfer-Encoding': 'chunked'}) -> True",
  'hint': "Check Transfer-Encoding header for 'chunked' substring.",
  'syntax_hint': "'chunked' in headers.get('Transfer-Encoding', '').lower()",
  'signature': 'def is_chunked(headers: dict[str, str]) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert is_chunked({'Transfer-Encoding': 'chunked'}) is True\n"
           "    assert is_chunked({'Transfer-Encoding': 'gzip, chunked'}) is True\n"
           "    assert is_chunked({'Content-Length': '10'}) is False\n"
           '    print("All tests passed.")\n',
  'solution': 'def is_chunked(headers: dict[str, str]) -> bool:\n'
              '    for k, v in headers.items():\n'
              "        if k.lower() == 'transfer-encoding':\n"
              "            return 'chunked' in v.lower()\n"
              '    return False\n'},
 {'slug': '18_redirect_builder',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Redirect Response Builder',
  'tags': ['http', 'redirect'],
  'description': 'Build a redirect response dict with status, Location header, and empty body.',
  'examples': "redirect('/login', 302) -> {'status':302,'headers':{'Location':'/login'},'body':''}",
  'hint': 'Return a plain dict with the three keys.',
  'syntax_hint': "return {'status': code, 'headers': {'Location': url}, 'body': ''}",
  'signature': 'def redirect(url: str, status: int = 302) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    r = redirect('/login', 302)\n"
           "    assert r['status'] == 302\n"
           "    assert r['headers']['Location'] == '/login'\n"
           "    assert r['body'] == ''\n"
           '    print("All tests passed.")\n',
  'solution': 'def redirect(url: str, status: int = 302) -> dict:\n'
              "    return {'status': status, 'headers': {'Location': url}, 'body': ''}\n"},
 {'slug': '19_auth_bearer_parse',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Bearer Token Parse',
  'tags': ['auth', 'http'],
  'description': 'Extract the bearer token from an Authorization header, or None if missing/invalid.',
  'examples': "bearer_token('Bearer abc123') -> 'abc123'",
  'hint': 'Split on space; require scheme Bearer (case-insensitive).',
  'syntax_hint': "parts = header.split(); scheme.lower() == 'bearer'",
  'signature': 'def bearer_token(header: str) -> str | None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert bearer_token('Bearer abc123') == 'abc123'\n"
           "    assert bearer_token('bearer xyz') == 'xyz'\n"
           "    assert bearer_token('Basic abc') is None\n"
           "    assert bearer_token('') is None\n"
           '    print("All tests passed.")\n',
  'solution': 'def bearer_token(header: str) -> str | None:\n'
              '    parts = header.split(None, 1)\n'
              "    if len(parts) != 2 or parts[0].lower() != 'bearer':\n"
              '        return None\n'
              '    return parts[1]\n'},
 {'slug': '20_path_normalize',
  'track': 'servers',
  'difficulty': 'medium',
  'title': 'Path Normalize',
  'tags': ['url', 'path'],
  'description': 'Normalize a URL path: collapse //, resolve . and .., ensure leading slash.',
  'examples': "normalize('/a/../b/./c') -> '/b/c'",
  'hint': 'Split segments; stack-based .. handling.',
  'syntax_hint': "stack append segment; on '..' pop if possible",
  'signature': 'def normalize(path: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert normalize('/a/../b/./c') == '/b/c'\n"
           "    assert normalize('//a//b//') == '/a/b'\n"
           "    assert normalize('/x/y/../z') == '/x/z'\n"
           "    assert normalize('/') == '/'\n"
           '    print("All tests passed.")\n',
  'solution': 'def normalize(path: str) -> str:\n'
              "    parts = [p for p in path.split('/') if p and p != '.']\n"
              '    stack: list[str] = []\n'
              '    for p in parts:\n'
              "        if p == '..':\n"
              '            if stack:\n'
              '                stack.pop()\n'
              '        else:\n'
              '            stack.append(p)\n'
              "    return '/' + '/'.join(stack) if stack else '/'\n"},
 {'slug': '21_header_order',
  'track': 'servers',
  'difficulty': 'easy',
  'title': 'Canonical Header Order',
  'tags': ['http', 'headers'],
  'description': 'Return headers reordered by canonical name (case-insensitive sort), preserving original casing of '
                 'values.',
  'examples': "order_headers({'B':'2','A':'1'}) -> [('A','1'),('B','2')]",
  'hint': 'Sort items by key.lower().',
  'syntax_hint': 'sorted(headers.items(), key=lambda kv: kv[0].lower())',
  'signature': 'def order_headers(headers: dict[str, str]) -> list[tuple[str, str]]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert order_headers({'B': '2', 'A': '1'}) == [('A', '1'), ('B', '2')]\n"
           '    assert order_headers({}) == []\n'
           "    assert order_headers({'z': '1', 'a': '2'})[0][0] == 'a'\n"
           '    print("All tests passed.")\n',
  'solution': 'def order_headers(headers: dict[str, str]) -> list[tuple[str, str]]:\n'
              '    return sorted(headers.items(), key=lambda kv: kv[0].lower())\n'},
 {'slug': '15_queue_class',
  'track': 'apps',
  'difficulty': 'easy',
  'title': 'Queue Class',
  'tags': ['oop', 'queue'],
  'description': 'Implement a FIFO Queue with enqueue(x), dequeue() (raise IndexError if empty), and is_empty().',
  'examples': 'q = Queue(); q.enqueue(1); q.dequeue() -> 1',
  'hint': 'Use collections.deque or a list with pop(0)/append.',
  'syntax_hint': 'from collections import deque; self._items = deque()',
  'signature': 'class Queue:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    q = Queue()\n'
           '    assert q.is_empty() is True\n'
           '    q.enqueue(1); q.enqueue(2)\n'
           '    assert q.dequeue() == 1\n'
           '    assert q.is_empty() is False\n'
           '    assert q.dequeue() == 2\n'
           '    try:\n'
           '        q.dequeue(); assert False\n'
           '    except IndexError:\n'
           '        pass\n'
           '    print("All tests passed.")\n',
  'solution': 'from collections import deque\n'
              '\n'
              'class Queue:\n'
              '    def __init__(self):\n'
              '        self._items: deque = deque()\n'
              '    def enqueue(self, x) -> None:\n'
              '        self._items.append(x)\n'
              '    def dequeue(self):\n'
              '        if not self._items:\n'
              "            raise IndexError('dequeue from empty queue')\n"
              '        return self._items.popleft()\n'
              '    def is_empty(self) -> bool:\n'
              '        return len(self._items) == 0\n'},
 {'slug': '16_event_emitter',
  'track': 'apps',
  'difficulty': 'medium',
  'title': 'Event Emitter',
  'tags': ['oop', 'events'],
  'description': 'Implement EventEmitter with on(event, handler), off(event, handler), and emit(event, *args) calling '
                 'all handlers.',
  'examples': "em.on('x', fn); em.emit('x', 1) calls fn(1)",
  'hint': 'Store handlers per event in a list of callables.',
  'syntax_hint': 'self._handlers: dict[str, list] = {}',
  'signature': 'class EventEmitter:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    em = EventEmitter()\n'
           '    log = []\n'
           "    em.on('x', lambda v: log.append(v))\n"
           "    em.emit('x', 42)\n"
           '    assert log == [42]\n'
           '    fn = lambda: log.append(1)\n'
           "    em.on('y', fn); em.off('y', fn); em.emit('y')\n"
           '    assert log == [42]\n'
           '    print("All tests passed.")\n',
  'solution': 'class EventEmitter:\n'
              '    def __init__(self):\n'
              '        self._handlers: dict[str, list] = {}\n'
              '    def on(self, event: str, handler) -> None:\n'
              '        self._handlers.setdefault(event, []).append(handler)\n'
              '    def off(self, event: str, handler) -> None:\n'
              '        if event in self._handlers:\n'
              '            self._handlers[event] = [h for h in self._handlers[event] if h is not handler]\n'
              '    def emit(self, event: str, *args) -> None:\n'
              '        for h in self._handlers.get(event, []):\n'
              '            h(*args)\n'},
 {'slug': '17_rate_limiter_class',
  'track': 'apps',
  'difficulty': 'medium',
  'title': 'Rate Limiter Class',
  'tags': ['oop', 'rate-limit'],
  'description': 'Implement RateLimiter(max_calls, period_seconds) with allow() returning True only if under the limit '
                 'in the sliding window.',
  'examples': 'rl = RateLimiter(2, 60); allow() twice True, third False',
  'hint': 'Track call timestamps; prune those older than period.',
  'syntax_hint': 'while calls and now - calls[0] >= period: calls.popleft()',
  'signature': 'class RateLimiter:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    rl = RateLimiter(2, 3600)\n'
           '    assert rl.allow() is True\n'
           '    assert rl.allow() is True\n'
           '    assert rl.allow() is False\n'
           '    print("All tests passed.")\n',
  'solution': 'import time\n'
              'from collections import deque\n'
              '\n'
              'class RateLimiter:\n'
              '    def __init__(self, max_calls: int, period_seconds: float):\n'
              '        self.max_calls = max_calls\n'
              '        self.period = period_seconds\n'
              '        self._calls: deque = deque()\n'
              '    def allow(self) -> bool:\n'
              '        now = time.monotonic()\n'
              '        while self._calls and now - self._calls[0] >= self.period:\n'
              '            self._calls.popleft()\n'
              '        if len(self._calls) >= self.max_calls:\n'
              '            return False\n'
              '        self._calls.append(now)\n'
              '        return True\n'},
 {'slug': '18_config_loader',
  'track': 'apps',
  'difficulty': 'easy',
  'title': 'Config Loader',
  'tags': ['config', 'io'],
  'description': 'Parse key=value lines (skip blanks and # comments) into a dict.',
  'examples': "load_config('host=localhost\\nport=80') -> {'host':'localhost','port':'80'}",
  'hint': "Split each line on first '='; strip whitespace.",
  'syntax_hint': "if line.startswith('#'): continue",
  'signature': 'def load_config(text: str) -> dict[str, str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert load_config('host=localhost\\nport=80') == {'host': 'localhost', 'port': '80'}\n"
           "    assert load_config('# comment\\n\\na=1') == {'a': '1'}\n"
           "    assert load_config('') == {}\n"
           '    print("All tests passed.")\n',
  'solution': 'def load_config(text: str) -> dict[str, str]:\n'
              '    out: dict[str, str] = {}\n'
              '    for raw in text.splitlines():\n'
              '        line = raw.strip()\n'
              "        if not line or line.startswith('#'):\n"
              '            continue\n'
              "        key, _, val = line.partition('=')\n"
              '        out[key.strip()] = val.strip()\n'
              '    return out\n'},
 {'slug': '19_memoize_class',
  'track': 'apps',
  'difficulty': 'medium',
  'title': 'Memoize Decorator Class',
  'tags': ['oop', 'decorator'],
  'description': 'Implement Memoize as a class decorator that caches function results by arguments tuple.',
  'examples': '@Memoize def f(x): ...; f(1) computed once',
  'hint': 'Use a dict keyed by args tuple in __call__.',
  'syntax_hint': 'self.cache: dict = {}; key = args',
  'signature': 'class Memoize:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    calls = {'n': 0}\n"
           '    @Memoize\n'
           '    def f(x):\n'
           "        calls['n'] += 1\n"
           '        return x * 2\n'
           '    assert f(3) == 6\n'
           '    assert f(3) == 6\n'
           "    assert calls['n'] == 1\n"
           '    assert f(4) == 8\n'
           "    assert calls['n'] == 2\n"
           '    print("All tests passed.")\n',
  'solution': 'class Memoize:\n'
              '    def __init__(self, fn):\n'
              '        self.fn = fn\n'
              '        self.cache: dict = {}\n'
              '    def __call__(self, *args):\n'
              '        if args not in self.cache:\n'
              '            self.cache[args] = self.fn(*args)\n'
              '        return self.cache[args]\n'},
 {'slug': '20_priority_queue',
  'track': 'apps',
  'difficulty': 'medium',
  'title': 'Priority Queue',
  'tags': ['oop', 'heap'],
  'description': 'Implement PriorityQueue with push(priority, item) and pop() returning lowest-priority item first '
                 '(min-heap).',
  'examples': "pq.push(2,'b'); pq.push(1,'a'); pq.pop() -> 'a'",
  'hint': 'heapq.heappush / heappop with (priority, item) tuples.',
  'syntax_hint': 'import heapq; heapq.heappush(self._heap, (priority, item))',
  'signature': 'class PriorityQueue:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    pq = PriorityQueue()\n'
           "    pq.push(2, 'b')\n"
           "    pq.push(1, 'a')\n"
           "    assert pq.pop() == 'a'\n"
           "    assert pq.pop() == 'b'\n"
           '    try:\n'
           '        pq.pop(); assert False\n'
           '    except IndexError:\n'
           '        pass\n'
           '    print("All tests passed.")\n',
  'solution': 'import heapq\n'
              '\n'
              'class PriorityQueue:\n'
              '    def __init__(self):\n'
              '        self._heap: list = []\n'
              '    def push(self, priority: int, item) -> None:\n'
              '        heapq.heappush(self._heap, (priority, item))\n'
              '    def pop(self):\n'
              '        if not self._heap:\n'
              "            raise IndexError('pop from empty priority queue')\n"
              '        return heapq.heappop(self._heap)[1]\n'},
 {'slug': '21_ring_buffer',
  'track': 'apps',
  'difficulty': 'medium',
  'title': 'Ring Buffer',
  'tags': ['oop', 'buffer'],
  'description': 'Implement RingBuffer(capacity) with write(x) overwriting oldest when full, and read_all() returning '
                 'items oldest-first.',
  'examples': 'rb = RingBuffer(2); write 1,2,3; read_all() -> [2,3]',
  'hint': 'Use a list and index pointer modulo capacity.',
  'syntax_hint': 'self._data = [None]*capacity; self._start = self._size = 0',
  'signature': 'class RingBuffer:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    rb = RingBuffer(2)\n'
           '    rb.write(1); rb.write(2)\n'
           '    assert rb.read_all() == [1, 2]\n'
           '    rb.write(3)\n'
           '    assert rb.read_all() == [2, 3]\n'
           '    rb.write(4); rb.write(5)\n'
           '    assert rb.read_all() == [4, 5]\n'
           '    print("All tests passed.")\n',
  'solution': 'class RingBuffer:\n'
              '    def __init__(self, capacity: int):\n'
              '        self.capacity = capacity\n'
              '        self._data: list = [None] * capacity\n'
              '        self._start = 0\n'
              '        self._size = 0\n'
              '    def write(self, x) -> None:\n'
              '        if self._size < self.capacity:\n'
              '            idx = (self._start + self._size) % self.capacity\n'
              '            self._data[idx] = x\n'
              '            self._size += 1\n'
              '        else:\n'
              '            self._data[self._start] = x\n'
              '            self._start = (self._start + 1) % self.capacity\n'
              '    def read_all(self) -> list:\n'
              '        return [self._data[(self._start + i) % self.capacity] for i in range(self._size)]\n'},
 {'slug': '13_patch_route',
  'track': 'fastapi',
  'difficulty': 'medium',
  'title': 'PATCH Route',
  'tags': ['fastapi', 'http'],
  'description': "Implement register(app) adding PATCH /items/{item_id} that accepts JSON body {'name': str} and "
                 'returns it with id.',
  'examples': "patch /items/5 {'name':'x'} -> {'id':5,'name':'x'}",
  'hint': 'Use @app.patch with path param and body dict.',
  'syntax_hint': "@app.patch('/items/{item_id}')",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.patch('/items/5', json={'name': 'x'})\n"
           '    assert r.status_code == 200\n'
           "    assert r.json() == {'id': 5, 'name': 'x'}\n"
           '    print("All tests passed.")\n',
  'solution': 'def register(app) -> None:\n'
              "    @app.patch('/items/{item_id}')\n"
              '    def patch_item(item_id: int, body: dict):\n'
              "        return {'id': item_id, 'name': body['name']}\n"},
 {'slug': '14_put_route',
  'track': 'fastapi',
  'difficulty': 'medium',
  'title': 'PUT Route',
  'tags': ['fastapi', 'http'],
  'description': "Implement register(app) adding PUT /items/{item_id} replacing the item; return {'id': item_id, "
                 "'data': body}.",
  'examples': "put /items/3 {'a':1} -> {'id':3,'data':{'a':1}}",
  'hint': 'PUT decorator with path param and dict body.',
  'syntax_hint': "@app.put('/items/{item_id}')",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.put('/items/3', json={'a': 1})\n"
           "    assert r.json() == {'id': 3, 'data': {'a': 1}}\n"
           '    print("All tests passed.")\n',
  'solution': 'def register(app) -> None:\n'
              "    @app.put('/items/{item_id}')\n"
              '    def put_item(item_id: int, body: dict):\n'
              "        return {'id': item_id, 'data': body}\n"},
 {'slug': '15_form_data',
  'track': 'fastapi',
  'difficulty': 'medium',
  'title': 'Form Data Route',
  'tags': ['fastapi', 'forms'],
  'description': 'Implement register(app) adding POST /login parsing application/x-www-form-urlencoded body for '
                 'username.',
  'examples': "post form username=eli&password=secret -> {'user':'eli'}",
  'hint': 'Read request.body and parse with urllib.parse.parse_qs.',
  'syntax_hint': 'from urllib.parse import parse_qs; data = parse_qs(body.decode())',
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.post('/login', data={'username': 'eli', 'password': 'secret'})\n"
           '    assert r.status_code == 200\n'
           "    assert r.json() == {'user': 'eli'}\n"
           '    print("All tests passed.")\n',
  'solution': 'from urllib.parse import parse_qs\n'
              'from starlette.requests import Request\n'
              '\n'
              'def register(app) -> None:\n'
              "    @app.post('/login')\n"
              '    async def login(request: Request):\n'
              '        body = await request.body()\n'
              '        data = parse_qs(body.decode())\n'
              "        return {'user': data.get('username', [''])[0]}\n"},
 {'slug': '16_file_upload_mock',
  'track': 'fastapi',
  'difficulty': 'medium',
  'title': 'File Upload Mock Header',
  'tags': ['fastapi', 'upload'],
  'description': 'Implement register(app) adding POST /upload reading filename from X-Filename header (mock upload '
                 'metadata).',
  'examples': "post with X-Filename: test.txt -> {'filename': 'test.txt'}",
  'hint': "Use Header(alias='X-Filename') instead of real multipart upload.",
  'syntax_hint': "from fastapi import Header; x_filename: str = Header(alias='X-Filename')",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.post('/upload', headers={'X-Filename': 'test.txt'})\n"
           '    assert r.status_code == 200\n'
           "    assert r.json() == {'filename': 'test.txt'}\n"
           '    print("All tests passed.")\n',
  'solution': 'from fastapi import Header\n'
              '\n'
              'def register(app) -> None:\n'
              "    @app.post('/upload')\n"
              "    def upload(x_filename: str = Header(alias='X-Filename')):\n"
              "        return {'filename': x_filename}\n"},
 {'slug': '17_response_headers',
  'track': 'fastapi',
  'difficulty': 'medium',
  'title': 'Custom Response Headers',
  'tags': ['fastapi', 'headers'],
  'description': 'Implement register(app) adding GET /data returning JSON with custom header X-Custom: yes via '
                 'Response.',
  'examples': 'get /data -> header X-Custom: yes',
  'hint': 'Return JSONResponse or Response with headers dict.',
  'syntax_hint': "from fastapi.responses import JSONResponse; headers={'X-Custom': 'yes'}",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.get('/data')\n"
           "    assert r.headers.get('x-custom') == 'yes'\n"
           "    assert r.json() == {'ok': True}\n"
           '    print("All tests passed.")\n',
  'solution': 'from fastapi.responses import JSONResponse\n'
              '\n'
              'def register(app) -> None:\n'
              "    @app.get('/data')\n"
              '    def data():\n'
              "        return JSONResponse({'ok': True}, headers={'X-Custom': 'yes'})\n"},
 {'slug': '18_tags_metadata',
  'track': 'fastapi',
  'difficulty': 'easy',
  'title': 'Route Tags Metadata',
  'tags': ['fastapi', 'openapi'],
  'description': "Implement register(app) adding GET /pets tagged 'animals' returning {'pets': []}. OpenAPI route must "
                 'include tag.',
  'examples': "route appears under 'animals' tag in openapi",
  'hint': "Pass tags=['animals'] to decorator.",
  'syntax_hint': "@app.get('/pets', tags=['animals'])",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    assert c.get('/pets').json() == {'pets': []}\n"
           '    schema = app.openapi()\n'
           "    paths = schema['paths']['/pets']['get']['tags']\n"
           "    assert 'animals' in paths\n"
           '    print("All tests passed.")\n',
  'solution': 'def register(app) -> None:\n'
              "    @app.get('/pets', tags=['animals'])\n"
              '    def pets():\n'
              "        return {'pets': []}\n"},
 {'slug': '19_timing_middleware',
  'track': 'fastapi',
  'difficulty': 'hard',
  'title': 'Timing Middleware',
  'tags': ['fastapi', 'middleware'],
  'description': 'Implement register(app) adding HTTP middleware that sets response header X-Processed: 1 on every '
                 'request.',
  'examples': 'any route returns X-Processed: 1 header',
  'hint': "Use @app.middleware('http') async wrapper.",
  'syntax_hint': "@app.middleware('http'); response.headers['X-Processed'] = '1'",
  'signature': 'def register(app) -> None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from fastapi import FastAPI\n'
           '    from fastapi.testclient import TestClient\n'
           '    app = FastAPI()\n'
           "    @app.get('/ping')\n"
           '    def ping():\n'
           "        return {'pong': True}\n"
           '    register(app)\n'
           '    c = TestClient(app)\n'
           "    r = c.get('/ping')\n"
           "    assert r.headers.get('x-processed') == '1'\n"
           '    print("All tests passed.")\n',
  'solution': 'def register(app) -> None:\n'
              "    @app.middleware('http')\n"
              '    async def add_header(request, call_next):\n'
              '        response = await call_next(request)\n'
              "        response.headers['X-Processed'] = '1'\n"
              '        return response\n'},
 {'slug': '13_concat_frames',
  'track': 'pandas',
  'difficulty': 'easy',
  'title': 'Concat DataFrames',
  'tags': ['pandas', 'concat'],
  'description': 'Vertically concatenate a list of DataFrames with ignore_index=True.',
  'examples': 'concat_frames([df1, df2]) -> combined frame',
  'hint': 'pd.concat(frames, ignore_index=True)',
  'syntax_hint': 'import pandas as pd; pd.concat(frames, ignore_index=True)',
  'signature': 'def concat_frames(frames: list):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    a = pd.DataFrame({'x': [1]})\n"
           "    b = pd.DataFrame({'x': [2, 3]})\n"
           '    out = concat_frames([a, b])\n'
           "    assert list(out['x']) == [1, 2, 3]\n"
           '    print("All tests passed.")\n',
  'solution': 'import pandas as pd\n'
              '\n'
              'def concat_frames(frames: list):\n'
              '    return pd.concat(frames, ignore_index=True)\n'},
 {'slug': '14_melt_frame',
  'track': 'pandas',
  'difficulty': 'medium',
  'title': 'Melt DataFrame',
  'tags': ['pandas', 'reshape'],
  'description': "Melt df with id_vars=['id'] and value_vars=['a','b']; return long-format frame.",
  'examples': 'melt_wide(df) unpivots a and b columns',
  'hint': "df.melt(id_vars=['id'], value_vars=['a','b'])",
  'syntax_hint': "df.melt(id_vars=['id'], value_vars=['a', 'b'], var_name='key', value_name='val')",
  'signature': 'def melt_wide(df):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    df = pd.DataFrame({'id': [1], 'a': [10], 'b': [20]})\n"
           '    out = melt_wide(df)\n'
           '    assert len(out) == 2\n'
           "    assert set(out['variable']) == {'a', 'b'}\n"
           '    print("All tests passed.")\n',
  'solution': "def melt_wide(df):\n    return df.melt(id_vars=['id'], value_vars=['a', 'b'])\n"},
 {'slug': '15_pivot_table_agg',
  'track': 'pandas',
  'difficulty': 'medium',
  'title': 'Pivot Table Mean',
  'tags': ['pandas', 'pivot'],
  'description': "Pivot df with index='region', columns='product', values='sales', aggfunc='mean', fill_value=0.",
  'examples': 'pivot_mean(df) -> pivoted means',
  'hint': "df.pivot_table(index='region', columns='product', values='sales', aggfunc='mean')",
  'syntax_hint': 'df.pivot_table(..., fill_value=0)',
  'signature': 'def pivot_mean(df):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           '    df = pd.DataFrame({\n'
           "        'region': ['n', 'n', 's'],\n"
           "        'product': ['a', 'a', 'b'],\n"
           "        'sales': [10, 30, 5],\n"
           '    })\n'
           '    out = pivot_mean(df)\n'
           "    assert out.loc['n', 'a'] == 20.0\n"
           "    assert out.loc['s', 'b'] == 5.0\n"
           '    print("All tests passed.")\n',
  'solution': 'def pivot_mean(df):\n'
              '    return df.pivot_table(\n'
              "        index='region', columns='product', values='sales', aggfunc='mean', fill_value=0\n"
              '    )\n'},
 {'slug': '16_apply_row',
  'track': 'pandas',
  'difficulty': 'medium',
  'title': 'Apply Row Function',
  'tags': ['pandas', 'apply'],
  'description': "Add column 'total' as sum of columns 'a' and 'b' using apply along rows.",
  'examples': 'add_total(df) -> df with total column',
  'hint': "df.apply(lambda row: row['a'] + row['b'], axis=1)",
  'syntax_hint': "df['total'] = df.apply(lambda r: r['a'] + r['b'], axis=1)",
  'signature': 'def add_total(df):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})\n"
           '    out = add_total(df)\n'
           "    assert list(out['total']) == [4, 6]\n"
           '    print("All tests passed.")\n',
  'solution': 'def add_total(df):\n'
              '    out = df.copy()\n'
              "    out['total'] = out.apply(lambda r: r['a'] + r['b'], axis=1)\n"
              '    return out\n'},
 {'slug': '17_astype_column',
  'track': 'pandas',
  'difficulty': 'easy',
  'title': 'Astype Column',
  'tags': ['pandas', 'types'],
  'description': "Convert column 'code' to string dtype and return the DataFrame.",
  'examples': 'astype_code(df) -> code column is str',
  'hint': "df.assign(code=df['code'].astype(str)) or df.copy with astype",
  'syntax_hint': "df['code'] = df['code'].astype(str)",
  'signature': 'def astype_code(df):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    df = pd.DataFrame({'code': [1, 2]})\n"
           '    out = astype_code(df)\n'
           "    assert out['code'].iloc[0] == '1'\n"
           "    assert out['code'].iloc[1] == '2'\n"
           '    print("All tests passed.")\n',
  'solution': "def astype_code(df):\n    out = df.copy()\n    out['code'] = out['code'].astype(str)\n    return out\n"},
 {'slug': '18_between_filter',
  'track': 'pandas',
  'difficulty': 'easy',
  'title': 'Between Filter',
  'tags': ['pandas', 'filter'],
  'description': "Return rows where column 'score' is between low and high inclusive.",
  'examples': 'between_scores(df, 10, 20) filters score column',
  'hint': "df[df['score'].between(low, high)]",
  'syntax_hint': "df['score'].between(low, high)",
  'signature': 'def between_scores(df, low: int, high: int):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    df = pd.DataFrame({'score': [5, 15, 25]})\n"
           '    out = between_scores(df, 10, 20)\n'
           "    assert list(out['score']) == [15]\n"
           '    print("All tests passed.")\n',
  'solution': "def between_scores(df, low: int, high: int):\n    return df[df['score'].between(low, high)]\n"},
 {'slug': '19_nunique_column',
  'track': 'pandas',
  'difficulty': 'easy',
  'title': 'Nunique Column',
  'tags': ['pandas', 'aggregate'],
  'description': "Return the number of unique values in column 'city'.",
  'examples': 'unique_cities(df) -> int count',
  'hint': "df['city'].nunique()",
  'syntax_hint': "df['city'].nunique()",
  'signature': 'def unique_cities(df) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import pandas as pd\n'
           "    df = pd.DataFrame({'city': ['a', 'b', 'a', 'c']})\n"
           '    assert unique_cities(df) == 3\n'
           "    assert unique_cities(pd.DataFrame({'city': []})) == 0\n"
           '    print("All tests passed.")\n',
  'solution': 'def unique_cities(df) -> int:\n'
              "    if df.empty or 'city' not in df.columns:\n"
              '        return 0\n'
              "    return int(df['city'].nunique())\n"},
 {'slug': '13_markdown_render',
  'track': 'rich',
  'difficulty': 'easy',
  'title': 'Markdown Render',
  'tags': ['rich', 'markdown'],
  'description': 'Render markdown text to a string using rich.markdown.Markdown and Console with StringIO.',
  'examples': "render_md('# Hi') -> string containing 'Hi'",
  'hint': 'Markdown(text); Console(file=StringIO()).print(md)',
  'syntax_hint': 'from rich.markdown import Markdown; from rich.console import Console',
  'signature': 'def render_md(text: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    s = render_md('# Hello')\n"
           "    assert 'Hello' in s\n"
           "    assert render_md('plain') != ''\n"
           '    print("All tests passed.")\n',
  'solution': 'import io\n'
              'from rich.console import Console\n'
              'from rich.markdown import Markdown\n'
              '\n'
              'def render_md(text: str) -> str:\n'
              '    buf = io.StringIO()\n'
              '    console = Console(file=buf, width=80, force_terminal=False)\n'
              '    console.print(Markdown(text))\n'
              '    return buf.getvalue()\n'},
 {'slug': '14_json_syntax',
  'track': 'rich',
  'difficulty': 'medium',
  'title': 'JSON Syntax Highlight',
  'tags': ['rich', 'json'],
  'description': "Return a rich.syntax.Syntax object for JSON text with lexer 'json'.",
  'examples': 'json_syntax(\'{"a":1}\') -> Syntax instance',
  'hint': "Syntax(code, 'json', theme='monokai')",
  'syntax_hint': "from rich.syntax import Syntax; Syntax(text, 'json')",
  'signature': 'def json_syntax(text: str):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from rich.syntax import Syntax\n'
           '    s = json_syntax(\'{"a": 1}\')\n'
           '    assert isinstance(s, Syntax)\n'
           "    assert s.lexer.name.lower() == 'json'\n"
           '    print("All tests passed.")\n',
  'solution': 'from rich.syntax import Syntax\n'
              '\n'
              'def json_syntax(text: str):\n'
              "    return Syntax(text, 'json', theme='monokai')\n"},
 {'slug': '15_simple_table',
  'track': 'rich',
  'difficulty': 'easy',
  'title': 'Simple Data Table',
  'tags': ['rich', 'table'],
  'description': 'Build a Table with columns Name and Value and one row from the given name/value pair.',
  'examples': "pair_table('x', '1') -> Table with 1 row",
  'hint': 'Table(); add_column twice; add_row(name, value)',
  'syntax_hint': "table.add_column('Name'); table.add_row(name, value)",
  'signature': 'def pair_table(name: str, value: str):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from rich.table import Table\n'
           "    t = pair_table('x', '1')\n"
           '    assert isinstance(t, Table)\n'
           '    assert len(t.columns) == 2\n'
           '    assert len(t.rows) == 1\n'
           '    print("All tests passed.")\n',
  'solution': 'from rich.table import Table\n'
              '\n'
              'def pair_table(name: str, value: str):\n'
              '    table = Table()\n'
              "    table.add_column('Name')\n"
              "    table.add_column('Value')\n"
              '    table.add_row(name, value)\n'
              '    return table\n'},
 {'slug': '16_justify_text',
  'track': 'rich',
  'difficulty': 'easy',
  'title': 'Justify Text',
  'tags': ['rich', 'text'],
  'description': 'Return a rich.align.Align renderable centering the string in the given width.',
  'examples': "justify_line('hi', 20) -> Align center renderable",
  'hint': 'Use rich.align.Align.center(s, width=width).',
  'syntax_hint': 'from rich.align import Align; Align.center(s, width=width)',
  'signature': 'def justify_line(s: str, width: int = 20):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from rich.align import Align\n'
           "    t = justify_line('hi', 20)\n"
           '    assert isinstance(t, Align)\n'
           "    assert t.renderable == 'hi'\n"
           '    print("All tests passed.")\n',
  'solution': 'from rich.align import Align\n'
              '\n'
              'def justify_line(s: str, width: int = 20):\n'
              '    return Align.center(s, width=width)\n'},
 {'slug': '17_emoji_strip',
  'track': 'rich',
  'difficulty': 'easy',
  'title': 'Strip Emoji',
  'tags': ['rich', 'text'],
  'description': 'Remove emoji characters from text using a simple regex (Unicode emoji ranges not required; strip '
                 'chars with ord > 0xFFFF or common emoji).',
  'examples': "strip_emoji('hi 👋') -> 'hi '",
  'hint': 'Filter chars where ord(c) < 0x10000 or use regex.',
  'syntax_hint': "''.join(c for c in s if ord(c) < 0x10000)",
  'signature': 'def strip_emoji(s: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert strip_emoji('hi 👋') == 'hi '\n"
           "    assert strip_emoji('plain') == 'plain'\n"
           "    assert '🎉' not in strip_emoji('x 🎉 y')\n"
           '    print("All tests passed.")\n',
  'solution': "def strip_emoji(s: str) -> str:\n    return ''.join(c for c in s if ord(c) < 0x10000)\n"},
 {'slug': '18_box_draw',
  'track': 'rich',
  'difficulty': 'easy',
  'title': 'Box Panel',
  'tags': ['rich', 'panel'],
  'description': 'Return a Panel around text using box style ROUNDED.',
  'examples': "box_panel('msg') -> Panel with ROUNDED box",
  'hint': 'Panel(text, box=box.ROUNDED)',
  'syntax_hint': 'from rich.panel import Panel; from rich import box; Panel(s, box=box.ROUNDED)',
  'signature': 'def box_panel(text: str):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from rich.panel import Panel\n'
           '    from rich import box\n'
           "    p = box_panel('msg')\n"
           '    assert isinstance(p, Panel)\n'
           '    assert p.box == box.ROUNDED\n'
           '    print("All tests passed.")\n',
  'solution': 'from rich import box\n'
              'from rich.panel import Panel\n'
              '\n'
              'def box_panel(text: str):\n'
              '    return Panel(text, box=box.ROUNDED)\n'},
 {'slug': '19_color_parse',
  'track': 'rich',
  'difficulty': 'medium',
  'title': 'Parse Style Color',
  'tags': ['rich', 'style'],
  'description': "Given 'bold red' style string, return a rich.style.Style with bold True and color red.",
  'examples': "parse_style('bold red') -> Style",
  'hint': "Style.parse('bold red')",
  'syntax_hint': 'from rich.style import Style; Style.parse(s)',
  'signature': 'def parse_style(s: str):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from rich.style import Style\n'
           "    st = parse_style('bold red')\n"
           '    assert isinstance(st, Style)\n'
           '    assert st.bold is True\n'
           "    assert 'red' in str(st.color).lower()\n"
           '    print("All tests passed.")\n',
  'solution': 'from rich.style import Style\n\ndef parse_style(s: str):\n    return Style.parse(s)\n'},
 {'slug': '13_create_index_sql',
  'track': 'sqlite',
  'difficulty': 'easy',
  'title': 'Create Index SQL',
  'tags': ['sqlite', 'sql'],
  'description': 'Return the SQL string to create index idx_name on table users(column name).',
  'examples': "index_sql('users', 'name') -> 'CREATE INDEX ...'",
  'hint': 'Static f-string with CREATE INDEX IF NOT EXISTS.',
  'syntax_hint': 'CREATE INDEX IF NOT EXISTS idx_{table}_{col} ON {table}({col})',
  'signature': 'def index_sql(table: str, column: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    s = index_sql('users', 'name')\n"
           "    assert 'CREATE INDEX' in s.upper()\n"
           "    assert 'users' in s and 'name' in s\n"
           "    assert index_sql('t', 'x') == index_sql('t', 'x')\n"
           '    print("All tests passed.")\n',
  'solution': 'def index_sql(table: str, column: str) -> str:\n'
              "    return f'CREATE INDEX IF NOT EXISTS idx_{table}_{column} ON {table}({column})'\n"},
 {'slug': '14_group_by_having',
  'track': 'sqlite',
  'difficulty': 'medium',
  'title': 'GROUP BY HAVING',
  'tags': ['sqlite', 'sql'],
  'description': 'Create in-memory db, insert (dept, sales) rows, return depts with SUM(sales) > threshold.',
  'examples': 'depts_over(rows, 100) -> list of dept names',
  'hint': 'GROUP BY dept HAVING SUM(sales) > ?',
  'syntax_hint': 'SELECT dept FROM t GROUP BY dept HAVING SUM(sales) > ?',
  'signature': 'def depts_over(rows: list[tuple[str, int]], threshold: int) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    rows = [('a', 50), ('a', 60), ('b', 30)]\n"
           "    assert depts_over(rows, 100) == ['a']\n"
           '    assert depts_over(rows, 200) == []\n'
           '    assert depts_over([], 0) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def depts_over(rows: list[tuple[str, int]], threshold: int) -> list[str]:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    conn.execute('CREATE TABLE t (dept TEXT, sales INTEGER)')\n"
              "    conn.executemany('INSERT INTO t VALUES (?, ?)', rows)\n"
              '    cur = conn.execute(\n'
              "        'SELECT dept FROM t GROUP BY dept HAVING SUM(sales) > ? ORDER BY dept',\n"
              '        (threshold,),\n'
              '    )\n'
              '    result = [r[0] for r in cur.fetchall()]\n'
              '    conn.close()\n'
              '    return result\n'},
 {'slug': '15_limit_offset',
  'track': 'sqlite',
  'difficulty': 'easy',
  'title': 'LIMIT OFFSET Page',
  'tags': ['sqlite', 'sql'],
  'description': 'Query items(name) with ORDER BY name LIMIT size OFFSET (page-1)*size; page is 1-based.',
  'examples': 'page_names(names, page=2, size=2) -> third and fourth names',
  'hint': 'OFFSET (page-1)*size LIMIT size',
  'syntax_hint': 'ORDER BY name LIMIT ? OFFSET ?',
  'signature': 'def page_names(names: list[str], page: int, size: int) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    names = ['a', 'b', 'c', 'd', 'e']\n"
           "    assert page_names(names, 1, 2) == ['a', 'b']\n"
           "    assert page_names(names, 2, 2) == ['c', 'd']\n"
           "    assert page_names(names, 3, 2) == ['e']\n"
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def page_names(names: list[str], page: int, size: int) -> list[str]:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    conn.execute('CREATE TABLE items (name TEXT)')\n"
              "    conn.executemany('INSERT INTO items VALUES (?)', [(n,) for n in names])\n"
              '    offset = (page - 1) * size\n'
              '    rows = conn.execute(\n'
              "        'SELECT name FROM items ORDER BY name LIMIT ? OFFSET ?',\n"
              '        (size, offset),\n'
              '    ).fetchall()\n'
              '    conn.close()\n'
              '    return [r[0] for r in rows]\n'},
 {'slug': '16_union_query',
  'track': 'sqlite',
  'difficulty': 'medium',
  'title': 'UNION Query',
  'tags': ['sqlite', 'sql'],
  'description': 'Insert names into tables a and b; return sorted unique names from UNION ALL then dedupe in Python, '
                 'or use UNION.',
  'examples': "union_names(['a','b'], ['b','c']) -> ['a','b','c']",
  'hint': 'SELECT name FROM a UNION SELECT name FROM b',
  'syntax_hint': 'UNION removes duplicates automatically',
  'signature': 'def union_names(list_a: list[str], list_b: list[str]) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert union_names(['a', 'b'], ['b', 'c']) == ['a', 'b', 'c']\n"
           "    assert union_names([], ['x']) == ['x']\n"
           "    assert union_names(['z'], []) == ['z']\n"
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def union_names(list_a: list[str], list_b: list[str]) -> list[str]:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    conn.execute('CREATE TABLE a (name TEXT)')\n"
              "    conn.execute('CREATE TABLE b (name TEXT)')\n"
              "    conn.executemany('INSERT INTO a VALUES (?)', [(n,) for n in list_a])\n"
              "    conn.executemany('INSERT INTO b VALUES (?)', [(n,) for n in list_b])\n"
              '    rows = conn.execute(\n'
              "        'SELECT name FROM a UNION SELECT name FROM b ORDER BY name'\n"
              '    ).fetchall()\n'
              '    conn.close()\n'
              '    return [r[0] for r in rows]\n'},
 {'slug': '17_case_when',
  'track': 'sqlite',
  'difficulty': 'medium',
  'title': 'CASE WHEN Label',
  'tags': ['sqlite', 'sql'],
  'description': "Insert scores; return list of labels: 'pass' if score >= 60 else 'fail'.",
  'examples': "label_scores([55, 70]) -> ['fail', 'pass']",
  'hint': "SELECT CASE WHEN score >= 60 THEN 'pass' ELSE 'fail' END",
  'syntax_hint': "CASE WHEN score >= 60 THEN 'pass' ELSE 'fail' END",
  'signature': 'def label_scores(scores: list[int]) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert label_scores([55, 70]) == ['fail', 'pass']\n"
           "    assert label_scores([60]) == ['pass']\n"
           '    assert label_scores([]) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def label_scores(scores: list[int]) -> list[str]:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    conn.execute('CREATE TABLE t (score INTEGER)')\n"
              "    conn.executemany('INSERT INTO t VALUES (?)', [(s,) for s in scores])\n"
              '    rows = conn.execute(\n'
              '        "SELECT CASE WHEN score >= 60 THEN \'pass\' ELSE \'fail\' END FROM t"\n'
              '    ).fetchall()\n'
              '    conn.close()\n'
              '    return [r[0] for r in rows]\n'},
 {'slug': '18_distinct_count',
  'track': 'sqlite',
  'difficulty': 'easy',
  'title': 'Distinct Count',
  'tags': ['sqlite', 'sql'],
  'description': 'Insert values into tags(name); return COUNT(DISTINCT name).',
  'examples': "distinct_count(['a','b','a']) -> 2",
  'hint': 'SELECT COUNT(DISTINCT name) FROM tags',
  'syntax_hint': 'COUNT(DISTINCT name)',
  'signature': 'def distinct_count(names: list[str]) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert distinct_count(['a', 'b', 'a']) == 2\n"
           '    assert distinct_count([]) == 0\n'
           "    assert distinct_count(['x']) == 1\n"
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def distinct_count(names: list[str]) -> int:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    conn.execute('CREATE TABLE tags (name TEXT)')\n"
              "    conn.executemany('INSERT INTO tags VALUES (?)', [(n,) for n in names])\n"
              "    n = conn.execute('SELECT COUNT(DISTINCT name) FROM tags').fetchone()[0]\n"
              '    conn.close()\n'
              '    return n\n'},
 {'slug': '19_table_info',
  'track': 'sqlite',
  'difficulty': 'medium',
  'title': 'Table Info Columns',
  'tags': ['sqlite', 'pragma'],
  'description': 'Create table with given column definitions dict name->type; return column names via PRAGMA '
                 'table_info.',
  'examples': "table_columns({'id':'INTEGER','name':'TEXT'}) -> ['id','name']",
  'hint': 'CREATE TABLE then PRAGMA table_info(t)',
  'syntax_hint': 'PRAGMA table_info(users); row[1] is column name',
  'signature': 'def table_columns(columns: dict[str, str]) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    cols = table_columns({'id': 'INTEGER', 'name': 'TEXT'})\n"
           "    assert cols == ['id', 'name']\n"
           "    assert table_columns({'x': 'REAL'}) == ['x']\n"
           '    print("All tests passed.")\n',
  'solution': 'import sqlite3\n'
              '\n'
              'def table_columns(columns: dict[str, str]) -> list[str]:\n'
              "    conn = sqlite3.connect(':memory:')\n"
              "    parts = ', '.join(f'{name} {ctype}' for name, ctype in columns.items())\n"
              "    conn.execute(f'CREATE TABLE users ({parts})')\n"
              "    rows = conn.execute('PRAGMA table_info(users)').fetchall()\n"
              '    conn.close()\n'
              '    return [r[1] for r in rows]\n'},
 {'slug': '12_prepared_post',
  'track': 'requests',
  'difficulty': 'medium',
  'title': 'Prepared POST',
  'tags': ['requests'],
  'description': 'Build and return a PreparedRequest for POST to url with form data dict (no network).',
  'examples': "prepare_post(url, {'a':'1'}) -> PreparedRequest with method POST",
  'hint': "Request('POST', url, data=data); Session().prepare_request(req)",
  'syntax_hint': 'from requests import Request, Session',
  'signature': 'def prepare_post(url: str, data: dict):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from requests import PreparedRequest\n'
           "    p = prepare_post('https://x.test/api', {'a': '1'})\n"
           '    assert isinstance(p, PreparedRequest)\n'
           "    assert p.method == 'POST'\n"
           '    body = p.body if isinstance(p.body, str) else p.body.decode()\n'
           "    assert 'a=1' in body\n"
           '    print("All tests passed.")\n',
  'solution': 'from requests import Request, Session\n'
              '\n'
              'def prepare_post(url: str, data: dict):\n'
              "    req = Request('POST', url, data=data)\n"
              '    return Session().prepare_request(req)\n'},
 {'slug': '13_redirect_flag',
  'track': 'requests',
  'difficulty': 'easy',
  'title': 'Redirect Flag',
  'tags': ['requests'],
  'description': 'Return whether a requests.Session should follow redirects for the given allow_redirects bool.',
  'examples': 'session_redirects(True) -> Session with allow_redirects behavior stored',
  'hint': 'Store allow_redirects on a simple wrapper or return session max_redirects config.',
  'syntax_hint': 's = requests.Session(); note: allow_redirects is per-request; return dict flag',
  'signature': 'def should_follow(allow: bool, status: int) -> bool:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert should_follow(True, 302) is True\n'
           '    assert should_follow(False, 302) is False\n'
           '    assert should_follow(True, 200) is True\n'
           '    print("All tests passed.")\n',
  'solution': 'def should_follow(allow: bool, status: int) -> bool:\n'
              '    if status in (301, 302, 303, 307, 308):\n'
              '        return allow\n'
              '    return True\n'},
 {'slug': '14_stream_false',
  'track': 'requests',
  'difficulty': 'easy',
  'title': 'Stream Disabled',
  'tags': ['requests'],
  'description': 'Return kwargs dict for requests.get with stream=False explicitly.',
  'examples': "no_stream() -> {'stream': False}",
  'hint': "Return {'stream': False}.",
  'syntax_hint': "return {'stream': False}",
  'signature': 'def no_stream() -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert no_stream() == {'stream': False}\n"
           "    assert no_stream()['stream'] is False\n"
           '    print("All tests passed.")\n',
  'solution': "def no_stream() -> dict:\n    return {'stream': False}\n"},
 {'slug': '15_hooks_dict',
  'track': 'requests',
  'difficulty': 'medium',
  'title': 'Response Hooks Dict',
  'tags': ['requests', 'hooks'],
  'description': "Given a callback function, return a requests hooks dict that registers it for the 'response' event.",
  'examples': "build_hooks(fn) -> {'response': [fn]}",
  'hint': 'Hooks map event name to list of callables.',
  'syntax_hint': "return {'response': [callback]}",
  'signature': 'def build_hooks(callback) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    log = []\n'
           '    def cb(r, *a, **k): log.append(r)\n'
           '    h = build_hooks(cb)\n'
           "    assert 'response' in h\n"
           "    assert h['response'][0] is cb\n"
           '    print("All tests passed.")\n',
  'solution': "def build_hooks(callback) -> dict:\n    return {'response': [callback]}\n"},
 {'slug': '16_trust_env_false',
  'track': 'requests',
  'difficulty': 'easy',
  'title': 'Trust Env Disabled',
  'tags': ['requests'],
  'description': 'Return a requests.Session with trust_env set to False.',
  'examples': 'session_no_env().trust_env is False',
  'hint': 'Create Session then assign s.trust_env = False.',
  'syntax_hint': 's = requests.Session(); s.trust_env = False',
  'signature': 'def session_no_env():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    s = session_no_env()\n'
           '    import requests\n'
           '    assert isinstance(s, requests.Session)\n'
           '    assert s.trust_env is False\n'
           '    print("All tests passed.")\n',
  'solution': 'import requests\n'
              '\n'
              'def session_no_env():\n'
              '    s = requests.Session()\n'
              '    s.trust_env = False\n'
              '    return s\n'},
 {'slug': '17_encode_params',
  'track': 'requests',
  'difficulty': 'easy',
  'title': 'Encode Query Params',
  'tags': ['requests', 'url'],
  'description': "Encode params dict into a query string using requests' prepared request or urllib.",
  'examples': "encode_params({'a': 1, 'b': 2}) contains a=1 and b=2",
  'hint': 'requests.models.RequestEncodingMixin._encode_params or urlencode',
  'syntax_hint': 'from urllib.parse import urlencode',
  'signature': 'def encode_params(params: dict) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    s = encode_params({'a': 1, 'b': 2})\n"
           "    assert 'a=1' in s and 'b=2' in s\n"
           "    assert encode_params({}) == ''\n"
           '    print("All tests passed.")\n',
  'solution': 'from urllib.parse import urlencode\n'
              '\n'
              'def encode_params(params: dict) -> str:\n'
              '    return urlencode(params)\n'},
 {'slug': '18_merge_cookies',
  'track': 'requests',
  'difficulty': 'easy',
  'title': 'Merge Cookies',
  'tags': ['requests', 'cookies'],
  'description': 'Merge two cookie dicts; values from the second override the first.',
  'examples': "merge_cookies({'a':'1'},{'a':'2','b':'3'}) -> {'a':'2','b':'3'}",
  'hint': 'Dict union {**a, **b}.',
  'syntax_hint': 'return {**first, **second}',
  'signature': 'def merge_cookies(a: dict, b: dict) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert merge_cookies({'a': '1'}, {'a': '2', 'b': '3'}) == {'a': '2', 'b': '3'}\n"
           "    assert merge_cookies({}, {'x': '1'}) == {'x': '1'}\n"
           '    print("All tests passed.")\n',
  'solution': 'def merge_cookies(a: dict, b: dict) -> dict:\n    return {**a, **b}\n'},
 {'slug': '11_frame_specs',
  'track': 'tkinter',
  'difficulty': 'easy',
  'title': 'Frame Specs',
  'tags': ['tkinter', 'frame'],
  'description': "Given list of frame names, return specs dicts with name, relief 'groove', borderwidth 2.",
  'examples': "frame_specs(['main']) -> [{'name':'main','relief':'groove','borderwidth':2}]",
  'hint': 'List comprehension building dicts.',
  'syntax_hint': "[{'name': n, 'relief': 'groove', 'borderwidth': 2} for n in names]",
  'signature': 'def frame_specs(names: list[str]) -> list[dict]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert frame_specs(['main']) == [{'name': 'main', 'relief': 'groove', 'borderwidth': 2}]\n"
           '    assert frame_specs([]) == []\n'
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              'def frame_specs(names: list[str]) -> list[dict]:\n'
              "    return [{'name': n, 'relief': 'groove', 'borderwidth': 2} for n in names]\n"},
 {'slug': '12_canvas_coords',
  'track': 'tkinter',
  'difficulty': 'easy',
  'title': 'Canvas Coordinates',
  'tags': ['tkinter', 'canvas'],
  'description': "Given (x1,y1,x2,y2), return canvas rect spec dict with coords and outline 'black'.",
  'examples': "rect_spec(0,0,10,10) -> {'coords':(0,0,10,10),'outline':'black'}",
  'hint': 'Return plain dict with coords tuple.',
  'syntax_hint': "return {'coords': (x1, y1, x2, y2), 'outline': 'black'}",
  'signature': 'def rect_spec(x1: int, y1: int, x2: int, y2: int) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert rect_spec(0, 0, 10, 10) == {'coords': (0, 0, 10, 10), 'outline': 'black'}\n"
           "    assert rect_spec(1, 2, 3, 4)['coords'] == (1, 2, 3, 4)\n"
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              'def rect_spec(x1: int, y1: int, x2: int, y2: int) -> dict:\n'
              "    return {'coords': (x1, y1, x2, y2), 'outline': 'black'}\n"},
 {'slug': '13_scrollbar_link',
  'track': 'tkinter',
  'difficulty': 'medium',
  'title': 'Scrollbar Link Spec',
  'tags': ['tkinter', 'scrollbar'],
  'description': 'Given widget and scrollbar names, return link spec dict connecting them for yscrollcommand/xview.',
  'examples': "scroll_link('text','scroll') -> dict with command keys",
  'hint': 'Map widget yscrollcommand to scrollbar.set pattern as data.',
  'syntax_hint': "return {'widget': w, 'scrollbar': s, 'orient': 'vertical'}",
  'signature': 'def scroll_link(widget: str, scrollbar: str) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    s = scroll_link('text', 'vsb')\n"
           "    assert s['widget'] == 'text'\n"
           "    assert s['scrollbar'] == 'vsb'\n"
           "    assert s['orient'] == 'vertical'\n"
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              'def scroll_link(widget: str, scrollbar: str) -> dict:\n'
              "    return {'widget': widget, 'scrollbar': scrollbar, 'orient': 'vertical'}\n"},
 {'slug': '14_event_binding_spec',
  'track': 'tkinter',
  'difficulty': 'easy',
  'title': 'Event Binding Spec',
  'tags': ['tkinter', 'events'],
  'description': "Given widget name and event sequence (e.g. '<Button-1>'), return binding spec dict.",
  'examples': "bind_spec('btn', '<Button-1>', 'on_click') -> binding dict",
  'hint': 'Dict with widget, sequence, handler keys.',
  'syntax_hint': "return {'widget': w, 'sequence': seq, 'handler': handler}",
  'signature': 'def bind_spec(widget: str, sequence: str, handler: str) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert bind_spec('btn', '<Button-1>', 'on_click') == {\n"
           "        'widget': 'btn', 'sequence': '<Button-1>', 'handler': 'on_click'}\n"
           "    assert bind_spec('x', '<Key>', 'h')['sequence'] == '<Key>'\n"
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              'def bind_spec(widget: str, sequence: str, handler: str) -> dict:\n'
              "    return {'widget': widget, 'sequence': sequence, 'handler': handler}\n"},
 {'slug': '15_font_tuple',
  'track': 'tkinter',
  'difficulty': 'easy',
  'title': 'Font Tuple Spec',
  'tags': ['tkinter', 'font'],
  'description': 'Return Tk font spec tuple (family, size, style) for given family, size, and optional style.',
  'examples': "font_tuple('Helvetica', 12, 'bold') -> ('Helvetica', 12, 'bold')",
  'hint': 'Return 3-tuple; default style empty string.',
  'syntax_hint': "return (family, size, style or '')",
  'signature': "def font_tuple(family: str, size: int, style: str = '') -> tuple:\n    pass",
  'tests': 'def run_tests() -> None:\n'
           "    assert font_tuple('Helvetica', 12, 'bold') == ('Helvetica', 12, 'bold')\n"
           "    assert font_tuple('Arial', 10) == ('Arial', 10, '')\n"
           "    assert font_tuple('Mono', 8, 'italic')[2] == 'italic'\n"
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              "def font_tuple(family: str, size: int, style: str = '') -> tuple:\n"
              "    return (family, size, style or '')\n"},
 {'slug': '16_image_ref_mock',
  'track': 'tkinter',
  'difficulty': 'easy',
  'title': 'Image Reference Spec',
  'tags': ['tkinter', 'image'],
  'description': 'Given path string, return image spec dict with path and keep_ref True (pattern for PhotoImage GC '
                 'safety).',
  'examples': "image_spec('/tmp/x.png') -> {'path':..., 'keep_ref': True}",
  'hint': 'Plain dict; no actual image load.',
  'syntax_hint': "return {'path': path, 'keep_ref': True}",
  'signature': 'def image_spec(path: str) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    s = image_spec('/tmp/x.png')\n"
           "    assert s['path'] == '/tmp/x.png'\n"
           "    assert s['keep_ref'] is True\n"
           "    assert image_spec('a.gif')['keep_ref'] is True\n"
           '    print("All tests passed.")\n',
  'solution': 'import tkinter  # noqa: F401\n'
              '\n'
              'def image_spec(path: str) -> dict:\n'
              "    return {'path': path, 'keep_ref': True}\n"},
 {'slug': '17_geometry_parse',
  'track': 'tkinter',
  'difficulty': 'medium',
  'title': 'Geometry Parse',
  'tags': ['tkinter', 'geometry'],
  'description': "Parse geometry string 'WxH+X+Y' into dict with width, height, x, y ints.",
  'examples': "parse_geometry('400x300+10+20') -> {'width':400,'height':300,'x':10,'y':20}",
  'hint': 'Regex or split on x and +.',
  'syntax_hint': 'import re; match WxH+X+Y pattern',
  'signature': 'def parse_geometry(s: str) -> dict:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert parse_geometry('400x300+10+20') == {'width': 400, 'height': 300, 'x': 10, 'y': 20}\n"
           "    assert parse_geometry('100x50+0+0')['width'] == 100\n"
           "    assert parse_geometry('800x600+5+15')['y'] == 15\n"
           '    print("All tests passed.")\n',
  'solution': 'import re\n'
              'import tkinter  # noqa: F401\n'
              '\n'
              "_GEOM = re.compile(r'^(\\d+)x(\\d+)\\+(\\d+)\\+(\\d+)$')\n"
              '\n'
              'def parse_geometry(s: str) -> dict:\n'
              '    m = _GEOM.match(s)\n'
              '    if not m:\n'
              "        raise ValueError('invalid geometry')\n"
              '    w, h, x, y = m.groups()\n'
              "    return {'width': int(w), 'height': int(h), 'x': int(x), 'y': int(y)}\n"},
 {'slug': '09_follow_redirects',
  'track': 'httpx',
  'difficulty': 'easy',
  'title': 'Follow Redirects Config',
  'tags': ['httpx'],
  'description': 'Return an httpx.Client with follow_redirects=True and MockTransport (no network).',
  'examples': 'client_follow() -> Client with follow_redirects True',
  'hint': 'httpx.Client(follow_redirects=True, transport=MockTransport(...))',
  'syntax_hint': 'httpx.Client(follow_redirects=True, transport=httpx.MockTransport(handler))',
  'signature': 'def client_follow():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import httpx\n'
           '    c = client_follow()\n'
           '    assert isinstance(c, httpx.Client)\n'
           '    assert c.follow_redirects is True\n'
           '    c.close()\n'
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def client_follow():\n'
              '    def handler(request):\n'
              "        return httpx.Response(200, json={'ok': True})\n"
              '    return httpx.Client(\n'
              '        follow_redirects=True,\n'
              '        transport=httpx.MockTransport(handler),\n'
              '    )\n'},
 {'slug': '10_cookies_jar',
  'track': 'httpx',
  'difficulty': 'medium',
  'title': 'Cookies on Client',
  'tags': ['httpx', 'cookies'],
  'description': 'Return httpx.Client with cookies set and MockTransport; GET returns cookie value in JSON.',
  'examples': "client_with_cookies({'sid':'abc'}) sends Cookie header",
  'hint': 'Pass cookies= to Client; verify via MockTransport handler.',
  'syntax_hint': "httpx.Client(cookies={'sid': 'abc'}, transport=MockTransport(handler))",
  'signature': 'def client_with_cookies(cookies: dict):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import httpx\n'
           '    captured = {}\n'
           '    def handler(request):\n'
           "        captured['cookie'] = request.headers.get('cookie', '')\n"
           "        return httpx.Response(200, json={'ok': True})\n"
           "    c = client_with_cookies({'sid': 'abc'})\n"
           '    c._transport = httpx.MockTransport(handler)\n'
           "    c.get('https://x.test/')\n"
           "    assert 'sid=abc' in captured.get('cookie', '')\n"
           '    c.close()\n'
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def client_with_cookies(cookies: dict):\n'
              '    def handler(request):\n'
              "        return httpx.Response(200, json={'ok': True})\n"
              '    return httpx.Client(cookies=cookies, transport=httpx.MockTransport(handler))\n'},
 {'slug': '11_event_hooks',
  'track': 'httpx',
  'difficulty': 'medium',
  'title': 'Event Hooks',
  'tags': ['httpx', 'hooks'],
  'description': 'Build httpx.Client with event hook that records request method; return recorded list via GET.',
  'examples': "fetch_with_hook() records 'GET'",
  'hint': "event_hooks={'request': [callback]} on Client.",
  'syntax_hint': "event_hooks={'request': [lambda req: log.append(req.method)]}",
  'signature': 'def fetch_with_hook(url: str) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    log = fetch_with_hook('https://x.test/api')\n"
           "    assert log == ['GET']\n"
           "    assert fetch_with_hook('https://other.test/') == ['GET']\n"
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def fetch_with_hook(url: str) -> list[str]:\n'
              '    log: list[str] = []\n'
              '    def on_request(request):\n'
              '        log.append(request.method)\n'
              '    def handler(request):\n'
              '        return httpx.Response(200)\n'
              '    with httpx.Client(\n'
              '        transport=httpx.MockTransport(handler),\n'
              "        event_hooks={'request': [on_request]},\n"
              '    ) as client:\n'
              '        client.get(url)\n'
              '    return log\n'},
 {'slug': '12_delete_method',
  'track': 'httpx',
  'difficulty': 'easy',
  'title': 'DELETE Request',
  'tags': ['httpx'],
  'description': 'Build httpx.Request for DELETE method (no network).',
  'examples': 'delete_request(url) -> Request with method DELETE',
  'hint': "httpx.Request('DELETE', url)",
  'syntax_hint': "httpx.Request('DELETE', url)",
  'signature': 'def delete_request(url: str):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import httpx\n'
           "    req = delete_request('https://x.test/items/1')\n"
           '    assert isinstance(req, httpx.Request)\n'
           "    assert req.method == 'DELETE'\n"
           "    assert str(req.url) == 'https://x.test/items/1'\n"
           '    print("All tests passed.")\n',
  'solution': "import httpx\n\ndef delete_request(url: str):\n    return httpx.Request('DELETE', url)\n"},
 {'slug': '13_patch_method',
  'track': 'httpx',
  'difficulty': 'medium',
  'title': 'PATCH JSON Request',
  'tags': ['httpx', 'json'],
  'description': 'Build httpx.Request for PATCH with JSON body (no network).',
  'examples': "patch_json(url, {'name':'x'}) has JSON body",
  'hint': "httpx.Request('PATCH', url, json=payload)",
  'syntax_hint': "httpx.Request('PATCH', url, json=payload)",
  'signature': 'def patch_json(url: str, payload: dict):\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import json\n'
           '    import httpx\n'
           "    req = patch_json('https://x.test/items/1', {'name': 'x'})\n"
           "    assert req.method == 'PATCH'\n"
           "    assert json.loads(req.content) == {'name': 'x'}\n"
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def patch_json(url: str, payload: dict):\n'
              "    return httpx.Request('PATCH', url, json=payload)\n"},
 {'slug': '14_http2_flag',
  'track': 'httpx',
  'difficulty': 'easy',
  'title': 'HTTP/2 Flag',
  'tags': ['httpx'],
  'description': 'Return httpx.Client with http2=False and MockTransport (explicitly disable HTTP/2).',
  'examples': 'client_no_http2()._transport is MockTransport',
  'hint': 'httpx.Client(http2=False, transport=...)',
  'syntax_hint': 'httpx.Client(http2=False, transport=httpx.MockTransport(handler))',
  'signature': 'def client_no_http2():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    import httpx\n'
           '    c = client_no_http2()\n'
           '    assert isinstance(c, httpx.Client)\n'
           '    assert c._transport is not None\n'
           '    c.close()\n'
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def client_no_http2():\n'
              '    def handler(request):\n'
              '        return httpx.Response(200)\n'
              '    return httpx.Client(http2=False, transport=httpx.MockTransport(handler))\n'},
 {'slug': '15_base_url_client',
  'track': 'httpx',
  'difficulty': 'medium',
  'title': 'Base URL Client',
  'tags': ['httpx', 'url'],
  'description': 'Return function using httpx.Client(base_url=...) with MockTransport to GET relative path and return '
                 'status.',
  'examples': "get_status('/api') with base_url returns 200",
  'hint': "Client(base_url='https://x.test', transport=MockTransport(...))",
  'syntax_hint': 'with httpx.Client(base_url=base, transport=...) as c: c.get(path)',
  'signature': 'def get_status(base: str, path: str) -> int:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert get_status('https://x.test', '/api') == 200\n"
           "    assert get_status('https://x.test', '/health') == 200\n"
           '    print("All tests passed.")\n',
  'solution': 'import httpx\n'
              '\n'
              'def get_status(base: str, path: str) -> int:\n'
              '    def handler(request):\n'
              '        return httpx.Response(200)\n'
              '    with httpx.Client(base_url=base, transport=httpx.MockTransport(handler)) as client:\n'
              '        return client.get(path).status_code\n'},
 {'slug': '09_parent_tag',
  'track': 'bs4',
  'difficulty': 'easy',
  'title': 'Parent Tag Name',
  'tags': ['bs4', 'html'],
  'description': 'Parse HTML and return the parent tag name of the first <span> element, or None.',
  'examples': "parent_name('<div><span>x</span></div>') -> 'div'",
  'hint': "soup.find('span').parent.name",
  'syntax_hint': "tag = soup.find('span'); tag.parent.name if tag else None",
  'signature': 'def parent_name(html: str) -> str | None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert parent_name('<div><span>x</span></div>') == 'div'\n"
           "    assert parent_name('<span>lonely</span>') in ('[document]', 'html', 'body')\n"
           "    assert parent_name('<p>no span</p>') is None\n"
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def parent_name(html: str) -> str | None:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    span = soup.find('span')\n"
              '    if span is None or span.parent is None:\n'
              '        return None\n'
              '    return span.parent.name\n'},
 {'slug': '10_next_sibling',
  'track': 'bs4',
  'difficulty': 'easy',
  'title': 'Next Sibling Text',
  'tags': ['bs4', 'html'],
  'description': 'Return stripped text of the next sibling element after the first <h1>, or None.',
  'examples': "next_after_h1('<h1>T</h1><p>body</p>') -> 'body'",
  'hint': "find('h1').find_next_sibling().get_text(strip=True)",
  'syntax_hint': "h1 = soup.find('h1'); sib = h1.find_next_sibling()",
  'signature': 'def next_after_h1(html: str) -> str | None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert next_after_h1('<h1>T</h1><p>body</p>') == 'body'\n"
           "    assert next_after_h1('<h1>Only</h1>') is None\n"
           "    assert next_after_h1('<p>x</p>') is None\n"
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def next_after_h1(html: str) -> str | None:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    h1 = soup.find('h1')\n"
              '    if h1 is None:\n'
              '        return None\n'
              '    sib = h1.find_next_sibling()\n'
              '    if sib is None:\n'
              '        return None\n'
              '    return sib.get_text(strip=True)\n'},
 {'slug': '11_decompose_tag',
  'track': 'bs4',
  'difficulty': 'medium',
  'title': 'Decompose Script Tag',
  'tags': ['bs4', 'html'],
  'description': 'Parse HTML, decompose all <script> tags, return remaining text stripped.',
  'examples': "without_scripts('<p>hi</p><script>x</script>') -> 'hi'",
  'hint': "for tag in soup.find_all('script'): tag.decompose()",
  'syntax_hint': "soup.find_all('script'); tag.decompose()",
  'signature': 'def without_scripts(html: str) -> str:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert without_scripts('<p>hi</p><script>x</script>') == 'hi'\n"
           "    assert without_scripts('<script>a</script><div>ok</div>') == 'ok'\n"
           "    assert without_scripts('<p>plain</p>') == 'plain'\n"
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def without_scripts(html: str) -> str:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    for tag in soup.find_all('script'):\n"
              '        tag.decompose()\n'
              '    return soup.get_text(strip=True)\n'},
 {'slug': '12_find_all_text',
  'track': 'bs4',
  'difficulty': 'easy',
  'title': 'Find All Paragraph Text',
  'tags': ['bs4', 'html'],
  'description': 'Return list of stripped text from all <p> tags in order.',
  'examples': "paragraph_texts('<p>a</p><p>b</p>') -> ['a','b']",
  'hint': "[p.get_text(strip=True) for p in soup.find_all('p')]",
  'syntax_hint': "soup.find_all('p')",
  'signature': 'def paragraph_texts(html: str) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           "    assert paragraph_texts('<p>a</p><p>b</p>') == ['a', 'b']\n"
           "    assert paragraph_texts('<div>x</div>') == []\n"
           "    assert paragraph_texts('<p> one </p>') == ['one']\n"
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def paragraph_texts(html: str) -> list[str]:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    return [p.get_text(strip=True) for p in soup.find_all('p')]\n"},
 {'slug': '13_meta_tags',
  'track': 'bs4',
  'difficulty': 'medium',
  'title': 'Meta Tag Content',
  'tags': ['bs4', 'html'],
  'description': "Return dict of meta name -> content for <meta name='...' content='...'> tags.",
  'examples': "meta_dict(html) -> {'description': '...'}",
  'hint': "find_all('meta'); read name and content attrs.",
  'syntax_hint': "m.get('name'): m.get('content') for m in soup.find_all('meta') if m.get('name')",
  'signature': 'def meta_dict(html: str) -> dict[str, str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    html = \'<meta name="description" content="demo"><meta name="author" content="eli">\'\n'
           "    assert meta_dict(html) == {'description': 'demo', 'author': 'eli'}\n"
           "    assert meta_dict('<p>x</p>') == {}\n"
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def meta_dict(html: str) -> dict[str, str]:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              '    out: dict[str, str] = {}\n'
              "    for m in soup.find_all('meta'):\n"
              "        name = m.get('name')\n"
              '        if name:\n'
              "            out[name] = m.get('content', '')\n"
              '    return out\n'},
 {'slug': '14_img_alt',
  'track': 'bs4',
  'difficulty': 'easy',
  'title': 'Image Alt Texts',
  'tags': ['bs4', 'html'],
  'description': 'Return list of alt attribute values from all <img> tags (empty string if missing).',
  'examples': 'img_alts(\'<img alt="logo"><img>\') -> [\'logo\',\'\']',
  'hint': "[img.get('alt','') for img in soup.find_all('img')]",
  'syntax_hint': "soup.find_all('img')",
  'signature': 'def img_alts(html: str) -> list[str]:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    assert img_alts(\'<img alt="logo"><img>\') == [\'logo\', \'\']\n'
           "    assert img_alts('<p>x</p>') == []\n"
           '    assert img_alts(\'<img alt="a"><img alt="b">\') == [\'a\', \'b\']\n'
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def img_alts(html: str) -> list[str]:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    return [img.get('alt', '') for img in soup.find_all('img')]\n"},
 {'slug': '15_nested_find',
  'track': 'bs4',
  'difficulty': 'medium',
  'title': 'Nested Find',
  'tags': ['bs4', 'html'],
  'description': 'Find div.main then the first a href inside it; return href or None.',
  'examples': 'main_link(\'<div class="main"><a href="/x">go</a></div>\') -> \'/x\'',
  'hint': "soup.find('div', class_='main').find('a')['href']",
  'syntax_hint': "div = soup.find('div', class_='main'); a = div.find('a') if div else None",
  'signature': 'def main_link(html: str) -> str | None:\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    html = \'<div class="main"><a href="/x">go</a></div>\'\n'
           "    assert main_link(html) == '/x'\n"
           '    assert main_link(\'<div class="main"><p>x</p></div>\') is None\n'
           '    assert main_link(\'<a href="/y">y</a>\') is None\n'
           '    print("All tests passed.")\n',
  'solution': 'from bs4 import BeautifulSoup\n'
              '\n'
              'def main_link(html: str) -> str | None:\n'
              "    soup = BeautifulSoup(html, 'html.parser')\n"
              "    div = soup.find('div', class_='main')\n"
              '    if div is None:\n'
              '        return None\n'
              "    a = div.find('a')\n"
              '    if a is None:\n'
              '        return None\n'
              "    return a.get('href')\n"},
 {'slug': '09_version_option',
  'track': 'click',
  'difficulty': 'easy',
  'title': 'Version Option',
  'tags': ['click', 'cli'],
  'description': 'Return a click command that prints version when --version is passed.',
  'examples': "invoke --version -> '1.0.0'",
  'hint': "@click.version_option(version='1.0.0')",
  'syntax_hint': "@click.version_option('1.0.0')",
  'signature': 'def make_version_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_version_cli()\n'
           '    runner = CliRunner()\n'
           "    r = runner.invoke(cli, ['--version'])\n"
           "    assert '1.0.0' in r.output\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              '@click.command()\n'
              "@click.version_option('1.0.0')\n"
              'def _version_cli():\n'
              "    click.echo('app')\n"
              '\n'
              'def make_version_cli():\n'
              '    return _version_cli\n'},
 {'slug': '10_count_argument',
  'track': 'click',
  'difficulty': 'easy',
  'title': 'Count Argument',
  'tags': ['click', 'cli'],
  'description': "Return click command taking integer count arg; prints 'x' repeated count times on one line.",
  'examples': "invoke 3 -> 'xxx'",
  'hint': "@click.argument('count', type=int)",
  'syntax_hint': "click.echo('x' * count)",
  'signature': 'def make_count_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_count_cli()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, ['3']).output.strip() == 'xxx'\n"
           "    assert runner.invoke(cli, ['0']).output.strip() == ''\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_count_cli():\n'
              '    @click.command()\n'
              "    @click.argument('count', type=int)\n"
              '    def cli(count: int):\n'
              "        click.echo('x' * count)\n"
              '    return cli\n'},
 {'slug': '11_echo_greet',
  'track': 'click',
  'difficulty': 'easy',
  'title': 'Echo Greet',
  'tags': ['click', 'cli'],
  'description': "Return click command with --name option defaulting to 'world'; echoes 'Hello {name}!'.",
  'examples': "invoke -> 'Hello world!'; --name Ada -> 'Hello Ada!'",
  'hint': "@click.option('--name', default='world')",
  'syntax_hint': "click.echo(f'Hello {name}!')",
  'signature': 'def make_greet_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_greet_cli()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, []).output.strip() == 'Hello world!'\n"
           "    assert runner.invoke(cli, ['--name', 'Ada']).output.strip() == 'Hello Ada!'\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_greet_cli():\n'
              '    @click.command()\n'
              "    @click.option('--name', default='world')\n"
              '    def cli(name: str):\n'
              "        click.echo(f'Hello {name}!')\n"
              '    return cli\n'},
 {'slug': '12_confirmation_flag',
  'track': 'click',
  'difficulty': 'medium',
  'title': 'Confirmation Flag',
  'tags': ['click', 'cli'],
  'description': "Return click command with --yes flag; with --yes prints 'confirmed', without prints 'skipped'.",
  'examples': "invoke --yes -> 'confirmed'",
  'hint': "@click.option('--yes', is_flag=True)",
  'syntax_hint': 'if yes: echo confirmed else skipped',
  'signature': 'def make_confirm_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_confirm_cli()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, ['--yes']).output.strip() == 'confirmed'\n"
           "    assert runner.invoke(cli, []).output.strip() == 'skipped'\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_confirm_cli():\n'
              '    @click.command()\n'
              "    @click.option('--yes', is_flag=True)\n"
              '    def cli(yes: bool):\n'
              "        click.echo('confirmed' if yes else 'skipped')\n"
              '    return cli\n'},
 {'slug': '13_hidden_option',
  'track': 'click',
  'difficulty': 'medium',
  'title': 'Hidden Option',
  'tags': ['click', 'cli'],
  'description': "Return click command with hidden --token option; when provided prints 'ok', else 'no'.",
  'examples': "invoke --token x -> 'ok'",
  'hint': "@click.option('--token', hidden=True)",
  'syntax_hint': 'hidden=True keeps option out of help',
  'signature': 'def make_token_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_token_cli()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, ['--token', 'x']).output.strip() == 'ok'\n"
           "    assert runner.invoke(cli, []).output.strip() == 'no'\n"
           "    assert '--token' not in runner.invoke(cli, ['--help']).output\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_token_cli():\n'
              '    @click.command()\n'
              "    @click.option('--token', hidden=True, default=None)\n"
              '    def cli(token):\n'
              "        click.echo('ok' if token else 'no')\n"
              '    return cli\n'},
 {'slug': '14_nargs_variadic',
  'track': 'click',
  'difficulty': 'medium',
  'title': 'Variadic Arguments',
  'tags': ['click', 'cli'],
  'description': 'Return click command with nargs=-1 on files argument; prints space-joined args.',
  'examples': "invoke a b c -> 'a b c'",
  'hint': "@click.argument('files', nargs=-1)",
  'syntax_hint': "click.echo(' '.join(files))",
  'signature': 'def make_files_cli():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_files_cli()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, ['a', 'b', 'c']).output.strip() == 'a b c'\n"
           "    assert runner.invoke(cli, []).output.strip() == ''\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_files_cli():\n'
              '    @click.command()\n'
              "    @click.argument('files', nargs=-1)\n"
              '    def cli(files):\n'
              "        click.echo(' '.join(files))\n"
              '    return cli\n'},
 {'slug': '15_result_callback',
  'track': 'click',
  'difficulty': 'hard',
  'title': 'Result Callback',
  'tags': ['click', 'cli'],
  'description': "Return click group where subcommand 'add' returns two ints and group result callback prints their "
                 'sum.',
  'examples': "invoke add 2 3 -> '5'",
  'hint': '@cli.result_callback(); @click.argument x,y on subcommand',
  'syntax_hint': '@cli.result_callback() def process(result): click.echo(sum(result))',
  'signature': 'def make_sum_group():\n    pass',
  'tests': 'def run_tests() -> None:\n'
           '    from click.testing import CliRunner\n'
           '    cli = make_sum_group()\n'
           '    runner = CliRunner()\n'
           "    assert runner.invoke(cli, ['add', '2', '3']).output.strip() == '5'\n"
           "    assert runner.invoke(cli, ['add', '4', '5']).output.strip() == '9'\n"
           '    print("All tests passed.")\n',
  'solution': 'import click\n'
              '\n'
              'def make_sum_group():\n'
              '    @click.group()\n'
              '    def cli():\n'
              '        pass\n'
              '\n'
              '    @cli.result_callback()\n'
              '    def process(result):\n'
              '        if result is not None:\n'
              '            click.echo(str(sum(result)))\n'
              '\n'
              '    @cli.command()\n'
              "    @click.argument('x', type=int)\n"
              "    @click.argument('y', type=int)\n"
              '    def add(x: int, y: int):\n'
              '        return [x, y]\n'
              '\n'
              '    return cli\n'}]
