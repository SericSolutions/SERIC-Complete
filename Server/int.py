import RPi.GPIO as GPIO
from time import sleep
from sys import exit, argv
from FacialRecognition import SERIC
import thread
from pygame import mixer

def main():
    seric = SERIC('Pictures.db')
    personID = seric.takePicture(True)

    if seric.userGateData(personID) == 1:
        unlock();
   #endif

    message = seric.userAttendantData(personID)

    if message is not None:
        mixer.init()
        mixer.music.load('./data/audio/' + message[0])
        thread.start_new_thread(mixer.music.play, ())
    #endif

def unlock():
    print("unlocked");
    lockPin = 18
    GPIO.output(lockPin, True)
    sleep(0.7)
    GPIO.output(lockPin, False)


def loop():
    try:
        GPIO.wait_for_edge(14, GPIO.FALLING)
        main()
        loop()
    except KeyboardInterrupt:
        print 'Quit'
        GPIO.cleanup()
        exit()


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(18, GPIO.OUT)
    print 'START'


if argv[1] == '1':
    init()
    loop()
elif argv[1] == '2':
    seric = SERIC('Pictures.db')
    seric.takePicture(True)
elif argv[1] == '3':
    init();
    unlock();
