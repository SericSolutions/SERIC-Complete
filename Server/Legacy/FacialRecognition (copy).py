import pyopenbr
import sqlite3
from os import rename
from shutil import copyfile
from commands import getstatusoutput as call
from sys import argv
from picamera import PiCamera
from time import sleep, time

def enroll (name, picture, sqlConn):
    cursor = sqlConn.cursor()

    addPersonToFaces(name, cursor);
    sqlConn.commit()
    id = getIdOfPerson(name, cursor);
    addPictureToEnroll(id, cursor)
    sqlConn.commit();

    id = getIdOfPicture(id, cursor);
    trainAndCopy(picture, id);

def reInforce (id, picture, sqlConn):
    cursor = sqlConn.cursor()

    addPictureToEnroll(id, cursor)
    sqlConn.commit()

    id = getIdOfPicture(id, cursor);
    trainAndCopy(picture, id);

def takePicture(facialRecognition, sqlConn):
    camera = PiCamera();
    timeStamp = time();
    path = './data/{}.jpg'.format(str(timeStamp))
    camera.capture(path)
    camera.close()

    if facialRecognition:
        personID = compare(path, sqlConn)
        mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',{})"\
        .format(int(timeStamp),path,personID)
    else:
        mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',-2)".format(int(timeStamp),path)
    #endif

    sqlConn.execute(mainQuery);
    sqlConn.commit();

    if facialRecognition:
        return personID
    #endif

def compare (picture, sqlConn):
    cursor = sqlConn.cursor()
    result = pyopenbr.run(algorithm="FaceRecognition", compare="{} ./data/enroll/main.gal".format(picture));

    if result.values()[0] == '-inf':
        return 0;
    #endif

    users = getIdOfAllUsers(cursor);

    for user in users:
        query = "SELECT id from enroll where personID = {}".format(user[0])
        avgArray = []
        cursor.execute(query);

        row = cursor.fetchone()
        while row is not None:
            avgArray.append(float(result['./data/enroll/{}.jpg'.format(row[0])]))
            row = cursor.fetchone()

        avg = sum(avgArray)/float(len(avgArray));
        print("{} user index {} mean = {}".format(user[0], avgArray, avg))
        if avg > 1:
            return user[0];
        #endif

    return -1;

def addDonaldTrump(sqlConn):
    cursor = sqlConn.cursor()
    enroll ("Donald Trump", "./data/DT1.jpg", conn)
    reInforce(getIdOfPerson("Donald Trump", cursor), "./data/DT2.jpg", conn)
    reInforce(getIdOfPerson("Donald Trump", cursor), "./data/DT3.jpg", conn)

def addPersonToFaces(name, sqlCursor):
    query = "INSERT into faces VALUES(null,'{}',0)".format(name);
    sqlCursor.execute(query);

def addPictureToEnroll(id,sqlCursor):
    query = 'INSERT into enroll values (NULL, {})'.format(id);
    sqlCursor.execute(query);

def getIdOfPerson(name, sqlCursor):
    query = "SELECT id from faces where personName = '{}'".format(name);
    sqlCursor.execute(query);
    id = sqlCursor.fetchone()[0];
    return id;

def getIdOfPicture(id,sqlCursor):
    query = "SELECT id from enroll where personID = {} order by id DESC".format(id);
    sqlCursor.execute(query);

    try:
        id = sqlCursor.fetchone()[0];
    except TypeError:
        id = 0

    return id

def getIdOfAllUsers(sqlCursor):
    query = "SELECT id from faces where id > 0" #order by id desc
    sqlCursor.execute(query);
    resultArray = sqlCursor.fetchall()

    return(resultArray);

def trainAndCopy(picture, id):
    fileName = './data/enroll/{}.jpg'.format(id);
    copyfile(picture, fileName);
    call("br -algorithm FaceRecognition -enroll {} ./data/enroll/temp.gal".format(fileName));
    copyfile("./data/enroll/main.gal", "./data/enroll/temp1.gal");
    call("br -cat ./data/enroll/temp.gal ./data/enroll/temp1.gal ./data/enroll/main.gal");
    call("rm ./data/enroll/temp1.gal ./data/enroll/temp.gal")

def extractNumber(string):
    end = -4
    start = end - 1
    while string[start].isdigit():
        start -= 1
    start += 1

    return int(string[start: end])
