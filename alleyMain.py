﻿# alleymain.py
# Driver code for maze lab
  
import viz
import vizshape
import vizcam
import math

from alley import *

# set size (in pixels) and title of application window
viz.window.setSize( 640*1.5, 480*1.5 )
viz.window.setName( "Bowling!!!!!" )

# get graphics window
window = viz.MainWindow
# setup viewing volume
33
# set background color of window to blue 
viz.MainWindow.clearcolor( [0,0,150] ) 

# allows mouse to rotate, translate, and zoom in/out on object
pivotNav = vizcam.PivotNavigate()

viz.phys.enable()

c = Alley()

import viz
import vizmat

viz.go()

import vizinfo
vizinfo.InfoPanel()

#Declare some constants
GRID_WIDTH = 6
GRID_HEIGHT  = 6
SPACING  = 1.1
MAX_BALLS = 20
MIN_POWER = 5
MAX_POWER = 10

#We need to enable physics
viz.phys.enable()

balls = []


for x in range(MAX_BALLS):
	ball = vizshape.addSphere(0.05, color = viz.BLACK)
	ball.collideSphere()
	balls.append(ball)

#Create a generator this will loop through the balls
nextBall = viz.cycle(balls)

#Add a green marker that will show where we are aiming, disable picking on it
import vizshape
marker = vizshape.addSphere(radius=0.1,color=viz.GREEN)
marker.visible(False)
marker.disable(viz.PICKING)

#Add a progress bar to the screen that will show how much power is charged up
power = viz.addProgressBar('Power',pos=(0.8,0.1,0))
power.disable()
power.set(0)

#Move the head position back and up and look at the origin
viz.MainView.setPosition([0,5,-20])
viz.MainView.lookAt([0,0,0])

#Disable mouse navigation
viz.mouse(viz.OFF)

#This function will reset all the boxes and balls
def ResetObjects():

    for b in balls:
        #Translate the ball underneath the ground
        b.setPosition([0,-5,0])
        #Disable physics on the ball
        b.disable(viz.PHYSICS)

ResetObjects()

#'r' key resets simulation
vizact.onkeydown('r',ResetObjects)

def ChargePower():
    #Get detailed information about where the mouse is pointed
    info = viz.pick(1)
    marker.setPosition(info.point)
    #Increment the amount of power charged up
    power.set(power.get()+0.05)

vizact.whilemousedown(viz.MOUSEBUTTON_LEFT,ChargePower)

def ShootBall():
    #Hide marker
    marker.visible(viz.OFF)
    #Convert the current mouse position from screen coordinates to world coordinates
    line = viz.MainWindow.screenToWorld(viz.mouse.getPosition())
    #Create a vector that points along the line the mouse is at
    vector = viz.Vector(line.dir)
    #Set length of vector based on the amount of power charged up
    vector.setLength(vizmat.Interpolate(MIN_POWER,MAX_POWER,power.get()))
    #Move the next ball to be fired to the begin point
    b = nextBall.next()
    b.setPosition(line.begin)
    #Reset the ball, set its velocity vector, and enable it
    b.reset()
    b.setVelocity(vector)
    b.enable(viz.PHYSICS)
    #Reset the power
    power.set(0)

vizact.onmouseup(viz.MOUSEBUTTON_LEFT,ShootBall)
