import time
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re
from src._sqlite import _sqlite
from src.__config import get_config
from datetime import datetime

url = 'https://covid.gov.pk/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()

patients = soup.find_all('span', class_='counter')  # cases counter....

last_24hr_cases = soup.find('span', class_='tests').text.replace("Last 24 hours: ", "")  # cases in last 24 hr
last_deaths = soup.find('span', class_='deaths').text.replace("Last 24 hours: ", "")  # death in last day
last_recoveries = soup.find('span', class_='recovered').text.replace("Last 24 hours: ", "")  # recoveries in last day
last_tests = soup.find("span", class_="active").text.replace("Last 24 hours: ", "")  # currrently active cases
critical_cases = soup.find("span", class_="total").text.replace("Last 24 hours: ", "")  # critical cases

confirm_total = patients[0].text  # confirmed total case
deaths = patients[1].text  # deaths confirmed
recoveries = patients[2].text  # recoveries confirmed
totalTests = patients[3].text  # totalTests taken
critical = patients[4].text  # critical cases

# Database
s = _sqlite()
conn = s.conn(get_config("database", './'))
# conn.create_tables()

# Prepare current datetime.
now = datetime.now()
date = datetime.strftime(now, "%Y-%m-%dT%H:%M:%S GMT+5")
date = date.replace(" GMT+5", "")

date1 = ""
already = conn.get_last("summery").fetchall()
if  len(already) != 0: date1 = already[0][1].split("-")[2].split("T")[0]
date2 = date.split("-")[2].split("T")[0]

if not date1 == date2:
    conn.insert("summery", {
        "datetime": date,
        "total_tests": totalTests,
        "total_cases": confirm_total,
        "total_deaths": deaths,
        "total_recovered": recoveries,
        "total_critical": critical,
        "last_tests": last_tests,
        "last_cases": last_24hr_cases,
        "last_deaths": last_deaths,
        "last_recovered": last_recoveries,
        "last_critical": critical_cases,
        "reference": url,
    })

# Finally, Done
print("Done, Thanks")
