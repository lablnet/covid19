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
        valid_data_types = ('NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB', 'TEXT', 'NUMERIC', 'NONE', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8', 'CHARACTER(20)', 'CHARACTER', 'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)', 'NVARCHAR', 'CLOB', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME' )
        for i in range(len(f)):
            if k[i].upper() not in valid_data_types :
                print(k[i].upper(), "is not a valid Data Type")
                continue
            prepareSql += f[i] + " " + k[i] + ","

        # remove last traling comma.
        prepareSql = prepareSql[0: len(prepareSql) - 1]
        prepareSql += ");"
        cur.executescript(prepareSql)
        # print sql statement
        #print(prepareSql)
create_tables()


def insert():
    pass
    #insert into table : insert key and values. auto generated id number(primary key)


def update():
    pass

# Append a column
