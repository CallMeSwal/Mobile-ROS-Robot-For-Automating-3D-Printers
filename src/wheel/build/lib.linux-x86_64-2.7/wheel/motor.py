import socket
import time
import random
import struct
import sys
import threading



class nextEng(object):
    
    def __init__(self, ipAddress, port):
        self.ipAddress = ipAddress
        self.port = port

    def connect(self):        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.sock.settimeout(0.2)
        self.sa = (self.ipAddress, self.port)
        self.sock.connect(self.sa)
    
    def boardTemperature(self):
        pass

    def busVoltage(self):
        pass

    def setLeds(self, red, blue, green):
        self.sendUint(8, red)
        self.sendUint(9, blue)
        self.sendUint(10, green)

    def setWheelDiameter(self, diameter):
        self.sendFloat(53, diameter)

    def getWheelVelocity(self):
        return self.getFloat(34)

    def setWheelVelocity(self, velocity):
        self.sendFloat(20, velocity)

    def setAcceleration(self, accel):
        self.sendFloat(25, accel)

    def setDeceleration(self, decel):
        self.sendFloat(26, decel)

    def setCurrentLimit(self, limit):
        self.sendUint(37, limit)

    def currentEncoderTicks(self):
        return self.getInt(52)

    def hallStatus(self):
        return self.getInt(57)
        
    def angularVelocity(self):
        return self.getFloat(33)

    def tickVelocity(self):
        return self.getFloat(31)

    def rpsVelocity(self):
        return self.getFloat(32)

    def setEncoderTicks(self, ticks):
        self.sendUint(60, int(ticks))

    def setControlMode(self, mode):
        self.sendUint(27, mode)

    def setPid(self, prop, integ, diff):
        self.sendFloat(22, prop)
        self.sendFloat(23, integ)
        self.sendFloat(24, diff)

    def requestTickVelocity(self, velocity):
        self.sendFloat(35, velocity)

    def windUpGaurd(self, value):
        self.sendFloat(36, value)

    def sendInt(self, register, value):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        packet += struct.pack('l', value)
        self.sendPacket(packet)
        self.recvPacket()

    def sendUint(self, register, value):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        packet += struct.pack('L', value)
        self.sendPacket(packet)
        self.recvPacket()

    def sendFloat(self, register, value):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        packet += struct.pack('f', value)
        self.sendPacket(packet)
        self.recvPacket()

    def sendDouble(self, register, value):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        packet += struct.pack('d', value)
        self.sendPacket(packet)
        self.recvPacket()

    def getInt(self, register):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        self.sendPacket(packet)
        return struct.unpack('i', self.recvPacket() )[0]

    def getUint(self, register):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        self.sendPacket(packet)
        return struct.unpack('L', self.recvPacket())[0]

    def getFloat(self, register):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        self.sendPacket(packet)
        return struct.unpack('f', self.recvPacket())[0]
        
    def getDouble(self, register):
        packet = b''
        packet += struct.pack('B', register)
        packet += struct.pack('B', 0)
        self.sendPacket(packet)
        return struct.unpack('d', self.recvPacket())[0]

    def sendPacket(self, packet):
        self.sock.send(packet)

    def recvPacket(self):
        x = self.sock.recv(100)
        return x

    def close(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

class robotBase(object):

    def __init__(self, motor1, motor2):
        self.motor1 = motor1
        self.motor2 = motor2
        self.newConnect = 0
        pass

    def connectMotors(self):
        try:
            self.motor1.connect()
            self.motor2.connect()
        except:
            print ("reconnecting")
            pass

    def disconnectMotors(self):
        try:
            self.motor1.close()
            self.motor2.close()
        except:
            pass


    def initMotors(self):

        #10k counts per revolution

        self.motor1.setCurrentLimit(2300)
        self.motor1.windUpGaurd(1500)
        self.motor1.setEncoderTicks(10000)
        self.motor1.setControlMode(2)
        self.motor1.setPid(0.04, 0.05, 0.02)
        self.motor1.setWheelDiameter(.125)
        self.motor1.setAcceleration(0.2)
        self.motor1.setDeceleration(0.2)

        self.motor2.setCurrentLimit(2300)
        self.motor2.windUpGaurd(1500)
        self.motor2.setEncoderTicks(10000)
        self.motor2.setControlMode(2)
        self.motor2.setPid(0.04, 0.05, 0.02)
        self.motor2.setWheelDiameter(.125)
        self.motor2.setAcceleration(0.2)
        self.motor2.setDeceleration(0.2)

        
    def setWheelVel(self, v1, v2):
        try:
            self.motor1.setWheelVelocity(-1 *v1)
            self.motor2.setWheelVelocity(v2)
        except:
            print ("Failed to set wheel vel")

    def getEncoderPos(self):
        try:
            pos1 = self.motor1.currentEncoderTicks() * -1
            pos2 = self.motor2.currentEncoderTicks()
            return pos1, pos2
        except:
            return None

    def checkConnected(self):
        try:
            self.motor1.currentEncoderTicks()
            self.motor2.currentEncoderTicks()
            return 1
        except:
            self.disconnectMotors()
            return 0

    def systemCheck(self):

        # if the motor drivers have been disconnected
        if self.checkConnected() == 0:
            print ("EStop")
            while self.checkConnected() == 0:
                self.connectMotors()
                time.sleep(1)
            print ("reinit motors")
            self.initMotors()
        else:
            return 1

            
            

if __name__ == "__main__":
              
    motor1 = nextEng("192.168.200.218", 9)
    motor2 = nextEng("192.168.200.114", 9)
    robot = robotBase(motor1, motor2)

    updateTimer = 0

    while 1:
        try:
            if robot.systemCheck() == 1:
                #robot.setWheelVel(float(sys.argv[1]), float(sys.argv[1]))
                print (motor1.currentEncoderTicks())
        except:
            pass

