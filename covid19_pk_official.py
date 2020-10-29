from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import re

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

url = "https://datastudio.google.com/embed/u/0/reporting/1PLVi5amcc_R5Gh928gTE8-8r8-fLXJQF/page/R24IB"
"""url = "http://covid.gov.pk/"

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

soup = BeautifulSoup(get_page(url), 'html.parser')


print(soup)
