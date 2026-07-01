# title: Generate Parentheses
# track: algorithms
# difficulty: medium
# tags: backtracking
# description: |
# Return all well-formed combinations of n pairs of parentheses.
# examples:
# generate(3) -> ["((()))","(()())","(())()","()(())","()()()"]
# hint: |
# Recurse with counts of open and close used; only add ')' if close < open.
# syntax_hint: |
# def back(cur, open, close): if len(cur)==2*n: ...


def generate(n: int) -> list[str]:
    pass


def run_tests() -> None:
    assert sorted(generate(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert generate(1) == ["()"]
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
