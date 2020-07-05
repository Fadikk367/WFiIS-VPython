import math

def factorial(n):
    result = 1
    while n>0:
        result *= n
        n = n - 1
    return result

def factorial_half(n):
    if n <= 1/2:
        return math.sqrt(math.pi)/2
    return n * factorial_half(n-1)

