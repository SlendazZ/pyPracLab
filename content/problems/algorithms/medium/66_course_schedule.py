# title: Course Schedule
# track: algorithms
# difficulty: medium
# tags: graph, dfs
# description: |
# prerequisites[i]=[a,b] means take b before a. Return True if all courses can finish.
# examples:
# can_finish(2, [[1,0]]) -> True
# hint: |
# Detect cycle in directed graph via DFS three-color or Kahn topo.
# syntax_hint: |
# build adjacency; dfs detect back edge


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    pass


def run_tests() -> None:
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(3, [[1, 0], [2, 0]]) is True
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
