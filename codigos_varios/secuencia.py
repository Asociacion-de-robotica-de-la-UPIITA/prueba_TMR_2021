#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from std_msgs.msg import Empty 
from time import time 
# Finally the GUI libraries
from PySide import QtCore, QtGui

GUI_UPDATE_PERIOD = 100 #ms
num = float(10)
cont=float(10)
# Here we define the keyboard map for our controller (note that python has no enums, so we use a class)


class Mainventana(QtGui.QMainWindow):
	def __init__(self):
		super(Mainventana,self).__init__()
		self.setWindowTitle('Bebop interfaz')

		self.redrawTimer = QtCore.QTimer(self)
		self.redrawTimer.timeout.connect(self.update)
		self.redrawTimer.start(GUI_UPDATE_PERIOD)  
		veces=1

		self.pitch = 0
		self.roll = 0
		self.yaw_velocity = 0 
		self.z_velocity = 0 
		
		self.arm = False
		self.toff = False
		self.ld = False
		#self.override = False

		self.pubCommandP = rospy.Publisher('/vuelo/cmd_vel',Twist,queue_size=10)
		self.pubLand    = rospy.Publisher('/vuelo/land',Int8,queue_size = 10)
		self.pubTakeoff = rospy.Publisher('/vuelo/takeoff',Int8,queue_size = 10 )
		#self.pubOverride = rospy.Publisher('/keyboard/override',Int8,queue_size = 10)
		self.keyb = Twist()

	# We add a keyboard handler to the DroneVideoDisplay to react to keypresses

		if veces==1:
######################## ADELANTE
			tiempo0=time()
			tiempo=tiempo0+2
			while tiempo>=tiempo0:                     
				self.pitch=0.1
                        	self.roll=0
				self.keyb.linear.x  = self.pitch
				self.keyb.linear.y  = self.roll
				self.pubCommandP.publish(self.keyb)
				rospy.loginfo(self.roll)
				rospy.loginfo(self.pitch)
				tiempo0=time()
			
######################## IZQUIERDA
			tiempo0=time()
			tiempo=tiempo0+2
			while tiempo>=tiempo0:  
			        self.pitch=0
                        	self.roll=0.1
				self.keyb.linear.x  = self.pitch
				self.keyb.linear.y  = self.roll
				self.pubCommandP.publish(self.keyb)
				rospy.loginfo(self.roll)
				rospy.loginfo(self.pitch)
                        	tiempo0=time()
			
######################## ATRAS
			tiempo0=time()
			tiempo=tiempo0+2
			while tiempo>=tiempo0:  
                        	self.pitch=-0.15
                        	self.roll=0
				self.keyb.linear.x  = self.pitch
				self.keyb.linear.y  = self.roll
				self.pubCommandP.publish(self.keyb)
				rospy.loginfo(self.roll)
				rospy.loginfo(self.pitch)
                        	tiempo0=time()
			
######################## DERECHA
			tiempo0=time()
			tiempo=tiempo0+2
			while tiempo>=tiempo0:  
		                self.pitch=0
		                self.roll=-0.2
				self.keyb.linear.x  = self.pitch
				self.keyb.linear.y  = self.roll
				self.pubCommandP.publish(self.keyb)
				rospy.loginfo(self.roll)
				rospy.loginfo(self.pitch)
		                tiempo0=time()
                        veces-=1
		else:	
			self.pitch=0
                        self.roll=0
			self.keyb.linear.x  = self.pitch
			self.keyb.linear.y  = self.roll
			self.pubCommandP.publish(self.keyb)
			rospy.loginfo(self.roll)
			rospy.loginfo(self.pitch)
                       


if __name__=='__main__':
	import sys
	rospy.init_node('vuelo')
	app = QtGui.QApplication(sys.argv)

	display = Mainventana()
	display.show()
	status = app.exec_()

	# and only progresses to here once the application has been shutdown
	rospy.signal_shutdown('Great Flying!')
	sys.exit(status)
