def add(*args):
    return sum(args)


def subtract(*args):
    if len(args) == 1:
        return -args[0]
    else:
        return args[0] - sum(args[1:])


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    if len(args) == 0:
        return "Error: Division by Zero"
    elif len(args) == 1:
        return 1 / args[0]
    else:
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by Zero"
            result /= num
        return result

