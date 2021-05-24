import sys
sys.path.append('./')

import sqlite3
import pandas as pd
from src.__config import get_config
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "\\") + "/"

conn = sqlite3.connect(folder + get_config("database", folder+"/Countries/Pakistan")['db_name'] + '.sqlite')

df = pd.read_sql("SELECT * FROM cases", conn)
df.to_csv(folder+'web/public/data/cases.csv')
df = pd.read_sql("SELECT * FROM global", conn)
df.to_csv(folder+'web/public/data/global.csv')
df = pd.read_sql("SELECT * FROM summery", conn)
df.to_csv(folder+'web/public/data/summery.csv')
df = pd.read_sql("SELECT * FROM vaccine", conn)
df.to_csv(folder+'web/public/data/vaccine.csv')
df = pd.read_sql("SELECT * FROM quarantines", conn)
df.to_csv(folder+'web/public/data/quarantines.csv')
df = pd.read_sql("SELECT * FROM labs", conn)
df.to_csv(folder+'web/public/data/labs.csv')

# Finally, Done
print("Done, Thanks")
