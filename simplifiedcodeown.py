
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def method():
    df = pd.read_csv('https://raw.githubusercontent.com/srujanavarma11/unveiling_dataset/main/data.csv')
    y = df['unit_consumption']
    X = df.drop(['_id','Time_Stamp','Device_ID','_updated','_created','_etag','Real_Power','unit_consumption'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
    X_train
    X_test
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_lr_train_pred = lr.predict(X_train)
    y_lr_test_pred = lr.predict(X_test)
    return lr

l = method()
