from vpython import *
import numpy as np

rangeScale = 1e9
velocityScale = 1e3
G = 6.7e-11

scene = canvas(width=700, height=700)



SUN = sphere(pos=vector(0,0,0), color=color.yellow, radius=20000000000)

SUN.mass = 2e30

MERCURY = sphere(pos=vector(70*rangeScale, 0, 0), color=color.cyan, radius=8000000000, make_trail=True)
VENUS = sphere(pos=vector(110*rangeScale, 0, 0), color=color.orange, radius=10000000000, make_trail=True)
EARTH = sphere(pos=vector(150*rangeScale, 0, 0), color=color.blue, radius=12000000000, make_trail=True)
MARS = sphere(pos=vector(250*rangeScale, 0, 0), color=color.red, radius = 16000000000, make_trail=True)

MERCURY.vel = vector(0, 47*velocityScale, 0)
VENUS.vel = vector(0, 35*velocityScale, 0)
EARTH.vel = vector(0, 30*velocityScale, 0)
MARS.vel = vector(0, 24*velocityScale, 0)

MERCURY.dist = 70*rangeScale
VENUS.dist = 110*rangeScale
EARTH.dist = 150*rangeScale
MARS.dist = 250*rangeScale

PLANTES = [MERCURY, VENUS, EARTH, MARS]

t = 0
dt = 24*60*60/24

sleep(3)

while t < 24*60*60*365*10:
    rate(1000)
    for planet in PLANTES:
        planet.a = - G * SUN.mass * planet.pos / np.power(mag(planet.pos), 3)
        planet.vel += planet.a * dt
        planet.pos += planet.vel * dt
        t += dt

    

