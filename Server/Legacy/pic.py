#DEAD CODE ONLY FOR FUTURE REFERENCE

"""
DEPRICIAED

import FacialRecognition
import pyopenbr
from sys import argv
import sqlite3
from time import sleep, time
from picamera import PiCamera
from pygame import mixer
import thread

conn = sqlite3.connect('Pictures.db')
cursor = conn.cursor()

def main(apicall = 0):
    camera = PiCamera();

    rowsQuery = "SELECT pictureName FROM main Order by CAST(pictureName as INTEGER) DESC";
    cursor.execute(rowsQuery)

    try:
    	i = int(cursor.fetchone()[0])
    except TypeError:
    	i = 0
    print(i);

    t = time();

    path = './data/{}.jpg'.format(str(t))

    print(path);

    camera.capture(path)
    camera.close()

    if apicall == 1:
        personID = FacialRecognition.compare(path, conn)
        mainQuery = "INSERT INTO main VALUES ('{}',{},{},'{}',{})"\
        .format(str(i+1),0,int(t),path,personID)
        print(mainQuery);
        conn.execute(mainQuery);
        conn.commit();

        secondQuery = "SELECT src from audio where rec = {} and active = 1".format(personID);
        cursor.execute(secondQuery);
        audioFile = cursor.fetchone()

        thirdQuery = "SELECT OpenDoor from faces where id = {}".format(personID)
        cursor.execute(thirdQuery);
        unlockGate = cursor.fetchone()

        if unlockGate == 1:
            lock.unlock();


        if audioFile is not None:
            print(audioFile);
            mixer.init()
            mixer.music.load("./data/audio/" + audioFile[0])
            thread.start_new_thread(mixer.music.play, ())
            return 1;
        #endif
        else:
            return 2;
    elif argv[1] == '1':
        personID = FacialRecognition.compare(path, conn)
        mainQuery = "INSERT INTO main VALUES ('{}',{},{},'{}',{})"\
        .format(str(i+1),0,int(t),path,FacialRecognition.compare(path, conn))
    elif argv[1] == '0':
        mainQuery = "INSERT INTO main VALUES ('{}',{},{},'{}',{})"\
        .format(str(i+1),0,int(t),path,-2)
    else:
        return -1;


    conn.execute(mainQuery);
    conn.commit();

if len(argv) > 1:
    main()

def run(p):
    cursor.execute("SELECT * FROM faces order by ID")
    row = cursor.fetchone()

    while row is not None:
	print(row[0])
        if row[0] < 1:
		row = cursor.fetchone()
		continue;

        start_time = time()
        result = pyopenbr.run(algorithm="FaceRecognition", compare="{} {}".format(p, row[2]))
        print("--- %s seconds --- Take Picture" % (time() - start_time))


        a = 0
        count = 0
        inf = 0

        for j, i in result.items():
            print(i)
            if i == "-inf":
                inf += 1
            a += float(i)
            count += 1

        print(inf);
        if(count == inf):
            return 0

        a = a/count
        print(a)

        if(a > 1):
            return(row[0])
        else:
            row = cursor.fetchone()

    return -1
"""
