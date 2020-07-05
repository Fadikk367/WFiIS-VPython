import numpy as np
import matplotlib.pyplot as plt
import random

def random_angle():
    return random.uniform(0, 2*np.pi)

def next_step(x_pos, y_pos):
    angle = random_angle()
    x_pos += np.cos(angle)
    y_pos += np.sin(angle)
    return (x_pos, y_pos)

colors = ['black', 'red', 'yellow', 'blue', 'orange', 'purple', 'cyan', 'brown', 'pink', 'green', 'grey', 'chocolate', 'navy', 'indigo', 'coral']

number_of_walks = 15

number_of_coin_flips = 10**5

for i in range(number_of_walks):
    x = []
    y = []
    x_pos = 0
    y_pos = 0
    for j in range(number_of_coin_flips + 1):
        (x_pos, y_pos) = next_step(x_pos, y_pos)
        x.append(x_pos)
        y.append(y_pos)
    plt.plot(x, y, lw=0.1, color=colors[i])
    plt.plot(x[-1], y[-1], 'o', ms=10, color=colors[i])

plt.savefig('plot1B.png', format="png", box_inches='tight', pad_inches=0.05)
plt.show()

