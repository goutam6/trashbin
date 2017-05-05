#!/usr/bin/python
 
import MySQLdb

import time

import datetime

import urllib2

import cookielib

from getpass import getpass

import os

import sys

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
         VALUES (1,2,3,4)"""

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







