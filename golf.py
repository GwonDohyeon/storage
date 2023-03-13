from vpython import *
#GlowScript 2.7 VPython

 

ground = box(size=vec(40,40,1), color= color.green)

ball = sphere(pos=vec(-18,0,0), radius = 0.5)

ground.pos.z = ground.pos.z - ground.width/2-ball.radius

hole=cylinder(pos=vec(15,0,ground.pos.z+ground.width/2),axis=vec(0,0,1), radius=3*ball.radius, color= vec(0.8,0.8,0.8))

hole.pos.z = hole.pos.z - mag(hole.axis)*0.9

 

#properties

ball.m = 0.045

g = 9.8

mu = 0.5

 

initialspeed = 18

 

scale = initialspeed

ball.v = initialspeed*vec(1,0,0)

 

#time

t = 0

dt = 0.01

 

while t < 100:

    rate(100)
    Fmu=-ball.m*g*mu*norm(ball.v)
    ball.v=ball.v+dt*(Fmu/ball.m)
    ball.pos=ball.pos+dt*ball.v
    t=t+dt
