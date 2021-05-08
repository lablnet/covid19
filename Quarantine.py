from _csv import reader
import urllib.request
import tabula
import os

pdf_path = "https://covid.gov.pk/facilities/List%20of%20Province-wise%20COVID-19%20Quarantine%20Facilities%20Pakistan" \
           ".pdf "


def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


download_file(pdf_path, "Quarantine_Center")


def convertTableToCSV(fileName):
    tabula.convert_into(fileName, "centers.csv", output_format='csv', pages='all')  # converted to csv


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
with open("centers.csv", 'r') as _file:
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
                isb_total = center['beds']
            elif Balochistan_tot == 0:
                Balochistan_tot = center['beds']
            elif KPK_total == 0:
                KPK_total = center['beds']
            elif punjab_tot == 0:
                punjab_tot = center['beds']
            elif sindh_tot == 0:
                sindh_tot = center['beds']
            elif kashmir_tot == 0:
                kashmir_tot = center['beds']
            else:
                gilgit_tot = center['beds']
        if center['beds'] != "" and str(center['beds']).isdigit() and center['address'] != 'Total':
            center_copy = center.copy()
            quarantine_center.append(center_copy)

print('Isb Total = ', isb_total)
print('sindh total = ', sindh_tot)
print('punjab total = ', punjab_tot)
print('Kpk Total = ', KPK_total)
print('Balochistan Total = ', Balochistan_tot)
print('Kashmir Total = ', kashmir_tot)
print('Gilgit Baltistan Total = ', gilgit_tot)

print('Locations details \n')

for center in quarantine_center:
    print('Location = ', center['address'], '------------------ Beds = ', center['beds'])

# delete files now.....

if os.path.exists('centers.csv') and os.path.exists('Quarantine_Center.pdf'):
    os.remove('centers.csv')
    os.remove("Quarantine_Center.pdf")
else:
    print('Files not exists')
