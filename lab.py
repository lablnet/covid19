import urllib.request
from _csv import reader
import os
import csv
import tabula
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime

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
        return "Baluchistan"
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
def getCity(row):
    if row['Functional Lab/Site'] != "":
        if row['City'] == "": return None
        else: return getstr(row['City'])
    elif row['Category'] != "":
        if row['Province/\nRegion (No)'] == "": return None
        else: return getstr(row['Province/\nRegion (No)'])
    else: return None

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
            new_city = getCity(row)
            if new_city != None:
                city = new_city
            Data.append({
            "lab name": getLab(row),
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
conn = s.conn(get_config("database", './'))
# conn.create_tables()

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
