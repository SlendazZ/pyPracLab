# title: Fizz Buzz
# track: algorithms
# difficulty: easy
# tags: loop, string
# description: |
# Return a list of strings for 1..n: 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for both, else the number as a string.
# examples:
# fizzbuzz(5) -> ["1","2","Fizz","4","Buzz"]
# hint: |
# Check the combined condition first (15), then 3, then 5.
# syntax_hint: |
# str(i) if neither; build with if/elif/else


def fizzbuzz(n: int) -> list[str]:
    pass


def run_tests() -> None:
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(3)[2] == "Fizz"
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
