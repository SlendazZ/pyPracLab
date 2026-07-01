def describe(status: int) -> str:
    match status:
        case 200:
            return 'ok'
        case 201:
            return 'created'
        case 404:
            return 'not found'
        case _:
            return 'error'
