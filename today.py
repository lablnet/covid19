from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import selenium as se
from webdriver_manager.firefox import GeckoDriverManager
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re
from src._sqlite import _sqlite
from src.__config import get_config

def get_covid_daily_stat(timer=15):
    driver = webdriver.Chrome(ChromeDriverManager().install())
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


def get_soup(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")
    return soup

# I have written this below code.... 

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


'''
print('New cases in ', last_24hr_cases, 'Total cases = ', confirm_total)
print('Deaths in  ', last_deaths, 'Total Deaths = ', deaths)
print('Recoveries in ', last_recoveries, 'Total Recoveries = ', recoveries)
print('Active cases', active_cases, 'Total tests taken = ', totalTests)
print('Critical Patients in A', critical_cases, 'Total Critical = ', critical)
print('Total.............................................Detail')
'''
s = _sqlite
conn = s.conn(get_config("database", './'))

cases = (conn.get_provience_wise("cases"))
print(cases)
