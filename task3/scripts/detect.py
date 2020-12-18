#!/usr/bin/env python
#-*- coding:utf-8   -*-
import rospy
from  obstacle_detector.msg import Obstacles
from Obstacle.msg import circles
from std_msgs.msg import String

def callback(data):
       if data.circles is not None:
            rospy.loginfo(str)
            pub.publish(str)
            condition= True
       else:
            pass
       
rospy.init_node('detect')
sub = rospy.Subscriber('/tb3_1/tracked_obstacles', Obstacles, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/comm', String,queue_size=1)


str="hello"  

ctrl_c=True


                 
condition = False
rospy.spin()

      

      