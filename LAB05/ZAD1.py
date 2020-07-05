import numpy as np

file = open('./result1.txt', 'w')

rooms = 500
reached = False

for i in range(1, 366 + 1):
    successes = 0
    for room in range(1, rooms + 1):
        a = np.random.randint(1, 365 + 1, i)
        b = a[ : , np.newaxis]
        c = (a == b)
        # minus i because we dont want to include the diagonal which represents te same person
        if (np.sum(c) - i) > 0:
            successes += 1
    if successes / rooms >= 0.5 and not reached:
        reached = not reached
        file.write('-'*10 + ' we have reached 0.5 ' + '-'*10 + '\n')
    file.write(str(i) + ') porbability: ' + str(successes/rooms) +  '\n')
        
