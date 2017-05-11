import time, sys
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
def action(pin):
    print 'bio degradable content detected'
    return
 
GPIO.add_event_detect(12, GPIO.RISING)
GPIO.add_event_callback(12, action)
 
try:
    while True:
        print ' detection in progress'
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
