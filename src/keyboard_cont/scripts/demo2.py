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
#ser = serial.Serial('/dev/ttyACM0', 9600)

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
        id=data.detections[0].id
        pos_x=data.detections[0].pose.pose.pose.position.x
        pos_y=data.detections[0].pose.pose.pose.position.y
        pos_z=data.detections[0].pose.pose.pose.position.z
        ori_x=data.detections[0].pose.pose.pose.orientation.x
        ori_y=data.detections[0].pose.pose.pose.orientation.y
        ori_z=data.detections[0].pose.pose.pose.orientation.z
        ori_w=data.detections[0].pose.pose.pose.orientation.w
        rot_x, rot_y, rot_z=euler_from_quaternion(ori_x, ori_y, ori_z, ori_w)
        print pos_z, rot_y, pos_x
        # move to tag
        if pos_z > DISTANCE_TO_TAG+0.8:
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
                speed_x=0.0
                speed_y=0.005
                print("forwards left")
            elif pos_x < -0.005:
                speed_x=0.0
                speed_y=-0.005
                print("forwards right")
            else:
                speed_x=0.002
                speed_y=0.00
                print("forwards")
        elif pos_z > DISTANCE_TO_TAG:
            if pos_x > 0.001:
                speed_x=0.0
                speed_y=0.002
                print("forwards left")
            elif pos_x < -0.001:
                speed_x=0.0
                speed_y=-0.002
                print("forwards right")
            else:
                speed_x=0.002
                speed_y=0.00
                print("forwards")
        else:
            # rotate to align with tag
            #if rot_y>0.5:
            #    speed_x=0.00
            #    speed_y=-0.01
            #    print("turn right")
            #elif rot_y<-0.5:
            #    speed_x=0.00
            #    speed_y=0.01
            #    print("turn left")
            #else:
            #    speed_x=0.00
            #    speed_y=0.00
            #    print("stop")
            speed_x=0.00
            speed_y=0.00
            end_counter+=1
            if end_counter>100:
                os.system("rosnode kill demo2")
                print("End Program")
            print("stop")
            
    else:
        print("No AprilTag detected")
    '''
    if data.data=="w":
        speed_x=0.1
        speed_y=0.0
    elif data.data=="s":
        speed_x=-0.04
        speed_y=0.0
    elif data.data=="a":
        ori_x=data.detections[0].pose.pose.pose.orientation.x        speed_x=0.0
        speed_y=0.1
        pub.publish(twist)
    elif data.data=="d":
        speed_x=0.0
        speed_y=-0.1
    elif data.data==" ":
        speed_x=0.0
        speed_y=0.0
    elif data.data=="n":
        ser.write("N")
    elif data.data=="m":
        ser.write("M")
    elif data.data=="i":
        ser.write("I")
    elif data.data=="o":
        ser.write("O")
    elif data.data=="p":
        ser.write("P")
    '''

def controller():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('demo2')
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
