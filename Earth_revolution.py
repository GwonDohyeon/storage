from vpython import *
#GlowScript 2.9 VPython
Earth=sphere(pos=vec(0,1.5e11,0),texture=textures.earth,radius=6.4e9)
Sun=sphere(pos=vec(0,0,0),color=color.yellow,radius=3.5e10)
G=6.67e-11
Earth.mass=5.97e24
Sun.mass=1.99e30
Earth.v=vec(-29783,0,0)
Sun.v=vec(0,0,0)
attach_trail(Earth,type='points',pps=150)
while True:
    rate(100)
    t=0
    dt=60*60*24
    r=Sun.pos-Earth.pos
    Earth.f=G*Earth.mass*Sun.mass/mag(r)**2*norm(r)
    Sun.f=-Earth.f
    Earth.v=Earth.v+Earth.f/Earth.mass*dt
    Sun.v=Sun.v+Sun.f/Sun.mass*dt
    Earth.pos=Earth.pos+Earth.v*dt
    Sun.pos=Sun.pos+Sun.v*dt
    t=t+dt
