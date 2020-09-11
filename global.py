import csv
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
        print(file_name, "Record Downloaded.")
    except :
        print(file_name, "Record not Downloaded.")

start_date = date(2020, 1, 22)
today_date = date(today_year, today_month, today_day)
today_date_str = str(today_month) + "-" + str(today_day) + "-" + str(today_year) + ".csv"

available_files = list()
missing_files = list()

for single_date in date_range(start_date, today_date):
    file = single_date.strftime("%m-%d-%Y") + ".csv"
    if path.exists(file) : available_files.append(file)
    else : missing_files.append(file)

print("From",start_date.strftime("%m-%d-%Y"), "Uptill", today_date.strftime("%m-%d-%Y"))
print("Available Records :", len(available_files))
print("Missing Records :", len(missing_files))
for file in missing_files :
    print(file)
if len(missing_files) > 0 :
    pause = input("Press Enter To Download Missing Records.")
    for file in missing_files :
        file_download(file)
