import FacialRecognition
from sys import argv
import sqlite3
from time import sleep, time
from picamera import PiCamera

def takePicture():
    camera = PiCamera();
    timeStamp = time();
    path = './data/{}.jpg'.format(str(timeStamp))
    camera.capture(path)
    camera.close()
    return [path, timeStamp]

def main():
    conn = sqlite3.connect('Pictures.db')
    #cursor = conn.cursor()

    if argv[1] == '0':
        pathTimeStampList = takePicture();
        path = pathTimeStampList[0]
        timeStamp = pathTimeStampList[1]

        mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',-2)".format(int(timeStamp),path)
        conn.execute(mainQuery);
        conn.commit();
    elif argv[1] == '1':
        pathTimeStampList = takePicture();
        path = pathTimeStampList[0]
        timeStamp = pathTimeStampList[1]

        personID = FacialRecognition.compare(path, conn)
        mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',{})".format(int(timeStamp),path,personID)
        conn.execute(mainQuery);
        conn.commit();
    elif argv[1] == '2':
        FacialRecognition.enroll(argv[2], argv[3], conn);
    elif argv[1] == '3':
        FacialRecognition.reInforce(int(argv[2]), argv[3], conn);


if len(argv) > 1:
    main()
