'''
from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO
servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

def servoMotor():
    servo.angle = 90
    sleep(2)
    servo.angle=-90
    sleep(2)
    servo.angle=0

    GPIO.cleanup()
   
    
'''
    
    
