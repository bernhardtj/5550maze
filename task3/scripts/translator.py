#!/usr/bin/env python2.7
import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy

if __name__ == '__main__':
    try:
        rospy.init_node('translator', anonymous=False)
        pub = rospy.Publisher('/tb3_0/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/joy', Joy, lambda data:
        pub.publish(Twist(Vector3(data.axes[1], 0, 0), Vector3(0, 0, data.axes[0]))))
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
