#!/usr/bin/env python
'''
RaspberryPi with GrovePi example 
Shows values from GrovePi Ultrasonic Ranger on GrovePi LCD RGB Backlight.
If ranger values are below threshold 20 color changes to red from green.
Connect ultrasonic ranger to digital port D4
Connect LCD RGB Backllight to 12C-1
Date: 12/28/2015
Author: Stefan Stranger
'''

import grovepi
from grove_rgb_lcd import *

#Set GrovePi LCD color to green
setText("Retrieving\nUltrasonic Ranger info")
setRGB(0,255,0)
time.sleep(1)

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4

while True:
    try:
        # Read distance value from Ultrasonic
        print (grovepi.ultrasonicRead(ultrasonic_ranger))
        if grovepi.ultrasonicRead(ultrasonic_ranger) >= 20:
			setText(str(grovepi.ultrasonicRead(ultrasonic_ranger))+' That\'s \nfar enough')
			setRGB(0,255,0)
	else:
			setText(str(grovepi.ultrasonicRead(ultrasonic_ranger))+'\nGetting to close')
			setRGB(255,0,0)

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
