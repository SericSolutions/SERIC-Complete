import RPi.GPIO as GPIO
import time   
GPIO.setmode(GPIO.BCM)  

Buzzer_pin = 22 #buzzer is connected to GPIO 22

#GPIO 22 set up as output
GPIO.setup(Buzzer_pin,GPIO.OUT)  

GPIO.output(Buzzer_pin, True)
time.sleep(1.5)
GPIO.output(Buzzer_pin, False)
GPIO.cleanup()
