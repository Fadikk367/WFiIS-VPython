from vpython import *
import numpy as np

scene = canvas(width=600, height=600)

radius = 0.5

side = 8.0
thick = 0.4
side_v1 = 2*side - thick
side_v2 = 2*side + thick

wallR = box (pos=vector( side, 0, 0), size=vector(thick, side_v1, side_v2),  color = color.green)
wallL = box (pos=vector(-side, 0, 0), size=vector(thick, side_v1, side_v2),  color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(side_v2, thick, side_v2),  color = color.blue)
wallT = box (pos=vector(0,  side, 0), size=vector(side_v2, thick, side_v2),  color = color.orange)
wallBK = box(pos=vector(0, 0, -side), size=vector(side_v1, side_v1, thick), color = color.cyan)

ball = sphere(pos = vec(0, 0, 0), radius = 0.5, color=color.white)

# ball.vel = vec(0.5, -0.2, 0.3)
ball.vel = vec(np.random.rand(), np.random.rand(), np.random.rand())

t = 0
dt = 0.01
while t < 1000:
    rate(1000)
    ball.pos += ball.vel*dt
    if ball.pos.x > side - thick/2 - ball.radius:
        ball.vel.x *= -1
        ball.color = color.green
    elif ball.pos.x < -side + thick/2 + ball.radius:
        ball.vel.x *= -1
        ball.color = color.red
    elif ball.pos.y > side - thick/2 - ball.radius:
        ball.vel.y *= -1
        ball.color = color.orange
    elif ball.pos.y < -side + thick/2 + ball.radius:
        ball.vel.y *= -1
        ball.color = color.blue
    elif ball.pos.z > side -thick/2 -ball.radius:
        ball.vel.z *= -1
        ball.color = color.white
    elif ball.pos.z < -side +thick/2 + ball.radius:
        ball.vel.z *= -1
        ball.color = color.cyan
    t += dt