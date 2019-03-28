# alleymain.py
# Driver code for maze lab
  
import viz
import vizshape
import vizcam
import math

from alley import *

# set size (in pixels) and title of application window
viz.window.setSize( 640*1.5, 480*1.5 )
viz.window.setName( "Maze Navigation" )

# get graphics window
window = viz.MainWindow
# setup viewing volume

# set background color of window to blue 
viz.MainWindow.clearcolor( [0,0,150] ) 

# allows mouse to rotate, translate, and zoom in/out on object
pivotNav = vizcam.PivotNavigate()

c = Alley()

# render the scene in the window
viz.go()
