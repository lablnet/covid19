# Usman code goes here...
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_covid_data() :
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(30)
    driver.get("https://datastudio.google.com/embed/u/0/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB")
    time.sleep(25)          # Lower this if you have good internet connection
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

    return data     # Dictionary containing all data


# Umer's code...
"""
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re

import selenium as se
from webdriver_manager.firefox import GeckoDriverManager


def get_page(url):
    if url is None:
        return None
    page = requests.get(url)
    if page.status_code != 200:
        print("Error")
        return None
    else:
        try:
            return page.content.decode()
        except:
            return page.content


def get_soup(url):

    # options = se.webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Firefox()
    options = se.webdriver.ChromeOptions()
    options.add_argument("--headless")
    # driver = se.webdriver.Chrome(chrome_options=options)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")

    # p_element = c.find_element_by_id(id_='intro-text')
    return soup


url = "https://datastudio.google.com/embed/u/0/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB"

# comment 

url = "http://covid.gov.pk/"

soup = BeautifulSoup(get_page(url), 'html.parser')

elements = soup.find('div', class_='status')

status_note = elements.find("span", class_='status-note').text
new_cases = elements.find("div", class_="new-cases").text
status_items = elements.find_all("div", class_="status-item")

cases = re.findall('[0-9\,0-9]{2,10}', str(status_items))

CASES = {
    "SINDH": cases[0],
    "KPK": cases[1],
    "PUNJAB": cases[2],
    "ISLAMABAD": cases[3],
    "BALOCHISTAN": cases[4],
    "AJK": cases[5],
    "GB": cases[6]
}
# Comment

# soup = BeautifulSoup(get_page(url), 'html.parser')
soup = get_soup(url)

items = soup.find_all("div", class_="valueLabel")

for item in items:
    print(item)
"""
