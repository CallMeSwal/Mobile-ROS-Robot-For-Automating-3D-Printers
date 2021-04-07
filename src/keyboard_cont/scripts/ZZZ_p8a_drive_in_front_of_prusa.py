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

speed_x=0
speed_y=0
twist=Twist()

initial_pose=Pose2D()
current_pose=Pose2D()

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
reset_pose = rospy.Publisher('reset_pose2d', String, queue_size=1)

first_time=True

def updatePose(new_pose):
    global current_pose
    global initial_pose
    global first_time
    if first_time:
         initial_pose=new_pose
         first_time=False
    '''
    current_pose.x=new_pose.x-initial_pose.x
    print(current_pose.x, new_pose.x, initial_pose.x)
    current_pose.y=new_pose.y-initial_pose.y
    current_pose.theta=new_pose.theta-initial_pose.theta
    '''
    current_pose.x=new_pose.x
    current_pose.y=new_pose.y
    current_pose.theta=new_pose.theta
    print(current_pose.x, current_pose.y, current_pose.theta)

if __name__ == "__main__":
    rospy.init_node('ZZZ_p8a_drive_in_front_of_prusa') #make node 
    rate=rospy.Rate(10)
    rospy.Subscriber('/pose2d',Pose2D,updatePose)
    first_time=True

    rospy.sleep(1)
    reset_pose.publish('RESET_POSE')
    rospy.sleep(1)
    
    while not rospy.is_shutdown() and current_pose.x>-0.80:
        twist.linear.x = -0.1
        twist.angular.z = 0.0
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1)
    reset_pose.publish('RESET_POSE')
    rospy.sleep(1)
    
    while not rospy.is_shutdown() and current_pose.theta>-72:
        twist.linear.x = 0.0
        twist.angular.z = -0.1
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1)
    reset_pose.publish('RESET_POSE')
    rospy.sleep(1)
    
    while not rospy.is_shutdown() and current_pose.y>-0.25:
        twist.linear.x = 0.05
        twist.angular.z = 0.0
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1)
    reset_pose.publish('RESET_POSE')
    rospy.sleep(1)

    while not rospy.is_shutdown() and current_pose.theta<72:
        twist.linear.x = 0.0
        twist.angular.z = 0.1
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1)
    reset_pose.publish('RESET_POSE')
    rospy.sleep(1)
    
    os.system("rosnode kill ZZZ_p8a_drive_in_front_of_prusa")
