def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack: list[int] = []
    for x in asteroids:
        while stack and x < 0 < stack[-1]:
            if stack[-1] < -x:
                stack.pop()
                continue
            if stack[-1] == -x:
                stack.pop()
            x = 0
            break
        if x:
            stack.append(x)
    return stack
