from vpython import *
import numpy as np

def check_wall_collision(ball):
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




radius = 0.5

side = 8.0
thick = 0.4
side_v1 = 2*side - thick
side_v2 = 2*side + thick

N = 50

balls = []

scene = canvas(width=600, height=600)

x = - side + thick/2 + radius
y = - side + thick/2 + radius
z = - side + thick/2 + radius

countx = 0
county = 0

for i in range(N):

    balls.append(sphere(pos = vec(x, y, z), radius = 0.5, color=color.white))
    balls[i].vel = vec(np.random.rand(), np.random.rand(), np.random.rand())
    if 0 <= countx < 8:
        x += 2 * radius
    else:
        x = - side + thick/2 + radius
        y += 2 *radius
        countx = 0
    countx +=1


wallR = box (pos=vector( side, 0, 0), size=vector(thick, side_v1, side_v2),  color = color.green)
wallL = box (pos=vector(-side, 0, 0), size=vector(thick, side_v1, side_v2),  color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(side_v2, thick, side_v2),  color = color.blue)
wallT = box (pos=vector(0,  side, 0), size=vector(side_v2, thick, side_v2),  color = color.orange)
wallBK = box(pos=vector(0, 0, -side), size=vector(side_v1, side_v1, thick), color = color.cyan)

t = 0
dt = 0.005

sleep(3)
while t < 10000:
    for i in balls:
        i.pos += i.vel*dt
        check_wall_collision(i)
    t += dt
