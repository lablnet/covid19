import sqlite3
import pandas as pd
from src.__config import get_config

conn = sqlite3.connect(get_config("database", './')['db_name'] + '.sqlite')

df = pd.read_sql("SELECT * FROM cases", conn)
df.to_csv('./web/public/data/cases.csv')
df = pd.read_sql("SELECT * FROM global", conn)
df.to_csv('./web/public/data/global.csv')
df = pd.read_sql("SELECT * FROM summery", conn)
df.to_csv('./web/public/data/summery.csv')
df = pd.read_sql("SELECT * FROM quarantines", conn)
df.to_csv('./web/public/data/quarantines.csv')

# Finally, Done
print("Done, Thanks")
