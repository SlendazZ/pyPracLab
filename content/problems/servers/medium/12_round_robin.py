# title: Round Robin Picker
# track: servers
# difficulty: medium
# tags: load-balancer
# description: |
# Implement RoundRobin(hosts) with .next() cycling through hosts in order.
# examples:
# rb=RoundRobin(['a','b']); rb.next(); rb.next() -> 'a' then 'b'
# hint: |
# Store index modulo len(hosts).
# syntax_hint: |
# self._i = (self._i + 1) % len(self.hosts)


class RoundRobin:
    def __init__(self, hosts: list[str]): pass
    def next(self) -> str: pass


def run_tests() -> None:
    rb = RoundRobin(['a','b','c'])
    assert rb.next() == 'a'
    assert rb.next() == 'b'
    assert rb.next() == 'c'
    assert rb.next() == 'a'
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
