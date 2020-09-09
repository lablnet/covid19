from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup

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


url = "http://covid.gov.pk/"

soup = BeautifulSoup(get_page(url), 'html.parser')

elements = soup.find('div', class_='status')

status_note = elements.find("span", class_='status-note').text
new_cases = elements.find("div", class_="new-cases").text
status_items = elements.find("div", class_="col-lg-12")

print(status_items)
