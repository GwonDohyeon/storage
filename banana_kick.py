from vpython import *
#GlowScript 2.9 VPython

#ground
ground = box(pos=vec(0,0,0),size=vec(100,0.10,70), color = color.green)

#init. positon & velocity of ball
init_pos = vec(-30,0.11,0)
ball2 = sphere(pos=init_pos,radius=0.11, color = color.orange) #m
#
ball2.m = 0.45 #kg
ball2.speed = 25 #m/s
ball2.angle = radians(35) #c.f) degrees
ball2.v = ball2.speed*vec(cos(ball2.angle),sin(ball2.angle),0)
attach_trail(ball2)
attach_arrow(ball2, "v", shaftwidth = 0.1, scale = 0.3, color=color.yellow)
ball = sphere(pos=init_pos,radius=0.11, color = color.red) #m
#
ball.m = 0.45 #kg
ball.speed = 25 #m/s
ball.angle = radians(35) #c.f) degrees
ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)
attach_trail(ball)
attach_arrow(ball, "v", shaftwidth = 0.1, scale = 0.3, color=color.yellow)

#wind
wind_speed = 5 #m/s
#wind_speed = -5 #m/s
#wind_speed = -10 #m/s
wind_v = wind_speed*vec(1,0,0)

#graph object
gball_x = gcurve()
scene.range = 30

#const.
g = -9.8 #m/s**2
rho = 1.204 #kg/m**3
Cd = 0.3#0.3#0.3#1 #laminar
Cm = 0 #0.5
w = 10*2*pi # 10 rev. per sec

#time setting
t = 0
dt = 0.01

scene.waitfor('click')
while t < 20:
    rate(1/dt)
    
    #Gravity Force
    grav = ball2.m * vec(0,g,0) #gravity
    
    #Drag Force
    drag = -0.5*rho*Cd*(pi*ball2.radius**2)*mag(ball2.v)**2*norm(ball2.v)
    ball.v_w = ball.v - wind_v
    drag_wind = -0.5*rho*Cd*(pi*ball.radius**2)*mag(ball.v_w)**2*norm(ball.v_w)
    print("gravity: ", mag(grav), 'drag force: ',mag(drag))
    
    #Sum of Forces
    ball2.f = grav + drag
    ball.f = grav + drag_wind
    
    #Time stepping
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball2.pos = ball2.pos + ball2.v*dt
    
    #Time stepping
    ball.v = ball.v + ball.f/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    
    #graph
    gball_x.plot(pos=(t,mag(init_pos - ball2.pos)))
    #gball_y.plot(pos=(t,ball.pos.y))
    
    #collision
    if ball2.pos.y - ball2.radius < 0:
        ball2.v = vec(0,0,0)
    if ball.pos.y - ball.radius < 0:
        #print(ball.pos.x)
        break
    t = t + dt
