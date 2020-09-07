from src._sqlite import _sqlite
from src.__config import get_config
import json
import csv

def add(self, key, value):
        self[key] = value

def csv_to_list() :
    data = dict()
    with open('WHO-COVID-19-global-data.csv', newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        dat = list(c_reader)
        for i in range(len(dat)) :
            data[str(i)] = str(dat[i])
        return data
data = csv_to_list()

s = _sqlite()
conn = s.conn(get_config("database", './','who.json'))
conn.create_tables()

conn.insert(_sqlite.db['tables']["1"]["name"], data)
