"""__config.py: Config manipulation."""
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq & Muhammad Usman Naeem"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

import sqlite3
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from __config import  get_config


# creating database
db = get_config("database", "../")    #Gets whole database in db. Instead of accessing file again and again
db_name = db['db_name']
conn = sqlite3.connect(db_name+".sqlite")
cur = conn.cursor()
valid_data_types = ('NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB', 'TEXT', 'NUMERIC', 'NONE', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8', 'CHARACTER(20)', 'CHARACTER', 'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)', 'NVARCHAR', 'CLOB', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME' )

def create_tables():
    tabl = db['tables']
    for tab in tabl :
        k = list(tabl[tab]['fields'].keys())
        v = list(tabl[tab]['fields'].values())

        prepareSql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + "  ("
        if v[0].upper().startswith("INT"):
            prepareSql += "id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"

        for i in range(len(k)):
            if v[i].upper() not in valid_data_types:
                print(v[i].upper(), "is not a valid Data Type", "of table:", tabl[tab]['name'])
                continue
            prepareSql += k[i] + " " + v[i] + ","

        # remove last talling comma.
        prepareSql = prepareSql[0: len(prepareSql) - 1]
        prepareSql += ");"

        cur.executescript(prepareSql)
        # print sql statement
        print("\n2", prepareSql)
create_tables()


def insert():
    pass
    #insert into table : insert key and values. auto generated id number(primary key) + Auto Increment

def update():
    pass

def delete():
    pass

# Append a column
