from flask import Flask
from src._sqlite import _sqlite
from src.__config import get_config
import json
app = Flask(__name__)


@app.route('/')
def index():

    s = _sqlite
    conn = s.conn(get_config("database", '../'))
    data = conn.get_data("cases", None, None)  # TableName, From(date), To(date)
    # data = conn.get_data("cases", '2020-12-01', '2020-12-31')
    conn.close()

    return json.dumps(data)


# feed.. pgintion ? pg=44
# newsltter emil.. SMTP ..
# chtbot

app.run()

