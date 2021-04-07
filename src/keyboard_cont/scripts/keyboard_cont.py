#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
import serial

speed_x=0
speed_y=0
twist=Twist()

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
ser = serial.Serial('/dev/ttyACM0', 9600)

def drive(data):
    global speed_x
    global speed_y
    global ser

    if data.data=="w":
        speed_x=0.1
        speed_y=0.0
    elif data.data=="s":
        speed_x=-0.04
        speed_y=0.0
    elif data.data=="a":
        speed_x=0.0
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


def controller():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('keyboard_cont_node', anonymous=True)
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        rospy.Subscriber("/key", String, drive)
        twist.linear.x = speed_x
        twist.angular.z = speed_y
        pub.publish(twist)
        rate.sleep()


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    controller()
