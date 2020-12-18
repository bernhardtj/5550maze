#!/usr/bin/env python
#-*- coding:utf-8   -*-
 
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/comm', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()