#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from nav_msgs import Odometry
from std_msgs.msg import Empty 
from time import time 
# Finally the GUI libraries
from PySide import QtCore, QtGui

GUI_UPDATE_PERIOD = 100 #ms
num = float(10)
cont=float(10)
# Here we define the keyboard map for our controller (note that python has no enums, so we use a class)


def callback(msg):
	x= msg.pose.pose.position.x
	print("La posicion X es: ", x)
		


if __name__=='__main__':
	od= rospy.Subscriber('bebop/odom', Odometry, callback)
	
	rospy.spin()
