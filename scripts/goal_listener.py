#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def moveToGoal(xGoal, yGoal):

    # define a client for to send goal requests to the move_base server through a SimpleActionClient
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    # wait for the action server to come up
    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/

    goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(60))

    if(ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
        return True

    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False


def callback(data):
    target = (data.data.strip("()").split(','))
    x = float(target[0])
    y = float(target[1])

    goalReached = False
    goalReached = moveToGoal(x, y)
    if (goalReached):
        rospy.loginfo("Congratulations!")
        rospy.sleep(5)
        moveToGoal(0.0, 0.0)
        # rospy.spin()
    else:
        rospy.loginfo("Hard Luck!")
    

    # rospy.loginfo(rospy.get_caller_id() + "x : %s", x)
    # rospy.loginfo(rospy.get_caller_id() + "y : %s", y)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("target", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        rospy.loginfo("You have reached the destination")
        listener()

    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")

