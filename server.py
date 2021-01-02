from flask import Flask
from flask import request
from flask import Response
from flask_cors import CORS
from src._sqlite import _sqlite
from src.__config import get_config
import json


# initialization
app = Flask(__name__)
CORS(app)

# Prefix for all routes.
app.config["APPLICATION_ROOT"] = "/api/"


@app.route('/')
def index():

    s = _sqlite
    conn = s.conn(get_config("database", './'))
    data = conn.get_data("cases", None, None)  # TableName, From(date), To(date)
    conn.close()

    return json.dumps(data)


@app.route('/feed')
def feed():
    page = request.args['page']

    s = _sqlite
    conn = s.conn(get_config("database", './'))
    data = conn.get_page_data("cases", page)  # TableName, Page(Number)
    conn.close()

    return json.dumps(data)


@app.route('/summery')
def summery():
    to = request.args['to']
    frm = request.args['from']

    s = _sqlite
    conn = s.conn(get_config("database", './'))
    data = conn.get_data("cases", frm, to)  # TableName, From(date), To(date)
    conn.close()

    return data #json.dumps(data)


@app.route('/newsletter')
def newsletter():
    data = request.form.to_dict()


@app.route('/chat', methods=['POST'])
def chat():
    data = request.form.to_dict()


app.run()
