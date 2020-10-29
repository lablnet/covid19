from src._sqlite import _sqlite
from src.__config import get_config
import requests
import json
import csv

def csv_to_dict() -> dict:
    data = dict()
    url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
    try :
        r = requests.get(url)
        file = open('WHO-COVID-19-global-data.csv', 'wb')
        file.write(r.content)
        print("File Updated.")
    except :
        print("File not Updated.")
        return

    with open('WHO-COVID-19-global-data.csv', newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=',')
        next(c_reader)  # skip header line
        i = 0
        for items in c_reader:
            data[i] = dict()
            data[i]['date_reported'] = items[0] if items[0] else ""
            data[i]['country_code'] = items[1] if 1 < len(items) else ""
            data[i]['country'] = items[2] if 2 < len(items) else ""
            data[i]['who_region'] = items[3] if 3 < len(items) else ""
            data[i]['new_cases'] = items[4] if 4 < len(items) else ""
            data[i]['cumulative_cases'] = items[5] if 5 < len(items) else ""
            data[i]['new_deaths'] = items[6] if 6 < len(items) else ""
            data[i]['cumulative_deaths'] = items[7] if 7 < len(items) else ""
            i = i + 1
        return data

def c_exists(date_reported, country_code) :
    cursor = conn.getCur()
    sql = "SELECT * FROM cases WHERE date_reported = ? and country_code = ?"
    match = conn.getCur().execute(sql, (date_reported, country_code)).fetchall()
    if len(match) >= 1 :
        return False
    else : return True

data = csv_to_dict()
s = _sqlite()
conn = s.conn(get_config("database", './','who.json'))
conn.create_tables()

for item in data:
    if c_exists(data[item]['date_reported'], data[item]['country_code']) :
        conn.insert(_sqlite.db['tables']["1"]["name"], data[item])
        print(item)
    else : print("Duplicate Data")
