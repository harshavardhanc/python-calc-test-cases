# simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Number cannot be divided by 0.")
    return x / y


def pow(x, y):
    return x ** y
