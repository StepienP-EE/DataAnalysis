import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math
import random as rnd

#Deklaracja dataseries_1
weekdays = ["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdaysSeries = pd.Series(weekdays)
freeDays = [False, False, False, False, False, True, True]
freeDaysSeries = pd.Series(freeDays)
holidays = {"New Year" : "2018-01-01", "Epiphany" : "2018-01-06", 'Easter' : '2018-04-01'}
holidaysSeries = pd.Series(holidays)
#Deklaracja dataseries_2
dataAsFloatList = []
for i in range(100000):
    dataAsFloatList.append(i*rnd.random())
dataAsFloatSeries = pd.Series(dataAsFloatList)
#Deklaracja dataseries_3
dataAsStringList = []
for i in range(100000):
    dataAsStringList.append(i*rnd.random())
dataAsStringSeries=pd.Series(dataAsStringList)

def printing_DataSeries(name):
    print(name)
    print("Size: \t", name.size)
    print("Memory usage: \t", name.memory_usage(deep=True))
    print("Shape: \t", name.shape)
    print("Axes: \t", name.axes)
    print("dtype: \t", name.dtype)
    print("Index: \t", name.index)
    print("Is unique? \t", name.is_unique)
    print("Is monotonic? \t", name.is_monotonic)



if __name__ == '__main__':
    #print(weekdaysSeries)
    #print(freeDaysSeries)
    #print(holidaysSeries)
    #holidaysSeries.size
    printing_DataSeries(dataAsFloatSeries)
    printing_DataSeries(dataAsStringSeries)