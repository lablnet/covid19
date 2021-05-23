import csv
import json

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
