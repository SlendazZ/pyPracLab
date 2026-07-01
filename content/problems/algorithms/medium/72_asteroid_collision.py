# title: Asteroid Collision
# track: algorithms
# difficulty: medium
# tags: stack, simulation
# description: |
# Positive moves right, negative left; same size destroy each other. Return final asteroids.
# examples:
# asteroid_collision([5,10,-5]) -> [5,10]
# hint: |
# Stack; negative asteroid collides with stack top while applicable.
# syntax_hint: |
# while stack and x < 0 < stack[-1]: compare sizes


def asteroid_collision(asteroids: list[int]) -> list[int]:
    pass


def run_tests() -> None:
    assert asteroid_collision([5, 10, -5]) == [5, 10]
    assert asteroid_collision([8, -8]) == []
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
