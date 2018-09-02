from FacialRecognition import SERIC
from sys import argv
import sqlite3


def main():
    seric = SERIC('Pictures.db')

    if argv[1] == '0':
        seric.takePicture(False);
    elif argv[1] == '1':
        seric.takePicture(True);
    elif argv[1] == '2':
        seric.enroll(argv[2], argv[3]);
    elif argv[1] == '3':
        seric.reInforce(int(argv[2]), argv[3]);


if len(argv) > 1:
    main()
