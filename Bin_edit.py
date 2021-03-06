# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)          
GPIO.setup(19,GPIO.OUT) 
p = GPIO.PWM(19,50)             
p.start(7.5)              

TRIG = 23
ECHO = 24
while 1:

	#print ("Quantity Measurement In Progress")

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	#print ("Waiting For Sensor To Settle")
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

	#print ("Distance:",distance,"cm")
	time.sleep(2)
	if distance<4:                                                                 
			                                     
			p.ChangeDutyCycle(12.5)                 
			time.sleep(3)                           
			p.ChangeDutyCycle(2.5)                  
			time.sleep(3)  

GPIO.cleanup()

