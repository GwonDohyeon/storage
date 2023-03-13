from vpython import *
#GlowScript 2.9 VPython
planet=sphere(radius=5.6256e6,color=color.orange)
planet.pos=vec(0,0,0)
planet.mass=4e18
G=6.67e-11
craft=sphere(radius=1e5,color=color.blue,make_trail=True)
craft.pos=vec(-planet.radius*1.1,0,0)
craft.mass=5
craft.v=vec(0,9.7,0)
t=0
dt=2000
while True:
    rate(100)
    r=planet.pos-craft.pos
    craft.f=G*craft.mass*planet.mass/mag(r)**2*norm(r)
    craft.v=craft.v+craft.f/craft.mass*dt
    craft.pos=craft.pos+craft.v*dt
    t=t+dt
