import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(14,GPIO.OUT) 
GPIO.output(14,GPIO.HIGH) 
