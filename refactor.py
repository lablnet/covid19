from src._sqlite import _sqlite
from src.__config import get_config

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

    f.write(str(row[0])+","+str(row[2])+","+str(provience)+","+str(newCases)+","+str(communicativeCases)+","+str(row[3])+","+str(row[4])+'\n')

f.close()
conn.close()

# Finally, Done
print("Done, Thanks")
