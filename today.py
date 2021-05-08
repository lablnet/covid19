import time
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re
from src._sqlite import _sqlite
from src.__config import get_config


url = 'https://covid.gov.pk/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()

patients = soup.find_all('span', class_='counter')  # cases counter....

last_24hr_cases = soup.find('span', class_='tests').text  # cases in last 24 hr
last_deaths = soup.find('span', class_='deaths').text  # death in last day
last_recoveries = soup.find('span', class_='recovered').text  # recoveries in last day
active_cases = soup.find("span", class_="active").text  # currrently active cases
critical_cases = soup.find("span", class_="total").text  # critical cases

confirm_total = patients[0].text  # confirmed total case
deaths = patients[1].text  # deaths confirmed
recoveries = patients[2].text  # recoveries confirmed
totalTests = patients[3].text  # totalTests taken
critical = patients[4].text  # critical cases


print('New cases in ', last_24hr_cases, 'Total cases = ', confirm_total)
print('Deaths in  ', last_deaths, 'Total Deaths = ', deaths)
print('Recoveries in ', last_recoveries, 'Total Recoveries = ', recoveries)
print('Active cases', active_cases, 'Total tests taken = ', totalTests)
print('Critical Patients in A', critical_cases, 'Total Critical = ', critical)
print('Total.............................................Detail')

