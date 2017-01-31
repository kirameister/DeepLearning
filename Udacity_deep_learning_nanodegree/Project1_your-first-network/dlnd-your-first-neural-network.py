import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## simply load the data from CSV file. The column headers are following: 
## instant,dteday,season,yr,mnth,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed,casual,registered,cnt
data_path = 'Bike-Sharing-Dataset/hour.csv'
rides = pd.read_csv(data_path)
print(rides.head())
rides[:24*10].plot()

dummy_fields = ['season', 'weathersit', 'mnth', 'hr', 'weekday']
for each in dummy_fields:
    dummies = pd.get_dummies(rides[each], prefix=each, drop_first=False)
    rides = pd.concat([rides, dummies], axis=1)

fields_to_drop = ['instant', 'dteday', 'season', 'weathersit', 
                  'weekday', 'atemp', 'mnth', 'workingday', 'hr']
data = rides.drop(fields_to_drop, axis=1)
print(data.head())
