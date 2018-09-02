T = 1.5
R = 1.0

from FacialRecognition import SERIC
import pyopenbr

def compare (this, picture, user):
    usersWith1 = []
    sqlCursor = this._getCursor()
    result = pyopenbr.run(algorithm="FaceRecognition", compare="{} ./data/enroll/main.gal".format(picture));

    if result.values()[0] == '-inf':
        return 0;
    #endif

    query = "SELECT id from enroll where personID = {}".format(user[0])
    avgArray = []
    sqlCursor.execute(query);

    row = sqlCursor.fetchone()
    while row is not None:
        avgArray.append(float(result['./data/enroll/{}.jpg'.format(row[0])]))
        row = sqlCursor.fetchone()

    avg = sum(avgArray)/float(len(avgArray));
    #print("{} user index {} mean = {}".format(user[0], avgArray, avg))
    return avg;

    return -1;

def main():
    seric = SERIC('Pictures.db');
    #seric.compare("./data/1516556140.57.jpg")

    users = seric._getIdOfAllUsers();

    for user in users:
        print("#####{}#####".format(user));
        sqlCursor = seric._getCursor()
        query = "SELECT id from enroll where personID != {}".format(user[0]);
        sqlCursor.execute(query);
        dataset = sqlCursor.fetchall()
        for data in dataset:
            r = compare(seric, './data/enroll/{}.jpg'.format(data[0]), user)
            if  R < r:
                query2 = "INSERT into antidata values({},{})".format(data[0], user[0])
                print("User {}, Picture {}, r = {}".format(user[0], data[0], r));
                sqlCursor.execute(query2)

    seric.sqlConn.commit();

        #print("user: {} ==== {}".format(user,dataset));
main()
