#!/usr/bin/env python
import roslib;
import rospy

from nav_msgs.msg import Odometry

def odometryCb(msg):
    print msg.pose.pose

if __name__ == "__main__":
    rospy.init_node('oodom_sub', anonymous=True) #make node 
    rospy.Subscriber('odom',Odometry,odometryCb)
    rospy.spin()
