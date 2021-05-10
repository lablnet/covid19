from src._sqlite import _sqlite
from src.__config import get_config
import csv
import os

# delete prev files.
if os.path.exists("./analysis/data.csv"):
    os.remove("./analysis/data.csv")
if os.path.exists("./analysis/dailyStats.csv"):
    os.remove("./analysis/dailyStats.csv")

def dbToCsv():
    s = _sqlite
    conn = s.conn(get_config("database", './'))

    data = conn.get('cases').fetchall()
    states = ["Islamabad", "Punjab", "Sindh", "KPK", "AJK", "GB", 'Balochistan']
    f = open('./analysis/data.csv', 'a')
    f.write('ID,datetime,province,new_cases,cumulative_cases,type,reference\n')

    for row in data:
        description = row[5]
        newCases = str(description.split(" ")[0].replace(',', ''))
        communicativeCases = str(description.split(" ")[-1].replace(',', ''))
        words = description.split(" ")
        provience = ""
        for word in words:
            if word in states:
                provience = word

        f.write(str(row[0]) + "," + str(row[2]) + "," + str(provience) + "," + str(newCases) + "," + str(
            communicativeCases) + "," + str(row[3]) + "," + str(row[4]) + '\n')

    f.close()
    conn.close()


def dayWiseTotalCases(fileName):
    dayWiseTotal = dict()
    current_date = None
    newCases = 0
    cases = []

    with open(fileName, 'r') as _file:
        data = csv.reader(_file, delimiter=",")
        for d in data:
            if d[0] == "ID":
                continue  # to skip first line...
            date = d[1].split('T')[0]
            if current_date is None:
                current_date = date
            if current_date == date and d[5] == "INFECTED":
                newCases = newCases + int(d[3])
            elif current_date != date:
                if newCases != 0:
                    dayWiseTotal['new_cases'] = newCases
                    dayWiseTotal['date'] = current_date
                    cases_copy = dayWiseTotal.copy()
                    cases.append(cases_copy)
                newCases = 0
                current_date = None
        _file.close()
        return cases


def createCSV(fileName):
    with open(fileName, 'w') as _file:
        i = 1
        data = dayWiseTotalCases("./analysis/data.csv")
        _file.write("sr# ,datetime,new_cases, \n")
        for details in data:
            _file.write(f" {i},{details['date']},{details['new_cases']}\n")
            i += 1
        _file.close()

dbToCsv()
createCSV('./analysis/dailyStats.csv')

# Finally, Done
print("Done, Thanks")
