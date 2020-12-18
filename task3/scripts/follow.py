#!/usr/bin/env python
#-*- coding:utf-8   -*-

import rospy
import os
import pickle
from sensor_msgs.msg import LaserScan # scan data type
from geometry_msgs.msg import Twist  # cmd_vel data type
from math import pow, atan2, sqrt, pi
import numpy as np

def scan_callback(msg):
    global g_range_ahead
    # g_range_ahead=min(msg.ranges)
    # g_range_ahead=msg.ranges[len(msg.ranges)/2]
    g_range_ahead=msg.ranges[len(msg.ranges)/2*0]
    print "range_ahead: %0.1f"%g_range_ahead
 
 
g_range_ahead=1
 
cmd_vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
scan_sub=rospy.Subscriber('scan',LaserScan,scan_callback)
 
rospy.init_node('wander')
 
deriving_forward=True
state_change_time=rospy.Time.now()+rospy.Duration(15)
rate=rospy.Rate(10)
 
while not rospy.is_shutdown():
    if deriving_forward :
        # print "3"
        if (g_range_ahead<0.8 or rospy.Time.now()>state_change_time):
            # print "4"
            deriving_forward=False
            state_change_time=rospy.Time.now()+rospy.Duration(5)
    else:
        # print "5"
        if (rospy.Time.now()>state_change_time or g_range_ahead>0.8 ):
        # if (rospy.Time.now()>state_change_time):
            # print "6"
            deriving_forward=True
            state_change_time=rospy.Time.now()+rospy.Duration(15)
 
    twist=Twist()
    
    if deriving_forward:
        
        if g_range_ahead>0.8:
            twist.linear.z=0.0
            twist.linear.x=0.5
            # print "1.1"
        else:
            twist.linear.x=-0.2
            twist.angular.z=0.5          
            print "1.2"
    else:
        if g_range_ahead>0.8:
            twist.linear.z=0.5
            twist.linear.x=0.0
            # print "2.1"
        else:
            twist.linear.x=-0.2
            twist.angular.z=0.5 
            print "2.2"
 
    cmd_vel_pub.publish(twist)
    rate.sleep()