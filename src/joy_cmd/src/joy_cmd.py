#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import time

sFactor=0.1
speed_x=0
speed_y=0
twist = Twist()

#pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
pub = rospy.Publisher('cmd_vel_BACKUP', Twist, queue_size=1)

def joyParse(data):
    global sFactor
    global speed_x
    global speed_y
    if (data.buttons[7] == 1): #RB
	    sFactor=1
    if (data.axes[4] == -1.0): #RT
        sFactor=0.5        
    if (sFactor>1):
        print(sFactor)
        sFactor=1
    if (sFactor<=0):
	    sFactor=0.1

    if (data.buttons[0]!=0):
        speed_x=sFactor*data.axes[1]
        speed_y=sFactor*data.axes[0]
        print(speed_x, speed_y)
    else:    
        speed_x = 0
        speed_y = 0	 	
    
def joy_cmds():
    global speed_x
    global speed_y
    rospy.init_node('joy_cmds')
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        rospy.Subscriber("/joy", Joy, joyParse)
        twist.linear.x = speed_x
        twist.angular.z = speed_y
        pub.publish(twist)
        rate.sleep()


if __name__ == '__main__':
    joy_cmds()

