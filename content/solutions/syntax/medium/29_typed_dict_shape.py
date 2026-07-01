from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def user(name: str, age: int) -> dict:
    return User(name=name, age=age)
