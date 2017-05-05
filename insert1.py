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






TRIG = 23
ECHO = 24



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

now = datetime.datetime.now()

#date=time.strftime("%c")

date= now.strftime("%d-%m-%Y %H:%M")

# Open database connection
db = MySQLdb.connect("localhost","root","raspberry","id985784_root" )

# prepare a cursor object using cursor() method
cursor = db.cursor()



# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO bin1(garbage,
         smoke,bio,other)
         VALUES (distance,3,4,5)"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
GPIO.cleanup()
