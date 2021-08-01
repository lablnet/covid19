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


# Download the PDF
name = folder + "vaccine_center.pdf"
# check if the file exists
if not os.path.isfile(name):
    response = urllib.request.urlopen("https://ncoc.gov.pk/facilities/MVCs_CVCs.pdf")
    with open("vaccine_center.pdf", 'wb') as file:
        file.write(response.read())
# check if with that name csv file exists
if not os.path.isfile(folder + "vaccine_center.csv"):
    tabula.convert_into(name, folder + "vaccine_center.csv", output_format="csv", pages="all")
    
# read csv file
with open(folder + "vaccine_center.csv", 'r') as file:
    reader = csv.reader(file)
    # loop through each row
    for row in reader:
        if len(row) > 5:
            if row[0] == 'Ser#': continue
            # get each row data here
            pass
            # todo: get the data from the row

# delete the above files
# os.remove(name)
# os.remove(folder + "vaccine_center.csv")
