import numpy as np
import matplotlib.pyplot as plt
import random

number_of_experiments = 500

distance = 0

x = [10, 100, 400, 1000, 2500, 10000]

for i in range(6):
    y = []
    for j in range(number_of_experiments):
        coin_flips = np.random.choice([-1, 1], size=x[i], replace=True)
        value = (np.sum(coin_flips))**2
        y.append(value)
    result = np.sqrt(sum(y)/number_of_experiments)
    plt.plot(x[i], result, 'o', lw=10, color='blue')
    distance = 0

x_axis = np.arange(0, 10000)
y_axis = np.sqrt(x_axis)
plt.plot(x_axis, y_axis, '-', color='red')

plt.savefig('plot2.png', format="png", box_inches='tight', pad_inches=0.05)
plt.show()

