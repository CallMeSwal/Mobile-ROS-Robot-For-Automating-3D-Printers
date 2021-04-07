#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from apriltag_ros.msg import AprilTagDetectionArray
import time
import serial
import math
import os

speed_x=0
speed_y=0
twist=Twist()
end_counter=0

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

DISTANCE_TO_TAG=0.600


def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x*180/math.pi, pitch_y*180/math.pi, yaw_z*180/math.pi # in radians

def drive(data):
    global speed_x
    global speed_y
    global ser
    global end_counter
    global DISTANCE_TO_TAG
    if data.detections:
        for detection in data.detections:
            if detection.id==(0,):
                id=detection.id
                pos_x=detection.pose.pose.pose.position.x
                pos_y=detection.pose.pose.pose.position.y
                pos_z=detection.pose.pose.pose.position.z
                ori_x=detection.pose.pose.pose.orientation.x
                ori_y=detection.pose.pose.pose.orientation.y
                ori_z=detection.pose.pose.pose.orientation.z
                ori_w=detection.pose.pose.pose.orientation.w
                rot_x, rot_y, rot_z=euler_from_quaternion(ori_x, ori_y, ori_z, ori_w)
                print pos_z, rot_y, pos_x
                # move to tag
                if pos_z > DISTANCE_TO_TAG+0.4:
                    if pos_x > 0.01:
                        speed_x=0.02
                        speed_y=0.02
                        print("forwards left fast")
                    elif pos_x < -0.01:
                        speed_x=0.02
                        speed_y=-0.02
                        print("forwards right fast")
                    else:
                        speed_x=0.03
                        speed_y=0.00
                        print("forwards fast")
                elif pos_z > DISTANCE_TO_TAG+0.2:
                    if pos_x > 0.005:
                        speed_x=0.01
                        speed_y=0.01
                        print("forwards left medium fast")
                    elif pos_x < -0.005:
                        speed_x=0.01
                        speed_y=-0.01
                        print("forwards right medium fast")
                    else:
                        speed_x=0.02
                        speed_y=0.00
                        print("forwards medium fast")
                elif pos_z > DISTANCE_TO_TAG+.01:
                    if pos_x > 0.005:
                        speed_x=0.002
                        speed_y=0.005
                        print("forwards left")
                    elif pos_x < -0.005:
                        speed_x=0.002
                        speed_y=-0.005
                        print("forwards right")
                    else:
                        speed_x=0.002
                        speed_y=0.00
                        print("forwards")
                elif pos_z > DISTANCE_TO_TAG:
                    if pos_x > 0.001:
                        speed_x=0.002
                        speed_y=0.002
                        print("forwards left")
                    elif pos_x < -0.001:
                        speed_x=0.002
                        speed_y=-0.002
                        print("forwards right")
                    else:
                        speed_x=0.002
                        speed_y=0.00
                        print("forwards")
                else:
                    speed_x=0.00
                    speed_y=0.00
                    print("stop")
                    end_counter+=1
                    if end_counter>100:
                        os.system("rosnode kill ZZZ_p6b_drive_to_plates")
                        print("End Program")
    else:
        print("No AprilTag detected")

def controller():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ZZZ_p6b_drive_to_plates')
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.Subscriber("/tag_detections", AprilTagDetectionArray, drive)
        twist.linear.x = speed_x
        twist.angular.z = speed_y
        pub.publish(twist)
        rate.sleep()


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    controller()
