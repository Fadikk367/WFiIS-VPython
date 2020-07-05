from vpython import *

# some constants

ball_radius = 0.2
g = -9.8

# functions

def calc_energy():
  E = 0
  for ball in balls:
    E += ball.m*abs(g)*ball.pos.y + (1/2) * ball.m * (ball.vel**2)
  return E


def calc_vel(obj1, obj2):
  velA = ((obj1.m - obj2.m) / (obj1.m + obj2.m)) * obj1.vel + (2*obj2.m / (obj1.m + obj2.m))*obj2.vel
  velB = (2*obj1.m / (obj1.m + obj2.m))*obj1.vel + ((obj2.m - obj1.m) / (obj1.m + obj2.m)) * obj2.vel

  obj1.vel = velA
  obj2.vel = velB


def check_collision(balls, dt):
  for idx, ball in enumerate(balls):
      for i in range(idx + 1, 3):
        if abs(ball.pos.y + ball.vel * dt - (balls[i].pos.y + balls[i].vel * dt)) <= ball.radius * 2:
          calc_vel(ball, balls[i])
      if ball.pos.y - ball.radius + ball.vel * dt <= 0:
        ball.vel = -ball.vel


def update(balls, dt):
  for ball in balls:
    ball.vel += g * dt
    ball.pos.y += ball.vel * dt


def update_label(txt):
  txt.text = "total energy: " + '%.5f'%(calc_energy()) + '\n' + \
             "ball3.y: " + '%.5f'%(ballC.pos.y)

# simulation objects

scene = canvas(width=800, height=600, range = 4)

plot = graph(
  width=800, 
  eight = 600,      
  title='y[t]', 
  xtitle='t[s]', 
  ytitle='balls y',
  background=color.black,
  foreground=color.black
  )

f1 = gcurve(color = color.orange)
f2 = gcurve(color = color.yellow)

ground = box(pos=vector(0, -0.25, 0), size=vector(6, 0.5, 0.1), color=color.green)

txt = label(
  pos = vec(3, 2, 0),
  space = 20,
  height = 20,
  color = color.white,
  text = "TEST"
)

ballA = sphere(
  pos = vec(0, 2, 0),
  radius = 0.2,
  color = color.red,
  m = 10,
  vel = 0
)

ballB = sphere(
  pos = vec(0, 2.5, 0),
  radius = 0.2,
  color = color.orange,
  m = 1,
  vel = 0
)

ballC = sphere(
  pos = vec(0, 3, 0),
  radius = 0.2,
  color = color.yellow,
  m = 0.1,
  vel = 0
)

balls = [ballA, ballB, ballC]

# simulation loop

t = 0
dt = 0.0005

while t < 60:
  rate(1000)
  check_collision(balls, dt)
  update(balls, dt)
  update_label(txt)
  f1.plot(t, ballB.pos.y)
  f2.plot(t, ballC.pos.y)
  t += dt