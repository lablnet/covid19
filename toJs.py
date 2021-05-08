import csv
import json

def make_json(csvFilePath, jsonFilePath, varname):
    # create a dictionary
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write("var "+ varname +" = "+json.dumps(data, indent=4))


make_json("./web/public/data/cases.csv", "./web/public/data/cases.js", "cases")
make_json("./web/public/data/summery.csv", "./web/public/data/summery.js", "summery")
make_json("./web/public/data/global.csv", "./web/public/data/global.js", "global")
