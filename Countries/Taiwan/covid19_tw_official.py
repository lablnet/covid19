import os
import sys
sys.path.append('./')
import csv
import requests
from datetime import datetime
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Taiwan", "") + "/"
url = "https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv"
csv_head = 'date,confirmed,recoveries,deaths,screening,excluded,yesterday_confirmed,yesterday_excluded,yesterday_screening'

def get_covid_daily_stat():
    response = requests.get(url)
    parsed_data = response.text.split('\n')[1]
    csv_reader = csv.reader(parsed_data, delimiter=',', skipinitialspace=True)

    rows = []
    tmp = ''
    for row_arr in csv_reader:
        if len(row_arr) == 2 and row_arr[0] == '' and row_arr[0] == '':
            number = int(tmp.replace(',', ''))
            tmp = ''
            rows.append(number)
            continue
        tmp += row_arr[0]
    csv_str = ','.join(map(str, rows))
    csv_str += '\n'

    return csv_str


# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%dT%H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")

# Get cases from website.
today = get_covid_daily_stat()

# Get cases form database.
csv_file_path = './datasets/covid19_tw_stats.csv'
if os.path.exists(csv_file_path) is False:
    today = csv_head + '\n' + today

file_handler = open(csv_file_path, 'r')
last_record = ','.join(file_handler.readlines()[-1].split(',')[1:])

if last_record == today:
    file_handler.close()
    print("Done. No column record is updated. Thanks.")
    exit()

file_handler.close()

file_handler = open(csv_file_path, 'a+')
file_handler.write(str(datetime.now()) + ',' + today)
file_handler.close()

# Finally, Done.
print("Done, Thanks")
