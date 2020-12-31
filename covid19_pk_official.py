from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
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

"""
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
"""

# soup = BeautifulSoup(get_page(url), 'html.parser')
soup = get_soup(url)

items = soup.find_all("div", class_="valueLabel")

for item in items:
    print(item)
