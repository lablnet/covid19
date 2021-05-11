import sys
sys.path.append('./')

import urllib.request
from _csv import reader
import os
import csv
import tabula
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "") + "/"

## To Remove all unnecessry white spaces (or anyother characters)
def getstr(string, param = None):
    if param != None:
        temp = string.split(param)
    else:
        temp = string.split()
    main_text = ""
    for substr in temp:
        main_text += substr + " "
    return main_text

## To download the pdf
# Parameter = None
# Return = filename
def downloadPdf(name, url):
    response = urllib.request.urlopen(url)
    with open(name, 'wb') as file:
        file.write(response.read())

## To delete the pdf
# Parameter = list of file paths
# Return = None
def deleteFiles(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

## To get Lab name from the row (as labs are the last entry of the row)
# Parameter = Row of csv file
# Return = name of Lab Institute
def getLab(row):
    if row['Functional Lab/Site'] != "":
        return getstr(row['Functional Lab/Site'])
    elif row['Category'] != "":
        return getstr(row['Category'])
    elif row['City'] != "":
        return getstr(row['City'])
    elif row['Province/\nRegion (No)'] != "":
        return getstr(row['Province/\nRegion (No)'])

## To get Province name from the row
# Parameter = Row of csv file
# Return = name of province or none
def getProvince(row):
    if row["Province/\nRegion (No)"].startswith("Federal"):
        return "Federal"
    elif row["Province/\nRegion (No)"].startswith("Punjab"):
        return "Punjab"
    elif row["Province/\nRegion (No)"].startswith("Sindh"):
        return "Sindh"
    elif row["Province/\nRegion (No)"].startswith("KP"):
        return "KP"
    elif row["Province/\nRegion (No)"].startswith("Baluchistan"):
        return "Balochistan"
    elif row["Province/\nRegion (No)"].startswith("AJ"):
        return "AJK"
    elif row["Province/\nRegion (No)"].startswith("Gilgit"):
        return "Gilgit Baltistan"
    elif row["Province/\nRegion (No)"].startswith("Pakis"):
        return "PAF"
    else: return None

## To get City name from the row
# Parameter = Row of csv file
# Return = name of city or none
def getCity(row, province = None):
    if province != None:
        if row['Functional Lab/Site'] != "":
            return row['City']
        else: return row["Province/\nRegion (No)"]
    if row['Functional Lab/Site'] != "":
        if row['City'] == "": return None
        else:
            city = getstr(row['City']).split("(")
            return city[0]
    elif row['Category'] != "":
        if row['Province/\nRegion (No)'] == "": return None
        else:
            city = getstr(row['Province/\nRegion (No)']).split("(")
            return city[0]
    else: return None

## To get province name from the city name
# Parameter = province name
# Return = city name
def getProv(city):
    if city.startswith("Karachi"): return "Sindh"
    elif city.startswith("Mianwali"): return "Punjab"
    elif city.startswith("Peshawar"): return "KP"
    elif city.startswith("Islamabad"): return "Federal"
    elif city.startswith("Kamra"): return "Punjab"
    elif city.startswith("Shorkot"): return "Punjab"
    elif city.startswith("Quetta"): return "Balochistan"
    elif city.startswith("Lahore"): return "Punjab"
    elif city.startswith("Sargodha"): return "Punjab"

## To get Categiry from the row
# Parameter = Row of csv file
# Return = Private, Public, Military or none
def getCategory(row):
    if row['Functional Lab/Site'] != "":
        return row['Category']
    elif row['Category'] != "":
        if row['City'] == "Public" or row['City'] == "Private":
            return row['City']
    elif row['City'] != "":
        if row['Province/\nRegion (No)'] == "Public" or row['Province/\nRegion (No)'] == "Private":
            return row['Province/\nRegion (No)']
    elif row['Province/\nRegion (No)'] == "": return None
    else: return None

## To read the pdf data
# Parameter = None (can add url later)
# Return = dictionary of data
def readFromPdf():
    url = "https://covid.gov.pk/facilities/29%20April%202021%20Current%20Laboratory%20Testing%20Capacity%20for%20COVID%20Web.pdf"
    n = getstr(url, "%20").split("/")
    name = n[len(n)-1]
    # If files does not exist Download and convert it
    if not os.path.exists(name):
        file = downloadPdf(name, url)
    if not os.path.exists("labs.csv"):
        tabula.convert_into(name, "labs.csv", output_format='csv', pages='all')
    files = [name, "labs.csv"]
    Data = []
    with open("labs.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # To overcome newline at the very last or blank entries
            try: id = row["S. No."]
            except: continue
            new_province = getProvince(row)
            if new_province != None:
                province = new_province
            new_category = getCategory(row)
            if new_category != None:
                category = new_category
            if category == "PAF":
                new_city = getCity(row, province)
                province = getProv(new_city)
            else: new_city = getCity(row)
            if new_city != None:
                city = new_city
            Data.append({
            "lab_name": getLab(row),
            "city": city,
            "provience": province,
            "category": category
            })

    deleteFiles(files)
    return Data


data = readFromPdf()

# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%dT%H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")

# Database
s = _sqlite()
conn = s.conn(get_config("database", folder), folder)
# conn.create_tables()
#
# for item in data:
#     print(item)
#     conn.insert("labs", {
#             "datetime": date,
#             "provience": item['provience'],
#             "name": item['lab_name'],
#             "city": item['city'],
#             "sector": item['category'],
#             "reference": "https://covid.gov.pk/facilities/29%20April%202021%20Current%20Laboratory%20Testing%20Capacity%20for%20COVID%20Web.pdf"
#         })
# # Inserting into Database
# for item in data:
#     provience = item
#     for name in data[provience]:
#         conn.insert("labs", {
#             "datetime": date,
#             "provience": provience,
#             "name": name,
#             "reference": "https://covid.gov.pk/facilities/29%20April%202021%20Current%20Laboratory%20Testing%20Capacity%20for%20COVID%20Web.pdf"
#         })


conn.close()

# Finally, Done
print("Done, Thanks")
