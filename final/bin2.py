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
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#change accordingly
TRIG = 17
ECHO = 27

GPIO.setup(26,GPIO.OUT) 
p = GPIO.PWM(26,50)              
p.start(7.5)

while 1:
	
	
	print ("Distance Measurement In Progress")
	time.sleep(5)
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
		time.sleep(2)									 
		p.ChangeDutyCycle(12.5)                 
		time.sleep(5)                           
		p.ChangeDutyCycle(2.5)                  
		#time.sleep(2) 

	GPIO.cleanup()

now = datetime.datetime.now()

#date=time.strftime("%c")

date= now.strftime("%d-%m-%Y %H:%M")

# Open database connection
db = MySQLdb.connect("166.62.27.148","smartbin","amith9481447790","id985784_root" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO bin1(garbage,
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


          
              



