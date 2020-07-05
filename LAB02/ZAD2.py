import math
import random

file = open('filePI_2.txt', 'w')

hits = 0
for i in range(1, int(1e7)):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y <= 1:
        hits += 1

    file.write(str(i) + ') ' + str(4*hits/i) + '\n')

file.close()