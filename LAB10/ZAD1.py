from vpython import *

N = 15
helixLength = 4
ballMass = 5
k = 1
airResist = 0
g = 0

def update_helixes():
    for i, spring in enumerate(helixes):
        if i == 0:
            spring.axis = balls[i].pos - vector(-(N+1)/2*helixLength, 0, 0) 
        elif i == len(helixes) - 1:
            spring.pos = balls[i-1].pos
            spring.axis = vector((N+1)/2*helixLength, 0, 0) - balls[i-1].pos
        else:
            spring.pos = balls[i-1].pos
            spring.axis = balls[i].pos - balls[i-1].pos

def update_balls(dt):
    for i, ball in enumerate(balls):
        if i == 0:
            ball.force = k * (vector(-(N+1)/2*helixLength, 0, 0) + balls[i+1].pos - 2*ball.pos) - airResist*ball.vel - vector(0, ball.mass*g, 0)
        elif i == len(balls) - 1:
            ball.force = k * (balls[i-1].pos + vector((N+1)/2*helixLength, 0, 0) - 2*ball.pos) - airResist*ball.vel - vector(0, ball.mass*g, 0)
        else:
            ball.force = k * (balls[i-1].pos + balls[i+1].pos - 2*ball.pos) - airResist*ball.vel - vector(0, ball.mass*g, 0)
        ball.acc = ball.force / ball.mass
        ball.vel += ball.acc * dt
        ball.pos += ball.vel * dt

def calculate_kinetic_energy():
    Ekin = 0
    for ball in balls:
        Ekin += (ball.mass*mag(ball.vel)**2)/2
    return Ekin


def calculate_potential_energy():
    Epot = 0
    for spring in helixes:
        Epot += (k*mag(spring.axis)**2)/2 
    return Epot

def update_label():
    Ekin = calculate_kinetic_energy()
    Epot = calculate_potential_energy()
    info.text = 'Ekin: ' + '%.6f'%(Ekin) + '\n' + \
                'Epot: ' + '%.6f'%(Epot) + '\n' + \
                'Ekin + Epot = ' + '%.6f'%(Ekin + Epot)

scene = canvas(width=1520, height=600, range=3*N)

rigthWall = box(
    pos=vector(-(N+1)/2*helixLength - 0.2, 0, 0), 
    size=vector(0.4, 8, 4), 
    color=color.red
)

leftWall = box(
    pos=vector((N+1)/2*helixLength + 0.2, 0, 0), 
    size=vector(0.4, 8, 4), 
    color=color.red
)

balls=[]
helixes=[]

info = label(
    pos=vector(0, 20, 0), 
    text="some text", 
    height=20,
    color=color.cyan,
    linecolor=color.red
)

helixes.append(helix(
    pos=vector(-(N+1)/2*helixLength, 0, 0), 
    axis=vector(helixLength, 0, 0), 
    radius=0.5,
    coils=10, 
    thickness=0.05,
    color=color.green
))

for i in range(N):
    balls.append(sphere(
        pos=helixes[i].pos + vector(helixLength, 0, 0),
        radius=0.5,
        mass=ballMass,
        color=color.yellow,
        vel=vector(0, 0, 0),
        acc=vector(0, 0, 0),
        force=vector(0, 0, 0)
    ))
    helixes.append(helix(
        pos=helixes[i].pos + vector(helixLength, 0, 0),
        radius=0.5,
        axis=vector(helixLength, 0, 0), 
        coils=10, 
        thickness=0.05,
        color=color.green
))

# starting conditions

balls[0].pos.y = 20
balls[-1].pos.y = -20

update_helixes()

sleep(2)

t = 0
dt = 0.003

while t < 500:
    rate(1000)
    update_balls(dt)
    update_helixes()
    update_label()
    t += dt


