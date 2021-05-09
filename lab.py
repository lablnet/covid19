import urllib.request
from _csv import reader
import os
import csv
import tabula

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
# Parameter = Row if csv file
# Return = name of Lab Institute
def getLab(row):
    if row['Functional Lab/Site'] != "":
        return row['Functional Lab/Site']
    elif row['Category'] != "":
        return row['Category']
    elif row['City'] != "":
        return row['City']
    elif row['Province/\nRegion (No)'] != "":
        return row['Province/\nRegion (No)']

# To read the pdf data
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
    federal = []
    punjab = []
    sindh = []
    kp = []
    baluchistan = []
    ajk = []
    gilgit = []
    paf = []
    current = ""
    with open("labs.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # To overcome newline at the very last or blank entries
            try: id = row["S. No."]
            except: continue
            if row["Province/\nRegion (No)"] == "Federal\n(32)":
                current = "fedral"
                continue
            elif row["Province/\nRegion (No)"] == "Punjab\n(68)":
                current = "punjab"
                continue
            elif row["Province/\nRegion (No)"] == "Sindh  (41)":
                current = "sindh"
                continue
            elif row["Province/\nRegion (No)"] == "KP ( 23)":
                current = "kp"
                continue
            elif row["Province/\nRegion (No)"] == "Baluchistan\n(0 6)":
                current = "baluchistan"
                continue
            elif row["Province/\nRegion (No)"] == "AJ K\n(0 4)":
                current = "ajk"
                continue
            elif row["Province/\nRegion (No)"] == "Gilgit-\nBalti stan\n(0 3)":
                current = "gilgit"
                continue
            elif row["Province/\nRegion (No)"] == "Pakist an Air\nFor ce":
                current = "paf"
                continue
            if current == "fedral":
                federal.append(getLab(row))
            elif current == "punjab":
                punjab.append(getLab(row))
            elif current == "sindh":
                sindh.append(getLab(row))
            elif current == "kp":
                kp.append(getLab(row))
            elif current == "baluchistan":
                baluchistan.append(getLab(row))
            elif current == "ajk":
                ajk.append(getLab(row))
            elif current == "gilgit":
                gilgit.append(getLab(row))
            elif current == "paf":
                paf.append(getLab(row))
            city = row["City"]
            category = row["Category"]
            site = row["Functional Lab/Site"]

    deleteFiles(files)
    return {"Fedral": federal,
    "Punjab": punjab,
    "Sindh": sindh,
    "KP": kp,
    "Baluchistan": baluchistan,
    "AJK": ajk,
    "Gilgit": gilgit,
    "PAF": paf}

print(readFromPdf())
