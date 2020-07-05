import numpy
import math

#for i in range(2, 7):
#    print("power level: " + str(i))
#    for j in range(1, 101):
#        for k in range(1, j):
#            result = numpy.power(numpy.power(j, i) + numpy.power(k, i), 1/i)
#            if numpy.int(result) == result:
#                print('a = ' + str(j) + ', b = ' + str(k) + ', c = ' + str(int(result)))

for i in range(2, 7):
    print("power level: " + str(i))
    for j in range(1, 101):
        for k in range(1, j):
            result = math.pow(math.pow(j, i) + math.pow(k, i), 1/i)
            if int(result) == result:
                print('a = ' + str(j) + ', b = ' + str(k) + ', c = ' + str(int(result)))

    

