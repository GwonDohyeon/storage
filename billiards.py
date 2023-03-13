from vpython import *
#GlowScript 2.9 VPython

#Creating Objects
ball1 = sphere(radius=0.5*65.5e-3, make_trail = True, retain = 100)
ball2 = sphere(radius=0.5*65.5e-3, make_trail = True, pos=vec(0.5,-0.5*65.5e-3,0), color=color.red, retain = 100)

#Creating Pool
l = 2.448
h = 1.224
thk = 0.01
pool = box(pos = vec(0,0,-ball1.radius-thk/2),color=color.green, size=vec(l,h,thk))

#initial condition & physical properties
ball1.v = vec(1,0,0)
ball2.v = vec(0,0,0)
ball1.m = 0.21
ball2.m = 0.21
g = 9.8

#Friction
ball1.mu = 0.01
ball2.mu = 0.01
ball1.f = vec(0,0,0)
ball2.f = vec(0,0,0)
tol = 0.001
e = 1
tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
t = 0
dt = 0.01
traj1 = gcurve(color = color.black)
traj2 = gcurve(color = color.red)
en_traj = gcurve(color = color.orange)

scene.autoscale = True
scene.range = 0.8
scene.center = 0.5*(ball1.pos + ball2.pos)

def collision(b1, b2, e):
    n = b1.pos - b2.pos
    n_hat = norm(n)
    dist = mag(n)
    v_relm = dot(b1.v - b2.v, n_hat)
    if v_relm > 0:
        return False
    tot_radius = b1.radius + b2.radius
    if dist > tot_radius:
        return False
    else:
        j = -(1+e)*v_relm
        j = j/(1/b1.m+1/b2.m)
        b1.v = b1.v + j*n_hat/b1.m
        b2.v = b2.v - j*n_hat/b2.m
        #_Option: Postion correction
        #scene.waitfor('click')
        #print(b1.radius + b2.radius - dist)
        b1.pos = b1.pos + n_hat*(tot_radius - dist)*b2.m/(b1.m + b2.m)
        b2.pos = b2.pos - n_hat*(tot_radius - dist)*b1.m/(b1.m + b2.m)
        #print(b1.radius + b2.radius - mag(b1.pos - b2.pos))
        #scene.waitfor('click')
        return True
        
def col_pool(ball, ground, e):
    col_flag = False
    # x-axis collision check
    if -ground.size.x/2 > ball.pos.x - ball.radius:
        ball.pos.x = -ground.size.x/2 + ball.radius
        ball.v.x = -e*ball.v.x
        col_flag = True
    if ground.size.x/2 < ball.pos.x + ball.radius:
        ball.pos.x = ground.size.x/2 - ball.radius
        ball.v.x = -e*ball.v.x
        col_flag = True
    # y-axis collision check
    if -ground.size.y/2 > ball.pos.y - ball.radius:
        ball.pos.y = -ground.size.y/2 + ball.radius
        ball.v.y = -e*ball.v.y
        col_flag = True
    if ground.size.y/2 < ball.pos.y + ball.radius:
        ball.pos.y = ground.size.y/2 - ball.radius
        ball.v.y = -e*ball.v.y
        col_flag = True
    return col_flag
    
while True:
    rate(1/dt)
    
    #collision handling
    colcheck = collision(ball1,ball2, e)
    
    #collision btw ball and pool
    coltopool = col_pool(ball1, pool, e)
    coltopool = col_pool(ball2, pool, e)
    
    #Force
    ball1.f = -ball1.mu*ball1.m*g*norm(ball1.v)
    ball2.f = -ball2.mu*ball2.m*g*norm(ball2.v)
    print("ball1.f:", mag(ball1.f), "ball1.v:", ball1.v)
    
    #ECM integration
    ball1.v = ball1.v + ball1.f/ball1.m*dt
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.pos = ball2.pos + ball2.v*dt
    
    #friction
    if mag(ball1.v) < tol:
        ball1.v = vec(0,0,0)
    if mag(ball2.v) < tol:
        ball2.v = vec(0,0,0)
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
    traj1.plot(pos=(t,mag(ball1.v)))
    traj2.plot(pos=(t,mag(ball2.v)))
    en_traj.plot(pos=(t,tot_energy))
    t = t + dt
