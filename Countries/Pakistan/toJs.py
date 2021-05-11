import sys
sys.path.append('./')

import csv
import json
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "") + "/"

def write_json(jsonFilePath, data, varname):
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write("var "+ varname +" = "+json.dumps(data, indent=4))


def make_json(csvFilePath, jsonFilePath, varname):
    # create a dictionary
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows

    write_json(jsonFilePath, data, varname)


# Csv to js
make_json(folder+"web/public/data/cases.csv", folder+"web/public/data/cases.js", "cases")
make_json(folder+"web/public/data/summery.csv", folder+"web/public/data/summery.js", "summery")
make_json(folder+"web/public/data/global.csv", folder+"web/public/data/global.js", "global")
make_json(folder+"web/public/data/quarantines.csv", folder+"web/public/data/quarantines.js", "quarantines")
make_json(folder+"web/public/data/labs.csv", folder+"web/public/data/labs.js", "labs")
make_json(folder+"web/public/data/forecast.csv", folder+"web/public/data/forecast.js", "forecast")
make_json(folder+"web/public/data/vaccine.csv", folder+"web/public/data/vaccine.js", "vaccine")

# Database to js
s = _sqlite
conn = s.conn(get_config("database", folder), folder)
data = conn.get_provience_wise("cases")
write_json(folder+"web/public/data/provience.js", data, "provience")
data = conn.get_processed("cases")
write_json(folder+"web/public/data/trend.js", data, "trend")
data = conn.get_page_data("cases", 1)  # TableName, Page(Number)
write_json(folder+"web/public/data/feed.js", data, "feed")
conn.close()

# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%d %H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")
write_json(folder+"web/public/data/last_update.js", {"update": date}, "update")


# Finally, Done.
print("Done, Thanks")
