'''import time 

import RPi.GPIO as GPIO 

 
OUT_PIN = 11
PULSE_FREQ = 50

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUT_PIN, GPIO.OUT) 

def servoMotor(angle=0.5):
    print("Starting")
    servo2 = GPIO.PWM(OUT_PIN, PULSE_FREQ) 

    servo2.start(0) 

    print("Spinning")
    
       
    # Jump between the opposite positions.
    servo2.ChangeDutyCycle(2)
    time.sleep(1)
    servo2.ChangeDutyCycle(12)
    time.sleep(1)
    servo2.ChangeDutyCycle(2)
    time.sleep(1)
    servo2.ChangeDutyCycle(12)
    time.sleep(4)
    GPIO.cleanup()'''