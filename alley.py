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
		#avatar's postion and rotation angle
		self.x = 7.5
		self.z = 2.5
		self.theta = 270
		self.value = 0
		
					
		self.avatar = viz.add('vcc_female.cfg')
		mat = viz.Matrix()
		mat.postScale(.3,.3,.3)
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x,.1,self.z);
		self.avatar.setMatrix(mat)
		
		self.mode = "firstperson"
		
		
		self.spectator1 = viz.add('vcc_male.cfg')
		spec1x = 3.5
		spec1z = .9
		spec1theta = 0
		spec1value = 0
		
		mat = viz.Matrix()
		mat.postScale(.3,.3,.3)
		mat.postAxisAngle(0,1,0,spec1theta)
		mat.postTrans(spec1x,.1,spec1z)
		self.spectator1.setMatrix(mat)
		
		self.spectator1.state(3)
		
		self.spectator2 = viz.add('vcc_male2.cfg')
		spec2x = 4.5
		spec2z = .9
		spec2theta = 0
		spec2value = 0
		
		mat = viz.Matrix()
		mat.postScale(.3,.3,.3)
		mat.postAxisAngle(0,1,0,spec2theta)
		mat.postTrans(spec2x,.1,spec2z)
		self.spectator2.setMatrix(mat)
		
		self.spectator2.state(4)
					
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
		mat.postScale(.5,.5,.5)
		mat.postAxisAngle(0,1,0,self.theta)
		mat.postTrans(self.x,.1,self.z);
		self.avatar.setMatrix(mat)
	
	
