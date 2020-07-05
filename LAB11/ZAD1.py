from vpython import *
import numpy as np
import random

def update_ball(ball):
    ball.pos += ball.vel*dt

def check_ball_collision(ballA, ballB):
    new_radius_A = ballA.pos + ballA.vel * dt
    new_radius_B = ballB.pos + ballB.vel * dt

    if mag(new_radius_A - new_radius_B) >= (ballA.radius + ballB.radius):
        return

    a = mag(ballA.vel - ballB.vel)**2
    b = -2*(new_radius_A - new_radius_B).dot(ballA.vel - ballB.vel)
    c = mag(new_radius_A - new_radius_B)**2 - (ballA.radius + ballB.radius)**2

    delta = b**2 - 4*a*c

    if a == 0 or delta < 0:
        return

    dt_prim = (-b + np.sqrt(delta)) / 2*a
    
    n_new_radiusA = new_radius_A - ballA.vel*dt_prim
    n_new_radiusB = new_radius_B - ballB.vel*dt_prim

    new_velA = ballA.vel - 2*(ballB.mass/(ballA.mass + ballB.mass))*((ballA.vel - ballB.vel).dot((n_new_radiusA - n_new_radiusB)/mag(n_new_radiusA - n_new_radiusB)))*((n_new_radiusA - n_new_radiusB)/mag(n_new_radiusA - n_new_radiusB))

    new_velB = ballB.vel + 2*(ballA.mass/(ballA.mass + ballB.mass))*((ballA.vel - ballB.vel).dot((n_new_radiusA - n_new_radiusB)/mag(n_new_radiusA - n_new_radiusB)))*((n_new_radiusA - n_new_radiusB)/mag(n_new_radiusA - n_new_radiusB))

    final_new_radiusA = n_new_radiusA + new_velA * dt_prim
    final_new_radiusB = n_new_radiusB + new_velB * dt_prim

    ballA.vel = new_velA
    ballB.vel = new_velB

    ballA.pos = final_new_radiusA
    ballB.pos = final_new_radiusB

def check_wall_collision(ball):
    if mag(ball.pos + ball.vel*dt) + ball.radius>= area.radius - area.thickness:
        ball.pos = ball.pos/mag(ball.pos)*(area.radius - area.thickness - ball.radius)
        vel_R = ball.pos/mag(ball.pos)*(ball.vel.dot(ball.pos/mag(ball.pos)))
        ball.vel = ball.vel -2*vel_R
        ball.pos += ball.vel*dt
        return True
    return False

def check_collisions_and_update():
    for idx, ball in enumerate(balls):
        if check_wall_collision(ball):
            continue
        else:
            update_ball(ball)
            for i in range(idx + 1, N):
                check_ball_collision(ball, balls[i])

scene = canvas(width=800, height=600, range=5)
area = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=4, thickness=0.1, color=color.red)

#parameters
N = 60
m = 1
M = 100

t = 0
dt = 0.005

balls = []

balls.append(sphere(
    pos = vec(random.uniform(-1,1)*2, random.uniform(-1,1)*2, 0),
    radius = 0.5, 
    color=color.yellow,
    vel = vector(0,0,0),
    mass = M,
    make_trail = True
))

for i in range(N):
    ball_pos = vector(0,0,0)
    #prevent overlaping balls at t = 0
    while True:
        ball_pos = vec(random.uniform(-1,1)*2.5, random.uniform(-1,1)*2.5, 0)
        is_free = True
        for ball in balls:
            if mag(ball.pos - ball_pos) < ball.radius + 0.1:
                is_free = False
        if is_free == True:
            break
        
    balls.append(sphere(
        pos = ball_pos,
        radius = 0.1, 
        color = color.white,
        vel = vector(np.random.rand(), np.random.rand(), 0),
        mass = m
    ))
    sleep(0.1)

N += 1

sleep(2)

while t < 500:
    rate(1000)
    check_collisions_and_update()
    t += dt
