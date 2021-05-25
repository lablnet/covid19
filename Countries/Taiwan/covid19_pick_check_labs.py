import requests

url = "https://od.cdc.gov.tw/icb/%e6%8c%87%e5%ae%9a%e6%8e%a1%e6%aa%a2%e9%86%ab%e9%99%a2%e6%b8%85%e5%96%ae(%e8%8b%b1%e6%96%87%e7%89%88).csv"
csv_head = 'agency_code,area,county,admin_district,agency_name,address,phone_number,longitude,latitude'

def get_pick_check_hospitals():
    response = requests.get(url)
    parsed_data = response.text.split('\n')
    parsed_data[0] = csv_head

    return '\n'.join(parsed_data)


# Get hospital lists from website.
hospital_lists = get_pick_check_hospitals()

# Store cases to datasets.
csv_file_path = './datasets/Countries/Taiwan/covid19_tw_pick_check_labs.csv'

file_handler = open(csv_file_path, 'w')
file_handler.write(hospital_lists)
file_handler.close()

# Finally, Done.
print("Done, Thanks")
