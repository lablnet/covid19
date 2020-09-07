from src._sqlite import _sqlite
from src.__config import get_config
import json
import csv

s = _sqlite()
conn = s.conn(get_config("database", './'))


def csv_to_list() :
    with open('WHO-COVID-19-global-data.csv', newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        return list(c_reader)
