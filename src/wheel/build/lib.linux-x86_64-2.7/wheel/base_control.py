import rospy
import motor
from std_msgs.msg import Int32, Int16

rightWheelSpeed = 0
leftWheelSpeed = 0
updateTimer = 0

def leftSpeedCB(data):
    global updateTimer
    global rightWheelSpeed
    rightWheelSpeed = data.data/10000.0
    updateTimer = 0
def rightSpeedCB(data):
    global updateTimer
    global leftWheelSpeed
    leftWheelSpeed = data.data/10000.0
    updateTimer = 0


def listener():

    # some variables
    global updateTimer

    # creat the publishers
    leftEncPub = rospy.Publisher('lwheel_ticks', Int32, queue_size = 10)
    rightEncPub = rospy.Publisher('rwheel_ticks', Int32, queue_size = 10)

    #creat the subscribers
    rospy.Subscriber("lwheel_desired_rate", Int32, leftSpeedCB)
    rospy.Subscriber("rwheel_desired_rate", Int32, rightSpeedCB)
    # setup the motors
    motor1 = motor.nextEng("192.168.200.218", 9)
    motor2 = motor.nextEng("192.168.200.114", 9)
    robot = motor.robotBase(motor1, motor2)
    rospy.init_node('base_control', anonymous=True)
    rate = rospy.Rate(10)

    encoderLeft = 0
    encoderLeftDiff = 0
    encoderLeftLast = 0
    encoderRight = 0
    encoderRightDiff = 0
    encoderRightLast = 0
    # robot.systemCheck()
    # pos=robot.getEncoderPos() # Changed from getEncoder() to getEncoderPos()
    # robot.setWheelVel(-10, 10)
    while not rospy.is_shutdown():
        if robot.systemCheck() == 1:
            # get the encoder positions
            pos = robot.getEncoderPos()
            encoderLeftDiff = pos[0] - encoderLeftLast
            encoderRightDiff = pos[1] - encoderRightLast
	    robot.setWheelVel(200, 0)

            if (abs(encoderLeftDiff) > 2000) or (abs(encoderRightDiff) > 2000):
                # if the difference is to large dont do anything
                encoderLeftLast = pos[0]
                encoderRightLast = pos[1]
            else:
                encoderLeftLast = pos[0]
                encoderRightLast = pos[1]
                encoderLeft += encoderLeftDiff
                encoderRight += encoderRightDiff

            # when the encoder resets we need to handle it
            pos = robot.getEncoderPos()
            leftEncPub.publish(encoderLeft)
            rightEncPub.publish(encoderRight)

            if updateTimer < 10:
                robot.setWheelVel(rightWheelSpeed, leftWheelSpeed)
            else:
                robot.setWheelVel(0, 0)
            updateTimer += 1
            rate.sleep()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

