'''
from flask import Flask
import requests

url = "https://co.vid19.pk/api/cases/feed/?limit=100"

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    req = requests.get(url)
    print(req.content)
    return 'Hello'
'''
