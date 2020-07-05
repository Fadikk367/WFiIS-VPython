from vpython import *
from math import *
import math

g1 = 9.80
g2 = 9.80000000000001
L = 1

phi = math.pi
theta = math.pi - 0.1

phi_prim = 0
theta_prim = 0

def calc_energy():
  E = g1*ballA.pos.y + g1*ballB.pos.y  + (1/2)*L**2 * (ballA.phi_prim**2 + ballA.phi_prim**2 + ballB.theta_prim**2 + 2*ballA.phi_prim*ballB.theta_prim*cos(ballA.phi - ballB.theta))
  return E

def update_balls(ballA, ballB, dt):
  phi_bis = ((-ballA.g/L)*(2*sin(ballA.phi) - sin(ballB.theta)*cos(ballA.phi - ballB.theta)) - (ballA.phi_prim**2) * sin(2*ballA.phi - 2*ballB.theta)/2 - ballB.theta_prim**2 * sin(ballA.phi - ballB.theta)) / (1 + (sin(ballA.phi - ballB.theta))**2)

  theta_bis = (-(ballA.g/L)*(2*sin(ballB.theta) - 2*sin(ballA.phi)*cos(ballA.phi - ballB.theta)) + (ballB.theta_prim**2) * sin(2*ballA.phi - 2*ballB.theta)/2 + 2*(ballA.phi_prim**2) * sin(ballA.phi - ballB.theta)) / (1 + (sin(ballA.phi - ballB.theta))**2)


  ballA.phi_prim += phi_bis*dt
  ballB.theta_prim += theta_bis*dt

  ballA.phi += ballA.phi_prim*dt
  ballB.theta += ballB.theta_prim*dt

  ballA.pos = vec(L * sin(ballA.phi), -L * cos(ballA.phi), 0)
  ballB.pos = vec(L * (sin(ballA.phi) + sin(ballB.theta)), - L * (cos(ballA.phi) + cos(ballB.theta)), 0)


def update_lines(lineA, lineB, ballA, ballB):
  lineA.axis = ballA.pos

  lineB.pos = ballA.pos
  lineB.axis = ballB.pos - ballA.pos

def update_label():
  E = calc_energy()
  txt.text = 'E = ' + '%.6f'%(E) + '\n'

scene = canvas(width=800, height=600, range=2.5)

txt = label(
  pos = vec(2, 2, 0),
  space = 20,
  height = 20,
  color = color.white,
  text = "TEST"
)

ballA = sphere(
  g = 9.8,
  pos = vec(L * sin(phi), - L * cos(phi), 0),
  radius = 0.1,
  color = color.red,
  phi = phi,
  phi_prim = phi_prim
)

ballB = sphere(
  pos = vec(L * (sin(phi) + sin(theta)), - L * (cos(phi) + cos(theta)), 0),
  radius = 0.1,
  color = color.white,
  theta = theta,
  theta_prim = theta_prim
)

lineA = cylinder(
  pos = vector(0, 0, 0), 
  axis = ballA.pos, 
  length = mag(ballA.pos), 
  radius = 0.01, 
  color = color.white
)

lineB = cylinder(
  pos = ballA.pos, 
  axis = vector(ballB.pos - ballA.pos), 
  length = mag(ballB.pos - ballA.pos), 
  radius = 0.01, 
  color = color.white
)

ballA_prim = sphere(
  g = 9.80000000000001,
  pos = vec(L * sin(phi), - L * cos(phi), 0),
  radius = 0.1,
  color = color.blue,
  phi = phi,
  phi_prim = phi_prim
)

ballB_prim = sphere(
  pos = vec(L * (sin(phi) + sin(theta)), - L * (cos(phi) + cos(theta)), 0),
  radius = 0.1,
  color = color.blue,
  theta = theta,
  theta_prim = theta_prim
)

lineA_prim = cylinder(
  pos = vector(0, 0, 0), 
  axis = ballA.pos, 
  length = mag(ballA.pos), 
  radius = 0.01, 
  color = color.blue
)

lineB_prim = cylinder(
  pos = ballA.pos, 
  axis = vector(ballB.pos - ballA.pos), 
  length = mag(ballB.pos - ballA.pos), 
  radius = 0.01, 
  color = color.blue
)



t = 0
dt = 0.0005

sleep(2)

while t < 1000:
  rate(1000)
  update_balls(ballA, ballB, dt)
  update_balls(ballA_prim, ballB_prim, dt)
  update_lines(lineA, lineB, ballA, ballB)
  update_lines(lineA_prim, lineB_prim, ballA_prim, ballB_prim)
  update_label()
  t += dt