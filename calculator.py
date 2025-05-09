#기본 계산기기
def add(a, b):
    return a + b    
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def logarithm(a, base=10):
    if a <= 0 or base <= 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(a, base)