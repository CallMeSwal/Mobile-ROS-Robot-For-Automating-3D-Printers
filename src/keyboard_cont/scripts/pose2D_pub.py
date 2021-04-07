#!/usr/bin/env python
import roslib;
import rospy
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose2D, Quaternion
from apriltag_ros.msg import AprilTagDetectionArray
import time
import serial
import math
import os
from nav_msgs.msg import Odometry
from tf import transformations

speed_x=0
speed_y=0
twist=Twist()
pose=Pose2D()

pub = rospy.Publisher('pose2d', Pose2D, queue_size=1)

initial=True
initial_pose=Pose2D()

def update2DPose(msg):
    global pose
    global initial_pose
    global initial
    if initial:
        initial_pose.x=msg.pose.pose.position.x
        initial_pose.y=msg.pose.pose.position.y
        q=(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
        e=transformations.euler_from_quaternion(q)
        initial_pose.theta=e[2]*180/math.pi
        initial=False
    pose.x=msg.pose.pose.position.x-initial_pose.x
    pose.y=msg.pose.pose.position.y - initial_pose.y
    q=(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    e=transformations.euler_from_quaternion(q)
    pose.theta=e[2]*180/math.pi - initial_pose.theta

def reset2DPose(msg):
    global initial
    initial=True

if __name__ == "__main__":
    rospy.init_node('pose2D_pub') #make node 
    rospy.Subscriber('odom',Odometry,update2DPose)
    rospy.Subscriber('reset_pose2d',String,reset2DPose)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(pose)
        rate.sleep()

    rospy.spin()
