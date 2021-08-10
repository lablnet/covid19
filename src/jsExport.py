import csv
import json

def write_json(jsonFilePath, data, varname=False):
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        if varname is False:
            jsonf.write(json.dumps(data, indent=4))
        else: jsonf.write("var "+ varname +" = "+json.dumps(data, indent=4))


def make_json(csvFilePath, jsonFilePath, varname=False):
    # create a dictionary
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows

    if varname is False:
        # get last item from the dictionary
        last_item = data[list(data.keys())[-1]]
        write_json(jsonFilePath, last_item, False)
    else: write_json(jsonFilePath, data, varname)
