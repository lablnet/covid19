import sys
sys.path.append('./')

from _csv import reader
import urllib.request
import tabula
import os
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "") + "/"

pdf_path = "https://covid.gov.pk/facilities/List%20of%20Province-wise%20COVID-19%20Quarantine%20Facilities%20Pakistan" \
           ".pdf "

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

# Comment for fast processing.
download_file(pdf_path, "Quarantine_Center")
tabula.convert_into("Quarantine_Center.pdf", "centers.csv", output_format='csv', pages='all')  # converted to csv


# lists to store dictionaries of different provinces qaurantine centers
quarantine_center = []

isb_total = 0
KPK_total = 0
Balochistan_tot = 0
punjab_tot = 0
sindh_tot = 0
kashmir_tot = 0
gilgit_tot = 0

center = dict()
with open("./centers.csv", 'r') as _file:
    data = reader(_file, delimiter=',')
    for line in data:
        if len(line[0]) < 4:
            center['address'] = line[1]
        else:
            if str(line[0])[0].isdigit():
                index = str(line[0]).find('.')
                address = str(line[0])[index + 1:]
                center['address'] = address
            else:
                center['address'] = line[0]
        center['beds'] = line[2]

        if center['address'] == 'Total':

            if isb_total == 0:
                isb_total = center['beds'].replace(',', '')
            elif Balochistan_tot == 0:
                Balochistan_tot = center['beds'].replace(',', '')
            elif KPK_total == 0:
                KPK_total = center['beds'].replace(',', '')
            elif punjab_tot == 0:
                punjab_tot = center['beds'].replace(',', '')

            elif sindh_tot == 0:
                sindh_tot = center['beds'].replace(',', '')
            elif kashmir_tot == 0:
                kashmir_tot = center['beds'].replace(',', '')
            else:
                gilgit_tot = center['beds'].replace(',', '')
        if center['beds'] != "" and str(center['beds'].replace(',', '')).isdigit() and center['address'] != 'Total':
            center_copy = center.copy()
            quarantine_center.append(center_copy)

seen = set()
new_centers = []
for d in quarantine_center:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_centers.append(d)

quarantine_center = new_centers

# Add provience to centers.
beds = 0
for center in quarantine_center:
    center['provience'] = ""
    beds += int(center['beds'].replace(',', ''))

    if int(beds) == int(isb_total):
        beds = 0
        center['provience'] = "Islamabad"

    elif int(beds) == int(Balochistan_tot):
        beds = 0
        center['provience'] = "Balochistan"

    elif int(beds) == int(KPK_total):
        beds = 0
        center['provience'] = "KPK"

    elif int(beds) == int(punjab_tot):
        beds = 0
        center['provience'] = "Punjab"

    elif int(beds) == int(sindh_tot):
        beds = 0
        center['provience'] = "Sindh"

    elif int(beds) == int(kashmir_tot):
        beds = 0
        center['provience'] = "AJK"

    elif int(beds) == int(gilgit_tot):
        beds = 0
        center['provience'] = "GB"

for center in quarantine_center:
    if center['provience'] == "Islamabad": break
    if center['provience'] == "": center['provience'] = "Islamabad"

for center in quarantine_center:
    if center['provience'] == "Balochistan": break
    if center['provience'] == "": center['provience'] = "Balochistan"

for center in quarantine_center:
    if center['provience'] == "KPK": break
    if center['provience'] == "": center['provience'] = "KPK"

for center in quarantine_center:
    if center['provience'] == "Punjab": break
    if center['provience'] == "": center['provience'] = "Punjab"

for center in quarantine_center:
    if center['provience'] == "Sindh": break
    if center['provience'] == "": center['provience'] = "Sindh"

for center in quarantine_center:
    if center['provience'] == "AJK": break
    if center['provience'] == "": center['provience'] = "AJK"

for center in quarantine_center:
    if center['provience'] == "GB": break
    if center['provience'] == "": center['provience'] = "GB"


# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%dT%H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")

# Database
s = _sqlite()
conn = s.conn(get_config("database", folder), folder)
# conn.create_tables()

# # Insert into database.
# for center in quarantine_center:
#     print(center)
#     conn.insert("quarantines", {
#         "datetime": date,
#         "provience": center['provience'],
#         "name": center['address'],
#         "beds": str(center['beds']),
#         "reference": pdf_path
#     })

conn.close()

# delete files now.....
if os.path.exists('centers.csv') and os.path.exists('Quarantine_Center.pdf'):
    os.remove('centers.csv')
    os.remove("Quarantine_Center.pdf")

# Finally, Done
print("Done, Thanks")
