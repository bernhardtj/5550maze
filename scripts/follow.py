#!/usr/bin/env python
#-*- coding:utf-8   -*-

import rospy
from  obstacle_detector.msg import Obstacles
from   obstacle_detector.msg import CircleObstacle
from geometry_msgs.msg import Twist  # cmd_vel data type
from math import pow, atan2, sqrt, pi
import numpy as np

def callback(data):
       msg= data.circles
       if  len(msg) !=0: # find robot M
            vel.linear.x=msg[0].velocity.x
            vel.linear.y=msg[0].velocity.y
            vel.linear.z=msg[0].velocity.z
            vel.angular.x=0
            vel.angular.y=0
            vel.angular.z=0
            pub.publish(vel)
       else:
            pass
       
rospy.init_node('follow')
sub = rospy.Subscriber('/tb3_1/tracked_obstacles', Obstacles, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/tb3_1/cmd_vel', Twist,queue_size=1)
vel=Twist()
rospy.spin()