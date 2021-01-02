"__config.py: Config manipulation."
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq & Muhammad Usman Naeem"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

import sqlite3

valid_data_types = ('NULL', 'INTEGER', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8' , 'TEXT', 'CHARACTER(20)', 'CHARACTER',
                      'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)',
                      'NVARCHAR', 'CLOB' , 'REAL', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT' , 'NUMERIC', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME')


def dict_from_row(row):
    return dict(zip(row.keys(), row))


class _sqlite:
    db_name = db = ""
    connection = cur = None

    @staticmethod
    def conn(config):
        _sqlite.db_name = config['db_name']
        _sqlite.db = config
        _sqlite.connection = sqlite3.connect(_sqlite.db_name + ".sqlite")
        # _sqlite.connection.row_factory = sqlite3.Row
        _sqlite.cur = _sqlite.connection.cursor()
        return _sqlite

    @staticmethod
    def create_tables():
        tabl = _sqlite.db['tables']
        for tab in tabl:
            k = list(tabl[tab]['fields'].keys())
            v = list(tabl[tab]['fields'].values())

            sql = "CREATE TABLE IF NOT EXISTS " + tabl[tab]['name'] + "  ("

            sql += "id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"

            for i in range(len(k)):
                if v[i].upper() not in valid_data_types:
                    print(v[i].upper(), "is not a valid Data Type of table:", tabl[tab]['name'])
                    continue
                sql += "'" + k[i] + "' " + v[i] + ","

            sql = sql[0: len(sql) - 1]
            sql += ");"

            _sqlite.cur.executescript(sql)
            print(tabl[tab]['name'], "Table Created.")

    @staticmethod
    def getCur():
        return _sqlite.cur

    @staticmethod
    def insert_one(table, file) :
        sql = "INSERT INTO " + table + " (date) VALUES ('" + file + "')"
        try:
            _sqlite.cur.execute(sql)
        except:
            print("Error")
        _sqlite.connection.commit()

    @staticmethod
    def insert(table, data):
        fields = tuple(data.keys())
        values = tuple(data.values())
        if len(fields) != len(values):
           return False
        if len(values) > 1:
            vals = str(tuple("?") * len(values)).replace("'", "")
        else:
            vals = str(tuple("?") * len(values))[0: len(values) - 3].replace("'", "") + ")"
        sql = "INSERT INTO " + table + " " + str(fields)[0:len(str(fields))-2].replace("'", "") + ")"
        sql += " VALUES " + vals + ";"
        try:
            _sqlite.cur.execute(sql, values)
        except:
            print("Error")
        _sqlite.connection.commit()
        return True

    @staticmethod
    def get_last(table, where=None):
        sql = "SELECT * FROM " + table
        if where is not None:
            sql += " WHERE " + where['field'] + " = " + where['value']
        sql += " ORDER BY id DESC LIMIT 1 ;"
        try:
            _sqlite.cur.execute(sql, ())
            return _sqlite.cur
        except:
            return False

    @staticmethod
    def get(table, where=None):
        sql = "SELECT * FROM " + table
        if where is not None:
            sql += " WHERE " + where['field'] + " = " + where['value']
        sql += ";"
        try:
            _sqlite.cur.execute(sql, ())
            return _sqlite.cur
        except:
            return False


    @staticmethod
    def get_data(table, From=None, To=None):
        sql = "SELECT * FROM " + table
        if From is not None:
            sql += " WHERE datetime > '" + From + "'"
        if To is not None:
            sql += " AND datetime < '" + To + "' AND "

        # group by Date(datetime)
        sql += " where type='INFECTED' ORDER BY Date(datetime) DESC limit 20;"
        # where Date(datetime) in (select DISTINCT DATE(datetime) from " + table + ")
       # try:
        _sqlite.cur.execute(sql, ())
        data = _sqlite.cur.fetchall()
        print(data)
        dataDict = []
        for item in data:
            dataDict.append({
                'id': item[0],
                'date': item[2],
                'type': item[3],
                'ref': item[4],
                'desc': item[5],
            })
        return dataDict
        #except:
         #   return False


    @staticmethod
    def get_page_data(table, Page):

        sql = "SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1 ;"
        _sqlite.cur.execute(sql, ())
        ID = int(_sqlite.cur.fetchone()[0])
        FROM = ID - (10*(int(Page) - 1))
        TO = ID - (10*int(Page))

        sql = "SELECT * FROM " + table
        sql += " WHERE id <= " + str(FROM)
        sql += " AND id > " + str(TO) + " ;"
        try:
            _sqlite.cur.execute(sql, ())
            data = _sqlite.cur.fetchall()
            dataDict = []
            for item in data:
                dataDict.append({
                    'id': item[0],
                    'date': item[2],
                    'type': item[3],
                    'ref': item[4],
                    'desc': item[5],

                })
            return dataDict #dict_from_row(data)
        except:
            return False

    @staticmethod
    def get_type(table):
        sql = "SELECT * FROM " + table + " ORDER BY type; "

    @staticmethod
    def get_type_percent(table):
        sql = "SELECT * FROM " + table + " ORDER BY type; "
        try:
            _sqlite.cur.execute(sql, ())
            data = _sqlite.cur.fetchall()
            dec = 0  # DECEASED
            inf = 0   # INFECTED
            recv = 0   # RECOVERED
            total = 0   # Total Cases
            for row in data:
                if row[3] == "DECEASED":
                    dec += 1
                elif row[3] == "INFECTED":
                    inf += 1
                elif row[3].startswith("RECOVERED"):
                    recv += 1
                else:
                    total += 1
            total += dec + inf + recv
            dataDict = {
                'DECEASED': dec,
                'INFECTED': inf,
                'RECOVERED': recv,
                'TOTAL': total
            }
            return dataDict
        except:
            return False

    @staticmethod
    def delete(table, field, value):
        sql = "DELETE FROM " + table + " WHERE " + field + " = ? ;"
        try:
            _sqlite.cur.execute(sql, (value,))
            return True
        except:
            return False


    @staticmethod
    def close():
        _sqlite.connection.close()

