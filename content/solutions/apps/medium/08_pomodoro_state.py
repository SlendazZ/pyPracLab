class Pomodoro:
    def __init__(self):
        self.mode = 'work'
        self.elapsed = 0
        self.dur = 25
    def tick(self) -> str:
        self.elapsed += 1
        if self.elapsed >= self.dur:
            self.mode = 'break' if self.mode == 'work' else 'work'
            self.dur = 5 if self.mode == 'break' else 25
            self.elapsed = 0
        return self.mode
