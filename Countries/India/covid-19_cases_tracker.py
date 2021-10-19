import requests
from bs4 import BeautifulSoup
import os
import csv
import datetime

def today_cases():
    url = "https://www.mohfw.gov.in/"

    response = requests.get(url)
    text = response.text
    data = BeautifulSoup(text, 'html.parser')
    values = []

    # extracting the para containing the active, discharged and deaths cases.
    para1 = data.find_all('div')[0].find_all('div')[0].find_all('section')[0].find_all('div')[0].find_all('div')[0].find_all('div')[0].find_all('div')[1]

    for x in range(3):
        values.append(para1.find_all('li')[x].find_all('span')[5].text.split('(')[0])

    # extractign the para of total vaccinations
    para2 = data.find_all('div')[0].find_all('div')[0].find_all('section')[0].find_all('div')[0].find_all('div')[0].find_all('div')[4].find_all('div')[1].find_all('span')[1]

    total = para2.text
    values.append(total)

    return ','.join(values)

labels = ["Active", "Discharged", "Deaths", "Total Vaccinated"]
csv_head = ','.join(labels)

csv_file_path = './datasets/Countries/India/covid-19_cases.csv'

today = today_cases()
print(today)
if os.path.exists(csv_file_path) is False:
    today = csv_head + '\n' + today

file_handler = open(csv_file_path, 'r')
last_record = ','.join(file_handler.readlines()[-1].split(',')[1:])

if last_record == today:
    file_handler.close()
    exit()

file_handler.close()

file_handler = open(csv_file_path, 'a+')
file_handler.write(str(datetime.now()) + ',' + today)
file_handler.close()

