import numpy as np
import matplotlib.pyplot as plt
import random

def fun1(x, y):
    newX = 0.85*x + 0.04*y
    newY = -0.04*x + 0.85*y + 1.6
    return (newX, newY)

def fun2(x, y):
    newX = 0.2*x - 0.26*y
    newY = 0.23*x + 0.22*y + 1.6
    return (newX, newY)

def fun3(x, y):
    newX = -0.15*x + 0.28*y
    newY = 0.26*x + 0.24*y + 0.44
    return (newX, newY)

def fun4(x, y):
    newX = 0
    newY = 0.16*y
    return (newX, newY)

def square_plot():
    plt.plot([0.5, 1], [6, 6], '-', color="red")
    plt.plot([0.5, 0.5], [6, 7], '-', color="red")
    plt.plot([1, 1], [6, 7], '-', color="red")
    plt.plot([0.5, 1], [7, 7], '-', color="red")

ax = plt.gca()
ax.set_facecolor("black")

x = 0
y = 0

x_axis = []
y_axis = []

count = 0

while count <= 1000000:
    # fun = np.random.choice([fun1, fun2, fun3, fun4], replace=False, p=[0.85, 0.07, 0.07, 0.01])
    # (x, y) = fun(x, y)
    num = random.uniform(0,100)
    if num<1.0:
        (x, y) = fun4(x, y)
    elif num<86.0:
        (x, y) = fun1(x, y)
    elif num<93.0:
        (x, y) = fun3(x, y)
    else:
        (x, y) = fun2(x, y)
    if (0.5 <= x <=1) and (y >= 6 and y <= 7):
        x_axis.append(x)
        y_axis.append(y)
        count += 1

plt.plot(x_axis, y_axis, ',', color='lime')
square_plot()
plt.savefig('plot22.png', format="png", box_inches='tight', pad_inches=0.05)
plt.show()











