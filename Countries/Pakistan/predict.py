# copyright 2020, Muhammad Ameer Hamza
# all rights reserved
# this code is released under MIT license
# For EDA check the code at
#      https://github.com/datanetai/Machine-Learning/blob/main/covid/eda.ipynb
# For Modeling and validation check the code at
#     https://github.com/datanetai/Machine-Learning/blob/main/covid/modeling.ipynb

###################################################


from pathlib import Path
import os
import warnings
import tensorflow as tf
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import sys
sys.path.append('./')

warnings.filterwarnings('ignore')

folder = str(Path("").parent.absolute()).replace(
    "Countries\Pakistan", "") + "/"
print(folder)
# delete file from public
if os.path.exists(folder+"web/public/data/forecast.csv"):
    os.remove(folder+"web/public/data/forecast.csv")

df = pd.read_csv(folder+'analysis/dailyStats.csv',
                 parse_dates=['datetime'], index_col='datetime')

# remove sr# column
df.drop(['sr# '], axis=1, inplace=True)
# remove column wih null values
df = df[df.columns[~df.isnull().all()]]


class NeuralAutoRegressiveModel(tf.keras.Model):
    # Neural AutoRegressive Model
    def __init__(self, input_shape=(10,)):
        """
        Initialize the model.
        param input_shape: shape of the input data
        """

        super(NeuralAutoRegressiveModel, self).__init__(input_shape)

        self.dense1 = tf.keras.layers.Dense(40, activation='swish')
        self.dense2 = tf.keras.layers.Dense(40, activation='swish')
        self.dense3 = tf.keras.layers.Dense(40, activation='swish')
        self.dense = tf.keras.layers.Dense(units=1)

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)
        x = self.dense(x)
        return x


def create_timeseries_dataset(X, y, timestep=1):
    """
    Create a timeseries dataset for forecasting
    params:
        X: input data for last timestep
        y: output data for last timestep
        timestep: number of timesteps to predict
    """
    Xs, ys = list(), list()
    for i in range(len(X)-timestep):
        v = X[i:(i+timestep)]
        Xs.append(v)
        ys.append(y[i+timestep])
    return np.array(Xs), np.array(ys)


def train(epoch=20, batch_size=2):
    """
    Train the model.
    params:
        epoch: number of epochs to train the model
        batch_size: batch size for training
    """
    model = NeuralAutoRegressiveModel()
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, batch_size=2, verbose=0)
    return model

# future prediction


def predict_future(model, X, start_date='2020-01-01', timestep=10, future_step=30,):
    """
    Predict future values for X
    params:
        model: keras model
        X: input data for last timestep
        timestep: number of timesteps to predict
    """
    prediction = np.zeros(future_step)
    for i in range(future_step):
        v = X[-timestep:]
        prediction[i] = model.predict(v.reshape(1, -1), verbose=False)[0][0]
        X = np.append(X, prediction[i])
    prediction = pd.DataFrame(prediction, index=pd.date_range(
        start_date, periods=future_step, freq='D'), columns=['new_cases'])
    return prediction


# create dataset
X, y = create_timeseries_dataset(df['new_cases'], df['new_cases'], timestep=10)
train_dataset = tf.data.Dataset.from_tensor_slices((X, y)).batch(2)

# train model
model = train()

# predict future
last_ten = X[-1:]
pred = predict_future(
    model, last_ten, start_date=df.index[-1], timestep=10, future_step=15)
# cast to int
pred['new_cases'] = pred['new_cases'].astype(int)

prediction = pd.DataFrame(
    {   'id': np.arange(1, len(pred)+1),
        'DATE': pred.index, 'PREDICT': pred['new_cases'].values}, index=np.arange(len(pred)))
prediction.to_csv(folder+'web/public/data/forecast.csv',index=False)


# Finally, Done
print("Done, Thanks")
