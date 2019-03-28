# alley.py starter Code

import viz
import vizshape
import vizcam
import math
from Model import *

# An instance of this class adds a maze to the scene along with 
# an avatar that can be navigated through it.
class Alley(viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		self.desk = Model('Bowling\\model.dae')
		self.desk.setOrientation(self.desk.getX() + 1, self.desk.getY(), self.desk.getZ() + 4, .3, 0)
		#self.desk.setPosition([0,.1,0]) 
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.callback(viz.MOUSEDOWN_EVENT,self.onMouseDown)
		#avatar's postion and rotation angle
		self.x = 0.5
		self.z = 0.5
		self.theta = 0
		self.value = 0
		
					
		self.avatar = viz.add('vcc_female.cfg')
		mat = viz.Matrix()
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x,.1,self.z);
		self.avatar.setMatrix(mat)
		
		self.mode = "thirdperson"
					
	# Key pressed down event code.
	def onKeyDown(self,key):
		if (key == viz.KEY_LEFT):
			# turn self.avatar ccw, as viewed from above
			self.theta -= 2
		elif (key == viz.KEY_RIGHT):
			# turn self.avatar cw, as viewed from above
			self.theta += 2
		elif (key == viz.KEY_UP):
			# move avatar forward 
			dx = 0.2*math.sin( math.radians( self.theta ) )
			dz = 0.2*math.cos( math.radians( self.theta ) )
			self.x = self.x + dx
			self.z = self.z + dz	
		elif (key == viz.KEY_DOWN):
			# increase the velocity of the ball
			dx = 0.2*math.sin( math.radians( self.theta ) )
			dz = 0.2*math.cos( math.radians( self.theta ) )
			self.x = self.x - dx
			self.z = self.z - dz
			
		elif (key == "1"):
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(1,0,0,90)
			mat.postTrans(0,20,0)
			view.setMatrix(mat)
			self.mode = "thirdperson"
			
		elif (key == "2"):
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(1,0,0,45)
			mat.postAxisAngle(0,1,0,-90)
			mat.postTrans(20,15,5)
			view.setMatrix(mat)
			self.mode = "thirdperson"
		elif (self.value == 1  and key == "w"):
			self.desk.setOrientation(self.desk.getX(), self.desk.getY(), self.desk.getZ() + 1, .3, 0)
		elif (self.value == 1  and key == "a"):
			self.desk.setOrientation(self.desk.getX(), self.desk.getY(), self.desk.getZ() - 1, .3, 0)
		elif (self.value == 1 and key == "s"):
			self.desk.setOrientation(self.desk.getX() + 1, self.desk.getY(), self.desk.getZ(), .3, 0)
		elif (self.value == 1  and key == "d"):
			self.desk.setOrientation(self.desk.getX() - 1, self.desk.getY(), self.desk.getZ(), .3, 0)
		elif (self.value == 1 and key == "r"):
			self.desk.setOrientation(self.desk.getX(), self.desk.getY(), self.desk.getZ(), .3, self.desk.getYRotation() + 5)
		
		elif (key == "3"):
			self.mode = "firstperson"

		if (self.mode == "firstperson"):
			dx =  0.1*math.sin( math.radians( self.theta ) )
			dz =  0.1*math.cos( math.radians( self.theta ) )
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(0,1,0,self.theta)
			mat.postTrans(self.x+dx,.8,self.z+dz)
			view.setMatrix(mat)		
		
		mat = viz.Matrix()
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x,.1,self.z);
		self.avatar.setMatrix(mat)
	def onMouseDown(self,button):
		if(button == viz.MOUSEBUTTON_LEFT):
			print("left mouse pressed")
			obj = viz.pick()
			if obj == self.desk.getNode():
				print("desk")
				self.value = 1
			elif obj == self.shelf.getNode():
				print("shelf")
				self.value = 2
			else:
				print("neither")
				self.value = 0
		
	# Adds coodinate system that originates at (0,0,0) and extends
	# down the +x, +y, and +z directions.  Locations 1 and 2 units
	# in each direction are marked on the axis.
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
		

