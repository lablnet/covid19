#!/usr/bin/env python3

from src._sqlite import _sqlite
from src.__config import get_config
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json
import random


# sqlite instance
s = _sqlite()
# open connection and passing the configs
conn = s.conn(get_config("database", './'))


# creating the table.
conn.create_tables()
i = 0

# next = conn.get_last("url").fetchall()[0][1]
# print(next)
# req = Request(next, headers={'User-Agent': 'PYTHON/3.8'})
# response = urlopen(req)
# data = response.read().decode()
# data = json.loads(data)
# next = "https://co.vid19.pk/api/cases/feed/?limit=100000"
next = "https://co.vid19.pk/api/cases/feed/?startDate=2019-02-26&endDate=2022-05-06&region=all&limit=500"
while True:
    if next is None:
        break
    conn.insert("url", {"url": next})
    req = Request(next, headers={'User-Agent': str(random.randint(00000,99999)) +' PYTHON/3.8  '+str(i)})
    response = urlopen(req)
    data = response.read().decode()
    data = json.loads(data)
    results = data["results"]
    next = data["next"]
    for items in results:
        # print(items['datetime'])
        conn.insert("cases", items)
    print(i)
    i = i + 1
