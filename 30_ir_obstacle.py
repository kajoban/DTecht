#!/usr/bin/env python
import RPi.GPIO as GPIO

ObstaclePin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
        
        status = 1; #clear 
        
	while True:
                
		if (0 == GPIO.input(ObstaclePin)  and status == 1)):  #while having no object is false
			print "Status: Obstruction Detected!"
			status = 0; #now obstructed 
			
		else if (0 != GPIO.input(ObstaclePin and status == 0)):  #while having no object is false
			print "Status: Clear."
			status = 1; #now clear 
        

                #status is either clear, or an obstruction has been detected. 
			

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()         #initial setup 
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

