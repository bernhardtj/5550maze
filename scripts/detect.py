#!/usr/bin/env python
#-*- coding:utf-8   -*-
import rospy
from  obstacle_detector.msg import Obstacles
from   obstacle_detector.msg import CircleObstacle
from std_msgs.msg import String
import numpy as np

def callback(data):
       msg= data.circles
       if  len(msg) !=0: # find robot M
            pub.publish(str)
           
       else:
            pass
       
rospy.init_node('detect')
sub = rospy.Subscriber('/tb3_1/tracked_obstacles', Obstacles, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/comm', String,queue_size=1)

str="hello"            

rospy.spin()

      

      