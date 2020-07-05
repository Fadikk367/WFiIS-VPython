import numpy as np

file = open('./result2.txt', 'w')

rooms = 500
reached = False

for i in range(1, 366 + 1):
    #rooms = np.random.randint(100, 1000 + 1)
    successes = 0
    for j in range(1, rooms + 1):
        a = np.random.randint(1, 365 + 1, i)
        count = np.zeros(365 + 1)
        for k in a:
            count[k] += 1
        for k in count:
            if k >= 3:
                successes += 1
                break
    if (successes / rooms >= 0.5 and not reached):
        reached = not reached
        file.write('-' * 10 + ' 0.5 probability reached ' + '-' * 10  + '\n')
    file.write(str(i) + ") successes: " + str(successes) + ", probability: " + str(successes / rooms) + '\n')
