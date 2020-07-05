import module
import numpy as np

factorial = module.factorial
factorial_half = module.factorial_half

def choose_factorial(n):
    if int(n) == n:
        return factorial(n)
    else:
        return factorial_half(n)

n = 1e6

file = open('file2.txt', 'w')  
for dim in range(2, 21):
    array = np.random.uniform(-1, 1, (int(n), dim))
    squares_array = array ** 2
    rows_sum = squares_array.sum(axis = 1)
    results = ( rows_sum < 1)
    hits = results.sum()

    cub_Vol = 2**dim
    sphere_Vol = cub_Vol * hits / n
    math_sphere_Vol = np.power(np.pi, dim / 2) / choose_factorial(dim / 2)
    file.write(str(dim) + ') ' + str(sphere_Vol) + ', ' + str(sphere_Vol/math_sphere_Vol) + ', ' + str(hits) + '\n')



    