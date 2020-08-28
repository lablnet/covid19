import sqlite3
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from __config import  get_config



# creating database
db_name = get_config("database", "../")['db_name']
conn = sqlite3.connect(db_name+".sqlite")
cur = conn.cursor()


def create_tables():
    tabl = get_config("database", "../")['tables']
    for tab in tabl :
        f = list(tabl[tab]['fields'].keys())
        k = list(tabl[tab]['fields'].values())
        # cur.execute('CREATE TABLE' , tabl[tab]['name'], 'title', f[0], 'plays', k[0])
        # print('CREATE TABLE' , tabl[tab]['name'], 'title', f, 'plays', k)
        prepareSql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + "  ("
        for i in range(len(f)):
            prepareSql += f[i] + " " + k[i] + ","

        # remove last traling comma.
        prepareSql = prepareSql[0: len(prepareSql) - 1]
        prepareSql += ");"
        cur.executescript(prepareSql)

        # print sql statement
        print(prepareSql)
create_tables()


def insert():
    pass


def update():
    pass

# Drawback = Checks existance of file again and again, Must read data once and for all.
