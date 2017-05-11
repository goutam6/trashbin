#!/usr/bin/python
# -*- coding: utf-8 -*-
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
while 1:
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

#change accordingly
	TRIG = 16
	ECHO = 20

	GPIO.setup(21,GPIO.OUT) 
	p = GPIO.PWM(21,50)              
	p.start(7.5)


	
	
	print ("Distance Measurement In Progress")
	#time.sleep(1)
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
#change it accordingly
	distance1 = 100-((distance/34.5)*100)

	distance1 = round(distance1)

	print ("Distance:",distance1,"%")

	if distance<4:                                                                 
		time.sleep(0.5)									 
		p.ChangeDutyCycle(12.5)                 
		time.sleep(1)                           
		p.ChangeDutyCycle(2.5)                  
		#time.sleep(2) 

	GPIO.cleanup()




          
              



