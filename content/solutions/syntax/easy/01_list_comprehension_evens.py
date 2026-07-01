def even_squares(numbers: list[int]) -> list[int]:
    return [x * x for x in numbers if x % 2 == 0]
