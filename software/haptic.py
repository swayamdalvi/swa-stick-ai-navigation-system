import RPi.GPIO as GPIO
import time

MOTOR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR, GPIO.OUT)

while True:
    GPIO.output(MOTOR, True)
    time.sleep(1)

    GPIO.output(MOTOR, False)
    time.sleep(1)
