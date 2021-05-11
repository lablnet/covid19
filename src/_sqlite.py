"__config.py: Config manipulation."
__author__ = "Muhammad Umer Farooq"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq & Muhammad Usman Naeem"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Production"

import sqlite3
from datetime import datetime, timedelta

valid_data_types = ('NULL', 'INTEGER', 'INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT, UNSIGNED BIG INT', 'INT2', 'INT8' , 'TEXT', 'CHARACTER(20)', 'CHARACTER',
                      'VARCHAR(255)', 'VARCHAR', 'VARYING CHARACTER(255)', 'VARYING CHARACTER', 'NCHAR(55)', 'NCHAR', 'NATIVE CHARACTER(70)', 'NATIVE CHARACTER', 'NVARCHAR(100)',
                      'NVARCHAR', 'CLOB' , 'REAL', 'DOUBLE', 'DOUBLE PRECISION', 'FLOAT' , 'NUMERIC', 'DECIMAL', 'BOOL', 'BOOLEAN', 'BOOLEAN(10,5)' 'DATE', 'DATETIME')


def dict_from_row(row):
    return dict(zip(row.keys(), row))


class _sqlite:
    db_name = db = ""
    connection = cur = None

    @staticmethod
    def conn(config, folder):
        _sqlite.db_name = config['db_name']
        _sqlite.db = config
        _sqlite.connection = sqlite3.connect(folder+_sqlite.db_name + ".sqlite")
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
    def get_previous_date(date):
        day = int(date[8:])
        month = int(date[5:7])
        year = int(date[:4])
        return str(datetime(year, month, day) - timedelta(1))[:10]

    @staticmethod
    def get_processed(table):
        # gets last date from database
        sq = "SELECT datetime FROM " + table + " ORDER BY datetime DESC LIMIT 1 ;"
        _sqlite.cur.execute(sq, ())
        date = _sqlite.cur.fetchone()[0][:10]
        prev_date = None
        data_list = []
        i = 0
        maxDays = 10
        while True:
            i += 1
            # print(i)        # Just to check line number / iteration number
            dec = 0  # DECEASED
            inf = 0  # INFECTED
            recv = 0  # RECOVERED
            day_data = {}
            sql = "SELECT * FROM " + table
            sql += " WHERE datetime > '" + date + "'"

            if i == maxDays: break;

            if prev_date is not None:
                sql += " AND datetime < '" + prev_date + "'"
            sql += ";"
            try:
                _sqlite.cur.execute(sql, ())
                data = _sqlite.cur.fetchall()
            except:
                return False

            for row in data:
                if row[3] == "INFECTED":
                    num = row[5].split(" ")[0].replace(',', '')
                    if num.isdigit():
                        inf += int(num)
                elif row[3] == "DECEASED":
                    num = row[5].split(" ")[0].replace(',', '')
                    if num.isdigit():
                        dec += int(num)
                elif row[3].startswith("RECOVERED"):
                    num = row[5].split(" ")[0].replace(',', '')
                    if num.isdigit():
                        recv += int(num)
            total = inf + dec + recv
            day_data.update({
                'DATE': date,
                'INFECTED': inf,
                'DECEASED': dec,
                'RECOVERED': recv,
                'TOTAL': total
            })
            data_list.append(day_data)
            prev_date = date
            date = _sqlite.get_previous_date(date)

        data_list.reverse()
        return data_list

    @staticmethod
    def get_data(table, From=None, To=None):
        sql = "SELECT * FROM " + table
        if From is not None:
            sql += " WHERE datetime > '" + From + "'"
        if To is not None:
            sql += " AND datetime < '" + To + "' AND "
        sql += " ORDER BY datetime DESC;"
        # where Date(datetime) in (select DISTINCT DATE(datetime) from " + table + ")
       # try:
        _sqlite.cur.execute(sql, ())
        data = _sqlite.cur.fetchall()
        print(data)
        dataDict = []

        # self.get_previous_date("2020-12-10")

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
        sql = "SELECT * FROM " + table + " ORDER BY id DESC;"
        # _sqlite.cur.execute(sql, ())
        # ID = int(_sqlite.cur.fetchone()[0])
        # FROM = ID - (6*(int(Page) - 1))
        # TO = ID - (6*int(Page))
        #
        # sql = "SELECT * FROM " + table
        # sql += " WHERE id <= " + str(FROM)
        # sql += " AND id > " + str(TO) + " ;"
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
                count = 0
                desc = row[5].split(" ")[0]
                if (desc.isdigit()):
                    count = int(desc)

                if row[3] == "DECEASED":
                    dec += count
                elif row[3] == "INFECTED":
                    inf += count
                elif row[3].startswith("RECOVERED"):
                    recv += count
                else:
                    total += 1
            total += dec + inf + recv
            dataDict = {
                'des': dec,
                'inf': inf,
                'rec': recv,
                'total': total
            }
            return dataDict
        except:
            return False


    @staticmethod
    def get_provience_wise(table):
        count = 0
        gb = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        kpk = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        isb = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        punjab = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        sindh = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        balochistan = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }
        ajk  = {
            'infected': {
                "last": 0,
                "total": 0,
            },
            'recovered': {
                "last": 0,
                "total": 0,
            },
            'deceased': {
                "last": 0,
                "total": 0,
            },
        }

        # isb
        isbSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%Islamabad%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(isbSql, ())
        isbData = _sqlite.cur.fetchall()
        count = isbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(isbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            isb['infected']['total'] = int(count)
            isb['infected']['last'] = last

        isbSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%Islamabad%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(isbSql, ())
        isbData = _sqlite.cur.fetchall()
        count = isbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(isbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            isb['recovered']['total'] = int(count)
            isb['recovered']['last'] = last

        isbSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%Islamabad%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(isbSql, ())
        isbData = _sqlite.cur.fetchall()
        count = isbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(isbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            isb['deceased']['total'] = int(count)
            isb['deceased']['last'] = last

        # punjab
        punjabSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%Punjab%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(punjabSql, ())
        pujnabData = _sqlite.cur.fetchall()
        count = pujnabData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(pujnabData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            punjab['infected']['total'] = int(count)
            punjab['infected']['last'] = last

        punjabSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%Punjab%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(punjabSql, ())
        pujnabData = _sqlite.cur.fetchall()
        count = pujnabData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(pujnabData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            punjab['recovered']['total'] = int(count)
            punjab['recovered']['last'] = last

        punjabSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%Punjab%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(punjabSql, ())
        pujnabData = _sqlite.cur.fetchall()
        count = pujnabData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(pujnabData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            punjab['deceased']['total'] = int(count)
            punjab['deceased']['last'] = last

        # sindth
        sindhSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%Sindh%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(sindhSql, ())
        sindhData = _sqlite.cur.fetchall()
        count = sindhData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(sindhData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            sindh['infected']['total'] = int(count)
            sindh['infected']['last'] = last

        sindhSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%Sindh%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(sindhSql, ())
        sindhData = _sqlite.cur.fetchall()
        count = sindhData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(sindhData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            sindh['recovered']['total'] = int(count)
            sindh['recovered']['last'] = last

        sindhSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%Sindh%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(sindhSql, ())
        sindhData = _sqlite.cur.fetchall()
        count = sindhData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(sindhData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            sindh['deceased']['total'] = int(count)
            sindh['deceased']['last'] = last

        # KPK
        kpkSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%KPK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(kpkSql, ())
        kpkData = _sqlite.cur.fetchall()
        count = kpkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(kpkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            kpk['infected']['total'] = int(count)
            kpk['infected']['last'] = last

        kpkSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%KPK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(kpkSql, ())
        kpkData = _sqlite.cur.fetchall()
        count = kpkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(kpkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            kpk['recovered']['total'] = int(count)
            kpk['recovered']['last'] = last

        kpkSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%KPK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(kpkSql, ())
        kpkData = _sqlite.cur.fetchall()
        count = kpkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(kpkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            kpk['deceased']['total'] = int(count)
            kpk['deceased']['last'] = last

        # GB
        gbSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%Gilgit Baltistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(gbSql, ())
        gbData = _sqlite.cur.fetchall()
        count = gbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(gbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            gb['infected']['total'] = int(count)
            gb['infected']['last'] = last

        gbSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%Gilgit Baltistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(gbSql, ())
        gbData = _sqlite.cur.fetchall()
        count = gbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(gbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            gb['recovered']['total'] = int(count)
            gb['recovered']['last'] = last

        gbSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%Gilgit Baltistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(gbSql, ())
        gbData = _sqlite.cur.fetchall()
        count = gbData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(gbData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            gb['deceased']['total'] = int(count)
            gb['deceased']['last'] = last

        # AJK
        ajkSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%AJK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(ajkSql, ())
        ajkData = _sqlite.cur.fetchall()
        count = ajkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(ajkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            ajk['infected']['total'] = int(count)
            ajk['infected']['last'] = last

        ajkSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%AJK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(ajkSql, ())
        ajkData = _sqlite.cur.fetchall()
        count = ajkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(ajkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            ajk['recovered']['total'] = int(count)
            ajk['recovered']['last'] = last

        ajkSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%AJK%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(ajkSql, ())
        ajkData = _sqlite.cur.fetchall()
        count = ajkData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(ajkData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            ajk['deceased']['total'] = int(count)
            ajk['deceased']['last'] = last

        # balochistan
        balochistanSql = "SELECT * FROM " + table + " Where type='INFECTED' and description LIKE '%Balochistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(balochistanSql, ())
        balochistanData = _sqlite.cur.fetchall()
        count = balochistanData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(balochistanData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            balochistan['infected']['total'] = int(count)
            balochistan['infected']['last'] = last

        balochistanSql = "SELECT * FROM " + table + " Where type='RECOVERED' and description LIKE '%Balochistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(balochistanSql, ())
        balochistanData = _sqlite.cur.fetchall()
        count = balochistanData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(balochistanData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            balochistan['recovered']['total'] = int(count)
            balochistan['recovered']['last'] = last

        balochistanSql = "SELECT * FROM " + table + " Where type='DECEASED' and description LIKE '%Balochistan%' ORDER BY id desc LIMIT 1; "
        _sqlite.cur.execute(balochistanSql, ())
        balochistanData = _sqlite.cur.fetchall()
        count = balochistanData[0][5].split(" ")[-1]
        count = str(count).replace(',', '')
        last = int(str(balochistanData[0][5].split(" ")[0].replace(',', '')))
        if (count.isdigit()):
            balochistan['deceased']['total'] = int(count)
            balochistan['deceased']['last'] = last

        dataDict = {
            'Islamabad': isb,
            'Punjab': punjab,
            'Sindh': sindh,
            'KPK': kpk,
            'GB': gb,
            'Balochistan': balochistan,
            'AJK': ajk,
        }
        return dataDict


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
        pass
        #_sqlite.connection.close()

