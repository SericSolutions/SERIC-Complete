#LEGACY CODE ONLY FOR FUTURE REFERENCE

import RPi.GPIO as GPIO
import time
from sys import argv

GPIO.setmode(GPIO.BCM)
lockPin = 18;

def unlock():
    GPIO.setup(lockPin,GPIO.OUT)
    GPIO.output(lockPin, True);
    time.sleep(0.3)
    GPIO.output(lockPin, False);
    GPIO.cleanup([lockPin]);

if len(argv) > 1:
    unlock();
