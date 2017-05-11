#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import MySQLdb

import time

import datetime

import urllib2

import cookielib

from getpass import getpass

import os
 
import sys


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)          # do not show any warnings
GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(21,GPIO.OUT)             # initialize GPIO19 as an output
p = GPIO.PWM(21,50)              # GPIO19 as PWM output, with 50Hz frequency
p.start(7.5)  
while 1:
	GPIO.setmode(GPIO.BCM)

	TRIG = 16
	ECHO = 20

	print ("Distance Measurement In Progress")

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print ("Waiting For Sensor To Settle")
	time.sleep(0.1)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print ("Distance:",distance,"cm")
	distance1 = 100-((distance/34.5)*100)

	distance1 = round(distance1)

	print ("Distance:",distance1,"%")

	
	
	if distance<4:
		p.ChangeDutyCycle(2.5) 
															# change duty cycle for getting the servo position to 90º
		time.sleep(4)                                      # sleep for 1 second
        #p.ChangeDutyCycle(12.5)                  			# change duty cycle for getting the servo position to 180º
        #time.sleep(3)                                     # sleep for 1 second
		p.ChangeDutyCycle(7.5)
		time.sleep(3)                 						# change duty cycle for getting the servo position to 0º
time.sleep(3)


GPIO.cleanup()														# sleep for 1 second

