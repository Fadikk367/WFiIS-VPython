import numpy as np
import matplotlib.pyplot as plt
import random

def coin_flip():
    rand = random.randint(0, 1)
    if rand == 0:
        return -1
    else:
        return 1

colors = ['black', 'red', 'yellow', 'blue', 'orange', 'purple', 'cyan', 'brown', 'pink', 'green', 'grey', 'chocolate', 'navy', 'indigo', 'coral']

number_of_walks = 15

number_of_coin_flips = 10**5

distance = 0

for i in range(number_of_walks):
    x = np.arange(0, number_of_coin_flips + 1)
    y = []
    for j in range(number_of_coin_flips + 1):
        distance += coin_flip();
        y.append(distance)
    plt.plot(x, y, lw=0.1, color=colors[i])
    distance = 0

plt.savefig('plot1A.png', format="png", box_inches='tight', pad_inches=0.05)
plt.show()

