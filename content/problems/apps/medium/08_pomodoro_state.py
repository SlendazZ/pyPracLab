# title: Pomodoro State Machine
# track: apps
# difficulty: medium
# tags: state
# description: |
# A Pomodoro cycles 'work' -> 'break' -> 'work'. Implement tick() that advances and returns the current mode after n ticks of 25 work / 5 break.
# examples:
# p = Pomodoro(); p.tick() x25 -> 'break'
# hint: |
# Track elapsed minutes; switch modes and reset the counter at the threshold.
# syntax_hint: |
# self.elapsed += 1; if self.elapsed >= self.dur: switch


class Pomodoro:
    pass


def run_tests() -> None:
    p = Pomodoro()
    assert p.mode == 'work'
    for _ in range(24):
        assert p.tick() == 'work'
    assert p.tick() == 'break'
    for _ in range(4):
        assert p.tick() == 'break'
    assert p.tick() == 'work'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
