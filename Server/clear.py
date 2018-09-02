import sqlite3
from time import sleep, time
import os, shutil

conn = sqlite3.connect('Pictures.db')

mainQuery = "delete from main"
conn.execute(mainQuery);
conn.commit();

folder = './data/pictures'

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
