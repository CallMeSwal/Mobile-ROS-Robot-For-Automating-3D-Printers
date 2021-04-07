#!/usr/bin/env python

import time
import serial
import os

ser = serial.Serial('/dev/ttyACM1', 9600)
time.sleep(2)

'''
ATTENTION
THIS CODE ASSUMES THE ROBOT LIFT IS ALREADY HOMED. 
LIFT SHOULD START FROM BOTTOM LIMIT.
SEND COMMAND 'P' TO MOVE ROBOT TO THIS POSITION
'''
# home tongs
ser.write("P")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "LIMIT PRESSED":
            break
    time.sleep(0.1)
time.sleep(1)


# raise tongs to above 3D printer
ser.write("Z")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED Z":
            break
    time.sleep(0.1)
time.sleep(1)

# Launch node that drives to tag 1 (prusa, p2)
#os.system("rosrun keyboard_cont ZZZ_pstraight.py")
#time.sleep(1)
os.system("rosrun keyboard_cont ZZZ_p2_locate_prusa.py")
time.sleep(1)

# lower tongs to print bed
ser.write("C")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED C":
            break
    time.sleep(0.1)
time.sleep(1)

# turn on magnets
ser.write("N")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "MAGNET ON":
            break
    time.sleep(0.1)
time.sleep(1)


# raise bed up
ser.write("Z")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED Z":
            break
    time.sleep(0.1)
time.sleep(1)


# launch node that drive to drop off table (p4_
os.system("rosrun keyboard_cont ZZZ_p4_drive_to_drop_off.py")


# lower tongs to alignment with table
ser.write("X")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED X":
            break
    time.sleep(0.1)
time.sleep(1)

# turn off magnets
ser.write("M")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "MAGNET OFF":
            break
    time.sleep(0.1)
time.sleep(1)

# raise tongs to above 3D printer
ser.write("Z")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED Z":
            break
    time.sleep(0.1)
time.sleep(1)

# launch node that drives robot fresh plates (p6)
os.system("rosrun keyboard_cont ZZZ_p6a_drive_in_front_of_fresh_plates.py")
time.sleep(1)
os.system("rosrun keyboard_cont ZZZ_p6b_drive_to_plates.py")
time.sleep(1)

# lower tongs until limit is pressed
ser.write("V")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED V":
            break
    time.sleep(0.1)
time.sleep(1)

# turn magnets on
ser.write("N")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "MAGNET ON":
            break
    time.sleep(0.1)
time.sleep(1)

# lift new build plate
ser.write("Z")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED Z":
            break
    time.sleep(0.1)
time.sleep(1)

# launch node that drives robot to be infront of prusa (p8, maybe split into 2 nodes and call p2 again)
os.system("rosrun keyboard_cont ZZZ_p8a_drive_in_front_of_prusa.py")
os.system("rosrun keyboard_cont ZZZ_p2_locate_prusa.py")

# lower tongs to be aligned with print bed
ser.write("C")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED C":
            break
    time.sleep(0.1)
time.sleep(1)

# turn magnets off
ser.write("M")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "MAGNET OFF":
            break
    time.sleep(0.1)
time.sleep(1)

# raise tongs to above print bed
ser.write("Z")
while True:
    if ser.in_waiting:
        cmd=ser.readline().strip()
        if cmd == "REACHED Z":
            break
    time.sleep(0.1)
time.sleep(1)

#launch node that drives robot backwards
os.system("rosrun keyboard_cont ZZZ_p10_drive_back.py")
ser.close()
