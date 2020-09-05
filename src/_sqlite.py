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
bool = False

# creating database
db = get_config("database", "../")
db_name = db['db_name']
conn = sqlite3.connect(db_name+".sqlite")
cur = conn.cursor()
#The benefit of below is that we can access All data types together and also indivisually i.e. Just Numeric Type neededc, or just text etc.
#null = ('NULL')
#int = ('INTEGER', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8')
#txt = ('TEXT', 'CHARACTER(20)', 'CHARACTER', 'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)', 'NVARCHAR', 'CLOB')
#real = ('REAL', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT')
#numeric = ('NUMERIC', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME')
valid_data_types = (  'NULL' , 'INTEGER', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8' , 'TEXT', 'CHARACTER(20)', 'CHARACTER',
                      'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)',
                      'NVARCHAR', 'CLOB' , 'REAL', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT' , 'NUMERIC', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME'    )

def menu():
    try : choice1 = int(input("Please Select from the below Menu :\n\t1. Create DataBase\n\t2. Insert Data in DataBase\n\t3. Find Data in Database\n\t4. Delete Data from DataBase\n\t5. Add Data Manually in DataBase\n\t0. Exit\n => "))
    except :
        print("Please Enter Numbers 1 - 5 Only")
        menu()
    if choice1 == 1 :
        create_tables()
        menu()
    elif choice1 == 2 :
        insert_data()
        menu()
    elif choice1 == 3 :
        #find_record()
        #menu()
        pass
    elif choice1 == 4 :
        delete_data()
        menu()
    elif choice1 == 5 :
        #manual_add()
        #menu()
        pass
    elif choice1 == 0 :
        quit()
    else :
        print("Invalid Input ! Try Again")
        menu()

def create_tables():
    tabl = db['tables']
    for tab in tabl :
        k = list(tabl[tab]['fields'].keys())
        v = list(tabl[tab]['fields'].values())

        prepareSql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + "  ("

        prepareSql += "id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"

        for i in range(len(k)):
            if v[i].upper() not in valid_data_types:
                print(v[i].upper(), "is not a valid Data Type of table:", tabl[tab]['name'])
                continue
            prepareSql += "'" + k[i] + "' " + v[i] + ","

        prepareSql = prepareSql[0: len(prepareSql) - 1]
        prepareSql += ");"

        cur.executescript(prepareSql)
        print(tab, "Table Created.")


testData = {
    "1": {
        'id': '01',
        'name': 'umer',
        'username': 'lablnet'
    },
    "2": {
        'id': '02',
        'name': 'usman',
        'username': 'USMAN'
    },
    "3": {
        'id': '03',
        'name': 'zain',
        'username': 'ZAIN'
    },
    "4": {
        'id': '04',
        'name': 'rehan',
        'username': 'REHAN'
    }
}
def insert_data():
    fields = db['tables']['1']['fields']
    x = list(fields.keys())
    insertSql = "INSERT INTO " + db['tables']['1']['name'] + "("
    for field in fields :
        insertSql += field + ","
    insertSql = insertSql[0: len(insertSql) - 1]
    insertSql += ")"
    insertSql += "    VALUES"
    if len(testData) == 1 :
        val = list(testData['1'].values())
        key = list(testData['1'].keys())
        insertSql += "("
        for i in range(len(val)) :
            if key[i].lower().startswith("id") :
                bool = True
                continue
            insertSql += "'" + val[i] + "',"
        insertSql = insertSql[0: len(insertSql) - 1]
        insertSql += ")"
        if bool :
            bool = False
            if (len(val) - 1) > len(x) :
                print( i+1, " Data Being Entered (", len(val) - 1, ") in Table '" + db['tables']['1']['name'] + "' Is more than Max fields (", len(x), "), Possible Data Loss." )
        else :
            if len(val) > len(x) :
                print( i+1, " Data Being Entered (", len(val) - 1, ") in Table '" + db['tables']['1']['name'] + "' Is more than Max fields (", len(x), "), Possible Data Loss." )

    else :
        for row in testData :
            insertSql += "("
            val = list(testData[row].values())
            key = list(testData[row].keys())
            for j in range(len(val)) :
                if key[j].lower().startswith("id") :
                    bool = True
                    continue
                insertSql += "'" + val[j] + "',"
            insertSql = insertSql[0: len(insertSql) - 1]
            insertSql += ")" + ", "
        insertSql = insertSql[0: len(insertSql) - 2]
        for row in testData :
            for i in range(len(val)) :
                if bool :
                    if (len(val) - 1) > len(x) :
                        print( i+1, " Data Being Entered (", len(val) - 1, ") in Table '" + db['tables']['1']['name'] + "' Is more than Max fields (", len(x), "), Possible Data Loss." )
                else :
                    if len(val) > len(x) :
                        print( i+1, " Data Being Entered (", len(val) - 1, ") in Table '" + db['tables']['1']['name'] + "' Is more than Max fields (", len(x), "), Possible Data Loss." )
    cur.executescript(insertSql)
    print("Data Entered in Tables.")


