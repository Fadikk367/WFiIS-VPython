import time
import random

N = 15

def draw(position):
    pos_msg = '';
    if position < 0:
        if position > -10:
            pos_msg = ' ' + str(position)
        else:
            pos_msg = str(position)
        print('|' + (N - abs(position)) * " " + "*" + (N + abs(position)) * " " + '|' + pos_msg)

    elif position > 0:
        if position >= 10:
            pos_msg = '+' + str(position)
        else:
            pos_msg = ' +' + str(position)
        print('|' + (N + position) * " " + "*" + (N - position) * " " + '|' + pos_msg)
    else:
        print('|' + " " * N + "*" + " " * N +  '|' + '  0')

def coin_flip():
    rand = random.randint(0, 1)
    if rand == 0:
        return -1
    else:
        return 1

print('|' + " " * (N - 2) + "START" + " " * (N - 2) +  '|pos' )
print('|' + " " * N + "*" + " " * N +  '|' + '  0')

position = 0
flips = 0
wall_hit = False

while not wall_hit:
    step = coin_flip()
    flips += 1
    position += step
    draw(position)
    if position == N or position == -N:
        wall_hit = True
        print('Succeded after ' + str(flips) + ' coin flips')
    time.sleep(0.02)

