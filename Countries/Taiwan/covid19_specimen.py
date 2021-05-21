from posixpath import join
import sys
sys.path.append('./')
import requests
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Taiwan", "") + "/"
url = "https://od.cdc.gov.tw/eic/covid19/covid19_tw_specimen.csv"
csv_head = 'inspection_date,notifiable_inspection,home_quarantine_inspection,expanded_inspection,total'

def get_daily_specimen():
    response = requests.get(url)
    parsed_data = response.text.split('\n')
    parsed_data[0] = csv_head

    return '\n'.join(parsed_data)


# Get specimen lists from website.
hospital_lists = get_daily_specimen()

# Store cases to datasets.
csv_file_path = './datasets/covid19_tw_specimen.csv'

file_handler = open(csv_file_path, 'w')
file_handler.write(hospital_lists)
file_handler.close()

# Finally, Done.
print("Done, Thanks")
