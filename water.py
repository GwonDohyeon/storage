from vpython import *

#GlowScript 2.7 VPython

#Creating Objects and Scene Setting

water = box(pos = vec(0,0,0), size=vec(10,10,10), color = color.blue,opacity = 0.5)
wood = box(pos = vec(0,10,0), size=vec(2,2,2), texture = textures.wood)
scene.background = color.white

# Initial Setting

wood.v = vec(0,0,0)
wood.rho = 900
wood.volume = wood.size.x*wood.size.y*wood.size.z
wood.volume_im = 0
wood.m = wood.rho*wood.volume

water.rho = 1000
air_rho = 1.2

rho = air_rho

Cd = 1.06

g = vec(0,-9.8,0)

def calc_im(pBox,pbox, rho): 
    float_height = (pbox.pos.y + 0.5*pbox.size.y) - (pBox.pos.y + 0.5*pBox.size.y)

    if float_height < 0:
        pbox.volume_im = pbox.volume
    else:
        pbox.volume_im = max(0, pbox.volume - float_height*pbox.size.x*pbox.size.z)
    if pbox.volume_im > 0:
        rho = water.rho
    else:
        rho = air_rho
    return pbox.volume_im, rho

scene.waitfor('click')
t = 0
dt = 0.001
while t < 100:
    
    rate(10/dt)

     #force

    wood.volume_im, rho = calc_im(water, wood, rho)
    
    grav = wood.m*g
    
    bouy = -water.rho*wood.volume_im*g

    drag = -0.5*rho*Cd*(wood.size.x*wood.size.y)*mag(wood.v)**2*norm(wood.v)

    

    wood.f = grav + bouy + drag
     #time integration
    wood.v = wood.v + wood.f/wood.m*dt

    wood.pos = wood.pos + wood.v*dt
    
    if wood.pos.y-(wood.size.y/2) <= water.pos.y-(water.size.y/2):
        print("collision!")
    
    #time update
    t = t + dt

     
