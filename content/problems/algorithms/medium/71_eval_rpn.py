# title: Evaluate Reverse Polish Notation
# track: algorithms
# difficulty: medium
# tags: stack, math
# description: |
# Evaluate valid RPN expression with + - * / on integers.
# examples:
# eval_rpn(["2","1","+","3","*"]) -> 9
# hint: |
# Stack numbers; on operator pop two and push result.
# syntax_hint: |
# stack = []; int(token) push else apply op


def eval_rpn(tokens: list[str]) -> int:
    pass


def run_tests() -> None:
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["10"]) == 10
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
