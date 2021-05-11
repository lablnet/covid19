import sys
sys.path.append('../../')

import pandas as pd
import numpy as np
import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import math
import os
from pathlib import Path

folder = str(Path("").parent.absolute()).replace("Countries\Pakistan", "")

# delete file from public
if os.path.exists(folder+"web/public/data/forecast.csv"):
    os.remove(folder+"web/public/data/forecast.csv")

df = pd.read_csv(folder+'analysis/dailyStats.csv')
dfx=df['datetime']
dfy=df["new_cases"]
raw_y=dfy.to_numpy()
y=dfy
y=np.array(y)
dfx=pd.to_datetime(dfx)
dfx=dfx.map(dt.datetime.toordinal)
x=dfx.to_numpy()
x=x[:,np.newaxis]

tau = .005
w = np.array([np.exp(- (x - x[i])**2/(2*tau)) for i in range(x.shape[0])])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.10,random_state=1000)
clf = LinearRegression()
clf.fit(x_train,y_train)

s=clf.score(x_test,y_test)
y_pred=clf.predict(x_train)

v1=dt.datetime.now().toordinal()

dates = []
for i in range(0, 8):
    dates.append((dt.datetime.now() + timedelta(days=i)).toordinal())

v=np.array(dates)
i = 0
cases = clf.predict(v[:,np.newaxis])
fh = open(folder+"web/public/data/forecast.csv", "a")
fh.write("id,DATE,PREDICT"+ '\n')
for item in cases:
    date = str(datetime.fromordinal(dates[i]))
    fh.write(str(i)+","+str(date)+","+str(math.ceil(item))+'\n')
    i = i + 1

# Finally, Done
print("Done, Thanks")
