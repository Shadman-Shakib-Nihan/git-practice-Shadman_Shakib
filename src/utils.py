def add(a, b):
    return a + b

def subtract(a, b):
    if a < b:
        raise ValueError("a should be greater than or equal to b")
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b