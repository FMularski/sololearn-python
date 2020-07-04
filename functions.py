def square_root(x):
    return x ** 0.5


def square_pow(x):
    return x ** 2


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if not b:
        return 0
    return a / b


ptr_to_fun = square_root
print(ptr_to_fun(9))
ptr_to_fun = square_pow
print(ptr_to_fun(4))
ptr_to_fun = add
print(ptr_to_fun(2, 3))

operations = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
print(operations.get('mul')(2, 16))