def update():
    pass

def find_record(choice):
    tabl = db['tables']
    print("Write name of Table to Look into.")
    tables = list()
    for tab in tabl:
        print(tabl[tab]["name"])
        tables.append(tabl[tab]["name"])
    print("Search All Above:  'All'")
    ch = input(" => ")
    if ch.lower() != "all" and ch.lower() not in tables :
        print("Please Enter Given Tables Only..! Find Again.")
        find_record()
    if ch.lower() == "all" :
        if choice == 1 :
            id_num = int(input("Enter ID number to Find => "))
            for tab in tabl :
                try :
                    findSql = "SELECT * FROM " + tab + " WHERE id = '" + id_num +"'"
                    cur.executescript(findSql)
                    print(findSql)
                    return
                except : continue
                finally :
                    Print("No record Found.")
                    return
        elif choice == 2 :
            id_name = input("Enter username to Find => ")
            for tab in tabl :
                try :
                    findSql = "SELECT * FROM " + tab + " WHERE test = '" + id_name +"'"
                    cur.executescript(findSql)
                    print(cur.executescript(findSql))
                    return
                except : continue
                finally :
                    Print("No record Found.")
                    return
        else :
            print("Please Enter Number Between 1 and 3.")
            find_record()
    if choice == 1 :
        id_num = int(input("Enter ID number to Find => "))
        findSql = "SELECT * FROM " + ch + " WHERE id = '" + id_num +"'"
        try :
            cur.executescript(findSql)
            print(findSql)
            return
        except :
            print("No record Found.")
            return
    elif choice == 2 :
        id_name = input("Enter username to Find => ")
        findSql = "SELECT * FROM " + ch + " WHERE test = '" + id_name +"'"
        try :
            cur.executescript(findSql)
            print(findSql)
            return
        except :
            Print("No record Found.")
            return
    else :
        print("Please Enter Number Between 1 and 3.")
        find_record()


def delete_data():
    try : choice = int(input("Please Select from menu :\n\t1. Delete All Records of a person From DataBase\n\t2. Delete One Field (column) From DataBase\n\t3. Delete Entire Database\n => "))
    except :
        print("Please Enter Number Only..!")
        delete_data()
    if choice == 1 :
        tabl = db['tables']
        Name = input("\nEnter username of Record => ")
        for tab in tabl :
            key = list(tabl[tab]['fields'].keys())
            for k in key :
                if k == "test" :
                    deleteSql = "DELETE FROM " + tabl[tab]["name"] + " WHERE " + k + " = '" + Name + "'"
                    cur.executescript(deleteSql)
                    print(" - Record Deleted it Existed. From Table", tabl[tab]["name"])

    elif choice == 2 :
        tabl = db['tables']
        Name = input("\nEnter name of Field (column) => ")
        for tab in tabl :
            key = list(tabl[tab]['fields'].keys())
            for k in key :
                if Name == k :
                    print("> Field Found in Table", tabl[tab]["name"], " <")
                    deleteSql = "DELETE " + Name + " FROM " + tabl[tab]["name"]
                    try :
                        cur.executescript(deleteSql)
                        print("Field Deleted !")
                    except :
                        print("No Field Found !")
                        return

    else :
        print("Please Enter Number Between 1 and 3.")
        return
        delete_data()


menu()

# Append a column
