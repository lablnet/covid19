print("Importing...")
from src._sqlite import _sqlite
from src.__config import get_config
import csv
import json
from datetime import date, timedelta
import requests
import os.path
from os import path

today_day = int(date.today().strftime("%d"))
today_month = int(date.today().strftime("%m"))
today_year = int(date.today().strftime("%Y"))

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def file_download(file_name) :
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + file_name
    try :
        r = requests.get(url)
        file = open(file_name, 'wb')
        file.write(r.content)
        filesize = os.path.getsize(file_name)
        if filesize < 10 :
            print("\n", file_name, "Downloaded but Empty\n")
            return
        print(file_name, "Record Downloaded.")
    except :
        print(file_name, "Record not Downloaded.")

def day_add(file):
    month = int(file[:2])
    day = int(file[3:5])
    year = int(file[6:10])
    value = date(year, month, day)
    Date = value.strftime("%m-%d-%Y") + ".csv"
    return Date

def c_exists(file) :
    cursor = conn.getCur()
    conn.getCur().execute("SELECT * FROM records WHERE date=?", (file,))
    match = conn.getCur().fetchall()
    if len(match) >= 1 :
        return False
    else : return True

start_date = date(2020, 1, 22)
today_date = date(today_year, today_month, today_day)
yesterday_date = date(today_year, today_month, today_day - 1)
today_date_str = "0" + str(today_month) + "-" + str(today_day) + "-" + str(today_year) + ".csv"

if not path.exists(today_date_str) :
    file_download(today_date_str)

available_files = list()
missing_files = list()

for single_date in date_range(start_date, today_date):
    file = single_date.strftime("%m-%d-%Y") + ".csv"
    if path.exists(file) : available_files.append(file)
    else : missing_files.append(file)

print("From",start_date.strftime("%m-%d-%Y"), "Uptill", today_date.strftime("%m-%d-%Y"))
print("\nAvailable Records :", len(available_files))
print("Missing Records :", len(missing_files))
for file in missing_files :
    print(file)
if len(missing_files) > 0 :
    pause = input("Press Enter To Download Missing Records.")
    for file in missing_files :
        file_download(file)

def csv_to_dict(file) -> dict:
    data = dict()
    with open(file, newline='') as csvfile:
        c_reader = csv.reader(csvfile, delimiter=',')
        next(c_reader)
        i = 0
        for items in c_reader:
            data[i] = dict()
            data[i]['fips'] = items[0] if items[0] else ""
            data[i]['admin2'] = items[1] if 1 < len(items) else ""
            data[i]['province_state'] = items[2] if 2 < len(items) else ""
            data[i]['country_region'] = items[3] if 3 < len(items) else ""
            data[i]['last_update'] = items[4] if 4 < len(items) else ""
            data[i]['lat'] = items[5] if 5 < len(items) else ""
            data[i]['long_'] = items[6] if 6 < len(items) else ""
            data[i]['confirmed'] = items[7] if 7 < len(items) else ""
            data[i]['deaths'] = items[8] if 8 < len(items) else ""
            data[i]['recovered'] = items[9] if 9 < len(items) else ""
            data[i]['active'] = items[10] if 10 < len(items) else ""
            data[i]['combined_key'] = items[11] if 11 < len(items) else ""
            data[i]['incidence_rate'] = items[12] if 12 < len(items) else ""
            data[i]['case_fatality_ratio'] = items[13] if 13 < len(items) else ""
            i = i + 1
        return data

def insert_data(file) :
        data = csv_to_dict(file)
        print("Inserting data of", file, "in Table:", _sqlite.db['tables']["1"]["name"])
        for item in data:
            conn.insert(_sqlite.db['tables']["1"]["name"], data[item])
            print(item, "Inserted")


s = _sqlite()
conn = s.conn(get_config("database", './','global.json'))
print("")
conn.create_tables()
print("\nTables Opened")

for single_date in date_range(start_date, yesterday_date):
    file = single_date.strftime("%m-%d-%Y") + ".csv"
    if c_exists(file) :             #First Checks if records are present in table: records
        print(file, "Inserted in records")
        conn.insert_one(_sqlite.db['tables']['2']['name'], file)        #inserts in records if not exisits already
        insert_data(file)                   #also inserts data of file in table: cases whose name is not in records

cursor = conn.getCur()
conn.getCur().execute("SELECT * FROM records WHERE date=(SELECT max(date) FROM records);")      #Gets last file from records
match = conn.getCur().fetchall()
last_record = day_add(match[0][1])
insert_data(last_record)
