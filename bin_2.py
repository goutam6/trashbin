# -*- coding: utf-8 -*-
#!/usr/bin/python
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


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)          
GPIO.setup(21,GPIO.OUT) 
p = GPIO.PWM(21,50)              
p.start(2.5)              

TRIG = 16
ECHO = 20
while 1:

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
			                                     
			p.ChangeDutyCycle(7.5)                 
			time.sleep(2)                           
			p.ChangeDutyCycle(2.5)                  
			time.sleep(2)  
	now = datetime.datetime.now()

#date=time.strftime("%c")
	

	date= now.strftime("%d-%m-%Y %H:%M")

# Open database connection
	db = MySQLdb.connect("166.62.27.148","smartbin","amith9481447790","id985784_root" )


# prepare a cursor object using cursor() method
	cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO bin2(garbage,
	 smoke,bio,other)
	 VALUES (%s,%s,%s,%s)"""

	try:
# Execute the SQL command
		cursor.execute(sql,(distance1,distance,distance,distance))
# Commit your changes in the database
		db.commit()
	except:
# Rollback in case there is any error
		db.rollback()

# disconnect from server
	db.close()
GPIO.cleanup()

