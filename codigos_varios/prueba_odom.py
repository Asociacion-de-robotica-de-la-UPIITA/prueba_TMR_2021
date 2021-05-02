#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty 
import time 


def Leer_Odometria(msg):
	#time.sleep(0.5)
	x= msg.pose.pose.position.x
	print("La posicion X es: ", x)
	y= msg.pose.pose.position.y
	print("La posicion Y es: ",y)
	z= msg.pose.pose.position.z
	print("La posicion Z es: ",z)
	print("-----------------------\n")


if __name__=='__main__':
	rospy.init_node('DronePosicion', anonymous = False)
	od= rospy.Subscriber('bebop/odom', Odometry, Leer_Odometria)
	
	rospy.spin()
