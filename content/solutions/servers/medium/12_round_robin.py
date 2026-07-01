class RoundRobin:
    def __init__(self, hosts: list[str]):
        self.hosts = hosts
        self._i = 0
    def next(self) -> str:
        host = self.hosts[self._i]
        self._i = (self._i + 1) % len(self.hosts)
        return host
