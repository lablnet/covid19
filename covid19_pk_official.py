from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import selenium as se
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime

def get_covid_daily_stat(timer=15):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    # driver = webdriver.Chrome(chrome_options=options, webdriver=ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.set_page_load_timeout(30)
    driver.get("https://datastudio.google.com/embed/u/0/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB")
    time.sleep(timer) # Lower this if you have good internet connection
    parsed_data = driver.find_elements_by_class_name("cell")
    data = {
        "date": parsed_data[0].text      # Date
    }
    i = 1
    while True :
        if i > len(parsed_data) - 1:
            break
        data.update({
            parsed_data[i].text: {                      # Province name
                "confirmed": parsed_data[i + 1].text,   # Confirmed Cases
                "active": parsed_data[i + 2].text,      # Active Cases
                "deaths": parsed_data[i + 3].text,      # Deaths
                "recoveries": parsed_data[i + 4].text   # Recoveries
            }})
        i += 5

    return data


# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%dT%H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")

# Get cases from website.
today = get_covid_daily_stat()

# Get cases form database.
s = _sqlite
conn = s.conn(get_config("database", './'))
cases = (conn.get_provience_wise("cases"))

for key in cases.keys():
    _prov = prov = key
    if (_prov == "GB"): _prov = "Gilgit Baltistan"


    infectedToday = today[prov]['confirmed'].replace(',', '')
    recoveredToday = today[prov]['recoveries'].replace(',', '')
    deceasedToday = today[prov]['deaths'].replace(',', '')
    infectedTotal = cases[prov]['infected']
    recoveredTotal = cases[prov]['recovered']
    deceasedTotal = cases[prov]['deceased']
    infected = str(str(int(infectedToday) - infectedTotal) + " new cases reported in  " + _prov + " taking the tally to " + infectedToday)
    recovered = str(str(int(recoveredToday) - recoveredTotal) + " recoveries reported in " + _prov + " taking the tally to " + recoveredToday)
    deaths = str(str(int(infectedToday) - infectedTotal) + " deaths reported in " + _prov + " taking the tally to " + deceasedToday)

    if (int(infectedToday) - infectedTotal) > 0:
        conn.insert("cases", {
            "datetime": date,
            # "_id": 0,
            "type": "INFECTED",
            "description": infected,
            "reference": "http://covid.gov.pk/",
        })

    if (int(recoveredToday) - recoveredTotal) > 0:
        conn.insert("cases", {
            "datetime": date,
            # "_id": 0,
            "type": "RECOVERED",
            "description": recovered,
            "reference": "http://covid.gov.pk/",
        })

    if (int(deceasedToday) - deceasedTotal) > 0:
        conn.insert("cases", {
            "datetime": date,
            # "_id": 0,
            "type": "DECEASED",
            "description": deaths,
            "reference": "http://covid.gov.pk/",
        })

# Finally, Done.
print("Done, Thanks")
