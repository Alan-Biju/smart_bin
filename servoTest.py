"""import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
  while True:
    
    p.ChangeDutyCycle(6.25)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(2.5)
    p.ChangeDutyCycle(6.25)
    time.sleep(0.5)
    p.ChangeDutyCycle(6.5)
    

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
"""
from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO
servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

servo.angle = 90
sleep(2)
servo.angle=-60
sleep(2)
servo.angle=0

GPIO.cleanup()
