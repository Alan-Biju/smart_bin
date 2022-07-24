"""
Pi Servo module.
"""
import time 

import RPi.GPIO as GPIO 
from main import *
 
OUT_PIN = 11
PULSE_FREQ = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUT_PIN, GPIO.OUT) 


def servoOpenMain():
    print("Starting")
    servo1 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

    servo1.start(0) 

    print("Spinning")
    
   
    # Start over and move in bigger, slower movements.
    servo1.ChangeDutyCycle(2)
    time.sleep(1)
    servo1.ChangeDutyCycle(7)
    time.sleep(1)
    servo1.ChangeDutyCycle(12)
    time.sleep(4)
    
   
    
    servo1.stop() 
    mainFile()


