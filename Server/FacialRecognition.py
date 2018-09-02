import pyopenbr
import sqlite3
from os import rename
from shutil import copyfile
from commands import getstatusoutput as call
from sys import argv
from picamera import PiCamera
from time import sleep, time, strftime, gmtime, localtime
from pyfcm import FCMNotification
import netifaces as ni
import sys
import bluetooth
byte_size = 512


class SERIC:
    sqlConn = None
    T = 2
    #R = 1
    notify = False;

    def __init__(this, dataBasePath):
        this.sqlConn = sqlite3.connect('Pictures.db')

    def enroll (this, name, picture):
        this._addPersonToFaces(name);
        this.sqlConn.commit()
        id = this._getIdOfPerson(name);
        this._addPictureToEnroll(id)
        this.sqlConn.commit();

        id = this._getIdOfPicture(id);
        this._trainAndCopy(picture, id);

    def reInforce (this, id, picture):
        this._addPictureToEnroll(id)
        this.sqlConn.commit()

        id = this._getIdOfPicture(id);
        this._trainAndCopy(picture, id);

    def takePicture(this, facialRecognition):
        sqlCursor = this._getCursor()
        timeStamp = time();
        path = "data/pictures/{}.jpg".format(str(timeStamp))
        try:
            camera = PiCamera();
            #camera.resolution = (1366, 768)
            camera.capture(path)
            camera.close()
        except:
            call("wget http://localhost:8080/?action=snapshot -O {}".format(path))

        q = "convert {} -pointsize 20  \
        -fill black -draw 'rectangle 5,12,200,45' \
        -fill white -annotate +10+35 '{}' \
        {}".format(path, strftime('%Y-%m-%d %H:%M:%S', localtime(timeStamp)), path)

        print(q)
        call(q)

        if facialRecognition:
            personID = this.compare(path)
            mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',{})"\
            .format(int(timeStamp),path,personID)
        else:
            mainQuery = "INSERT INTO main VALUES (NULL,0,{},'{}',-2)".format(int(timeStamp),path)
        #endif

        sqlCursor.execute(mainQuery);
        this.sqlConn.commit();

        if this.notify:
            try:
                if facialRecognition:
                    this.sendNotification(this._getNameOfPerson(personID), '/' + path)
                    return personID
                else:
                    this.sendNotification(this._getNameOfPerson(-2), '/' + path)
    		pass
                #endif
            except KeyError:
                this.sendFile(path);

        return personID

    def compare (this, picture):
        usersWith1 = []
        sqlCursor = this._getCursor()
        result = pyopenbr.run(algorithm="FaceRecognition", compare="{} ./data/enroll/main.gal".format(picture));

        if result.values()[0] == '-inf':
            return 0;
        #endif

        users = this._getIdOfAllUsers();

        for user in users:
            query = "SELECT id from enroll where personID = {}".format(user[0])
            avgArray = []
            sqlCursor.execute(query);

            row = sqlCursor.fetchone()
            while row is not None:
                avgArray.append(float(result['./data/enroll/{}.jpg'.format(row[0])]))
                row = sqlCursor.fetchone()

            x = sum(avgArray)/float(len(avgArray));
            print("{} user index {} mean = {}".format(this._getNameOfPerson(user[0]), avgArray, x))
            if x > this.T:
                avgArray = []
                query = "SELECT id from antidata where personID = {}".format(user[0])
                sqlCursor.execute(query);
                row = sqlCursor.fetchone()
                while row is not None:
                    avgArray.append(float(result['./data/enroll/{}.jpg'.format(row[0])]))
                    row = sqlCursor.fetchone()

                if len(avgArray) > 0:
                    y = sum(avgArray)/float(len(avgArray))
                    print("\t{} user index {} mean = {}".format(this._getNameOfPerson(user[0]), avgArray, y))
                else:
                    y = 0

                if x > y:
                    usersWith1.append((user[0],x));
            #endif

        Max = (0, 0)
        for user in usersWith1:
            if user[1] > Max[1]:
                Max = user

        if(Max[1] > 1.5):
            print("#############")
            print(this._getNameOfPerson(Max[0]));
            print(Max[1])
            print("#############")
            return Max[0];

        return -1;

    def userAttendantData(this, personID):
        sqlCursor = this._getCursor()
        secondQuery = \
            'SELECT src from audio where rec = {} and active = 1'.format(personID)
        sqlCursor.execute(secondQuery)
        audioFile = sqlCursor.fetchone()

        return audioFile

    def userGateData(this, personID):
        print("**{}**".format(personID));

        sqlCursor = this._getCursor()

        thirdQuery = \
            'SELECT OpenDoor from faces where id = {}'.format(personID)
        sqlCursor.execute(thirdQuery)

        unlockGate = sqlCursor.fetchone()

        return unlockGate[0];

    def _addPersonToFaces(this, name):
        sqlCursor = this._getCursor()
        query = "INSERT into faces VALUES(null,'{}',0)".format(name);
        sqlCursor.execute(query);

    def _addPictureToEnroll(this, id):
        sqlCursor = this._getCursor()
        query = 'INSERT into enroll values (NULL, {})'.format(id);
        sqlCursor.execute(query);

    def _getIdOfPerson(this, name):
        sqlCursor = this._getCursor()
        query = "SELECT id from faces where personName = '{}'".format(name);
        sqlCursor.execute(query);
        id = sqlCursor.fetchone()[0];
        return id;

    def _getNameOfPerson(this, name):
        sqlCursor = this._getCursor()
        query = "SELECT personName from faces where id = '{}'".format(name);
        sqlCursor.execute(query);
        name = sqlCursor.fetchone()[0];
        return name;

    def _getIdOfPicture(this, id):
        sqlCursor = this._getCursor()
        query = "SELECT id from enroll where personID = {} order by id DESC".format(id);
        sqlCursor.execute(query);

        try:
            id = sqlCursor.fetchone()[0];
        except TypeError:
            id = 0

        return id

    def _getIdOfAllUsers(this):
        sqlCursor = this._getCursor()
        query = "SELECT id from faces where id > 0" #order by id desc
        sqlCursor.execute(query);
        resultArray = sqlCursor.fetchall()

        return(resultArray);

    def _trainAndCopy(this, picture, id):
        fileName = './data/enroll/{}.jpg'.format(id);
        copyfile(picture, fileName);
        call("br -algorithm FaceRecognition -enroll {} ./data/enroll/temp.gal".format(fileName));
        copyfile("./data/enroll/main.gal", "./data/enroll/temp1.gal");
        call("br -cat ./data/enroll/temp.gal ./data/enroll/temp1.gal ./data/enroll/main.gal");
        call("rm ./data/enroll/temp1.gal ./data/enroll/temp.gal")

    def _getCursor(this):
        return this.sqlConn.cursor()

    def _reBuildgal(this):
        mainGal = './data/enroll/main.gal'
        backupGal = './data/enroll/main.bak'
        rename(mainGal, backupGal)
        sqlCursor = this._getCursor()
        ids = this._getIdOfAllUsers()

        arr = []
        for userID in ids:
            query = "SELECT id from enroll where personID = {} order by id DESC".format(userID[0]);
            sqlCursor.execute(query);
            pictureIDs = sqlCursor.fetchall();
            for pictureID in pictureIDs:
                fileName = './data/enroll/{}.jpg'.format(pictureID[0]);
                arr.append(fileName);

        final = ''
        for i in arr:
            final += " {}".format(i);

        call("br -algorithm FaceRecognition -enroll {} ./data/enroll/main.gal".format(final));

    def getIP(this):
        ni.ifaddresses('eth0')
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        return ip

    def sendNotification(this, name, picture):
        push_service = FCMNotification(api_key="AAAAXVKY1K4:APA91bEfdiunFvYRfB5WDRmlPVH_vam_58wm0gEtgFkmkB05e0lSxo6qT3yDgZ7nEja1JyaTiqROmzOj0y6y7b489gKHNHk7ytD3-QAifKMfs-fk0XtcZHRaFfa8u-XkdGwEt-N7UpKR")
        registration_id = "dT1-oELeodM:APA91bGIchUnyKj-TsV77IXQCSb5xoXW6qBKY8VU1lcWQfx7zejX3RCCwRgRO6vX9ynmzWQpK4xj5UvnnJsNDM0b05K4fHLNJTENwoK8kkG-7mkw40_jZFuzV4_2ySPRrNUuS1xIYHNG"

        message_title = "Someones at the door"
        message_body = "{} is at the door".format(name)

        data_message = {
        "Person": name,
        "Picture": "http://" + this.getIP() + picture
        }

        result = push_service.notify_single_device(
        registration_id=registration_id,
        message_title=message_title,
        message_body=message_body,
        data_message=data_message
        )
        print result;

    def sendFile(this, file):
    	sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
    	bt_addr="5C:C5:D4:64:E8:0C"
    	port = 0x1001
    	sock.connect((bt_addr, port))
    	sock.send("0")
    	#file = open(file, "rb")
    	#byte = file.read(byte_size)
    	#while byte:
    	#    sock.send(byte)
    	#    byte = file.read(byte_size)
    	sock.close()
