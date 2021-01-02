#!/usr/bin/env python3

from src._sqlite import _sqlite
from src.__config import get_config
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

# sqlite instance
s = _sqlite()
# open connection and passing the configs
conn = s.conn(get_config("database", './'))

s.get_processed("cases")
quit()

# creating the table.
conn.create_tables()
i = 0
next = conn.get_last("url").fetchall()[0][1]
req = Request(next, headers={'User-Agent': 'PYTHON/3.8'})
response = urlopen(req)
data = response.read().decode()
data = json.loads(data)
next = data["previous"]
while True:
    if next is None:
        break
    conn.insert("url", {"url": next})
    req = Request(next, headers={'User-Agent': 'PYTHON/3.8'})
    response = urlopen(req)
    data = response.read().decode()
    data = json.loads(data)
    results = data["results"]
    next = data["previous"]
    for items in results:
        conn.insert("cases", items)
    print(i)
    i = i + 1
