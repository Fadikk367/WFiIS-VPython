import math

file = open('sinus.txt', 'w')

row_length = 50

angles = [x*2*math.pi/50 for x in range(51)]

row = []
for i in angles:
    value = round(math.sin(i) * row_length)
    #print(value, end=" ")
    if value < 0:
        row.append('-'*(-value))
        #print('/')
    elif value == 0:
        row.append('0')
        #print('0')
    elif value > 0:
        row.append('+'*value)
        #print('+')
    
for i in row:
    file.write(i + '\n')

file.close()

