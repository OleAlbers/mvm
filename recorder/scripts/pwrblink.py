import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(14,GPIO.OUT) 
while(true)
    GPIO.output(14,GPIO.HIGH) 
    time.sleep(1)
    GPIO.output(14,GPIO.LOW) 
    time.sleep(1)