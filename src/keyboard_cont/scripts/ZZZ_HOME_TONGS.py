#!/usr/bin/env python

import time
import serial

ser = serial.Serial('/dev/ttyACM1', 9600)
time.sleep(2)

# lower tongs until they hit bottom limit
ser.write("O")
time.sleep(1)

ser.close()
