def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    for a, b in prerequisites:
        graph[b].append(a)
    state = [0] * num_courses
    def dfs(node: int) -> bool:
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True
        state[node] = 1
        for nxt in graph[node]:
            if not dfs(nxt):
                return False
        state[node] = 2
        return True
    return all(dfs(i) for i in range(num_courses))
