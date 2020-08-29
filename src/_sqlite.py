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
        boo = False

        if tab == "1" and not v[0].upper().startswith("INT") :         #Creates Start table a Primary key Index. (If field 1 is int type)
            prepareSql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + " ('ID'    INTEGER,    PRIMARY KEY('ID' AUTOINCREMENT))"       #'ID' INTEGER NOT NULL UNIQUE,   PRIMARY KEY(" + k[0] + " AUTOINCREMENT)"
            print(prepareSql)
            cur.executescript(prepareSql)
            boo = True

        if boo :
            for i in range(len(k)):
                prepareSql = "ALTER TABLE " + tabl[tab]['name'] + " ADD "
                if v[i].upper() not in valid_data_types :
                    print(v[i].upper(), "is not a valid Data Type")
                    return False        # -- It will exit the Entire Function..! To skip this column and go to the next, we should use continue.
                prepareSql += k[i] + " " + v[i] + ";"
                print("1", prepareSql)
                cur.executescript(prepareSql)
        else :
            prepareSql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + "  ("
            for i in range(len(k)):
                if v[i].upper() not in valid_data_types :
                    print(v[i].upper(), "is not a valid Data Type")
                    return False
                prepareSql += k[i] + " " + v[i] + ","
              # remove last traling comma.
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
