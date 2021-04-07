
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import tf.transformations
from geometry_msgs.msg import Twist
import memcache
shared = memcache.Client(['127.0.0.1:11211'], debug=0)
import time

ledTimer = 2

def callback(data):
    global ledTimer
    checkValues = [data.linear.x, data.linear.y, data.linear.z, data.angular.x, data.angular.y,data.angular.z]
    for value in checkValues:
        if value != 0:
            shared.set('red', 10)
            shared.set('blue', 0)
            shared.set('green', 120)
            ledTimer = time.time()
            return

def listener():
    print("Starting")

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    while 1:
        if (time.time() - ledTimer) > 2.0:
            shared.set('red', 0)
            shared.set('blue', 100)
            shared.set('green', 0)
        time.sleep(0.1)

if __name__ == '__main__':
    listener()
