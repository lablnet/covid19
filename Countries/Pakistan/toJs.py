import sys
sys.path.append('./')
from src._sqlite import _sqlite
from src.__config import get_config
from src.jsExport import make_json, write_json
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "") + "/"


# Csv to js
make_json(folder+"web/public/data/cases.csv", folder+"web/public/data/cases.js", "cases")
make_json(folder+"web/public/data/summery.csv", folder+"web/public/data/summery.js", "summery")
make_json(folder+"web/public/data/summery.csv", folder+"web/public/data/app.json", False)

make_json(folder+"web/public/data/global.csv", folder+"web/public/data/global.js", "global")
make_json(folder+"web/public/data/quarantines.csv", folder+"web/public/data/quarantines.js", "quarantines")
make_json(folder+"web/public/data/labs.csv", folder+"web/public/data/labs.js", "labs")
make_json(folder+"web/public/data/forecast.csv", folder+"web/public/data/forecast.js", "forecast")
make_json(folder+"web/public/data/vaccine.csv", folder+"web/public/data/vaccine.js", "vaccine")

# Database to js
s = _sqlite
conn = s.conn(get_config("database", folder+"/Countries/Pakistan"), folder)
data = conn.get_provience_wise("cases")
write_json(folder+"web/public/data/provience.js", data, "provience")
data = conn.get_processed("cases")
write_json(folder+"web/public/data/trend.js", data, "trend")
data = conn.get_page_data("cases", 1)  # TableName, Page(Number)
write_json(folder+"web/public/data/feed.js", data, "feed")
conn.close()

# Finally, Done.
print("Done, Thanks")
