import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	i=GPIO.input(4)
	if i==1:
		print "smoke detected"
	else:
		print "smoke not detected"	
	time.sleep(0.1)
