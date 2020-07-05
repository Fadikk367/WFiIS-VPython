import module
import random
import math

factorial = module.factorial
factorial_half = module.factorial_half

def choose_factorial(n):
    if int(n) == n:
        return factorial(n)
    else:
        return factorial_half(n)

n = 1e6

file = open('file1.txt', 'w')

def check_if_hit(shot):
    squares_sum = 0
    for i in shot:
        squares_sum += i * i
    if squares_sum < 1:
        return 1
    else:
        return 0
        
for dim in range(2, 21):
    hits = 0
    for i in range(1, 10**6 + 1):
        shot = [random.uniform(-1, 1) for x in range(dim)]
        hits += check_if_hit(shot)
    cub_Vol = 2**dim
    sphere_Vol = cub_Vol * hits / n
    math_sphere_Vol = math.pow(math.pi, dim / 2) / choose_factorial(dim / 2)
    (str(dim) + ') ' + str(sphere_Vol) + ', ' + str(sphere_Vol/math_sphere_Vol) + ', ' + str(hits) + '\n')
    hits = 0



