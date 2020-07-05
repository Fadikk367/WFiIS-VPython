from vpython import *

# some constants

counter = 0

k = 0

dist = 6
big_box_size = vector(2,2,0.1)
small_box_size = vector(2,2,0.1)

wall_size = vector(1, 8, 0.1)
wall_pos = vector(dist + wall_size.x / 2, 2, 0)

# functions

def calc_vel(obj1, obj2):
  velA = ((obj1.m - obj2.m) / (obj1.m + obj2.m)) * obj1.vel + (2*obj2.m / (obj1.m + obj2.m))*obj2.vel
  velB = (2*obj1.m / (obj1.m + obj2.m))*obj1.vel + ((obj2.m - obj1.m) / (obj1.m + obj2.m)) * obj2.vel

  obj1.vel = velA
  obj2.vel = velB

def check_collision(obj1, obj2, wall, dt):
  if (obj1.pos.x + obj1.size.x / 2 + obj1.vel * dt >= obj2.pos.x - obj2.size.x / 2):
    obj1.b_col += 1
    calc_vel(obj1, obj2)
  else:
    if (obj2.pos.x + obj2.size.x / 2 + obj2.vel * dt >= wall.pos.x - wall.size.x / 2):
      obj2.w_col += 1
      obj2.vel = -obj2.vel

def update(obj1, obj2, dt):
  obj1.pos.x += obj1.vel * dt
  obj2.pos.x += obj2.vel * dt

def update_label(obj1, obj2):
  txt.text = "collisions: " + '%d'%(obj1.b_col + obj2.w_col) + '\n'

# simulation objects

scene = canvas(width=800, height=600, range = 10)

wall = box(pos=wall_pos, size=wall_size, color=color.yellow)
floor = box(pos=vector(0, -1.5, 0), size=vector(18, 1, 0.1), color=color.yellow)

boxA = box(pos=vector(0,0,0), size=big_box_size, color = color.red, vel=1, m = 100**k, b_col = 0)
boxB = box(pos=vector(4,0,0), size=small_box_size, color = color.red, vel=0, m = 1, w_col = 0)

txt = label(
  pos = vec(0, 6, 0),
  space = 20,
  height = 20,
  color = color.white,
  text = "TEST"
)

# simulation loop

t = 0
dt = 0.01
if k <= 1:
  dt = 0.00001
elif 4 > k > 1:
  dt /= 10**k
else:
  dt = 0.000001 / 10**(k - 4)

while t < 20:
  # rate(1000)
  check_collision(boxA, boxB, wall, dt)
  update(boxA, boxB, dt)
  update_label(boxA, boxB)
  t += dt