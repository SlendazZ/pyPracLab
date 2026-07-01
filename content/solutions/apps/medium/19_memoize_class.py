class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.cache: dict = {}
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.fn(*args)
        return self.cache[args]
