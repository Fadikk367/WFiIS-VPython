import math

file = open('filePI_1.txt', 'w')

def getPI(iter):
    suma = 0
    flag = 1
    for i in range(1, int(iter)):
        suma += 1 / (2*i - 1) * flag
        flag = -flag
        file.write(str(i) + ') ' + str(4*suma) + '\n')
    return 4 * suma

getPI(1e7)

file.close()



