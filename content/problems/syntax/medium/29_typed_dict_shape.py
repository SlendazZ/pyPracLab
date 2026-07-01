# title: TypedDict User
# track: syntax
# difficulty: medium
# tags: typing
# description: |
# Given name and age, return a dict matching TypedDict User with keys name (str) and age (int).
# examples:
# user('Ada', 36) -> {'name':'Ada','age':36}
# hint: |
# Define TypedDict User; return {'name': name, 'age': age}.
# syntax_hint: |
# class User(TypedDict): name: str; age: int


def user(name: str, age: int) -> dict:
    pass


def run_tests() -> None:
    assert user('Ada', 36) == {'name': 'Ada', 'age': 36}
    assert user('Bob', 0)['age'] == 0
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
