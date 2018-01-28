#!/usr/bin/env python
import RPi.GPIO as GPIO

ObstaclePin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():

        status = 1 #status is clear initially
        
	while True:
                
		if (GPIO.input(ObstaclePin) and status == 0):  #while having no object is false and status is clear
			print "Status: Clear."
			status = 0 #status changes to obstructed 
		elif ((GPIO.input(ObstaclePin) != 0) and status == 1): #while having no object is true and status is obstructed 
                        print "Status: Obstruction Detected!"
                        status = 1 #status changes to clear 
			

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()         #initial setup 
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
